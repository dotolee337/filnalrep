
import matplotlib.pyplot as plt
"""
#두 축 설정
x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

#plt.plot(x_value, y_value)
#plt.plot([2, 4, 6, 7, 10],[1, 4, 5, 8, 9])

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

plt.xlabel("x축")
plt.ylabel("y축")

#plt.show()

#solid 픽셀크기-간격
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (10, 0)), label="PData(km)")

#문자열 색 지정
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="(rgb 값 코드)", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

#rgb값 얻는 법 -> 윈도우 그림판에서 rgb값 얻기 가능

#모양 설정(선 두께, 둥근모양 / 사각형 모양 설정 )
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, dash_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, dash_capstyle="round", label="Value(m)"
#plt.show()

#마커 / 선 동시 설정
# c=cyan d=diamond
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "go-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "co-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

#plt.show()

#marker 파라메터 사용
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=D, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")

#plt.show()

#그래프 영역 채우기

xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.xlabel("x_data")
plt.ylabel("y_data")

#세로 축 채우기
#plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5) #x와 y 데이터 범위 같아야함
#plt.fill_between(xdata[2:4], ydata[2:4], alpha=1)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#가로 축 채우기
#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

#plt.show()

#plt.plot([1, 3, 5, 7, 9],[2, 4, 6, 8, 10])
#plt.plot(xdata, ydata)

#두 선간의 영역 채우기
#x축이 동일한 두 선간의 공백을 채우기
#plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], clolr = "C2", alpha=0.5)

#영역 채우기
#plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 3.1], alpha=0.5)

plt.show()
"""
#==================================================================
"""
#배경 설정
#배경 그리드 변경

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val , label= "PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label= "Value(m)")
#plt.plot =([1,4,5,9],[2,3.8.10])
plt.xlabel("x-data")
plt.ylabel("y-data")

#배경그리드
#plt.grid()

#plt.show()

# x축 그리드
#plt.grid(axis="x")

# y축 그리드
#plt.grid(axis="y")

# 색상 설정
#plt.grid(axis="y", color="g")
#plt.grid(axis="y", color="b")

# 투명도 설정
#plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
#plt.grid(axis="y")
#plt.grid(axis="y", color="g", alpha=0.5, linestyle="--")
#plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

#plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
#plt.grid(axis="x", color="r", alpha=0.3, linestyle="-.")

#plt.show()

#눈금표시

#plt.xticks()
#plt.yticks()

# 임의 데이터 지정
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

#plt.xticks([1,3,5,7,9,11])
#plt.xticks([2,4,6,8,10,12])

# 라벨 지정
#plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지
#plt.tick_params(axis="x", direction="in")
#plt.tick_params(axis="x", direction="out")
#plt.tick_params(axis="y", direction="in")
"""

#막대그래프 그리기
"""
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

plt.bar(x_years, y_data)
#plt.show()

#색 지정
plt.bar(x_years, y_data, color="g")
#plt.bar(x_years, y_data, color="C7")
#plt.bar(x_years, y_data, color="#57ADCC")

#개별 색 지정
plt.bar(x_years, y_data, color=clr)

#막대 너비 설정
plt.bar(x_years, y_data, color=clr, width=2)
#plt.bar(x_years, y_data, color=clr, width=0.5)
#plt.bar(x_years, y_data, color=clr, width=0.1)

#막대 위치 선정 edge/center
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

#막대 테두리 설정
# 라인 색 선택
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)

# 테두리 라인 설정
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

#축 설정
#plt.xticks()
plt.yticks([100, 200, 300, 400, 500, 600, 900])

plt.show()
"""
#수평 그래프 그리기

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

plt.barh(x_years, y_data)

#그래프 설정
#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()