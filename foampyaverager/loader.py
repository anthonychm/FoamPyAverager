import numpy as np

class Reader:
    def __init__(self, case_path, time):
        self.time_path = case_path + '/' + str(time) + '/'

    def read_file(self, file_name):
        # Reads openfoam file
        file = open(self.time_path + file_name)
        setattr(self, file_name, file.read())
        file.close()

    def extract_internal_field(self, file_name):
        # Extracts internal field from an openfile file
        start = getattr(self, file_name).find('(') + 1
        end = getattr(self, file_name).find('boundaryField')
        setattr(self, file_name, getattr(self, file_name)[start:end])

    def remove_artifacts(self, file_name):
        # Remove unwanted artifacts in the extracted internal field
        setattr(self, file_name, getattr(self, file_name).replace('(', ''))
        setattr(self, file_name, getattr(self, file_name).replace(')', ''))
        setattr(self, file_name, getattr(self, file_name).replace(';', ''))

    def convert_to_np(self, file_name):
        # Convert openfoam string file into numpy array
        arr = np.loadtxt(getattr(self, file_name).splitlines())
        setattr(self, file_name, arr)
