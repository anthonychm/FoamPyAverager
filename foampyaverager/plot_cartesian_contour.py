"""
Run this file to plot a contour of a two-dimensional domain-averaged result
"""

import ast
import argparse
from foampyaverager import loader, contour_plotter

def main(path, unique_coords_file, avg_var_file, avg_var_col, x_ticks, y_ticks, c_levels, cmap):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(path, unique_coords_file, avg_var_file, avg_var_col)

    # Create domain and averaged variable grids
    ccp = contour_plotter.CartesianContourPlotter(reader.unique_coords)
    ccp.create_grids()
    ccp.fill_gridv(reader.averaged_var)

    # Plot cartesian contour
    ccp.plot_cartesian_contour(x_ticks, y_ticks, c_levels, cmap)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, type=str)
    parser.add_argument("--unique_coords_file", required=True, type=str)
    parser.add_argument("--avg_var_file", required=True, type=str)
    parser.add_argument("--avg_var_col", required=True, type=int)
    parser.add_argument("--x_ticks", required=True)
    parser.add_argument("--y_ticks", required=True)
    parser.add_argument("--c_levels", required=True)
    parser.add_argument("--cmap", required=True, type=str)
    args = parser.parse_args()

    x_ticks = ast.literal_eval(args.x_ticks)
    y_ticks = ast.literal_eval(args.y_ticks)
    c_levels = ast.literal_eval(args.c_levels)

    main(args.path, args.unique_coords_file, args.avg_var_file, args.avg_var_col,
         x_ticks, y_ticks, c_levels, args.cmap)
    # main("", "unique_Cx_Cy", "averaged_U", 1, [-0.4, -0.38, -0.36, -0.34, -0.32, -0.30, -0.28, -0.26, -0.24],
    #      [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040], [0, 2, 4, 6, 8, 10, 12, 14, 16], 'plasma')