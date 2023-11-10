#비동기 처리
"""
import asyncio
import random as rd
import time

async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
        
    print(f"end of {name}")

async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))

    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end",end-start)
    
if __name__ == '__main__':
    asyncio.run(main())
"""    
#비동기처리 2
"""
import asyncio
import time

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)
        
async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
async def main():
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())

    print("start task")
    start = time.time()
    await task_1
    await task_2
    end = time.time()
    print("end-",end-start)
    print("end task")
    
if __name__ == "__main__":
    asyncio.run(main())
"""
#스케쥴 
"""
import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    print(f"end of {name}")

def run():    
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()


if __name__ == "__main__":
    run()
    # main()
    print("end")
    
#문자열 비교
#pip install diff_match_patch <-터미널에 넣고 설치

import diff_match_patch.diff_match_patch as dm


origin = "To be or not to be, That is a question!"
copyed = "To be or not to be, This is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)
"""
#테스트용 데이터 생성
#pip install Faker <- 터미널에 넣고 설치
"""
from faker import Faker 
# from a import b => a 에 b를 집어 넣겟다? (cf_a.b ex_faker.faker(faker는 이 형태가 지원이 안됨))

temp = Faker()
temp = Faker("ko-KR")
print(temp.name())

#temp = Faker("ko-KR")
print(temp.name())
print(temp.address())
print(temp.postcode())
print(temp.country())
print(temp.company())
print(temp.job())
print(temp.phone_number())
print(temp.email())
print(temp.user_name())
print(temp.ipv4_private())
print(temp.catch_phrase())
print(temp.color_name())

with open("fktemp.txt","w",newline = '') as f :  #엑셀로 열면 데이터 값이 보임
    for i in range(30):
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
"""
#시스템명령어 사용
"""
import subprocess as sp

#res = sp.run(["cmd", "/c", "dir"], capture_output=True)
res = sp.run(["cmd", "/c", "ipconfig", "all"], capture_output=True)
print(res)
"""
#에러처리
"""
import traceback as tb

def tester() :
    #return 1/0
    return 1

def caller():
    tester()
    
def  main() :
    try: 
        caller()

    #except ZeroDivisionError:
        #print("zde error")
    # 0을 나누어 에러 발생시 처리

    except ValueError as ex:
        print("ve error")
    # 유효하지 않는 정수를 입력했을시 처리

    except Exception as ex :
        print("ex error", ex)
    # 모든 예외를 처리할때 처리

    else :
        print("ok")
    # 에러가 없으면

    finally :
        print("end")
    # 해당 함수가 에러가 있든 없든, 완료될때 처리
    
if __name__ == "__main__":
    main()
"""
#HTML

#CSS

#웹크롤링
#pip install beautifulsoup4 <-터미널 넣고 실행
"""
from bs4 import BeautifulSoup as bs
import requests as rq

url = "http://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h2")
print(pres)
print("\n1===================== \n")
print(pres.get_text().strip())
print("\n2===================== \n")
print(pres.next_element.get_text().strip())
print("\n6===================== \n")
print(pres.get_text())

tres = res_html.find("title")
print(tres)
print("\n3===================== \n")
print(tres.next_element)
print("\n4===================== \n")
print(tres.get_text().strip)

fares = res_html.findAll("a")
for i in fares:    
    print(i.get_text())
    
#print(fares)
print("\n5===================== \n")

clres = res_html.findAll(class_ = "doc - title")
print(clres)

print("\n6===================== \n")
clrs = res_html.find(class_ = "head_top")
print(clres)
print(clrs.get_text())
"""
#select
"""
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt,'html.parser')

item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")
#print(item)
print(item.get_text())
goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text())
#wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")

iss = res_html.select("a.wrap_thumb")

for i in iss:
    issue = i.get_text()
    print(issue)
    
print(" \n ============= \n")
ct = res_html.slelct("a.wrap_thumb")
for j in ct:
    c = j.attrs["data-tiara-custom"]
    print(c + "\n")
"""