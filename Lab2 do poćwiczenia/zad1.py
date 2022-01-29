import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])
def myPredictRow(sl,sw,pl,pw):
    if pw<0.9:
        return 'Iris-setosa'
    elif pl>4.8:
        return 'Iris-virginica'
    else:
        return 'Iris-versicolor'

zgodnosc = 0
for i in range(len(df)):
    iris_klasa = df['target'][i]
    a,b,c,d = df['sepal length'][i],df['sepal width'][i],df['petal length'][i],df['petal width'][i]
    if (myPredictRow(a,b,c,d) == iris_klasa):
        zgodnosc+=1
print(zgodnosc/150*100,"%")

#95,3%