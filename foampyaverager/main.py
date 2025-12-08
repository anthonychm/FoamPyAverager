"""
Run this file to execute domain averaging in an OpenFOAM case
"""
import loader
import core

def main(case_path, time, avg_var, avg_dirs):

    # Load openfoam files
    reader = loader.Reader(case_path, time)
    for var in ['C', avg_var]:
        reader.read_file(var)
        reader.extract_internal_field(var)
        reader.remove_artifacts(var)
        reader.convert_to_np(var)

    # Perform averaging
    averager = core.Averager(reader, avg_dirs)
    averager.get_unique_coords()
    averager.get_coords_indexes()
    averager.calc_averaged(avg_var)

    # Write unique coordinates and averaged variable
    averager.write_unique_coords()
    averager.write_averaged(avg_var)

if __name__ == '__main__':
    main("../examples/Re_tau945_RANS_M3.64m", 100000, "U", ["z"])