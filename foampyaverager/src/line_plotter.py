import numpy as np
import matplotlib.pyplot as plt

class CartesianLinePlotter:
    def __init__(self, unique_coords, averaged_var):
        assert unique_coords.ndim == 1
        self.unique_coords = unique_coords
        self.averaged_var = averaged_var

    def plot_cartesian_line(self, x_ticks, y_ticks, save_name):
        plt.plot(self.unique_coords, self.averaged_var, linewidth=1, color='b', marker='x', markeredgecolor='k', clip_on=False)
        plt.xlim(np.min(self.unique_coords), np.max(self.unique_coords))
        plt.ylim(np.min(self.averaged_var), np.max(self.averaged_var))

        plt.xticks(x_ticks, fontsize=14)
        plt.yticks(y_ticks, fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.savefig(save_name)
        plt.show()
