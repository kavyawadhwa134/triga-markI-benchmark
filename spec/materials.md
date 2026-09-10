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
> Agreed shared library (supervisor, 2026-09-10): **ENDF/B-VIII.0 HDF5,
> same release both sides (pcM + pcL).**
>
> pcM copy: `/Users/kavyawadhwa/Documents/Digital Twin/nuclear_data/endfb-viii.0-hdf5/`
> (13 GB; `cross_sections.xml` 46 KB,
> md5 `7d5aafd5badbc1882d01c7ec5e33beb6`).
> `OPENMC_CROSS_SECTIONS` points at this `cross_sections.xml`.
> pcL to confirm identical md5 on its side.
>
> NOT the shared library: `~/moose/cross_sections/endfb-vii.1-hdf5/`
> (ENDF/B-VII.1 HDF5, 5.8 GB) also exists on pcM but must NOT be used
> for benchmark runs.
