"""
Run this file to execute domain averaging in an OpenFOAM case
"""
import argparse
from foampyaverager import loader, core

def main(case_path, time, avg_var, avg_dirs):

    # Load openfoam files
    reader = loader.OpenFoamReader(case_path, time)
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
    parser = argparse.ArgumentParser(description="Domain averager")
    parser.add_argument("--case", required=True, type=str, help="Your OpenFOAM case")
    parser.add_argument("--time", required=True, help="Time folder for averaging")
    parser.add_argument("--var", required=True, type=str, help="Variable to be averaged")
    parser.add_argument("--directions", required=True, nargs='+', help="Direction of averaging")
    args = parser.parse_args()
    main(args.case, args.time, args.var, args.directions)