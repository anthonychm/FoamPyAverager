class ContourGridCreator:
    def __init__(self, unique_coords):
        self.unique_coords = unique_coords
        assert self.unique_coords.shape[1] == 2
        self.unique1 = self.unique_coords[:, 0]
        self.unique2 = self.unique_coords[:, -1]

# class ContourPlotter:
