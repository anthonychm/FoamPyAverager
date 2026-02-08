import ast
import argparse
import numpy as np

class ArgsReader:
    class CartAveragerArgsReader:
        def __init__(self):
            self.parser = argparse.ArgumentParser()

        def parse_args(self):
            self.parser.add_argument("--case", required=True, type=str)
            self.parser.add_argument("--time", required=True)
            self.parser.add_argument("--var", required=True, type=str)
            self.parser.add_argument("--directions", required=True, nargs='+')
            self.args = self.parser.parse_args()

    class PolarAveragerArgsReader:
        def __init__(self):
            self.parser = argparse.ArgumentParser()

        def parse_args(self):
            self.parser.add_argument("--case", required=True, type=str)
            self.parser.add_argument("--time", required=True, type=int)
            self.parser.add_argument("--var", required=True, type=str)
            self.parser.add_argument("--origin", required=True, type=str)
            self.parser.add_argument("--axial_dir", required=True, type=str)
            self.parser.add_argument("--num_unique_radii", required=True, type=int)
            self.args = self.parser.parse_args()

        def eval_origin(self):
            self.origin = ast.literal_eval(self.args.origin)

    class LineArgsReader:
        def __init__(self):
            self.parser = argparse.ArgumentParser()

        def parse_args(self):
            self.parser.add_argument("--unique_coords_path", required=True, type=str)
            self.parser.add_argument("--avg_var_path", required=True, type=str)
            self.parser.add_argument("--avg_var_col", required=True, type=int)
            self.parser.add_argument("--x_ticks", required=True)
            self.parser.add_argument("--y_ticks", required=True)
            self.parser.add_argument("--save_name", required=True, type=str)
            self.args = self.parser.parse_args()

        def eval_ticks(self):
            self.x_ticks = ast.literal_eval(self.args.x_ticks)
            self.y_ticks = ast.literal_eval(self.args.y_ticks)

    class ContourArgsReader:
        def __init__(self):
            self.parser = argparse.ArgumentParser()

        def parse_args(self):
            self.parser.add_argument("--unique_coords_path", required=True, type=str)
            self.parser.add_argument("--avg_var_path", required=True, type=str)
            self.parser.add_argument("--avg_var_col", required=True, type=int)
            self.parser.add_argument("--x_ticks", required=True)
            self.parser.add_argument("--y_ticks", required=True)
            self.parser.add_argument("--c_levels", required=True)
            self.parser.add_argument("--cmap", required=True, type=str)
            self.parser.add_argument("--save_name", required=True, type=str)
            self.args = self.parser.parse_args()

        def eval_ticks(self):
            self.x_ticks = ast.literal_eval(self.args.x_ticks)
            self.y_ticks = ast.literal_eval(self.args.y_ticks)
            self.c_levels = ast.literal_eval(self.args.c_levels)


class OpenFoamReader:
    def __init__(self, case_path, folder):
        self.path = case_path + '/' + str(folder) + '/'

    def read_file(self, var):
        # Reads openfoam file
        file = open(self.path + var)
        setattr(self, var, file.read())
        file.close()

    def extract_internal_field(self, var):
        # Extracts internal field from an openfile file
        start = getattr(self, var).find('(') + 1
        end = getattr(self, var).find('boundaryField')
        setattr(self, var, getattr(self, var)[start:end])

    def remove_artifacts(self, var):
        # Remove unwanted artifacts in the extracted internal field
        setattr(self, var, getattr(self, var).replace('(', ''))
        setattr(self, var, getattr(self, var).replace(')', ''))
        setattr(self, var, getattr(self, var).replace(';', ''))

    def convert_to_np(self, var):
        # Convert openfoam string file into numpy array
        arr = np.loadtxt(getattr(self, var).splitlines())
        setattr(self, var, arr)

class AveragedReader:
    def __init__(self, unique_coords_path, avg_var_path, avg_var_col):
        self.unique_coords = np.loadtxt(unique_coords_path)
        self.averaged_var = np.loadtxt(avg_var_path)[:, avg_var_col]
