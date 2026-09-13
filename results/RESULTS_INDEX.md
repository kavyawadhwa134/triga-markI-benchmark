# Results index

This directory holds both calculations of the TRIGA Mark I benchmark. Files are prefixed
by the code that produced them.

## Reports

| File | Contents |
|---|---|
| `TRIGA_Reference_Report.pdf` | **Combined report** — problem definition, both calculations presented separately, then the comparison, verification status, limitations and reproduction |
| `CROSSCODE_COMPARISON.md` | Case-by-case comparison, 12 cases, with working |
| `crosscode_comparison.csv` | The same comparison, machine-readable |
| `CARDINAL_RESULTS.md` | Cardinal result package |
| `latex/` | LaTeX source and figures for the combined report |

## GeN-Foam / OFFBEAT — 2-group diffusion, finite volume

| File | Contents |
|---|---|
| `validation_step2.csv` | Solver acceptance (SmallESFR, point kinetics) |
| `validation_step5.csv` | Two-group lattice constants and the diffusion smoke test |
| `validation_step6.csv` | Core eigenvalue and transient summary |
| `transient_rod_power.csv` | +0.5 $ transient time history |
| `paraview_*.png` | Field visualisations |

Case inputs: `../genfoam/`

## Cardinal / OpenMC / MOOSE / NekRS — continuous-energy Monte Carlo

| File | Contents |
|---|---|
| `cardinal_openmc_unitcell.csv` | k-infinity, all configurations and seeds |
| `cardinal_openmc_core.csv`, `_core_homog.csv` | k-effective, heterogeneous and homogenised |
| `cardinal_fuel_temperature_coefficient.csv` | Temperature-coefficient sweep, 296–1000 K |
| `cardinal_coupled_smoke.csv`, `cardinal_coupled_production_*.csv` | Coupled results per Picard iteration |
| `cardinal_thermal_profiles.csv` | Axial and radial temperature profiles |
| `cardinal_nekrs_convergence.csv` | CFD convergence history, 201 samples |
| `cardinal_pin_power_core.csv`, `cardinal_power_*.csv` | Power distributions |
| `figures/` | Report figures, regenerable from the CSVs above |

Case inputs: `../cardinal/`

## Reading the comparison

The two calculations solve **different equations**. Where they are methodologically
comparable — Monte Carlo pin cell against Monte Carlo pin cell — they agree to **280 pcm**,
inside the 500 pcm acceptance criterion. Larger differences trace to homogenisation,
solution method, or scope, and are decomposed in the combined report.

**Neither result is validated.** No experimental data was used on either side, and both
cores are bare, without reflector or control rods.
