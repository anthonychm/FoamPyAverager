
class Reader:
    def __init__(self, case_path, time, avg_var):
        time_path = case_path + '/' + str(time) + '/'

        def read_file(file_name):
            # Reads openfoam file
            file = open(time_path + file_name)
            setattr(self, file_name, file.read())
            file.close()

        def extract_internal_field(file_name):
            # Extracts internal field from an openfile file
            start = getattr(self, file_name).find('(') + 1
            end = getattr(self, file_name).find(')')
            setattr(self, file_name, getattr(self, file_name)[start:end])
            
        # Read openfoam files
        read_file('Cx')
        read_file('Cy')
        read_file('Cz')
        read_file(avg_var)

        # Extract internal fields
        extract_internal_field('Cx')
        extract_internal_field('Cy')
        extract_internal_field('Cz')
        extract_internal_field(avg_var)


