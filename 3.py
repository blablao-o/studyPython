#딕셔너리 실습
pairs = {'아이유' : '자장가','day6' : '한 페이지가 될 수 있게', '디아크' : '빛'}

#하나의 키 value 쌍을 더 추가
print(pairs)
pairs['나인뮤지스'] = '드라마'
print(pairs)

#하나의 키 value 쌍을 삭제
del pairs['디아크']
print(pairs)

#key value 값 찾기
print(pairs.get('day6'))