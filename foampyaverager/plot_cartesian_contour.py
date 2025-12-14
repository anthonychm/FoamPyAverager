"""
Run this file to plot a contour of a two-dimensional domain-averaged result
"""

from foampyaverager import loader
from contour_plotter import CartesianContourPlotter

def main(pth, unique_coords_file, avg_var_file, avg_var_col, x_ticks, y_ticks, c_levels, cmap):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(pth, unique_coords_file, avg_var_file, avg_var_col)

    # Create domain and averaged variable grids
    ccp = CartesianContourPlotter(reader.unique_coords)
    ccp.create_grids()
    ccp.fill_gridv(reader.averaged_var)

    # Plot cartesian contour
    ccp.plot_cartesian_contour(x_ticks, y_ticks, c_levels, cmap)


if __name__ == "__main__":
    main("", "unique_Cx_Cy", "averaged_U", 1, [-0.4, -0.38, -0.36, -0.34, -0.32, -0.30, -0.28, -0.26, -0.24],
         [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040], [0, 2, 4, 6, 8, 10, 12, 14, 16], 'plasma')