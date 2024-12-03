# Player class represents a player in the game with their name and marker (X or O)
class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

# Board class represents the game board and handles game logic
class Board:
    def __init__(self, size):
        self.reset(size)

    # Reset the board to its initial state
    def reset(self, size):
        # Initialize empty board of given size
        self.board = [['' for x in range(size)].copy() for y in range(size)]

        # Initialize counters for win condition checking
        self.rowCounts = {}  # Tracks markers in each row
        self.colCounts = {}  # Tracks markers in each column 
        self.diagCounts = {}  # Tracks markers in main diagonal
        self.antiDiagCounts = {}  # Tracks markers in anti-diagonal
        
        self.size = size

    # Place a marker on the board and check for win
    def place(self, player, x, y):
        marker = player.marker

        # Check if the position is already taken
        if self.board[x][y] != '':
            raise ValueError(f"Position {x}, {y} is already occupied")

        else:
            # Place marker on board
            self.board[x][y] = marker

            # Check row win condition
            self.rowCounts[x] = self.rowCounts.get(x, {})
            self.rowCounts[x][marker] = self.rowCounts[x].get(marker, 0) + 1

            if self.rowCounts[x][marker] == self.size:
                return True

            # Check column win condition  
            self.colCounts[y] = self.colCounts.get(y, {})
            self.colCounts[y][marker] = self.colCounts[y].get(marker, 0) + 1

            if self.colCounts[y][marker] == self.size:
                return True
            
            # Check main diagonal win condition
            if x == y:
                self.diagCounts["forwards"] = self.diagCounts.get("forwards", {})
                self.diagCounts["forwards"][marker] = self.diagCounts["forwards"].get(marker, 0) + 1

                if self.diagCounts["forwards"][marker] == self.size:
                    return True
                
            # Check anti-diagonal win condition
            if x + y == self.size - 1:
                self.diagCounts["backwards"] = self.diagCounts.get("backwards", {})
                self.diagCounts["backwards"][marker] = self.diagCounts["backwards"].get(marker, 0) + 1

                if self.diagCounts["backwards"][marker] == self.size:
                    return True
            
            return False

# Game class controls the game flow and player turns
class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    # Main game loop
    def playGame(self):
        currTurn = 1
        gameOver = False

        while not gameOver:
            # Alternate between players
            currPlayer = self.player1 if currTurn % 2 == 1 else self.player2
            
            # Get player move coordinates
            x = int(input(f"{currPlayer.name}, enter the x coordinate: "))
            y = int(input(f"{currPlayer.name}, enter the y coordinate: "))

            # Place marker and check for win
            if self.board.place(currPlayer, x, y):
                print(f"{currPlayer.name} wins!")
                gameOver = True
            else:
                currTurn += 1


# Driver code to start the game
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")

board = Board(3)

game = Game(player1, player2, board)
game.playGame()
