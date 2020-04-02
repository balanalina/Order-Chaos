from Game.game import gameBoard

class ui:
    def __init__(self,g):
        self._board = g

    def menu(self):
        playerTurn = True
        print("The highest row is the 1st one, lowest row is the 6th! \n");
        print("Win by connecting 5 symbols!");
        while not self._board.gameLost() and not self._board.gameWon():
            self._board.saveGame()
            print("\n")
            print(self._board)
            if playerTurn:
                try:
                    r,c,s = self.readMove()
                    self._board.humanMove(r, c, s)
                    playerTurn = False
                except myException as e:
                    print(e)
            else:
                playerTurn = True
                self._board.computerMove()

        print("\n")
        print(self._board)
        if self._board.gameLost():
            print("You lost!")
        else:
            print("You won!")
                
    def readMove(self):
        row= input("Enter row: ")
        column = input("Enter column: ")
        symbol = input("Entersymbol(X or O): ")
        self.validMove(row, column, symbol)
        return row,column,symbol
             
             
    """
    Validator for the player's input.
    Input: r,c,s - strings ; raw,column and symbol
    Output: - raises an error in case of invalid input
    """
    def validMove(self,r,c,sy):
        s = ''
        if int(r)<1 or  int(r)>6:
            s+="Row outside the board!"
        if int(c)<1 or int(c)>6:
            s +="Column outside the board!"
        if sy!="X" and sy!="O":
            s += "Symbol must be X or O!"
        if len(s)!=0:
            raise myException(s)
        l = self._board.getEmptySquares()
        for i in range(len(l)):
            if l[i] == 6*(int(r)-1) + int(c)-1:
                return
        raise myException("This square is not empty!")
            

class myException(Exception):
    def __init__(self,msg):
        self._msg = msg
        
    def __str__(self):
        return str(self._msg)
    