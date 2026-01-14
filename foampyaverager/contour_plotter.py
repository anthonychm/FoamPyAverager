import numpy as np
import matplotlib.pyplot as plt

class ContourPlotter:
    def __init__(self, unique_coords):
        assert unique_coords.shape[1] == 2
        self.unique_coords = unique_coords
        self.unique1 = np.unique(self.unique_coords[:, 0])
        self.unique2 = np.unique(self.unique_coords[:, 1])
        self.n1, self.n2 = len(self.unique1), len(self.unique2)

    def create_grids(self):
        # Create cartesian and averaged variable grid
        self.grid1 = np.tile(self.unique1, (self.n2, 1))
        self.grid2 = np.tile(np.expand_dims(self.unique2, axis=1), (1, self.n1))
        self.gridv = np.full((self.n2, self.n1), np.nan)

    def fill_gridv(self, averaged_var):
        # Fill averaged variable grid
        i1 = np.searchsorted(self.unique1, self.unique_coords[:, 0])
        i2 = np.searchsorted(self.unique2, self.unique_coords[:, 1])
        self.gridv[i2, i1] = averaged_var

    def plot_cartesian_contour(self, x_ticks, y_ticks, c_levels, cmap, save_name):
        # Plot cartesian contour
        cont = plt.contourf(self.grid1, self.grid2, self.gridv, cmap=cmap, extend='both', levels=c_levels)
        pk = PlotKit()
        pk.set_axis_lims(self.grid1, self.grid2)
        pk.set_ticks(x_ticks, y_ticks, 14)
        pk.set_cbar(cont, c_levels, 14, 'vertical')
        plt.savefig(save_name)
        plt.show()

    def plot_tri_contour(self, averaged_var, x_ticks, y_ticks, c_levels, cmap, save_name):
        # Plot tri-contour
        cont = plt.tricontourf(self.unique_coords[:, 0], self.unique_coords[:, 1], averaged_var,
                               cmap=cmap, extend='both', levels=c_levels)
        pk = PlotKit()
        pk.set_axis_lims(self.unique1, self.unique2)
        pk.set_ticks(x_ticks, y_ticks, 14)
        pk.set_cbar(cont, c_levels, 14, 'vertical')
        plt.savefig(save_name)
        plt.show()


class PlotKit:
    @staticmethod
    def set_axis_lims(x, y):
        plt.xlim(np.min(x), np.max(x))
        plt.ylim(np.min(y), np.max(y))

    @staticmethod
    def set_ticks(x_ticks, y_ticks, fontsize):
        plt.xticks(x_ticks, fontsize=fontsize)
        plt.yticks(y_ticks, fontsize=fontsize)
        plt.tick_params(axis='both', which='major', labelsize=fontsize)

    @staticmethod
    def set_cbar(cont, c_levels, fontsize, cbar_orient):
        cbar = plt.colorbar(cont, orientation=cbar_orient)
        cbar.set_ticks(c_levels)
        cbar.set_ticklabels(c_levels)
        cbar.ax.tick_params(labelsize=fontsize)
