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
    args_reader = loader.ArgsReader.LineArgsReader()
    args_reader.parse_args()
    args_reader.eval_ticks()
    main(args_reader.args.path, args_reader.args.unique_coords_file,
         args_reader.args.avg_var_file, args_reader.args.avg_var_col,
         args_reader.x_ticks, args_reader.y_ticks, args_reader.args.save_name)