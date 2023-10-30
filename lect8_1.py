#cls와 self의 차이
"""
class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count)

#클래스 정의 예시

class Champion:
    lv = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.358
    def __init__(self, name, speed):
        self.hp = 100
        self.name = name        
        self.level = 1
        self.setSpeed(speed)
        self.setatkSpd()
        self.setMovSpd()

    def setAtkSpd(self):
        self.AtkSpd = 0.658*(1.0334)*(Champion.lv)
    
    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20 + self.speed) *100
    
    def beAtk(self, dem):
        print("be attack",dem,200)
        self.dem = self.dem * 0.78
    """

#객체지향 프로그래밍 특징(5가지) 
# : 캡(슐화) 추(상화) 다(형성) 정(보은닉) 상(속)

#상속(가장중요)
#한 클래스가 다른 클래스의 특성과 동작을 그대로 물려받아 사용하는것
#클래스간 계층적 관계를 구성(부모클래스(상위,슈퍼) - 자식클래스(서브))
"""
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)

class Garen(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName()
user1.getLevel()

user2.getName()
user2.getLevel()
user2.levelup()
user2.levelup()
user2.getLevel()

#상속 -처리2
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
    
class Yasuo(Champion) : ()  #변경없이 똑같이 상속
class Garan(Champion) : ()

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName()
user1.getLevel()

user2.getName()
user2.getLevel()
"""
#오버로딩(과적,과부하)
#동일한 이름의 메서드를 사용하나 매개변수의 타입,갯수를 다르게 정의하는 메카니즘
#파이썬에서는 지원하지 않음

# 오버라이딩(재정의)
# "상속” 받은 자식클래스에서 메서드의 내용을 재정의 하는 것
#타입과 갯수는 부모클래스와 동일 해야함
"""
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")

user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel()
"""
#추상화
#사물의 개체나 시스템을 모델링하기 위해 필요한 특징을 추출하고 강조하는 프로세스
#객체의 복잡성을 관리,중요한 부분을 강조,핵심 특성을 구성하는데 사용
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett = [circ, rect]
for st in sett :
    print(st.area())
"""
#정보은닉
#클래스 내부 속성을 감추어 외부에서 접근을 차단하는 메카니즘
#해당 속성에 접근하기 위해 공개된 인터페이스를 사용하게끔 구성
"""
class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1 = Person("Alice",30,"01011112222")

print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)  #오류뜸
print(user1._number)
"""
#다형성
#동일한 인터페이스를 통해 다양한 객체 타입을 구성할 수 있는 매카니즘.
#코드의 유연성과 재사용성을 향상시키는 역할
"""
class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1 = Student("alice",23,"01011112222") 
user2 = Teacher("bob",25,"01033334444")

print(getPersonName(user1))
print(getPersonName(user2))
"""
#캡슐화
#객체와 관련된 데이터와 메서드를 하나의 단위로 묶는 것을 의미
"""
class Person : 
	def __init__(self, name, age, num) :
		self.name = name
		self.age = age
		self.number = num

	def getName(self) :
        return self.name
    
	def setName(self, newName) :
        self.name = newName
        return

	def getNumber(self) :
        return slef.number
    
	def setNumber(self, newNum) :
        self.number = newNum
        return
p1.getNumber("01011111111")
p2.getNumber("01022222222")

p1.setNumber("11111111111")
p1.setNumber("22222222222")
"""