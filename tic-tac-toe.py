class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

class Board:
    def __init__(self, size):
        self.reset(size)

    # Reset the board to its initial state
    def reset(self, size):
        self.board = [['' for x in range(size)].copy() for y in range(size)]

        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.antiDiagCounts = {}

        self.size = size

    def place(self, player, x, y):
        marker = player.marker

        # check if the position is valid
        if self.board[x][y] != '':
            raise ValueError(f"Position {x}, {y} is already occupied")

        else:
            self.board[x][y] = marker

            self.rowCounts[x] = self.rowCounts.get(x, {})
            self.rowCounts[x][marker] = self.rowCounts[x].get(marker, 0) + 1

            if self.rowCounts[x][marker] == self.size:
                return True

            self.colCounts[y] = self.colCounts.get(y, {})
            self.colCounts[y][marker] = self.colCounts[y].get(marker, 0) + 1

            if self.colCounts[y][marker] == self.size:
                return True
            
            if x == y:
                self.diagCounts["forwards"] = self.diagCounts.get("forwards", {})
                self.diagCounts["forwards"][marker] = self.diagCounts["forwards"].get(marker, 0) + 1

                if self.diagCounts["forwards"][marker] == self.size:
                    return True
                
            if x + y == self.size - 1:
                self.diagCounts["backwards"] = self.diagCounts.get("backwards", {})
                self.diagCounts["backwards"][marker] = self.diagCounts["backwards"].get(marker, 0) + 1

                if self.diagCounts["backwards"][marker] == self.size:
                    return True
            
            return False

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def playGame(self):
        currTurn = 1
        gameOver = False

        while not gameOver:
            currPlayer = self.player1 if currTurn % 2 == 1 else self.player2
            x = int(input(f"{currPlayer.name}, enter the x coordinate: "))
            y = int(input(f"{currPlayer.name}, enter the y coordinate: "))

            if self.board.place(currPlayer, x, y):
                print(f"{currPlayer.name} wins!")
                gameOver = True
            else:
                currTurn += 1


# Driver code

player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")

board = Board(3)

game = Game(player1, player2, board)
game.playGame()


