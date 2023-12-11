#다중 그래프 출력

import matplotlib.pyplot as plt

"""
# 사용데이터
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

plt.subplot(2, 1, 1)    # 1set
#plt.subplot(1, 2, 1)    # 2set
#plt.subplot(3, 1, 1)    # 3set
#plt.subplot(2, 2, 1)    # 4set
plt.plot(x1, y1, "o-")


plt.title("x2 Graph")
plt.xlabel("x2-data")
plt.ylabel("y2-data")

#스타일 지정
plt.style.use("bmh")
#plt.style.use("ggplot")
#plt.style.use("Solarize_Lightz")
#plt.style.use("classic")

plt.subplot(2, 2, 4)
plt.plot(x1, y1, ".-")
plt.plot(x2, y2, ".-")

#plt.show()

#이미지 저장
plt.savefig("data/img.jpg")
plt.savefig("data/img.png")
"""

#다중 객체를 이용한 막대 그래프 출력
"""
x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2)
#ax1.bar(x_years, y_data)
#ax2.bar(x_years, y_data)
#ax3.bar(x_years, y_data)
#ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color = "aquamarine", edgecolor = "black", hatch = " /" )
ax2.bar(x_years, y_data, color = "salmon", edgecolor = "black", hatch = " \\")
ax3.bar(x_years, y_data, color = "navajowhite", edgecolor = "black", hatch = "+")
ax4.bar(x_years, y_data, color = "lightskyblue", edgecolor = "black", hatch = "*")

plt.show()
"""

# Seaborn 사용

import seaborn as sns
import pandas as pd
import FinanceDataReader as fdr
"""
tips = sns.load_dataset("tips")
print(tips)
sns.regplot(x="total_bill", y="tip", data=tips)

plt.show()
"""
"""
#각 지표별 상관관계 출력

tips = sns.load_dataset("tips")
print(tips)

plt.figure(figsize=(10,6))

#sns.regplot(x="day", y="tip", data=tips)
sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
#sns.regplot(x="tip", y="total_bill", data=tips)
#sns.regplot(x="sex", y="total_bill", data=tips)
#sns.regplot(x="sex", y="tip", data=tips)
#sns.regplot(x="smoker", y="tip", data=tips)
#sns.regplot(x="time", y="total_bill", data=tips)

plt.title("Average tips")
plt.xlabel("x")
plt.ylabel("average")
"""
#타이타닉 데이터
"""
titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show()

#각 지표별 출력
# 탑승클래스별 인원구성
sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)

plt.show()
"""

#주식 데이터 분석
"""
df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

df0["Close"].plot()

plt.grid(True)

plt.show()

#다우지수와 코스피 비교

dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# 각 지수별 종가 기준 그래프 출력
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

#최고가 기준
plt.plot(dow.index, dow.High, "r--", label="Dow")
plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

#해당 날짜 기준 증가 상승율 상대 수익을 계산
d = (dow.Close / dow.Close.loc["2010-05-01"]) * 100
k = (kospi.Close / kospi.Close.loc["2010-05-01"]) * 100
plt.plot(d.index, d, "r--",label = "Dow")
plt.plot(k.index, k, "b",label = "Kospi")

plt.grid(True)
plt.legend()
plt.show()
"""
#국내 개별 종목 분석
#국내 주식 코드 확인
# 해당 데이터를 가져오는 URL
# code 는 종목명
url = "https://finance.naver.com/item/sise_day.nhn?code={005930}"

#데이터 파싱

import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs
"""
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

df_list = []

#해당 site 1~ 100 페이지 파싱
page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
    
print(df_list)

#리스트에 담긴 dataframe을 한번에 연결
df = pd.cmcat(df_list,ignore_index = True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.figure(figsize = (15,5))
plt.title("Target(close)")
plt.xticks(rotation = 45)
plt.plot(["날짜"],df["증가"],"co-")
plt.plot(df["날짜"], df["종가"], "co-")
"""

#미국 개별 종목 분석
import yfinance as yf
"""
#MS
ticker = "MSFT"

# Apple
ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

#시각화
plt.figure(figsize=(12,6))
plt.plot(data["Close"],label = "Close Price")

#평균 계산
# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()
"""

#국가별 인구 데이터 분석

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

countries = []
populations =  []


#테이블 분석
rows = soup.select("#example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)
    
top_countries = countries[:10]
top_population = populations[:10]