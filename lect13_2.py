import matplotlib.pyplot as plt
"""
x_years = [1,1.5,2,2.5,3,3.5,4,4.5,5]
y_data = [1,1.5,2,2.5,3,3.5,4,4.5,5]
clr = ["r", "g", "b"]

plt.barh(x_years, y_data)
"""
#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
#plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//////")

#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\")

#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="++")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+++")

#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")

#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="....")

#plt.show()

#산점도 그래프 그리기
"""
x = 1
y = 1

plt.scatter(x, y)
plt.scatter(x+1, y+1)
plt.scatter(x+2, y+1)
plt.scatter(x+3, y+1)
plt.scatter(x+3, y+2)
plt.scatter(x+3, y+3)
plt.scatter(x+4, y+1)
plt.scatter(x+4, y+2)
plt.scatter(x+4, y+3)
plt.scatter(x+4, y+4)

#크기, 색상 변경 
#         {x}{y}{포인트크기}{색상설정}{투명}
plt.scatter(x+1.5, y+1.5, 100, "C1")
plt.scatter(x+1.5, y+1.5, 150, "red")
plt.scatter(x+1.5, y+1.5, 200, 4)

#plt.scatter(x+1.5, y+1.5, 100, 2, alpah=5)
#plt.show()

plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Spectral")
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Blues")
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="inferno")
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magama")
#plt.colorbar()

plt.show()
"""
#히스토그램 그리기

import numpy as np
"""
rn = np.random.randint(1,30,size = 20)
print(rn)

plt.hist(rn, bins=10, label = "def")

# 투명도 설정
#plt.hist(rn,  bins=10, label="def", alpha=0.5)
#plt.hist(rn,  bins=5, label="def", alpha=0.5)

# 그래프 스타일 설정
#plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
#plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfilled")
#plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="barstacked")

#plt.legend()
#plt.show()
"""
#파이챠트 그리기

rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

# plat.pie({data})
plt.pie(rate)

#plt.show()

#라벨 표시
plt.pie(rate, labels=labels)

#퍼센트 표시
plt.pie(rate, labels=labels, autopct='%.1d%%')
plt.pie(rate, labels=labels, autopct='%.1f%%')

#시작각도 설정
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)

plt.show()