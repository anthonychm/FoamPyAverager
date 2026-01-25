import numpy as np
from sklearn.cluster import KMeans

class PolarAverager:
    def __init__(self, reader, origin, ax_col_dir):
        for name, value in reader.__dict__.items():
            setattr(self, name, value)
        self.origin = origin
        self.dirs_dict = {'x': 0, 'y': 1, 'z': 2}
        if ax_col_dir is not None:
            self.ax_col_idx = self.dirs_dict[ax_col_dir]
            self.C = np.delete(self.C, self.ax_col_idx, axis=1)

    def get_polar_coords(self):
        # Convert cartesian coordinates to polar coordinates
        self.C[:, 0] -= self.origin[0]
        self.C[:, 1] -= self.origin[1]
        self.radii = np.sqrt((self.C[:, 0]**2) + (self.C[:, 1]**2))
        self.theta = np.atan2(self.C[:, 1], self.C[:, 0])

    def get_unique_radii(self, n_groups):
        # Get representative unique radii in the domain using k means clustering
        self.radii = np.array(self.radii).reshape(-1, 1)
        kmeans = KMeans(n_clusters=n_groups)
        self.radii_idx = kmeans.fit_predict(self.radii)

        unique_radii_idx = np.unique(self.radii_idx)
        self.idx_to_average_radii = {i: self.radii[self.radii_idx == i].mean() for i in unique_radii_idx}
        self.radii = [self.idx_to_average_radii[i] for i in self.radii_idx]

class CartesianAverager:
    def __init__(self, reader, avg_dirs):
        for name, value in reader.__dict__.items():
            setattr(self, name, value)
        self.avg_dirs = avg_dirs
        self.dirs_dict = {'x': 0, 'y': 1, 'z': 2}
        self.avg_col_idx = [self.dirs_dict[d] for d in self.avg_dirs]

    def get_unique_coords(self):
        # Get unique coordinates in the non-averaging directions
        self.plane_C = np.delete(self.C, self.avg_col_idx, axis=1)
        self.unique_coords, self.unique_coords_inv = np.unique(self.plane_C, axis=0, return_inverse=True)

    def create_unique_coords_dict(self):
        return {tuple(c): None for c in self.unique_coords}

    def get_coords_indexes(self):
        # Get a list of indexes for each unique coordinate
        self.unique_coords_idx = self.create_unique_coords_dict()
        for i, c in enumerate(self.unique_coords_idx.keys()):
            self.unique_coords_idx[c] = np.where(self.unique_coords_inv == i)[0]

    def calc_averaged(self, avg_var):
        # Calculate averaged values of the averaging variable
        self.unique_coords_avg = self.create_unique_coords_dict()
        for c in self.unique_coords_avg.keys():
            vals = getattr(self, avg_var)[self.unique_coords_idx[c]]
            self.unique_coords_avg[c] = vals.mean(axis=0)
        self.averaged_var = np.vstack(list(self.unique_coords_avg.values()))

    def write_unique_coords(self):
        # Write unique coordinates to file
        plane_dirs = list(self.dirs_dict.keys())
        for i in self.avg_dirs:
            plane_dirs.remove(i)
        coords_file_name = "unique" + "".join(f"_C{i}" for i in plane_dirs)
        np.savetxt(coords_file_name, self.unique_coords)

    def write_averaged(self, avg_var):
        # Write averaged variable to file
        np.savetxt("averaged_" + avg_var, self.averaged_var)
