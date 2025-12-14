import numpy as np

class CartesianContourPlotter:
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
        i2 = np.searchsorted(self.unique2, self.unique_coords[:, -1])
        self.gridv[i2, i1, :] = averaged_var
        i2 = np.searchsorted(self.unique2, self.unique_coords[:, 1])
        self.gridv[i2, i1] = averaged_var

# class CurvilinearContourPlotter:
