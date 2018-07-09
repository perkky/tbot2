from abc import ABC, abstractmethod

class Data(ABC):

    def __init__(self):
        super.__init__()

    @abstractmethod
    def getNextCandle(self):
        pass
        
    @abstractmethod
    def setLimitOrder(self, amount, price):
        pass

    @abstractmethod
    def setMarketOrder(self, amount):
        pass

    @abstractmethod
    def setStopLoss(self, amount, price):
        pass

    @abstractmethod
    def cancelAllOrders(self):
        pass

    #gets the value of the account
    @abstractmethod
    def getValue(self):
        pass