import pyxel


class Player:
    def __init__(self, name):
        self.name = name
        self.token = 1 if self.name == "Joueur 1" else 2
        self.token_column = 0

    def check(self, grid, y, x):
        count = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for index, direction in enumerate(directions):
            dy, dx = direction
            x_i = x + dx
            y_i = y + dy
            if index % 2 == 0:
                count = 1
            while 0 <= x_i <= 6 and 0 <= y_i <= 5 and grid[y_i][x_i] == self.token:
                count += 1
                x_i += dx
                y_i += dy
            if count >= 4:
                print("gagné")
                return self.name
        return False

    def place_token(self, grid, x):
        y = 5
        while not (grid[y][x] == 0 or y < 0):
            y -= 1
        if y != -1:
            grid[y][x] = self.token
        return grid, y, x

    def token_position(self):
        column_choice = {-1: 6, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 0}
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.token_column = column_choice[self.token_column - 1]
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.token_column = column_choice[self.token_column + 1]
        return self.token_column


class App:
    def __init__(self):
        pyxel.init(188, 200)
        pyxel.load("./theme.pyxres")
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.player1 = Player("Joueur 1")
        self.player2 = Player("Joueur 2")
        self.tour = 1
        self.column = -1
        self.place = 0
        self.won = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tour == 1:
            self.place = self.player1.token_position()
            if pyxel.btnp(pyxel.KEY_SPACE) and self.grid[0][self.place] == 0 and not self.won:
                self.grid, last_y, last_x = self.player1.place_token(self.grid, self.place)
                self.won = self.player1.check(self.grid, last_y, last_x)
                self.tour = 2
                self.column = -1
        else:
            self.place = self.player2.token_position()
            if pyxel.btnp(pyxel.KEY_SPACE) and self.grid[0][self.place] == 0 and not self.won:
                self.grid, last_y, last_x = self.player2.place_token(self.grid, self.place)
                self.won = self.player2.check(self.grid, last_y, last_x)
                self.tour = 1
                self.column = -1

    def draw(self):
        pyxel.bltm(10, 45, 0, 0, 0, 168, 190, 0)
        pyxel.rect(0, 0, 200, 40, 0)
        self.draw_token()
        self.draw_curent_token(self.place)
        self.draw_winner()

    def draw_token(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[1])):
                if self.grid[y][x] == 1:
                    pyxel.blt(x * 24 + 14, y * 24 + 49, 0, 0, 0, 16, 16, 0)
                elif self.grid[y][x] == 2:
                    pyxel.blt(x * 24 + 14, y * 24 + 49, 0, 0, 16, 16, 16, 0)

    def draw_curent_token(self, column_place):
        if self.tour == 1:
            pyxel.blt(column_place * 24 + 14, 20, 0, 0, 32, 16, 16, 0)
        elif self.tour == 2:
            pyxel.blt(column_place * 24 + 14, 20, 0, 16, 32, 16, 16, 0)

    def draw_winner(self):
        if self.won:
            pyxel.text(10, 10, "partie terminee", 2)


App()
