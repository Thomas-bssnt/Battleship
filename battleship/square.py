class Square:
    def __init__(self):
        self.has_been_hit = False
        self.has_a_ship = False
        self.ship = None

    def __str__(self):
        if self.has_a_ship and self.has_been_hit:
            return "X"
        elif self.has_a_ship and not self.has_been_hit:
            return "."
        elif not self.has_a_ship and self.has_been_hit:
            return "O"
        else:
            return " "

    def is_part_of_a_ship(self, ship):
        self.has_a_ship = True
        self.ship = ship
