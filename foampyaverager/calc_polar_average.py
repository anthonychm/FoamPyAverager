"""
Run this file to execute domain averaging
in cylindrical coordinates for an OpenFOAM case
"""

from foampyaverager import loader, core

def main(case_path, time, avg_var, origin, axial_dir, num_unique_radii):

    # Load openfoam files
    reader = loader.OpenFoamReader(case_path, time)
    for var in ['C', avg_var]:
        reader.read_file(var)
        reader.extract_internal_field(var)
        reader.remove_artifacts(var)
        reader.convert_to_np(var)

    # Convert cartesian coordinates to polar coordinates
    averager = core.PolarAverager(reader, origin, axial_dir)
    averager.get_polar_coords()

    # Perform averaging
    averager.get_unique_radii(num_unique_radii)
    averager.calc_averaged(avg_var)

    # Write unique radii and averaged variable
    averager.write_unique_radii()
    averager.write_averaged(avg_var)

if __name__ == '__main__':
    main("../examples/pipeCyclic", 227, "U", [0, 0], "x", 5)