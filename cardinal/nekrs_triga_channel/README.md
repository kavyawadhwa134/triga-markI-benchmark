# Reduced TRIGA NekRS channel surrogate

This case is a reduced NekRS hydraulic surrogate for the pcL Tier-1 TRIGA
conditions. It reuses the validated `turbPipe.re2` computational channel so
the GPU path can be exercised without attempting a whole-core mesh.

Matched operating condition:

- inlet velocity: 0.2 m/s
- inlet scalar temperature: 293 K
- CUDA backend
- one MPI rank for the first GPU smoke run

The mesh is not a TRIGA full-core mesh and the scalar is a passive surrogate;
this case is for NekRS/Cardinal GPU bring-up. It must not be reported as the
full 250 kWth TRIGA thermal-hydraulics solution.
