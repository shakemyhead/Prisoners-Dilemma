__author__ = 'kummef'

class Prisoner:

    def __init__(self):
        self.nice = 0
        self.mean = 1
        self.prevMove = -1
        self.prevOppMove = -1

    def getNice(self):
        return self.nice

    def getMean(self):
        return  self.mean

    #default is to always be nice
    def chooseNextMove(self):
        return self.nice

    def setPrevMove(self, prevMove):
        self.prevMove = prevMove

    def setPrevOppMove(self, prevOppMove):
        self.prevOppMove = prevOppMove

    def getPrevMove(self):
        return self.prevMove

    def getPrevOppMove(self):
        return self.prevOppMove

    def isFirstTurn(self):
        if((self.prevMove == -1) and (self.prevOppMove == -1)):
            return True
        else:
            return False

    def reset(self):
        self.prevMove = -1
        self.prevOppMove = -1