import numpy as np

class Averager:
    def __init__(self, reader, avg_dirs):
        for name, value in reader.__dict__.items():
            setattr(self, name, value)
        self.avg_dirs = avg_dirs
        self.dirs_dict = {'x': 0, 'y': 1, 'z': 2}
        self.avg_col_idx = [self.dirs_dict[d] for d in self.avg_dirs]

    def get_unique_coords(self):
        # Get unique coordinates in the non-averaging directions
        self.plane_C = np.delete(self.C, self.avg_col_idx, axis=1)
        self.unique_coords = np.unique(self.plane_C, axis=0)

    def create_unique_coords_dict(self):
        return {tuple(c): None for c in self.unique_coords}

    def get_coords_indexes(self):
        # Get a list of indexes for each unique coordinate
        self.unique_coords_idx = self.create_unique_coords_dict()
        for c in self.unique_coords_idx.keys():
            C_view = self.plane_C.view([('', self.plane_C.dtype)] * self.plane_C.shape[1])
            c_view = np.array(c).view([('', self.plane_C.dtype)] * self.plane_C.shape[1])
            self.unique_coords_idx[c] = np.where(C_view == c_view)[0]

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
