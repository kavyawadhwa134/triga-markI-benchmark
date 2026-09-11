# Cardinal/OpenMC TRIGA Mark I pin-cell smoke case.
# Run make_triga_model.py first so model.xml exists in this directory.

[Mesh]
  [pin]
    type = GeneratedMeshGenerator
    dim = 3
    xmin = -2.1175
    xmax = 2.1175
    ymin = -2.1175
    ymax = 2.1175
    zmin = -1.0
    zmax = 1.0
    nx = 1
    ny = 1
    nz = 1
  []
[]

[Problem]
  type = OpenMCCellAverageProblem
  verbose = true
  particles = 500
  inactive_batches = 3
  batches = 10
[]

[Executioner]
  type = Steady
[]

[Postprocessors]
  [k_eff]
    type = KEigenvalue
  []
[]

[Outputs]
  csv = true
[]
