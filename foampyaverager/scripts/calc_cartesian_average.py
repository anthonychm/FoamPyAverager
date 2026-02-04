"""
Run this file to execute domain averaging in an OpenFOAM case
"""

from foampyaverager.src import loader, core

def main(case_path, time, avg_var, avg_dirs):

    # Load openfoam files
    reader = loader.OpenFoamReader(case_path, time)
    for var in ['C', avg_var]:
        reader.read_file(var)
        reader.extract_internal_field(var)
        reader.remove_artifacts(var)
        reader.convert_to_np(var)

    # Perform averaging
    averager = core.CartesianAverager(reader, avg_dirs)
    averager.get_unique_coords()
    averager.get_coords_indexes()
    averager.calc_averaged(avg_var)

    # Write unique coordinates and averaged variable
    averager.write_unique_coords()
    averager.write_averaged(avg_var)

if __name__ == '__main__':
    args_reader = loader.ArgsReader.CartAveragerArgsReader()
    args_reader.parse_args()
    main(args_reader.args.case, args_reader.args.time,
         args_reader.args.var, args_reader.args.directions)