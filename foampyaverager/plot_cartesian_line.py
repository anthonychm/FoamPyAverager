"""
Generates a line plot of a one-dimensional domain-averaged result
"""

from foampyaverager import loader, line_plotter

def main(path, unique_coords_file, avg_var_file, avg_var_col, x_ticks, y_ticks, save_name):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(path, unique_coords_file, avg_var_file, avg_var_col)

    # Plot cartesian line plot
    lp = line_plotter.CartesianLinePlotter(reader.unique_coords, reader.averaged_var)
    lp.plot_cartesian_line(x_ticks, y_ticks, save_name)


if __name__ == "__main__":
    main("", "unique_Cy", "averaged_U", 1, [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040],
         [0, 2, 4, 6, 8, 10, 12, 14, 16], "test.png")