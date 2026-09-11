# pcM Cardinal TRIGA stage

This directory contains the Cardinal/OpenMC pin-cell stage corresponding to
the pcL TRIGA reference. It uses the same TRIGA U-ZrH / SS304 / water pin,
ENDF/B-VIII.0 cross sections, 293 K default temperature, and reflective
infinite-lattice boundaries.

The low-memory smoke case is `triga_openmc.i` (500 particles, 10 batches,
3 inactive). The pcL-matched reference input is `triga_openmc_pcl.i` (8000
particles, 70 batches, 20 inactive). `make_triga_model.py` must be run in
this directory first; it writes the combined OpenMC `model.xml` that Cardinal
reads.

These are the Cardinal/OpenMC neutronics inputs. The full pcL Tier-1
250 kWth homogenized core and the NekRS thermal-hydraulics coupling are not
represented by this pin-cell stage yet; they require a Cardinal full-core mesh
and NekRS case before production coupling is scientifically valid.
