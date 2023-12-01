import pandas as pd

tr = pd.read_csv("./data/train.csv")
#print(tr)
print("\n ================== \n")
#print(tr.head())

#res = tr.isnull().sum()
#print(res)

#승선지
print("\n ================== \n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
#print(res)

# 컬럼 매핑
res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

#연령
print("\n ================== \n")
res = pd.crosstab(tr["Age"], tr["Survived"])
#print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

#승차등급별
#print("\n ================== \n")
res = pd.crosstab(tr["Pclass"], tr["Survived"])
#print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

#성별별
#print("\n ================== \n")
res = pd.crosstab(tr["Sex"], tr["Survived"])
#print(res)

#호칭 
#print("\n ================== \n")
tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
#print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
res = print(tr["Title"].value_counts())

#print(res)

#print(tr["Age"].isnull())
#print(tr["Age"].isnull().sum())

meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)
#print(tr["Age"].head(20))

#print("\n ================== \n")

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
    
#print(tr)

#print(tr["Age"].head(20))
#print(tr["Age"].isnull().sum())

#나이 구간 나누기
tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
#print(tr.head())
#print("\n ================== \n")
#print(tr.dtypes)

tr.AgeCate = tr.AgeCate.astype(int)
#print(tr.head())
#print(tr.dtypes)

tr.Cabin.fillna("N",inplace = True)
tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
tr["CabinCate"].value_counts()
