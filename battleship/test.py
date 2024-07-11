from player import Player

if __name__ == "__main__":
    player_1 = Player()
    player_2 = Player()

    player_1._opponent = player_2
    player_2._opponent = player_1

    player_1.put_a_ship(["A1", "A2"])
    player_1.put_a_ship(["B4", "C4", "D4"])
    player_1.put_a_ship(["J4", "J5", "J6"])
    player_1.put_a_ship(["C9", "D9", "E9", "F9", "G9"])
    player_1.put_a_ship(["E2", "F2", "G2", "H2"])

    player_2.put_a_ship(["B1", "B2"])
    player_2.put_a_ship(["B7", "C7", "D7"])
    player_2.put_a_ship(["J4", "J5", "J6"])
    player_2.put_a_ship(["C9", "D9", "E9", "F9", "G9"])
    player_2.put_a_ship(["E2", "F2", "G2", "H2"])

    print(player_1.upper_grid)
    print(player_1.lower_grid)

    player_1.play_square("B2")
    player_2.play_square("F2")

    print(player_1.upper_grid)
    print(player_1.lower_grid)

    player_1.play_square("C2")
    player_2.play_square("C6")

    print(player_1.upper_grid)
    print(player_1.lower_grid)

    print(player_2.upper_grid)
    print(player_2.lower_grid)
