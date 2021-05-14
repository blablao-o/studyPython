#문자열 실습

str = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리입니다."

#덧셈
print(str+str2)

#곱셈
print(str*3)

#인덱싱
print(str[4])
print(str2[5])

#슬라이싱
print(str[0:3])

#문자열길이구하기_len(문자열 변수)
print(len(str))

#특정문자의 등장횟수 반환
str3 = "멋쟁이 사자처럼은 사랑스러워"
print(str3.count('멋'))

#특정기준으로 나누기
print(str3.split())
str4 = "사과,바나나,포도"
print(str4.split(","))

#특정문자 인덱스
print("find: ",str3.find('사'))
print("index: ",str3.index('사'))

#find, index 차이점: find는 -1 반환, index는 오류 발생
print("find: ",str3.find('무'))
print("index: ",str3.index('무'))
