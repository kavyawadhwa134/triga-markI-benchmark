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
| T2 `mesh.i --mesh-only` (lwr_mgxs assembly) | ~7.5 s wall; 48 MB `mesh_in.e` |
| T2 MGXS generation (lwr_mgxs `openmc_mgxs.i`, CASMO_2, 100 particles, 5 inactive / 30 batches, `mpiexec -n 2`) | ~39 s wall; k-eff (combined) = 0.64675 ± 0.00556; 119 MB `openmc_mgxs_out.e` with 2-group XS; Solve Converged. Note: staged `model.xml` patched `C0` → natural C12/C13 (local VIII.0 copy lacks `C0.h5`); Cardinal source untouched |
| T3 standalone NekRS (turbPipe, order 7 stock) | BLOCKED on 8 GB RAM: 4-rank run blew past 45 GB virtual twice and hung the box (test spec wants `min_slots = 16`). Root cause is the launch-time Nek5000 compile, not the solve: each MPI rank spawns a redundant `f951` chain (12–13 GB each at -O2); `turbPipe.o` SIGKILLed (signal 9) even single-rank/-j1 at -O1 (~3.4 GB peak) and -O0 with ~0 free RAM + capped swap (13 GB disk free). Mitigations applied: `standalone_smoke` case (order 3, Serial backend, 2 steps, 2→1 ranks, `OMP_NUM_THREADS=1`, `MAKEFLAGS=-j1`); template `L2 -O2→-O0` patches attempted (install + `_deps` copies; generated makefile is baked into `libnekrs.so`, patched live via watcher — confirmed `L2 = $(G) -O0` active, still SIGKILLed). Retry condition: `sudo purge` + ~2 GB truly free, else a smaller-element case. Implication for STEP 5: full-order NekRS CFD is infeasible on pcM — reduced-order/small-mesh only |
| T4 coupled OpenMC+MOOSE conduction (lwr_solid `solid.i` + openmc sub-app, 1000 particles, 5 inactive / 10 batches, 1 step) | ~11 s wall, peak RSS 1.36 GB; k-eff (combined) = 1.13061 ± 0.01230; Solve Converged (both apps) |

Tutorial 5 (sfr_7pin coupled NekRS+OpenMC, instructions STEP 3) PENDING — feasibility assessment required first (same NekRS build constraint as T3).
