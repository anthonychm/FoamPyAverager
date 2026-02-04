"""
Run this file to plot a contour of a two-dimensional
domain-averaged result on an unstructured triangular grid
"""

from foampyaverager import loader, contour_plotter

def main(path, unique_coords_file, avg_var_file, avg_var_col,
         x_ticks, y_ticks, c_levels, cmap, save_name):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(path, unique_coords_file,
                                   avg_var_file, avg_var_col)

    # Plot tri-contour
    cp = contour_plotter.ContourPlotter(reader.unique_coords)
    cp.plot_tri_contour(reader.averaged_var, x_ticks, y_ticks,
                        c_levels, cmap, save_name)


if __name__ == "__main__":
    args_reader = loader.ArgsReader.ContourArgsReader()
    args_reader.parse_args()
    args_reader.eval_ticks()
    main(args_reader.args.path, args_reader.args.unique_coords_file,
         args_reader.args.avg_var_file, args_reader.args.avg_var_col,
         args_reader.x_ticks, args_reader.y_ticks, args_reader.c_levels,
         args_reader.args.cmap, args_reader.args.save_name)