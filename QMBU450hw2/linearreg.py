import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from csv import reader
class linearReg:
    def __init__(self,data,x=None,y=None,error=None,B=None,var=None,stdDev=None):
        data=data.dropna()
        data= np.asmatrix(data)
        self.x = data[:,2]
        self.y = data[:,1]
    def regression(self,x,y):
       #b = np.linalg.inv(x.T @ x) @ x.T @ y
        self.B = np.dot(np.dot(np.linalg.inv(np.dot(x.T,x)),x.T),y)
        self.e = self.y-np.dot(self.x,self.B)
        self.stdDev = np.std(self.e)
        self.var = np.dot(np.linalg.inv(np.dot(x.T,x)),self.stdDev)

    def normalize_data(self,data):
        return ((np.asmatrix(data)-np.min(data))/(np.max(data)-np.min(data)))
    def predict(self,data):
        predicted = np.dot(data,self.B)
        less_data=[]
        less_data_x=[]
        high_data_x=[]
        high_data=[]

        for x in range(0,len(predicted)):
            if (self.y[x]-predicted[x]<=0.05):
                less_data.append(np.array(predicted[x]))
                less_data_x.append(np.array(self.x[x]))
            elif(self.y[x]-predicted[x]>0.05):
                high_data.append(np.array(predicted[x]))
                high_data_x.append(np.array(self.x[x]))
            else:
                return None

        plt.plot(np.squeeze(less_data_x),np.squeeze(less_data),'ro',color='green',label = 'Interval=>0.95')
        plt.plot(np.squeeze(high_data_x),np.squeeze(high_data),'ro',color='orange',label='Interval<0.95')





