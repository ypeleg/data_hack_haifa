
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

train = pd.read_csv(r'house_prices.csv')
test = pd.read_csv(r'test.csv')
print('Train: ', train.shape, 'Test: ', test.shape)

df = pd.concat((train, test))
df.drop('Id', axis = 'columns', inplace = True)

print(df.isnull().sum())


print(df.dtypes)
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    print(col, df[col].isnull().sum())
    df[col].fillna(0, inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    print(col, df[col].isnull().sum())
    df[col].fillna('missing', inplace=True)

df = pd.get_dummies(df)

y = df['SalePrice']
df.drop('SalePrice', axis='columns', inplace=True)

X = df[:train.shape[0]]
X_comp = df[train.shape[0]:]

y = np.log(y)

print(X.shape)
print(X_comp.shape)
print(y.shape)

def rmsle(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

models = []
for train_index, test_index in KFold(5).split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    mdl = RandomForestRegressor()
    mdl.fit(X_train, y_train)
    print('score: ', rmsle(y_test, mdl.predict(X_test)))
    models.append(mdl)

prediction = np.array([model.predict(X_comp) for model in models]).mean(axis=0)

sub = pd.read_csv('sample_sub.csv')
sub['SalePrice'] = np.exp(prediction)
sub.to_csv("sub.csv", index=False)
