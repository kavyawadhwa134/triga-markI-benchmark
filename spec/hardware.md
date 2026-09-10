# Hardware / software baseline (pcL)

- CPU: 4 cores; RAM ~11 GB (`nproc`=4).
- OpenFOAM: **ESI/OpenCFD v2606** at `~/openfoam/OpenFOAM-v2606`
  (`WM_PROJECT_VERSION=v2606`). Default shell also has Foundation v9
  at `/opt/openfoam9` — NEVER build/run foamForNuclear under v9.
  Aliases: `of2606` (ESI v2606), `of9` (Foundation v9).
- Solver: **foamForNuclear** (GeN-Foam successor; old
  `foam-for-nuclear/GeN-Foam` repo is archived), master `fc47611`,
  at `~/foamForNuclear`, built 2026-09-08 under v2606.
  Binaries: `GeN-Foam`, `offbeat` in
  `~/OpenFOAM/kavya-v2606/platforms/linux64GccDPInt32Opt/bin`.
- OpenMC 0.16.0 in conda env `openmc` (see materials.md).
- ParaView: bundled 5.6 at `/opt/paraviewopenfoam56`
  (`pvpython`, `paraFoam`, `foamToVTK`); headless offscreen rendering
  verified (see `results/` screenshots).
- MPI: Open MPI; on this box use `mpirun --oversubscribe` for `-np 4`
  (slot detection undercounts).
