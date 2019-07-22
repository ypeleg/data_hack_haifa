
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = datasets.load_diabetes()
x = data.data
y = data.target
y = np.expand_dims(y, 1)
x = x[:,0]
x = np.expand_dims(x, 1)

x_train, x_test, y_train, y_test = train_test_split(x,y)
print(x_train.shape)
print(x.shape)

model = linear_model.LinearRegression()
model.fit(x, y)
print(dir(model))
print(model.coef_)
pred = model.predict(x)
plt.plot(x, pred)
plt.scatter(x, y)
# plt.show()


