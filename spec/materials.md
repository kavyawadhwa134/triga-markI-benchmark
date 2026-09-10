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

- **2 groups** (fast + thermal). Thermal cutoff to be fixed in Step 5
  (proposal: 0.625 eV) and recorded here before any coupled run.
- Per region / per group in `nuclearData`: sigmaTot, sigmaA,
  nuSigmaF, chi, scattering matrix (or D); plus beta_i / lambda_i
  for transients.

## TRIGA fuel (to be detailed in Step 5)

- U-ZrH rod, Zr clad, water gap; reflector cells as needed.
- Lattice model lives in `openmc/`; k-eff sanity-checked against
  published TRIGA Mark I values before generating MGXS.
