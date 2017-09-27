import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

data = pd.read_csv('customers.csv')
data.drop(['Region', 'Channel'], axis = 1, inplace = True)
print ("Wholesale customers dataset has {} samples with {} features each.".format(*data.shape))


#scale
# scaler = MinMaxScaler()
# data.loc[:] = scaler.fit_transform(data.loc[:])

# print(data.head())
# print(data.describe())
# portion= int(data.shape[0]/4)

# bar_width = 0.1
# fig,ax = plt.subplots()
# index=np.arange(data.shape[0])
# graph1 = plt.bar(index,data['Fresh'],bar_width,label='Fresh')
# graph2 = plt.bar(index + 0.2,data['Milk'] ,bar_width,label='Milk')
# graph3 = plt.bar(index + 0.4,data['Grocery'],bar_width)
# graph4 = plt.bar(index + 0.6,data['Frozen'],bar_width)
# plt.tight_layout()
# plt.show()

# plt.hist(data['Fresh'],100)
# plt.tight_layout()
# plt.show()


sns.pairplot(data,diag_kind='kde',kind='reg',size=5)
plt.tight_layout()
plt.show()
