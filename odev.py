import random
class Portfolio:
    def __init__(self):
        self.cash = float(0)
        self.stock = {}
        self.mutualFunds = {}
        self.transactions = []
    def history(self):
        for hist in self.transactions:
            print(hist)
			print("selam")
			price++
    def addCash(self,money):
	asdasdas
	yeni
        self.cash += money
        self.transactions.append("Added Cash : %d" % money)
    def buyStock(self,number,stock):
        if(stock.symbol in self.stock.keys()):
            self.stock.update({stock.symbol: [self.stock.get(stock.symbol)
                                             + number, stock.price]})
        else:
            self.stock.update({stock.symbol: [number, stock.price]})

        self.cash -= stock.price*number
        self.transactions.append("Bought Stock: %s  Bought Number : %d" %(stock.symbol,number))
    def sellStock(self,symbol,number):
        price = self.stock.get(symbol)
        self.stock.update({symbol:[self.stock.get(symbol)[0]-number,self.stock.get(symbol)[1]]})
        self.cash += number*random.uniform(0.5,1.5)* price[1]
        self.transactions.append("Sold Stock: %s Sold Number: %d" % (symbol,number))
    def buyMutualFund(self,number,mutualFunds):
        if(mutualFunds.name in self.mutualFunds.keys()):
            self.mutualFunds.update(({mutualFunds.name :
                                          self.mutualFunds.get(mutualFunds.name) + float(number)}))
        else:
            self.mutualFunds.update({mutualFunds.name:number})
        self.cash -= float(number)
        self.transactions.append("Bought MutualFunds: %s Bought Number: %f" %(mutualFunds.name,number))
    def sellMutualFund(self,mutualFund,number):
        self.mutualFunds.update({mutualFund:self.mutualFunds.get(mutualFund)-number})
        self.cash += number*random.uniform(0.9,1.2)
        self.transactions.append("Sold MutualFunds : %s Sold Number:%d" % (mutualFund,number))
    def withdrawCash(self, number):
        self.cash -= float(number)
        self.transactions.append("Withdrew Cash : %d" % number)
    def __str__(self):
        for keys,values in self.stock.items():
            print str(keys), str(values[0])
        for keys,values in self.mutualFunds.items():
            print str(keys), str(values)
        print ("Cash : %f" %self.cash)
        return ""

"""random.uniform(0.9,1.2)
"""

class MutualFunds:
    def __init__(self, name):
        self.name = name

class Stock:
    def __init__(self,price,symbol):
        self.price = price
        self.symbol = symbol
"""""
class Bonds(Stock):
    def __init__(self,price,symbol):
        Stock.__init__(self,price,symbol)
"""
"""
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20,"HFH")
portfolio.buyStock(5,s)
mf1 = MutualFunds("BRT")
mf2 = MutualFunds("GHT")
portfolio.buyMutualFund(10.3,mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT",3)
portfolio.sellStock("HFH",1)
portfolio.withdrawCash(50)
portfolio.history()
"""