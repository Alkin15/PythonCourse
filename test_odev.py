import unittest
from odev import Portfolio,Stock,MutualFunds

class testOdev(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio()
        self.s = Stock(20, "HFH")
        self.mf1 = MutualFunds("BRT")
        self.mf2 = MutualFunds("GHT")
        self.portfolio.addCash(300.50)

    def test_addCash(self):
        self.portfolio.addCash(50)
        self.assertEqual(self.portfolio.cash, 350.5)
    def test_buyStock(self):
        self.portfolio.buyStock(5,self.s)
        self.assertEqual(self.portfolio.stock, {"HFH":[5,20]})
    def test_buyMutualFund(self):
        self.portfolio.buyMutualFund(10.3,self.mf1)
        self.portfolio.buyMutualFund(2,self.mf2)
        self.assertEqual(self.portfolio.mutualFunds,{"BRT":10.3,"GHT":2})
    def test_sellMutualFund(self):
        self.portfolio.buyMutualFund(10.3, self.mf1)
        self.portfolio.buyMutualFund(2, self.mf2)
        cash = self.portfolio.cash
        self.portfolio.sellMutualFund("BRT",3)
        self.assertEqual(self.portfolio.mutualFunds,{"BRT":7.300000000000001,"GHT":2})
        self.assertNotEqual(self.portfolio.cash,cash)
    def test_sellStock(self):
        self.portfolio.buyStock(5,self.s)
        cash=self.portfolio.cash
        self.portfolio.sellStock("HFH",1)
        self.assertEqual(self.portfolio.stock,{"HFH":[4,20]})
        self.assertNotEqual(self.portfolio.cash,cash)
    def test_withdrarCash(self):
        self.portfolio.withdrawCash(50)
        self.assertEqual(self.portfolio.cash,250.50)

if __name__ == '__main__' :
    unittest.main()