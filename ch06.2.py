# 반복문
# for문
for waiting_no in [1, 2, 3, 4, 5]:
    print('대기번호 : {0}'.format(waiting_no))
for waiting_no in range(5): # 0~4 출력
    print('대기번호 : {0}'.format(waiting_no))
for waiting_no in range(1, 6):  # 1~5 출력
    print('대기번호 : {0}'.format(waiting_no))
for waiting_no in range(1,6,2): # 1부터 5사이를 2만큼의 간격씩 출력 -> 1, 3, 5
    print('대기번호 : {0}'.format(waiting_no))
orders = ['아이언맨', '토르', '스파이더맨']
for customer in orders:
    print('{0}님, 커피가 준비됐습니다'.format(customer))

# 딕셔너리 순회
dic = {'apple':'사과','banana':'바나나','grape':'포도'}
for i in dic.keys():
    print(i)
# 리스트 순회
li = ['1000', '2000', '3000']
for i in li:
    print(i)
# 세트 순회
s = {'삼성', '엘지', '애플'}
for i in s:
    print(i)
# while문
index = 5
while index>=1:
    print('{}님 커피가 준비됐습니다'.format(customer))
    index-=1
    print('{}번 남았어요~'.format(index))
    if index == 0:
        print('커피는 버려집니다~')
customer = '아이언맨'
index = 1
customer = input('성함은요?')
index = int(input('횟수를 입력하세요'))
while index >= 1:
    print(f'{customer}님 커피가 준비됐습니다')
    index -= 1
    print(f'{index}번 남았습니다')
    if index == 0:
        print('커피 버립니다~')
'''while True:
    print('{0}님 커피가 준비 됐습니다. {1}번째 호출입니다'.format(customer, index))
    index+=1'''
customer = '토르'
person = None
while person != customer:
    print('{0}님 커피가 준비됐습니다'.format(customer))
    person = input('이름이 어떻게 되세요?')
# 흐름 제어 : continue와 break
# continue
absent=[2,5]
for student in range(1,11):
    if student in absent:
        continue
    print('{0}번 책 읽어라'.format(student))
# break
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print('{0}번 학생은 교무실로 따라와'.format(student))
# for문 한 줄로 작성 : 동작 for 변수 in 반복 대상ß
# for문에 있는 변수와 앞에 있는 변수 이름이 같아야함
student = [1, 2, 3, 4, 5]
print(student)
oddNumber = [i for i in range(1, 10, 2)]
print(oddNumber)
# 외부의 변수를 사용하는 건 괜찮
student = [i+100 for i in student]
print(student)
x = 100
oddNumber = [x+i for i in range(1, 10, 2)]
print(oddNumber)
student = ['IronMan', 'Thor', 'SpiderMan']
print(student)
student = [len(i) for i in student]
print(student)
# p.185 실습문제 : 택시 승객 수 하기
# 손님별 운행별 소요시간 : 5~50분 난수로
# 운행 소요시간 5~15분인 손님만 매칭. 매칭되면 [0], 안되면 []
from random import *
cnt = 0 # 총 손님 수
for i in range(1, 51):
    dtime = randrange(5, 51) # 운행 소요시간
    if 5<=dtime<=15:
        print('[0]{0}번째 손님 (소요시간 : {1}분)'.format(i, dtime))
        cnt+=1
    else:
        print('[]{0}번째 손님 (소요시간 : {1}분)'.format(i, dtime))
print('총 탑승객 : {0}명'.format(cnt))
# p.188 셀프체크 : 편의점에서 같은 상품 2+1 행사중, 구매상품 수에 따라 가격 계산
# 조건 : 상품가격=1000, 3의 배수에 해당하는 상품을 구매. 스캔할 때마다 '2+1상품입니다' 출력
price = 1000
goods = 3
tprice = 0
for i in range(1, goods+1):
    print('2+1 상품입니다')
    if i%3==0 :
        continue
    tprice+=price
print('총 가격은 ' + str(tprice) + '입니다')