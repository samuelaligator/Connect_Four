import pyxel


class Player:
    def __init__(self, name):
        self.name = name
        self.token = '🟡' if self.name == "Joueur 1" else '⭕'

    def check(self, grid, row, column):
        count = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for index, direction in enumerate(directions):
            dy, dx = direction
            column_i = column + dx
            row_i = row + dy
            if index % 2 == 0:
                count = 1
            while 0 <= column_i <= 6 and 0 <= row_i <= 5 and grid[row_i][column_i] == self.token:
                count += 1
                column_i += dx
                row_i += dy
            if count >= 4:
                print(f"{self.name} a gagné")
        return count

    def play(self, grid):
        column = -1
        while (column > 6 or column < 0) or grid[0][column] != '⚪' or type(column) != int:
            column = input(f"\n{self.name}, choisissez une colonne : ")
            column = int(column) if column.isnumeric() else -1
        i = 5
        while not (grid[i][column] == '⚪' or i < 0):
            i -= 1
        grid[i][column] = self.token
        self.check(grid, i, column)
        return grid

    def draw_coin(self, grid):
        pass


class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.load("./theme.pyxres")
        self.grid = [['⚪' for _ in range(7)] for _ in range(6)]
        self.player1 = Player("Joueur 1")
        self.player2 = Player("Joueur 2")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 165, 140, 0)
        self.player1.draw_coin(self.grid)
        self.player2.draw_coin(self.grid)


App()
