# TRIGA Mark I benchmark — shared spec (pcL + pcM)

Target: TRIGA Mark I multiphysics (neutronics + thermal-hydraulics).
This repo is cloned on pcL (GeN-Foam/foamForNuclear side) and pcM
(OpenMC + Cardinal side). See `pcL.md` / pcM instructions for roles.

Layout:

- `spec/` — geometry, materials, operating, hardware (this folder)
- `openmc/` — lattice model + group-constant generation scripts
- `genfoam/` — GeN-Foam case for the TRIGA core
- `cardinal/` — populated on pcM
- `tools/` — converters (`openmc2genfoam.py`) + comparison scripts
- `results/` — committed reference CSVs from BOTH machines

Commit rule: small CSV/probe outputs and all inputs are committed.
Never commit big VTK/Exodus meshes or time directories.
Remote: pcM owns the canonical remote; pcL adds it as `origin`
once the link is provided.
