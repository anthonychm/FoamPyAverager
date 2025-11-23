"""
Run this file to execute domain averaging in an OpenFOAM case
"""
import loader

def main(case_path, time, avg_var, avg_dirs):

    # Load openfoam files
    reader = loader.Reader(case_path, time)
    for var in ['C', avg_var]:
        reader.read_file(var)
        reader.extract_internal_field(var)
        reader.remove_artifacts(var)
        reader.convert_to_np(var)

if __name__ == '__main__':
    main("../examples/Re_tau945_RANS_M3.64m", 100000, "U", ["z"])