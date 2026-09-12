# cardinal/ — pcM working area

Independent TRIGA Mark I reference calculation using Cardinal (OpenMC + MOOSE + NekRS).
Produced **without reference to the GeN-Foam case in `../genfoam/`** or to any pcL result.

Full history and tags: `github.com/kavyawadhwa134/pcm-triga-cardinal`
(independence tag `pcm-independent-v1` marks the state before any pcL file was read).

## Layout

| Path | Contents |
|---|---|
| `openmc/` | Materials, geometry, settings, tallies, run and post-processing (Python API) |
| `openmc/temperature_coefficient.py` | Fuel temperature-coefficient sweep — the TRIGA physics check |
| `moose/mesh.i` | Solid mesh: fuel + clad stitched into direct contact (no gap in the spec) |
| `coupling/` | Cardinal master input (`solid.i`), OpenMC sub-app (`openmc.i`), 3-D model generator |
| `nekrs/` | Coolant subchannel: mesh generators, `.re2`, `.par`, `.udf`, `.oudf` |
| `scripts/` | Environment audit and run scripts (portable macOS/Linux) |
| `docs/` | Runbook, porting notes, and pcM's specification record |

## Running

```bash
./scripts/audit_environment.sh          # check the environment first
./scripts/run_openmc.sh unitcell baseline
./scripts/run_coupled.sh production 8
./scripts/run_nekrs.sh 8                # never fewer than 2 ranks — see docs/RUNBOOK.md
```

`docs/RUNBOOK.md` is self-contained and documents four traps that cost significant time,
including a single-rank NekRS memory failure that exhausted an 8 GiB machine.
