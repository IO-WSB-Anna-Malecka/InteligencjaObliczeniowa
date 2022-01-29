import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

df = pd.read_csv("iris.csv")
#numervozne kolumnv
all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values

#piata kolumna, z gatunkiem
all_classes = df['variety'].values
(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)
print("Ilość trenowanych: ",train_classes.shape[0])

drzewo = DecisionTreeClassifier()
drzewo.fit(train_inputs, train_classes)

plt.figure()
tree.plot_tree(drzewo)
plt.savefig('tree.eps', format='eps', bbox_inches='tight')

wizualnedrzwo = tree.export_text(drzewo)
print("Drzewo: \n",wizualnedrzwo)


#dokladnosc modelu
dokl=drzewo.score(test_inputs,test_classes)
print("Dokładność modelu: ", dokl)

#zgadniete nazwy irysow
test_zgadniete=drzewo.predict(test_inputs)
macierz_bledow = confusion_matrix(test_classes, test_zgadniete)
print("Macierz błędów: \n",macierz_bledow)


