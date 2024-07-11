from square import Square


class Grid:
    def __init__(self):
        self._grid = [[Square() for _ in range(10)] for _ in range(10)]

    def __getitem__(self, item):
        col, row = item
        return self._grid[row][col]

    def __str__(self):
        str_ = "   A B C D E F G H I J\n"
        for i, line in enumerate(self._grid, 1):
            if i != 10:
                str_ += " "
            str_ += str(i) + " "
            for square in line:
                str_ += str(square) + " "
            str_ = str_[:-1]
            str_ += "\n"
        return str_
