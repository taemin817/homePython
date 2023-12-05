# 표준 입력받기
'''
answer = input('아무 값이나 입력하세요 : ')
print('입력한 값은 '+answer+'입니다')
answer = input('아무 값이나 입력하세요 : ')
print('입력한 값은 '+answer+'입니다')
print(type(answer))
answer = input('아무 값이나 입력하세요(숫자) : ')
print(int(answer))
print(type(int(answer)))
'''
# 표준 출력시 유용한 기능
# 구분자 : sep
print('파이썬', '자바')
print('파이썬'+'자바')
# 값을 ',' 로 구분
print('파이썬', '자바', sep=',')
print('파이썬', '자바', sep='vs')
# 문장 끝 지정 : end
# end의 기본 값은 \n(개행), 대신 다른 값 넣어줄 수 있다
print('파이썬', '자바', sep=', ', end='?')
print('무엇이 더 재밌을까요?')
# 출력 위치 지정하기 : file
import sys
print('파이썬', '자바', file=sys.stdout)
print('파이썬', '자바', file=sys.stderr)
scores = {'수학':20, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject, score)
# 공간 확보하기 : ljust(), rjust()
scores = {'수학':20, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject.ljust(3), str(score).rjust(4), sep=':')
                # 왼쪽정렬              # 오른쪽정렬
for subject, score in scores.items():
    print(subject.center(6), str(score).rjust(4), sep=':')
                # 가운데정렬
# 빈칸 0으로 채우기 : zfill()
for num in range(1,6):
    print('대기번호 : '+str(num))
# 3자리 확보 후 남은 공간을 0으로 채움
for num in range(1,21):
    print('대기번호 : '+str(num).zfill(3))
org = '+hello'
print(org.zfill(8))
# zfill()의 값이 음수이면 문자 그대로 출력
org = 'hello'
print(org.zfill(-8))
# format()
print('{0}'.format(500))
# 10칸 확보 후 오른쪽 정렬
print('{0: >10}'.format(500))
# 10칸 확보 후 왼쪽 정렬, 나머지는 +로 채움
print('{0:+<10}'.format(500))
# 10칸 확보 후 +붙이고 오른쪽 정렬, 나머지는 빈칸
print('{0: >+10}'.format(500))
# 10칸 확보 후 그대로 출력하고 오른쪽 정렬, 나머지는 빈칸
print('{0: >10}'.format(-500))
# 3자리마다 , 사용하기
print('{0:,}'.format(100000000))
# 소수 출력
print('{0}'.format(5/3))
print('{0:f}'.format(5/3))
# 소수점 이하 2번째자리까지 출력
print('{0:.2f}'.format(5/3))