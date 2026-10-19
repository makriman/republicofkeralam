# Chronology and date normalization

## Preserve the date that the source actually gives

Store the original expression, calendar or era when known, the thing being dated, the author’s proposed conversion, the evidence for conversion and the precision. Never replace a range with its midpoint merely to fill an annual page. Never turn “circa,” a reign, a palaeographic attribution or an archaeological phase into an exact date without an explicit argument.

The starter’s historical integer convention is **negative = BCE, positive = CE, no zero**. Thus `-1` means 1 BCE and `1` means 1 CE. This is an internal historical convention, **not ISO astronomical year numbering**. Any ISO/EDTF export must implement and test that distinction. The repository is EDTF-informed, not a complete EDTF implementation [S026](../sources/S026.md).

The third century BCE is represented as the inclusive indexing range `-300` to `-201`. Starting annual files at its earliest year is a navigation decision. It does not assert that the first relevant record dates to 300 BCE. If an earlier source is identified and critically supported, extend `annual_start`, rebuild and document the change.

## Distinct date roles

| Role | What is dated | Frequent error to prevent |
|---|---|---|
| Event | Action or condition in the world | Assigning the date a later historian wrote about it |
| Object production / inscription | Manufacture, writing or engraving | Confusing a later copy or reuse with initial production |
| Text composition | Composition or redaction of a work | Treating a story’s setting as composition date |
| Surviving witness | Particular manuscript, impression or copy | Treating the age of the work as the age of this copy |
| Observation / collection / excavation | Recovery or documentation | Dating an ancient object by its discovery year |
| Scientific measurement | Laboratory run | Dating the organism, sediment or rock by analysis year |
| Publication / online / volume | Release milestones for scholarship | Assuming a DOI digit or hosting date is the first publication |
| Digitization / catalogue | Access and metadata creation | Treating digitization as manuscript creation |
| Access / revision | This project’s interaction with the source | Claiming access implies full inspection or permanent availability |

Additional roles can be added; they must be named. Do not silently reuse an `event_date` field for another purpose.

## Historical date types in this release

`kind: historical` stores an inclusive `start_year` and `end_year`. A same-year value can still have `precision: conventional_year`, rather than certainty. A genuine day-level date also has a checked date string. An interval has `precision: interval` and normally remains on a dossier page. An attributed proposed year may link to its annual page under the conspicuous proposed-date heading.

`kind: undated` can retain relative attributions such as “Lower Palaeolithic” or an unresolved date claim. It must not have an annual event link. A separately dated later study can be a different record linked by source or dossier.

A later schema extension should support multiple disjoint alternatives, bounds such as “before” and “after,” and calendrical constraints. Do not flatten these into a single interval interpreted as uniformly probable. A reign-derived range is not necessarily a probability distribution.

## Radiocarbon

Radiocarbon BP conventionally refers to 1950, but a radiocarbon age is not the same as elapsed calendar years [S025](../sources/S025.md). A source saying “5210 years ago” without a laboratory code, measurement error or calibration information is insufficient for a precise conversion. Preserve it as a reported value, not a normalized BCE event.

For a proper measurement record, capture laboratory ID, sample material, taxon where relevant, pretreatment, measured value, uncertainty and its convention, calibration curve and version, software/version, reservoir corrections, calibrated intervals and probabilities, stratigraphic relationship and the author’s interpretation. Clearly distinguish `14C BP`, `cal BP`, `cal BCE/CE` and prose approximations. Account for potential old-wood, redeposition and reservoir issues as appropriate to the study; do not add corrections without evidence.

## Geological time

Use Ma or Ga with the unit and interpretation. Keep the observed material, method and inferred process separate. A detrital grain’s formation age is not automatically the host sediment’s deposition age. A metamorphic rim does not simply reset every older part of the rock. Do not use a whole-territory geological birthday.

The initial geological records store `older_ma` and `younger_ma`. The Quilon example retains the authors’ preferred depositional range and explicitly does **not** relabel it a confidence interval [S007](../sources/S007.md). Formal stage boundaries require a cited and versioned chronostratigraphic chart; the chart was not retrieved successfully in this pass [S042](../sources/S042.md).

## Regnal, regional and religious calendars

Future additions must retain original dates in Kollam Era, Saka, Hijri, regnal years and other systems. A conversion needs its calendar conventions, year start, local day convention, intercalation, reading and uncertainty. Do not implement a single universal offset for all documents. Julian/Gregorian conversion likewise requires an explicitly documented basis.

The arrival-journal extract is a useful warning: its sequence around May 20 and May 22 needs the critical edition before day-level normalization. The repository retains 1498 at year level [S022](../sources/S022.md).

## No annual precision by repetition

A site phase covering 300 BCE–500 CE is one interval record, not 800 separately established events. Annual pages can link to the phase dossier, but must label it broader context. Exact commencement of a law, by contrast, may have an annual entry with a day. The law’s adoption and commencement remain separate records when they differ [S023](../sources/S023.md).
