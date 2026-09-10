# TRIGA Mark I Benchmark — shared project repository

Single shared source of truth for the TRIGA Mark I multiphysics
benchmark (pcM: Cardinal/OpenMC+NekRS+MOOSE reference; pcL: OpenMC
lattice; GeN-Foam diffusion/transients).

## Layout

- `spec/` — shared specifications. `geometry.md`, `materials.md`,
  `operating.md` are PENDING supervisor approval. `hardware.md` records
  the pcM workstation.
- `cardinal/` — pcM working area (OpenMC `.py` inputs, NekRS `.re2`/`.par`,
  MOOSE master `.i`).
- `openmc/` — pcL-side OpenMC inputs reference.
- `genfoam/` — GeN-Foam-side case reference.
- `tools/` — comparison tooling (e.g. `compare.py`: ExodusII/VTK →
  common probe CSVs).
- `results/` — committed probe/CSV outputs for Tier 0 / Tier 2 comparison.

## Scientific rule

Do NOT create an independent TRIGA model or assume final geometry.
pcL and pcM require consistent geometry, operating conditions,
materials, nuclear-data library, and group structure. No production
models until the shared specification is approved.
