"""Conservative, read-only freshness checks. No source revision is rewritten."""
import subprocess


def source_freshness_errors(entries, target, read=None):
    if read is None:
        def read(spec):
            return subprocess.check_output(["git", "show", spec], stderr=subprocess.PIPE)
    errors = []
    pairs = sorted({(e['source_revision'], e['source_path']) for e in entries if e.get('staged_file')})
    for revision, path in pairs:
        try:
            pinned = read(f'{revision}:{path}')
            current = read(f'{target}:{path}')
        except subprocess.CalledProcessError:
            errors.append(f'freshness: cannot read pinned or target source {path} ({revision}, {target})')
            continue
        if pinned != current:
            errors.append(f'freshness: {path} changed between {revision} and {target}; translation review required')
    return errors
