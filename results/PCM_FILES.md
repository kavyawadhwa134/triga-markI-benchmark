# Results index — which files belong to which side

`results/` now holds both calculations. Files are prefixed by origin.

## pcM — Cardinal / OpenMC / MOOSE / NekRS (continuous-energy Monte Carlo)

| File | Contents |
|---|---|
| `pcM_TRIGA_Report.pdf` | **Formal report**, 15 pages — scope, methodology, results, verification status, full comparison |
| `PCM_PCL_COMPARISON.md` | Case-by-case pcM/pcL comparison, 12 cases |
| `pcm_pcl_comparison.csv` | The same comparison, machine-readable |
| `PCM_RESULTS.md` | pcM result package |
| `pcm_openmc_unitcell.csv` | k-infinity, all configurations and seeds |
| `pcm_openmc_core.csv` | k-effective, heterogeneous bare core |
| `pcm_openmc_core_homog.csv` | k-effective, homogenised variants |
| `pcm_fuel_temperature_coefficient.csv` | Temperature-coefficient sweep, 296–1000 K |
| `pcm_coupled_smoke.csv`, `pcm_coupled_production_*_vii1.csv` | Coupled neutronics–conduction per Picard iteration |
| `pcm_thermal_profiles.csv` | Axial and radial temperature profiles |
| `pcm_nekrs_convergence.csv` | CFD convergence history, 201 samples |
| `pcm_pin_power_core.csv`, `pcm_power_*.csv` | Power distributions |
| `figures/` | Report figures (regenerate from the CSVs above) |

## pcL — GeN-Foam / OFFBEAT (2-group diffusion)

| File | Contents |
|---|---|
| `validation_step2.csv` | Solver acceptance (SmallESFR, point kinetics) |
| `validation_step5.csv` | Lattice constants and `genfoam_smoke_keff` |
| `validation_step6.csv` | Core eigenvalue and transient summary |
| `transient_rod_power.csv` | +0.5 $ transient time history |
| `paraview_*.png` | GeN-Foam field visualisations |

## Reading the comparison

The two calculations solve **different equations**. Where they are methodologically
comparable — Monte Carlo pin cell against Monte Carlo pin cell — they agree to **280 pcm**,
inside the 500 pcm threshold. Larger differences trace to homogenisation, solution method,
or scope, and are decomposed in `PCM_PCL_COMPARISON.md`.

**Neither result is validated.** No experimental data was used on either side, and both
cores are bare without reflector or control rods.
