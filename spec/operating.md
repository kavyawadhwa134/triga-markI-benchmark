# Operating conditions — Tier-1 TRIGA (fixed 2026-09-10)

## Tier-1 scope (this step)

Single homogenized zone (core porous + sub-scale U-ZrH pins), 2D slab
0.495 m wide x 0.60 m tall x 0.04235 m thick, vacuum neutronic BCs,
forced inlet (Tier-1 stand-in for natural circulation).

## Steady state

- Power: **250 kWth** (`0/uniform/reactorState`: power 250000).
- Coolant: demineralized water, inlet **293 K**, pRef 100000 Pa.
- Inlet velocity 0.2 m/s (forced; Tier-2 replaces with
  buoyancy-driven pool loop), outlet zeroGradient.
- Buoyancy on (g = (0 0 -9.81)), laminar, 1 atm.
- Acceptance: coupled run converges (neutroResidual small), report
  k_eff, power tilt, max fuel centerline T. Expect k > 1 (bare
  homogenized box, vacuum BCs); single zone => flat tilt by
  construction; Tmax must stay well below the 750 C U-ZrH/SS
  steady-state practice limit.

## Transient (rod withdrawal)

- Point-kinetics from steady flux shape; external reactivity ramp
  **+0.5 $ in 0.5 s** (betaTot = 0.0065 => +0.00325 dk/k), then hold.
- Fuel Doppler feedbackCoeffTFuel = **-1.0e-4 dk/k/K** (TRIGA prompt
  coefficient, UT overview). Others 0; driveline coeff 0.
- Expect power excursion turned by Doppler, settles to new level;
  record peak power + peak fuel T in results/.
