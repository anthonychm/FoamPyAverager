"""
Generates a line plot of a one-dimensional domain-averaged result
"""
import argparse
import ast

from foampyaverager import loader, line_plotter

def main(path, unique_coords_file, avg_var_file, avg_var_col, x_ticks, y_ticks, save_name):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(path, unique_coords_file, avg_var_file, avg_var_col)

    # Plot cartesian line plot
    lp = line_plotter.CartesianLinePlotter(reader.unique_coords, reader.averaged_var)
    lp.plot_cartesian_line(x_ticks, y_ticks, save_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, type=str)
    parser.add_argument("--unique_coords_file", required=True, type=str)
    parser.add_argument("--avg_var_file", required=True, type=str)
    parser.add_argument("--avg_var_col", required=True, type=int)
    parser.add_argument("--x_ticks", required=True)
    parser.add_argument("--y_ticks", required=True)
    parser.add_argument("--save_name", required=True, type=str)
    args = parser.parse_args()

    x_ticks = ast.literal_eval(args.x_ticks)
    y_ticks = ast.literal_eval(args.y_ticks)

    main(args.path, args.unique_coords_file, args.avg_var_file, args.avg_var_col, x_ticks, y_ticks, args.save_name)
    # main("", "unique_Cy", "averaged_U", 1, [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040],
    #      [0, 2, 4, 6, 8, 10, 12, 14, 16], "test.png")