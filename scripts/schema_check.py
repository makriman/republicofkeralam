#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Small standard-library executor for the JSON Schema subset used in schemas/.

It is deliberately strict about itself: a keyword it does not implement raises
SchemaError instead of being ignored, so a schema can never look enforced while
silently doing nothing. Errors are returned as readable strings, never raised
for bad data.
"""
from __future__ import annotations
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNOTATIONS = {'$schema', '$id', '$comment', 'title', 'description', 'examples', '$defs'}
SUPPORTED = ANNOTATIONS | {
    'type', 'required', 'properties', 'additionalProperties', 'items', 'minItems', 'maxItems',
    'enum', 'const', 'pattern', 'minLength', 'minimum', 'maximum', 'not', 'allOf', 'anyOf',
    'oneOf', 'if', 'then', 'else', '$ref', 'format',
}
TYPES = {
    'object': lambda v: isinstance(v, dict),
    'array': lambda v: isinstance(v, list),
    'string': lambda v: isinstance(v, str),
    'integer': lambda v: isinstance(v, int) and not isinstance(v, bool),
    'number': lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    'boolean': lambda v: isinstance(v, bool),
    'null': lambda v: v is None,
}


class SchemaError(Exception):
    """The schema itself uses something this executor does not implement."""


def load_schema(name: str) -> dict:
    return json.loads((ROOT / 'schemas' / name).read_text(encoding='utf-8'))


def _fmt(path: str) -> str:
    return path or '(root)'


def _join(path: str, key) -> str:
    if isinstance(key, int):
        return f'{path}[{key}]'
    return f'{path}.{key}' if path else str(key)


def _is_date(v: str) -> bool:
    if not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', v):
        return False
    try:
        dt.date.fromisoformat(v)
        return True
    except ValueError:
        return False


class Validator:
    def __init__(self, schema: dict):
        self.root = schema

    def resolve(self, ref: str) -> dict:
        if not ref.startswith('#/'):
            raise SchemaError(f'Only local $ref values are supported: {ref}')
        node = self.root
        for part in ref[2:].split('/'):
            node = node[part]
        return node

    def errors(self, value, schema: dict | bool | None = None, path: str = '') -> list[str]:
        schema = self.root if schema is None else schema
        if schema is True:
            return []
        if schema is False:
            return [f'{_fmt(path)}: property not allowed here']
        unknown = set(schema) - SUPPORTED
        if unknown:
            raise SchemaError(f'Unsupported schema keyword(s) {sorted(unknown)} at {_fmt(path)}')
        if '$ref' in schema:
            return self.errors(value, self.resolve(schema['$ref']), path)
        out: list[str] = []
        rule = f" (rule: {schema['title']})" if 'title' in schema else ''
        t = schema.get('type')
        if t is not None:
            names = t if isinstance(t, list) else [t]
            if not any(TYPES[n](value) for n in names):
                out.append(f'{_fmt(path)}: expected {" or ".join(names)}, got {type(value).__name__} {json.dumps(value, ensure_ascii=False)[:60]}')
                return out  # further keywords would only add noise
        if 'enum' in schema and value not in schema['enum']:
            out.append(f'{_fmt(path)}: {json.dumps(value, ensure_ascii=False)} is not one of {schema["enum"]}')
        if 'const' in schema and value != schema['const']:
            out.append(f'{_fmt(path)}: must equal {json.dumps(schema["const"])}')
        if isinstance(value, str):
            if 'minLength' in schema and len(value) < schema['minLength']:
                out.append(f'{_fmt(path)}: string is shorter than minLength {schema["minLength"]}')
            if 'pattern' in schema and not re.search(schema['pattern'], value):
                out.append(f'{_fmt(path)}: {value!r} does not match pattern {schema["pattern"]}')
            if schema.get('format') == 'date' and not _is_date(value):
                out.append(f'{_fmt(path)}: {value!r} is not a valid YYYY-MM-DD date')
        if TYPES['number'](value):
            if 'minimum' in schema and value < schema['minimum']:
                out.append(f'{_fmt(path)}: {value} is below minimum {schema["minimum"]}')
            if 'maximum' in schema and value > schema['maximum']:
                out.append(f'{_fmt(path)}: {value} is above maximum {schema["maximum"]}')
        if isinstance(value, dict):
            for key in schema.get('required', []):
                if key not in value:
                    out.append(f'{_fmt(_join(path, key))}: required property missing')
            props = schema.get('properties', {})
            for key, sub in props.items():
                if key in value:
                    out.extend(self.errors(value[key], sub, _join(path, key)))
            extra = schema.get('additionalProperties', True)
            for key in value:
                if key in props:
                    continue
                if extra is False:
                    out.append(f'{_fmt(_join(path, key))}: property not allowed here')
                elif isinstance(extra, dict):
                    out.extend(self.errors(value[key], extra, _join(path, key)))
        if isinstance(value, list):
            if 'minItems' in schema and len(value) < schema['minItems']:
                out.append(f'{_fmt(path)}: needs at least {schema["minItems"]} item(s)')
            if 'maxItems' in schema and len(value) > schema['maxItems']:
                out.append(f'{_fmt(path)}: allows at most {schema["maxItems"]} item(s)')
            if 'items' in schema:
                for i, item in enumerate(value):
                    out.extend(self.errors(item, schema['items'], _join(path, i)))
        for sub in schema.get('allOf', []):
            out.extend(self.errors(value, sub, path))
        if 'anyOf' in schema and not any(not self.errors(value, s, path) for s in schema['anyOf']):
            out.append(f'{_fmt(path)}: matches none of the allowed alternatives{rule}')
        if 'oneOf' in schema:
            n = sum(not self.errors(value, s, path) for s in schema['oneOf'])
            if n != 1:
                out.append(f'{_fmt(path)}: must match exactly one alternative (matched {n}){rule}')
        if 'not' in schema and not self.errors(value, schema['not'], path):
            out.append(f'{_fmt(path)}: matches a forbidden form{rule}')
        if 'if' in schema:
            branch = 'then' if not self.errors(value, schema['if'], path) else 'else'
            if branch in schema:
                sub = schema[branch]
                note = f" (rule: {sub['title']})" if isinstance(sub, dict) and 'title' in sub else ''
                out.extend(e + note for e in self.errors(value, sub, path))
        return out


def check(value, schema_name: str) -> list[str]:
    return Validator(load_schema(schema_name)).errors(value)
