import wbdata
import datetime
from linearreg import linearReg
import matplotlib.pyplot as plt
import pandas as pd

data_date = (datetime.datetime(1900, 1, 1), datetime.datetime(2018, 1, 1))
indicators = {"EN.ATM.CO2E.KT" : "carbon" , "SP.POP.TOTL" : "population"}
df = wbdata.get_dataframe(indicators, country="1W", data_date=data_date)

df.to_csv('econ.csv')
df.describe()


df = pd.read_csv('econ.csv')
populationList= df['population']
carbon = df['carbon']
reg = linearReg(df)
reg.x=reg.normalize_data(reg.x)
reg.y=reg.normalize_data(reg.y)
plt.plot(reg.x,reg.y,'ro',label='data')
plt.xlabel('Population')
plt.ylabel('CarbonEmission')
reg.regression(reg.x,reg.y)
reg.predict(reg.x)
plt.legend(loc='upper left')
plt.show()