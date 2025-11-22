"""
Run this file to execute domain averaging in an OpenFOAM case
"""
import loader

def main(case_path, time, avg_var, avg_dir):
    reader = loader.Reader(case_path, time, avg_var)


if __name__ == '__main__':
    main("../examples/Re_tau945_RANS_M3.64m", 100000, "U", "z")