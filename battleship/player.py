from re import search

from grid import Grid
from ship import Ship


class Player:
    def __init__(self):
        self.lower_grid = Grid()
        self.upper_grid = Grid()
        self._opponent = None
        self._has_put_his_fleet = False
        self._has_to_play = True
        self.fleet = [Ship(self, length) for length in (2, 3, 3, 4, 5)]

    def put_a_ship(self, coordinates_str):
        coordinates = [self.convert_to_coordinates(coord_str) for coord_str in coordinates_str]

        # Check if coordinates are on a line and unique
        if (
            len({coordinate[0] for coordinate in coordinates}),
            len({coordinate[1] for coordinate in coordinates}),
        ) not in [(1, len(coordinates)), (len(coordinates), 1)]:
            raise ValueError("Bad coordinates.")

        # Check if the coordinates do not overlap with another _ship
        for coordinate in coordinates:
            if self.lower_grid[coordinate].has_a_ship:
                raise ValueError("The ships overlap.")

        # Put the _ship
        for ship in self.fleet:
            if ship.coordinates is None and ship.length == len(coordinates):
                ship.place_on_the_grid(coordinates)
                break
        else:
            raise ValueError("The _ship does not exist or has already been initialized.")

        # Check if player has put his whole fleet
        self._has_put_his_fleet = True
        for ship in self.fleet:
            if ship.coordinates is None:
                self._has_put_his_fleet = False

    @staticmethod
    def convert_to_coordinates(coordinates_str):
        if search(r"^[A-Ja-j]([1-9]|10)$", "A1") is not None:
            letter = coordinates_str[0].upper()
            number = int(coordinates_str[1:])
            return "ABCDEFGHIJ".index(letter), number - 1
        else:
            raise ValueError(f"The coordinates {coordinates_str} are not valid.")

    def play_square(self, coordinates_str):
        if self._has_put_his_fleet and self._opponent._has_put_his_fleet and self._has_to_play:
            state = self._opponent.is_there_a_ship_on_square(coordinates_str)
            print(state)

            coordinates = self.convert_to_coordinates(coordinates_str)
            self.upper_grid[coordinates].has_been_hit = True
            if state in ("hit", "hit and sunk"):
                self.upper_grid[coordinates].has_a_ship = True

            self._has_to_play = False
        else:
            print("It is not your turn.")

    def is_there_a_ship_on_square(self, coordinates_str):
        coordinate = self.convert_to_coordinates(coordinates_str)
        self._has_to_play = True
        self.lower_grid[coordinate].has_been_hit = True
        if self.lower_grid[coordinate].has_a_ship:
            if self.lower_grid[coordinate].ship.has_sunk:
                return "hit and sunk"
            return "hit"
        else:
            return "miss"
