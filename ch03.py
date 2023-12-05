# 연산자
# 산술 연산자
print(10+10)
print(10-10)
print(10*10)
print(10/10) # 실수로 표현됨
# ** : 연산자 왼쪽을 오른쪽만큼 거듭제곱
print(2**4)
# % : 연산자 왼쪽을 오른쪽으로 나눈 나머지
print(7%3)
# // : 연산자 왼쪽을 오른쪽으로 나눈 몫
print(7//3)
# 비교 연산자 : 결과가 불린으로 출력
print(10>3)
print(4>=7)
print(10<3)
print(5<=5)
print(5==5)
print(5!=4)
a = 10
print(0<= a <= 15)
print(11 < a < 13)
# 논리 연산자
print((3>0) and (3>5))
print((3>0) or (3>5))
print(not(1!=3))
print(5>4>3)
print(4>5>3)
# in 으로 해당 글자가 포함돼있는지 확인
print('곰' in '곰돌이')
print('푸' in '곰돌이')
# 변수 연산
number = 2+3*4
print(number)
number = 2+3*4+2
# 중복된 내용을 줄여보자
print(number)
number = 2+3*4
print(number)
number = number+2
# 한번 더 줄여보자
print(number)
number = 2+3*4
number+=2
print(number)
# 함수로 연산
print(abs(-5)) # print()도 함수다..!
print(pow(2,3)) # 2를 3제곱
print(pow(10,2,3)) # 10의 2제곱을 3으로 나눈 나머지
print(max(4,9)) # 4와 9중 큰 값
print(min(2,8)) # 2와 8중 작은 값
print(round(4.6893, 2)) # 4.6893을 소수점이하 2번째 자리까지 반올림한 값
print(round(3.14)) # 소수점이하 몇자리까지 반올림할지 밝히지않으면 정수까지 반올림
# math 모듈
from math import * # math에 있는 모든 기능을 가져다 쓰겠다
# math 중 숫자연산을 수행하는 함수. floor() : 내림, ceil() : 올림, sqrt() : 제곱근
result = floor(4.99)
print(result)
result = ceil(3.14)
print(result)
result = sqrt(16)
print(result)
import math # math에 있는 모든 기능을 가져다 쓰겠다
# import math는 math에 있는 함수를 사용할 때 math. 이라고 명시해야함. 어느 모듈에서 가져왔는지 알기 위해
result = math.floor(4.99)
print(result)
result = math.ceil(3.14)
print(result)
result = math.sqrt(16)
print(result)
# random 모듈 : 0 이상 1 미만의 실수를 무작위로 출력
from random import *
print(random())
print(int(random()*10)) # 0 이상 10 미만의 '실수'를 정수로 변환하여 출력
print(random())
# 10 이상 20 '미만'의 '정수'를 무작위로 출력, 10<= <20
print(randrange(10, 20))
# 10 이상 20 '이하'의 '정수'를 무작위로 출력, 10<= <=20
print(randint(10, 20))
# 로또를 위한 난수 생성
print(int(random()*45)+1)
# p.88 실습문제 : 스터디 날짜 정하기
# 조건 : 날짜는 무작위, 최소 28일까지, 1~3일은 준비기간으로 제외
date = str(randint(4,28))
print('오프라인 스터디 모임 날짜는 매월 ' + date + '일로 선정되었습니다')
# p.92 셀프체크 : 온도 단위 변환 프로그램
# 조건 : 섭씨온도 변수 생성, 공식을 이용해 화씨온도 변수에 저장
# 섭씨 30도 일 때
c = 30
f = (c*9/5)+32
print(f)
# 섭씨 10도 일 때
c = 10
f = (c*9/5)+32
print(f)