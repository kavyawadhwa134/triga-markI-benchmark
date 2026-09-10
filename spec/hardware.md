# pcM hardware & software record — TRIGA Mark I benchmark

Recorded: 2026-09-10. Machine: pcM (Cardinal workstation, Mac).

## Machine

| Item | Value |
|---|---|
| CPU | Apple M2 (`sysctl machdep.cpu.brand_string`) |
| Logical cores | 8 (`sysctl hw.ncpu`) |
| RAM | 8 GB (`sysctl hw.memsize`) |
| Model | Mac14,2 (MacBook Air, laptop — thermally throttles; plug in charger) |
| macOS | 26.6.2 (build 25G83) |
| Displays | Built-in Liquid Retina + BenQ GW2790 1080p (informational) |

## GPU / NekRS backend

- GPU: Apple M2, 8 cores, Metal 4 (`system_profiler SPDisplaysDataType`).
- Apple-silicon GPUs are NOT usable by NekRS (CUDA/HIP only) → **CPU-only**.
- No `nek`/`nrsmpi` tools in the `moose` conda env bin (expected:
  Cardinal vendors its own NekRS build under
  `~/moose/cardinal/build/nekrs/`).
- Implication: plan for the REDUCED model (instructions STEP 5, option B —
  symmetry sector or unit-cell reference).

## Software / environments

| Item | Value |
|---|---|
| conda | 24.11.0 |
| `moose` env python | 3.14.6 (conda-forge); MOOSE toolchain from `https://conda.software.inl.gov/public` (`moose-dev`, `moose-libmesh`, `moose-petsc`, `moose-tools`, `moose-wasp`) |
| `openmc` env python | 3.13.1, `openmc` 0.15.1.dev0 (pip) |
| Cardinal exe | `~/moose/cardinal/cardinal-opt` (Mach-O arm64), run under the `moose` env |
| Cardinal version | `snapshot-20-10-27-54609-g8b05495ce0` (`cardinal-opt --version`) |
| OpenMC in `moose` env | NOT installed as a python module (expected — Cardinal builds its own OpenMC under `~/moose/cardinal/build/openmc/`) |
| Cross sections (local, unapproved) | `~/moose/cross_sections/endfb-vii.1-hdf5/` (ENDF/B-VII.1 HDF5, 5.8 GB) |

## Verification timings (wall-clock, 2026-09-10)

| Check | Wall time |
|---|---|
| `conda run -n moose cardinal-opt --version` | ~2.4 s |
| `conda run -n openmc python -c "import openmc"` | ~2.3 s |
| T1 `mesh.i --mesh-only` (lwr_solid, `~/cardinal_tutorials/`) | ~2.4 s |
| T1 standalone OpenMC eigenvalue (lwr_solid `openmc.i`, 500 particles, 50 inactive / 100 batches, VIII.0 CE) | ~11 s wall; k-eff (combined) = 1.15162 ± 0.00623; Solve Converged |

Tutorials 2–5 (instructions STEP 3) are PENDING; timings will be
appended here as they complete.
