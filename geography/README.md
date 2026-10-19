# Geographic eligibility

## The target

The study frame is the territory now administered as Kerala, provisionally referenced to **11 October 2026**. Its name is only a locator. The target is not every land ever ruled by Cheras, every Malayalam-speaking community, all historical Travancore, all historical Malabar, or the watershed of every river entering the state.

**A verified current boundary polygon has not been obtained.** `scope.json` explicitly stores null geometry, rights and checksum. Automated spatial filtering is disabled. Do not use a random outline map as a substitute for a sourced and licensed boundary dataset.

## Core and context

| Relation | Inclusion test |
|---|---|
| Core | The dated object, place or phenomenon is inside the verified modern frame, or provisionally located there with uncertainty disclosed |
| External reference | A text or record outside the frame explicitly concerns a relevant place or polity; the identification is documented |
| External action affecting core | A decision, transaction or movement outside the area materially affects in-scope land or people |
| Regional geological/environmental context | Necessary regional evidence helps explain the local material history; it is not relabelled a local find |
| Custody and research context | A repository, excavation, publication or digitization affects knowledge of in-scope evidence |
| Global context | Limited explanation needed for planetary origin or a measured local process |

## Boundary traps already identified

The States Reorganisation Act’s sections 4–6 must be read together. Section 5 includes the relevant remaining Travancore-Cochin territories, Malabar with named island exclusions, and Kasaragod taluk from South Kanara [S023](../sources/S023.md). Those historic administrative labels must not be mistaken for identical current boundaries.

Mahe’s district administration is under Puducherry [S024](../sources/S024.md). It can be essential historical context without belonging to the core administrative polygon. Similarly, a historic kingdom can contain both core and external places. Classify at the smallest defensible geographic unit rather than excluding an entire document or admitting the whole kingdom.

## Acquisition gate for geometry

Obtain a current boundary dataset with creator, date, coordinate reference system, scale/resolution, legal/administrative basis, stated license and checksum. Check enclaves, islands, inland waters, coast treatment and later boundary changes. Preserve the original and any transformation log where reuse permits. A GIS layer is a representation with a date and resolution, not an automatically authoritative legal instrument.

When spatial filtering is enabled, validation requires `geometry_file` to name an existing readable regular file relative to the repository root. Absolute paths and paths or symlinks escaping the checkout are rejected. The actual file bytes must match `geometry_sha256`. These checks establish file presence and integrity only; they do not establish polygon validity, licensing sufficiency or legal boundary correctness. The acquisition and human cross-check requirements above still apply.

Record geometry version in every automated spatial decision. Keep unresolved locations in a review queue rather than excluding them with a false point-in-polygon result. A boundary name change without a territorial change should not reset the history dataset.

## Temporal gazetteer

Create stable place IDs independent of spelling. Each alias should retain the language, script, transliteration system, source, attestation date and geographic confidence. Modern Kozhikode and a source’s Calicut can be linked with evidence; an ancient port and a modern excavation site need an explicit identification claim, not automatic alias merging.

Store ancient place described, artefact production place, discovery location and current repository separately. Historic coordinates need their original coordinate system; ancient coordinates are not simply modern GIS points.

## Deep time and offshore context

For deep time, the modern frame selects rocks and sediments to investigate; plate reconstruction follows their changing positions. Present coordinates are not ancient coordinates. Offshore basin evidence can explain local erosion and deposition without redefining the offshore basin as current terrestrial Kerala.

Do not equate present legal boundaries with past beaches, exposed continental shelves, river channels or habitats. Maintain separate palaeogeographic layers with source models and uncertainty.
