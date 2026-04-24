import pandas as pd
from sklearn.model_selection imort train_test_split
df=pd.read_csv("train")
X=df[["Sex","Pclass","Age","Fare"]].copy()
X["Sex"]=X["Sex"].map({"male": 0, "female": 1})
X["Age"]=X["Age"].fillna(mean("Age")
