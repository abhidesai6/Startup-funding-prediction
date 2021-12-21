import sys
import pandas as pd
from sklearn import linear_model

dataset=pd.read_excel("D:\\College notes\\Sem_5\\BDA\\PBL\\Django\\edited.xlsx")

X = dataset[['R&D Spend', 'Administration', 'Marketing Spend', 'City  Location', 'Industry Vertical']]
y = dataset['Profit']

regressor = linear_model.LinearRegression()
regressor.fit(X, y)

predictedProfit = regressor.predict([[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]])
print(predictedProfit)
