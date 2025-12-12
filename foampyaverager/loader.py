import numpy as np

class OpenFoamReader:
    def __init__(self, case_path, time):
        self.time_path = case_path + '/' + str(time) + '/'

    def read_file(self, var):
        # Reads openfoam file
        file = open(self.time_path + var)
        setattr(self, var, file.read())
        file.close()

    def extract_internal_field(self, var):
        # Extracts internal field from an openfile file
        start = getattr(self, var).find('(') + 1
        end = getattr(self, var).find('boundaryField')
        setattr(self, var, getattr(self, var)[start:end])

    def remove_artifacts(self, var):
        # Remove unwanted artifacts in the extracted internal field
        setattr(self, var, getattr(self, var).replace('(', ''))
        setattr(self, var, getattr(self, var).replace(')', ''))
        setattr(self, var, getattr(self, var).replace(';', ''))

    def convert_to_np(self, var):
        # Convert openfoam string file into numpy array
        arr = np.loadtxt(getattr(self, var).splitlines())
        setattr(self, var, arr)

class AveragedReader:
    def __init__(self, pth,unique_coords_file, avg_var_file):
        self.unique_coords = np.loadtxt(pth + unique_coords_file)
        self.averaged_var = np.loadtxt(pth + avg_var_file)
