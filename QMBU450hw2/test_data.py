import unittest
import data
from linearreg import linearReg
import pandas as pd
import numpy as np
class mytest(unittest.TestCase):
    def setUp(self):
        df=pd.read_csv("econ.csv")
        self.reg = linearReg(df)
    def test_nan(self):
        self.assertFalse(np.isnan(self.reg.x).any())
        self.assertFalse(np.isnan(self.reg.y).any())
