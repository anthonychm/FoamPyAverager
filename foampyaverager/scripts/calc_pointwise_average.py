"""
Run this file to execute domain averaging for a pointwise query in an OpenFOAM case
"""

from foampyaverager.src import loader

def main(case_path, time, avg_var, points, avg_dir):

    # Load openfoam time directory files
    time_reader = loader.OpenFoamReader(case_path, time)
    for var in ['C', avg_var]:
        time_reader.read_file(var)
        time_reader.extract_internal_field(var, end_str='boundaryField')
        time_reader.remove_artifacts(var)
        time_reader.convert_to_np(var)

    # Load openfoam polymesh directory files
    mesh_reader = loader.OpenFoamReader(case_path, 'constant/polymesh')
    for var in ['faces', 'neighbour', 'owner', 'points']:
        mesh_reader.read_file(var)
        mesh_reader.extract_internal_field(var, end_str=')')
        mesh_reader.remove_artifacts(var, artifacts=['4(', '(', ')'])
        mesh_reader.convert_to_np(var)

if __name__ == '__main__':
    main('../../examples/channel395', 1000, 'UMean', 1, 'x')