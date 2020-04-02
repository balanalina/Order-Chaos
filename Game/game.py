from texttable import Texttable
from random import choice
import unittest
class gameBoard():
    def __init__(self):
        self._board = [0] * 36
    
    def __str__(self):
        t = Texttable()   
        dict = {0:" ",1:"O",-1:"X"}  
        for i in range(6):
            list = self._board[6*i:6*i+6]
            for j in range(6):
                list[j] = dict[list[j]]
            t.add_row(list)
        return t.draw()
    
    def gameWon(self):
        for i in range(36):
            if self._board[i]!=0:
                if self.winRow(i):
                    return True
                elif self.winColumn(i):
                    return True
                elif self.winDP(i):
                    return True
                elif self.winDS(i):
                    return True
        return False
    """
    This function check if there is a combination of symbols that means that the player won.They check this on a row,column, principal diagonal and secundary diagonal.
    Input: i - integer, a position having a symbol
    Output: True or False, if the symbol from position i is in a winning combination
    """
    def winRow(self,i):
        if i%6 > 1:
            return False
        if self._board[i] == self._board[i+1] and self._board[i+1] == self._board[i+2] and self._board[i+2] == self._board[i+3] and self._board[i+3] == self._board[i+4]:
            return True
        return False
        
    def winColumn(self,i):
        if i>11:
            return False
        if self._board[i] == self._board[i+6] and self._board[i+6] == self._board[i+2*6] and self._board[i+2*6] == self._board[i+3*6] and self._board[i+3*6] == self._board[i+4*6]:
            return True
        return False
        
    def winDP(self,i):
        if i >7:
            return False
        if self._board[i] == self._board[i+7] and self._board[i+7] == self._board[i + 2*6 +2] and self._board[i + 2*6 + 2] == self._board[i+3*6 + 3] and self._board[i+3*6+3] == self._board[i+4*6 + 4]:
            return True
        return False
        
    def winDS(self,i):
        if i == 4 or i == 5 or i == 10 or i == 11 :
            if self._board[i] == self._board[i+6-1] and self._board[i+6-1] == self._board[i+6*2-2] and self._board[i+6*2-2] == self._board[6*3+i-3] and self._board[6*3+i-3] == self._board[6*4+i-4]:
                return True
        return False
    
    """
    The function checks if the board is full,there are no empty squares.
    Input: - 
    Output: True or False, if the game is lost, no empty squares
    """
    def gameLost(self):
        if len(self.getEmptySquares()) == 0:
            return True
        return False
    """
    Input: - 
    Output:  a list containing the positions of the empty squares
    """
    def getEmptySquares(self):
        list = []
        for i in range(36):
            if self._board[i] == 0:
                list.append(i)
        return list
    
    """
    The function that moves based on the player's input.
    Input: r - string,row ; c - string,column ; s - string,symbol
    Output: - 
    """
    
    def humanMove(self,r,c,s):
        dict = {"X" : -1 , "O" : 1}
        self._board[6*(int(r)-1) + int(c)-1] = dict[s]
        
    """
    The function generates a random move made by the computer based on the empty squares.
    """
    def computerMove(self):
        for i in range(36):
            if self._board[i]!=0:
                if self.checkRow5(i):
                    self._board[i+4] = self._board[i]*(-1)
                    return
                elif self.checkRow4(i):
                    self._board[i+3] = self._board[i]*(-1)
                elif self.checkRow3(i):
                    self._board[i+2] = self._board[i] *(-1)
                elif self.checkRow2(i):
                    self._board[i+1] = self._board[i] * (-1)
                elif self.checkColumn5(i):
                    self._board[i+4*6] = self._board[i] * (-1)
                elif self.checkDP5(i):
                    self._board[i+4*6 + 4] = self._board[i] * (-1)
                elif self.checkDS5(i):
                    self._board[6*4+i-4] = self._board[i] * (-1)
                elif self.checkColumn4(i):
                    self._board[i+3*6] = self._board[i] * (-1)
        l = self.getEmptySquares()
        self._board[choice(l)] = choice([1,-1])

    #checks for the computer's next move
    def checkRow5(self,i):
        if i%6 > 1:
            return False
        if self._board[i] == self._board[i+1] and self._board[i+1] == self._board[i+2] and self._board[i+2] == self._board[i+3] and self._board[i+4] == 0:
            return True
        return False
    
    def checkRow4(self,i):
        if i%6 > 1:
            return False
        if self._board[i] == self._board[i+1] and self._board[i+1] == self._board[i+2] and self._board[i+2] == self._board[i+4] and self._board[i+3] == 0:
            return True
        return False
    
    def checkRow3(self,i):
        if i%6 > 1:
            return False
        if self._board[i] == self._board[i+1] and self._board[i+1] == self._board[i+3] and self._board[i+3] == self._board[i+4] and self._board[i+2] == 0:
            return True
        return False
    
    def checkRow2(self,i):
        if i%6 > 1:
            return False
        if self._board[i] == self._board[i+2] and self._board[i+2] == self._board[i+3] and self._board[i+3] == self._board[i+4] and self._board[i+1] == 0:
            return True
        return False
    
    def checkColumn5(self,i):
        if i>11:
            return False
        if self._board[i] == self._board[i+6] and self._board[i+6] == self._board[i+2*6] and self._board[i+2*6] == self._board[i+3*6] and self._board[i+4*6] == 0:
            return True
        return False
    
    def checkColumn4(self,i):
        if i>11:
            return False
        if self._board[i] == self._board[i+6] and self._board[i+6] == self._board[i+2*6] and self._board[i+3*6] == self._board[i+4*6] and self._board[i+3*6] == 0:
            return True
        return False
    
    def checkDP5(self,i):
        if i >7:
            return False
        if self._board[i] == self._board[i+7] and self._board[i+7] == self._board[i + 2*6 +2] and self._board[i + 2*6 + 2] == self._board[i+3*6 + 3] and self._board[i+4*6 + 4] == 0:
            return True
        return False

    def checkDS5(self,i):
        if i == 4 or i == 5 or i == 10 or i == 11 :
            if self._board[i] == self._board[i+6-1] and self._board[i+6-1] == self._board[i+6*2-2] and self._board[i+6*2-2] == self._board[6*3+i-3] and self._board[6*4+i-4] == 0:
                return True
        return False
        
    def saveGame(self):
        f = open("game.txt","w")
        for i in range (36):
            p = str(str(self._board[i]))
            f.write(p)
        f.close()
        
    def getBoard(self):
        return self._board
            
class test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def tests(self):
        j = gameBoard()
        j.humanMove('1','1', 'X')
        assert len(j.getBoard()) == 36
        j.humanMove('2','2', 'X')
        j.humanMove('3','3', 'X')
        j.humanMove('4','4', 'X')
        j.humanMove('5','5', 'X')
        assert j.gameWon() == True
        assert j.winDP(1) == True
        assert j.winRow(5) == False 
        assert j.winDP(25) == False
        l = j.getEmptySquares()
        assert len(l) == 31