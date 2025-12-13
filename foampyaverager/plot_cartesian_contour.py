"""
Run this file to plot a contour of a two-dimensional domain-averaged result
"""

from foampyaverager import loader
from contour_plotter import CartesianContourPlotter

def main(pth, unique_coords_file, avg_var_file):
    # Get unique coordinates and averaged variable data
    reader = loader.AveragedReader(pth, unique_coords_file, avg_var_file)
    cgc = ContourGridCreator(reader.unique_coords)
    ccp = CartesianContourPlotter(reader.unique_coords)
    ccp.create_grids()


if __name__ == "__main__":
    main("", "unique_Cx_Cy", "averaged_U")