"""
Run this file to plot a contour of a two-dimensional domain-averaged result
"""

from foampyaverager import loader, contour_plotter

def main(path, unique_coords_file, avg_var_file, avg_var_col, x_ticks, y_ticks, c_levels, cmap, save_name):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(path, unique_coords_file, avg_var_file, avg_var_col)

    # Create domain and averaged variable grids
    cp = contour_plotter.ContourPlotter(reader.unique_coords)
    cp.create_grids()
    cp.fill_gridv(reader.averaged_var)

    # Plot cartesian contour
    cp.plot_cartesian_contour(x_ticks, y_ticks, c_levels, cmap, save_name)


if __name__ == "__main__":
    args_reader = loader.ArgsReader.ContourArgsReader()
    args_reader.parse_args()
    args_reader.eval_ticks()

    main(args_reader.args.path, args_reader.args.unique_coords_file,
         args_reader.args.avg_var_file, args_reader.args.avg_var_col,
         args_reader.x_ticks, args_reader.y_ticks, args_reader.c_levels,
         args_reader.args.cmap, args_reader.args.save_name)
    # main("", "unique_Cx_Cy", "averaged_U", 0, [-0.4, -0.38, -0.36, -0.34, -0.32, -0.30, -0.28, -0.26, -0.24],
    #      [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040], [0, 2, 4, 6, 8, 10, 12, 14, 16],
    #      'plasma', 'test.png')