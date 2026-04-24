import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("train")
X=df[["Sex","Pclass","Age","Fare"]].copy()
X["Sex"]=X["Sex"].map({"male": 0, "female": 1})
X["Age"]=X["Age"].fillna(X["Age"].mean())
Y=df["Survived"]
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2)
model=LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
print("Accuracy:", model.score(X_test,Y_test))

