"""
from faker import Faker as fk
import os
import pandas as pd

temp = fk("ko-KR")

folder = "data/"

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
        
target = folder + "fktemp.csv"

df = pd.read_csv(target)
"""
#rank 매기기
"""
df["aver"] = df.postcode.rank(method="average")
print(df[["postcode","aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode","dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode","first"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode","min"]])

df["max"] = df.postcode.rank(method="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode","max"]])

print(df[["postcode","max","min","first","dense","aver"]])
"""

# 전치 컬럼 로우 변환
"""
print(df.transpose())

# 누적 계산

print(df["postcode"].expanding().sum())
print(df["postcode"].expanding().max())
print(df["postcode"].expanding())

# 가장 작은수
df.postcode.idxmax(axis=0) 
# 가장 큰수
df.postcode.idxmin(axis=0)

# 빈 dataframe 확인
print(df.empty())
print(df.company.empty())

# 검색
print(df.isin[48742])
print(df.isin["박이배"])

print(df.isin[88742,12834])

print(df.isin[88742,12834,"장상호"])


# 기간 계산
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf)

i = pd.date_range("2023-11-10", periods=10, freq="1H") 
# 한 시간 단위로 증가함 ^
# i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# 특정시간 찾기
print(df.at_time("09:00"))
print(df.at_time("03:00"))

print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="3:00", end_time="00:00"))

#x일 간격 생성 - 기간별 찾기
i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# print(df.first("3D"))

# print(df.first("7D"))

# print(df.last("7D"))
"""
# 코스피 지수
"""
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001")"""

"""print(ksp)
 
print("\n----------------------------------\n")

# 최고가
res1 = ksp["High"].max()
print(res1)
res2 = ksp["High"].idxmax()
print(res2)

# 최저가
res3 = ksp["Low"].min()
print(res3)
res4 = ksp["Low"].idxmin()
print(res4)

# 최하위가
res5 = ksp["Volume"].nsmallest(n=5)
res6 = ksp["Close"].nsmallest(n=5)
res7 = ksp["Cose"].nlargest(n=5)
print(res5)
print(res6)
print(res7)

# kospi 3000 달성 최초일 찾기
# cond = ksp["Close"] >= 2000
cond = cond = ksp["Close"] >= 3000
print(cond)
res = ksp[cond].index[0]
print(res)
"""

# 위(shift) 값 참조, 처리
"""
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
print(ksp)

# res = ksp["up"] != ksp["up"].shift().cumsum()
# print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift().cumsum())
print(ksp)

# 연속 증가값 확인
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

print(ksp["up_cnt"].max())
"""

# 변환
import pandas as pd

target = "data/apt.csv"

df = pd.read_csv(target, encoding="CP949")
# print(df.head())

df.to_csv("data/apt.csv", encoding="utf8")

df = pd.read_csv("data/apt.csv", index_col=0)

# 컬럼명 바꾸기
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

# array 변환
arr = df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

# print(df.describe())

# print(df.transpose())
# print("\n--------------------\n")
# print(df.T.head())