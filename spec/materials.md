# Materials + nuclear data (TRIGA Mark I)

## Cross-section library (MUST be identical on pcL and pcM)

- Release: **ENDF/B-VIII.0 official HDF5 library** (OpenMC development
  team, ACE via NJOY 2016.68).
- Download:
  `https://anl.box.com/shared/static/uhbxlrx7hvxqw27psymfbhi7bx7s6u6a.xz`
  (3.2 GB archive, ~13 GB extracted).
- Contents: incident neutron + photoatomic + atomic relaxation +
  thermal scattering. Neutron temperatures: 250 K, 293.6 K, 600 K,
  900 K, 1200 K, 2500 K.
- pcL path:
  `/home/kavya/Documents/Default Project/nuclear_data/endfb-viii.0-hdf5/`
  with `OPENMC_CROSS_SECTIONS=.../endfb-viii.0-hdf5/cross_sections.xml`
  (set as conda env var on env `openmc`).
- `cross_sections.xml` sha256:
  `ba7f6d5a371b5a8de8157356f8ef5d1c17cb0ed60accccfbc3075f46ae13f489`
- OpenMC: 0.16.0 (`conda create -n openmc -c conda-forge openmc`),
  verified: 690 libraries registered, U235 temperatures OK,
  pincell k-eff test passes.
- Depletion chains (downloaded alongside, same release):
  `nuclear_data/chain-endfb-viii.0-thermal.xml` and
  `chain-endfb-viii.0-fast.xml`.

## Group structure (project-wide, fixed 2026-09-10)

- **2 groups**, fast + thermal, thermal cutoff **0.625 eV**
  (OpenMC groups [0, 0.625 eV] thermal, [0.625 eV, 20 MeV] fast).
- Pin-cell k-inf (ENDF/B-VIII.0, 70 batches / 20 inactive / 8000
  particles): **1.38810 +/- 0.00123**, leakage 0. Sanity: supercritical
  infinite lattice as expected for 20 %-enriched ZrH (finite core goes
  critical via leakage + rods + reflector); cf. storage studies where
  infinite TRIGA arrays stay supercritical below ~6.5 cm pitch.
- Homogenized constants (`genfoam/constant/neutroRegion/nuclearData`,
  SI units), zone0:
  removal (4.77341, 8.4919) 1/m; nuSigmaF (0.379899, 12.5219) 1/m;
  scatter ((39.7524, 4.22693), (0.023426, 201.932)) 1/m;
  D (0.00749023, 0.00158363) m; chi (1, 0); IV (6.63e-06, 3.32e-04) s/m.
- Kinetics: U-235 Keepin 6-group lambdas/betas (TRIGA is U-235 driven;
  NOT the Pu-like tutorial values). discFactor = 1, chiDelayed = (1 0).
- Smoke test: constants run in GeN-Foam diffusion (2D channel case),
  neutronics converges, k = 1.331 (consistent with k-inf minus leakage).

## TRIGA fuel (to be detailed in Step 5)

- U-ZrH rod, Zr clad, water gap; reflector cells as needed.
- Lattice model lives in `openmc/`; k-eff sanity-checked against
  published TRIGA Mark I values before generating MGXS.
