#제어문 실습
#분기문
# if(조건):

#예제1: 85점 이상이면 pass, 85점 이하면 fail 출력
#score = int(input("점수를 입력하세요: "))
#if(score>=85):
#    print("pass")
#else:
#    print("fail")

#예제2
#activity = input("너 동아리 멋쟁이 사자처럼이야?")
#if(activity=="응"):
#    print("어! 나도 멋사자야!")
#else:
#    print("아..그래...")

#예제3
#money = int(input("너 돈 얼마있어? "))
#if(money>=50000):
#    print("아웃백을 가자")
#elif(money>=10000):
#    print("학식 먹으러 가자!")
#elif(money>=5000):
#    print("컵밥 먹으러 가자!")
#elif(money>=1000):
#    print("컵라면 먹으러 가자!")
#else:
#    print("집이나 가자")

#반복문예
#ex1
#num = 0
#while(True):
#    print(num)
#    num = num +1 #num += 1
#    if(num == 3):
#        break

#ex2
for i in range(10):
    if(i%2==0):
        continue
    print(i)
