"""Generate a Cardinal-compatible OpenMC model for the TRIGA pin benchmark.

This is the Cardinal/OpenMC stage of the benchmark.  It intentionally mirrors
openmc/triga_pin.py while exporting one combined model.xml for Cardinal.
"""
import os
import openmc

HERE = os.path.dirname(os.path.abspath(__file__))
PITCH = 4.235
R_FUEL = 1.815
R_CLAD = 1.866


def build_model(particles=500, batches=10, inactive=3):
    fuel = openmc.Material(name="uzrh_fuel", material_id=1)
    fuel.set_density("g/cc", 6.0)
    fuel.add_nuclide("U235", 1.7, "wo")
    fuel.add_nuclide("U238", 6.8, "wo")
    fuel.add_element("Zr", 89.862, "wo")
    fuel.add_nuclide("H1", 1.638, "wo")
    fuel.add_s_alpha_beta("c_H_in_ZrH")
    fuel.add_s_alpha_beta("c_Zr_in_ZrH")

    clad = openmc.Material(name="ss304", material_id=2)
    clad.set_density("g/cc", 7.9)
    clad.add_element("Fe", 70.5, "wo")
    clad.add_element("Cr", 19.0, "wo")
    clad.add_element("Ni", 9.0, "wo")
    clad.add_element("Mn", 1.0, "wo")
    clad.add_element("Si", 0.5, "wo")

    water = openmc.Material(name="water", material_id=3)
    water.set_density("g/cc", 1.0)
    water.add_nuclide("H1", 2.0, "ao")
    water.add_nuclide("O16", 1.0, "ao")
    water.add_s_alpha_beta("c_H_in_H2O")

    fuel_cyl = openmc.ZCylinder(r=R_FUEL)
    clad_cyl = openmc.ZCylinder(r=R_CLAD)
    fuel_cell = openmc.Cell(name="fuel", fill=fuel, region=-fuel_cyl)
    clad_cell = openmc.Cell(name="clad", fill=clad,
                            region=+fuel_cyl & -clad_cyl)
    water_cell = openmc.Cell(name="water", fill=water, region=+clad_cyl)
    pin = openmc.Universe(name="pin", cells=[fuel_cell, clad_cell, water_cell])

    lattice = openmc.RectLattice(name="core_lat")
    lattice.pitch = (PITCH, PITCH)
    lattice.lower_left = (-PITCH / 2, -PITCH / 2)
    lattice.universes = [[pin]]

    xmin = openmc.XPlane(-PITCH / 2, boundary_type="reflective")
    xmax = openmc.XPlane(PITCH / 2, boundary_type="reflective")
    ymin = openmc.YPlane(-PITCH / 2, boundary_type="reflective")
    ymax = openmc.YPlane(PITCH / 2, boundary_type="reflective")
    root = openmc.Cell(fill=lattice, region=+xmin & -xmax & +ymin & -ymax)

    geometry = openmc.Geometry(openmc.Universe(cells=[root]))
    settings = openmc.Settings()
    settings.run_mode = "eigenvalue"
    settings.particles = particles
    settings.batches = batches
    settings.inactive = inactive
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Box(
            [-PITCH / 2, -PITCH / 2, -1.0],
            [PITCH / 2, PITCH / 2, 1.0]))

    materials = openmc.Materials([fuel, clad, water])
    return openmc.Model(geometry, materials, settings)


if __name__ == "__main__":
    model = build_model()
    model.export_to_xml(directory=HERE)
    print("Wrote Cardinal model.xml for TRIGA pin-cell smoke case")
