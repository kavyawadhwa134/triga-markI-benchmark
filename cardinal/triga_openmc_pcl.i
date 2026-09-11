# Cardinal/OpenMC TRIGA Mark I pin-cell reference case.
# Conditions match pcL's OpenMC reference: 8000 particles, 70 batches,
# 20 inactive batches, ENDF/B-VIII.0, and 293 K default temperature.
# Generate model.xml first with TRIGA_PARTICLES=8000, TRIGA_BATCHES=70,
# and TRIGA_INACTIVE=20.

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
  particles = 8000
  inactive_batches = 20
  batches = 70
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
