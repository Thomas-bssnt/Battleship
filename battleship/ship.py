class Ship:
    def __init__(self, player, length):
        self._grid = player.lower_grid
        self.length = length
        self.coordinates = None

    def place_on_the_grid(self, coordinates):
        self.coordinates = coordinates
        for coordinate in coordinates:
            self._grid[coordinate].is_part_of_a_ship(self)

    @property
    def has_sunk(self):
        state = True
        for coordinate in self.coordinates:
            if not self._grid[coordinate].has_been_hit:
                state = False
        return state
