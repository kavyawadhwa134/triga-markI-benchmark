# Materials & nuclear data specification — TRIGA Mark I benchmark

> **Status: PENDING supervisor approval.**
>
> This file will become the single shared source of truth for materials,
> nuclear-data library, and (later) multigroup structure. pcM and pcL
> must use the EXACT same library release — comparison is invalid
> otherwise.
>
> Do NOT assume compositions, densities, temperatures, or library
> releases. Wait for the supervisor-approved specification.
>
> Planned contents:
> - Material compositions and densities (fuel, clad, coolant, reflector)
> - Temperature references for cross-section evaluation
> - Nuclear-data library release, file sizes, md5sum
> - Multigroup structure (shared with pcL, if generated via Cardinal)
>
> Local note (pcM, recorded 2026-09-10, NOT yet approved as the shared
> library): `~/moose/cross_sections/endfb-vii.1-hdf5/` exists locally
> (ENDF/B-VII.1 HDF5, 5.8 GB; `cross_sections.xml` 63 KB,
> md5 `7b757a25054bdc75ad6bb921017b9c66`). Supervisor to confirm whether
> the shared library is this release or ENDF/B-VIII.0.
