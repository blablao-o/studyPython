#리스트 실습

li = [3,1,"배가",4,"고파요",5,1]

#인덱싱
print(li[2])

#슬라이싱
print(li[0:4])

#길이 구하기
print(len(li))

#오름차순 정렬
li2 = [3,1,4,5,2]
li2.sort()
print(li2)

#참고:sorted
li3=sorted(li2)
print(li3)
print(li2)
li2.sort()
print(li2)

#sort()로 내림차순 하는 법
li2.sort(reverse=True)
print(li2)

#리스트 내의 특정 원소 인덱스 반환
print(li.index("배가"))

#특정 원소 갯수
print(li.count(1))