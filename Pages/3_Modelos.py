import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(url, names=name)

#dividir los datos en entrenamiento y prueba

x_train, x_test, y_train, y_test = train_test_split(
    df[df.columns[0:4]],df[df.columns[-1]], test_size=0.2)

modelos = []
x_test.shape
modelo = LogisticRegression(random_state=0).fit(x_train, y_train)
modelo.score(x_test,y_test)
modelo.predict(x_test)
#y_test
##Crossvalidation
kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
resultados = cross_val_score(modelo,x_train,y_train, cv=kfold, scoring="accuracy")
#resultados
modeloKN = KNeighborsClassifier(n_neighbors=3)
modeloKN.fit(x_train,y_train)
modeloKN.score(x_test,y_test)
modeloKN.predict(x_test)
x_train = x_train[ x_train["sepal-length"] != "sepal.length" ]
x_train["sepal-length"].replace("sepal.length",.5,inplace=True)
