"""
#예제1: 리턴문도 없고 인자도 없는 함수
def printHello():
    print("Hello, user")

printHello()

#예제2: 리턴문이 없는 함수
def printHi(name):
    print("Hi",name)

name = input("당신의 이름은? ")
printHi(name)

#예제3: 리턴문이 있는
def printWelcome(user):
    word = "Welcome, " + str(user)
    return word

user = input("당신의 학번은? ")
print(printWelcome(user))

#예제4 세 개의 값을 동시에 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c = func_mul(10)
print(a, b, c)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

a= func_mul(10)
print(a)

#문자열 안에 우리가 원하는 값을 삽입
#format 함수 사용
#https://wikidocs.net/13 < 다른 포매팅방법
print("저는 덕성 멋사 {}기 입니다.".format(9))

#문자열에 문자열을 입력받아 대입
fruit = input("당신이 좋아하는 과일은? ")
print("내가 좋아하는 과일은 {}입니다.".format(fruit))

#두개 이상의 값 넣기 숫자 인덱스 문자는 이름으로 삽입
print("저는 {0}학번 {major}과입니다.".format(20,major = "텍스타일디자인"))
"""
