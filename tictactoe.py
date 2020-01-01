#Creating a tictactoe command-line based game
## By github.com/jeff-fred
#Imports
import os



#Board
class Game:
    def __init__(self):
        self.board = [0," "," "," "," "," "," "," "," "," "]

    #Displays board with nice welcome message
    def display(self):
        os.system("cls")
        print("\nWelcome to TicTacToe!\n")
        print(" {0} | {1} | {2} ".format(self.board[1],self.board[2], self.board[3]))
        print(" ---------- ")
        print(" {0} | {1} | {2} ".format(self.board[4],self.board[5], self.board[6]))
        print(" ---------- ")
        print(" {0} | {1} | {2} ".format(self.board[7],self.board[8], self.board[9]))
        print("\n")

    #Take input for position and set board position to player
    def move(self, position, player):
        self.board[position] = player
    
    #Reprint the board, updated list
    def update(self):
        os.system("cls")
        print("\n")
        print(" {0} | {1} | {2} ".format(self.board[1],self.board[2], self.board[3]))
        print(" ---------- ")
        print(" {0} | {1} | {2} ".format(self.board[4],self.board[5], self.board[6]))
        print(" ---------- ")
        print(" {0} | {1} | {2} ".format(self.board[7],self.board[8], self.board[9]))
        print("\n")

    #Using other functions to check if win is True
    def CheckIfWin(self, player):
        if self.verticalWin(player) == True or self.horizontalWin(player) == True or self.diagonalWin(player) == True:
            return True
        else:
            return False

    #Checking for tie
    def CheckForTie(self, player):
        if " " not in self.board and self.CheckIfWin(player) == False:
            return True
        else:
            pass

    #Check all columns for same character, if so return True
    def verticalWin(self, player):
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        elif self.board[3] == player and self.board[6] == player and self.board[9] == player:
            return True

    #Check all rows for same character, if so return True
    def horizontalWin(self, player):
        if self.board[1] == player and self.board[2] == player and self.board[3] == player:
            return True
        elif self.board[4] == player and self.board[5] == player and self.board[6] == player:
            return True
        elif self.board[7] == player and self.board[8] == player and self.board[9] == player:
            return True

    #Check all diagonal spots for same character, if so return True
    def diagonalWin(self, player):
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        elif self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True 
        
#Play game       
def playTicTacToe():
    gameOn = True
    game = Game()
    game.display()
    while gameOn:

    #Setting the position inputed by X player, and checking validity    
        Xpos = int(input("Player X. Position: "))
        while game.board[Xpos] != " ":
            game.update()
            print("\nInvalid position.")
            Xpos = int(input("Player X. Position: "))

        while Xpos not in range(1,10):
            game.update()
            print("\nInvalid position.")
            Xpos = int(input("Player X. Position: "))
            
        game.move(Xpos, "X")

        if game.CheckIfWin("X") == True:
            game.update()
            print("Player X Wins!\n")
            break
        elif game.CheckForTie("X") == True:
            game.update()
            print("There has been a tie!")
            break

        game.update()

        #Setting the position inputed by Y player, and checking validity
        Ypos = int(input("Player Y. Position: "))
        while game.board[Ypos] != " ":
            game.update()
            print("\nInvalid position.")
            Xpos = int(input("Player X. Position: "))
        while Ypos not in range(1,10):
            game.update()
            print("\nInvalid position.")
            Ypos = int(input("Player Y. Position: "))


        game.move(Ypos, "Y")

        if game.CheckIfWin("Y") == True:
            game.update()
            print("Player Y Wins!\n")
            break
        elif game.CheckForTie("Y") == True:
            game.update()
            print("There has been a tie!")
            break

        game.update()
    
        
playTicTacToe()