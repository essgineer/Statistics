import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

data=pd.read_csv('data.csv')

plt.scatter(data['Body_kg'],data['Brain_g'],color='k')
plt.title("Linear Model")

data['logBrain']=np.log10(data['Brain_g'])
data['logBody']=np.log10(data['Body_kg'])
meanLogBody=data['logBody'].mean()
meanLogBrain=data['logBrain'].mean()  ##there is a better way...

x = np.array([data['Body_kg'].min(), data['Body_kg'].max()]) 
a= data['logBody'].cov(data['logBrain'])/data['logBody'].var()
b=a*(-meanLogBody)+meanLogBrain #from equation y-!y=a(x-!x)
y=a*x+b
print ('%f *x+ %f' %(a,b))
plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')
print ('meanLogBody= %f , meanLogBrain %f' %(meanLogBody,meanLogBrain))
plt.grid(True,which="both")
plt.xlabel("Body Weight")
plt.ylabel("Brain Weight") 
plt.show() 
