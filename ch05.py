# 리스트
stations = []
stations.append('사당')
print(stations)
stations.append('신촌')
stations.append('홍대')
print(stations)
# 2번째 인덱스에 추가
stations.insert(2, '강남')
print(stations)
# 마지막 인덱스의 원소를 삭제
stations.pop()
print(stations)
# 1번째 인덱스 삭제  *변수에 할당한 값이 리스트의 크기보다 크거나 같다면 error 후 종료
stations.pop(1)
print(stations)
stations.append('신도림')
stations.append('삼성')
stations.append('잠실')
print(stations)
# 해당하는 원소를 삭제  *해당 원소가 존재하지 않으면 error 후 종료
stations.remove('삼성')
print(stations)
stations.append('신도림')
stations.append('삼성')
stations.append('신도림')
stations.append('삼성')
# 중복 값 확인
print(stations)
print(stations.count('신도림'))
stations.append('신림')
stations.append('문래')
# 정렬
stations.sort() # 반환값 없기 때문에 print(stations.sort()) 불가능, 해당 리스트 자체를 정렬
print(stations)
num_list = [5, 2, 4, 3, 1, 6]
# 오름차순 정렬 1
num_list.sort()
print(num_list)
# 오름차순 정렬 2  * 원본 리스트 변경 없이 정렬된 리스트를 새로 생성
new_list = sorted(num_list)
print('sorted(num_list) : ' + str(num_list))
print(new_list)
# 내림차순 정렬
num_list.sort(reverse=True)
print(num_list)
# 순서(인덱스) 뒤집기
num_list.reverse()
# 출력 결과 : [6, 1, 3, 4, 2, 5]
print(num_list)
# 전체 지우기
stations.clear()
print(stations)
# 리스트 확장
mix_list = ['문자열', 20, True, [5, 4, 3, 2, 1]]
print(mix_list)
num_list.extend(mix_list)
print(num_list)
# 딕셔너리
cabinet = {3:'푸', 100:'피글렛'}
print(cabinet)
print(cabinet.items())
# print(cabinet)과 print(cabinet.items())의 차이점은 이후에 다룸
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) : 5에 해당하는 원소가 없으면 error 후 종료
# print(cabinet.get(5)) : 5에 해당하는 원소가 없으면 None
print(cabinet.get(5, '사용가능'))  # 5가 없다면 사용가능 이라고 출력
# 해당 딕셔너리에 존재하는지 확인
print(3 in cabinet)
print(5 in cabinet)
cabinet = {'a':'푸', 'b':'곰돌이'}
# 값을 변경, 새로 추가하는 것은 대괄호 사용
cabinet['a'] = '티거'  # 해당 키가 있다면 변경
cabinet['c'] = '이요르'  # 해당 키가 없다면 추가
print(cabinet)
# 값을 삭제
del cabinet['c']
print(cabinet)
# 키만 출력
print(cabinet.keys())
# 밸류만 출력
print(cabinet.values())
# 전부 삭제
cabinet.clear()
print(cabinet)
# 튜플
menu = ('돈가스', '치즈가스', '카레추가')
print(menu[0])
print(menu[1])
print(menu[:2])
# 다른 방식으로 출력해보자
# 왼 오 의 갯수가 같아야한다
(name, age, hobby) = ('피글렛', 20, '코딩')
print(name, age, hobby)
(departure, arrival) = ('김포', '제주')
print(departure, '>', arrival)
(departure, arrival) = (arrival, departure)
print(departure, '>', arrival)
# 세트
my_set = {1, 3, 2, 3, 3}
print(my_set)
java = {'푸', '피글렛', '티거'}
# 다른 방식으로 set에 저장해보자
python = set(['푸', '이요르'])
# 교집합 출력
print(java & python)
print(java.intersection(python))
# 합집합 출력
print(java | python)
print(java.union(python))
# 차집합
print(java - python)
print(java.difference(python))
# 추가
python.add('피글렛')
print(python)
# 제거  * 존재하는 원소를 삭제해야 한다
java.remove('피글렛')
print(java)
# 빈 세트 생성
empty_set = set()
# 자료구조 변환하기
menu = {'커피', '우유', '주스'}
print(menu)
print(type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))
# random 모듈 연습
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
# p.152 실습문제 : 당첨자 뽑기
# 조건 : 댓글은 20명이 작성, 아이디는 1~20으로. 무작위추첨 중복허용x
# random 모듈의 shuffle, sample사용. 치킨 1명, 커피 3명
id = range(1,21)
# range()로 만든 결과는 리스트가 아니기 때문에 list로 형변환
id = list(id)
shuffle(id)
selected = sample(id, 4)
print('치킨 당첨자 {0}'.format(selected[0])) # ch04. 54line 참조
print('치킨 당첨자 {0}'.format(selected[1:]))
# p.157 셀프체크 : 중복 없애기
# 조건 : 신청과목은 리스트로 관리, 같은 과목 2번이상 포함되면 1개남기고 삭제. 출력 순서는 상관없음
subjectList = ['자료구조', '알고리즘', '자료구조', '운영체제']
subjectList = set(subjectList)
subjectList = list(subjectList)
print('신청한 과목은 다음과 같습니다')
print(subjectList)