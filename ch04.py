# 문자열
s1 = '밥먹자'
s2 = "그만 먹어라"
# s1이 어떤 타입의 변수인지 확인하고 싶을 때
print(s1, type(s1))
# 문자열이 여러 줄로 이뤄졌을 때
s3 = '''엄마: 밥먹자
나: 배 안고파'''
print(s3)
# 원하는 만큼 문자열 자르기 : 슬라이싱
# 인덱스 형식
'''
변수명[특정 인덱스]
변수명[시작 인덱스 : 종료 인덱스]
변수명[시작 인덱스 : ] 시작 인덱스부터 끝까지
변수명[ : 종료 인덱스] 첫 인덱스부터 종료 인덱스까지
'''
# 종료 인덱스 이전(미만)까지 출력한다
jumin = '990229-1234567'
print('연 : '+ jumin[0:2])
print('월 : '+ jumin[2:4])
print('일 : '+ jumin[4:6])
print('생년월일 : ' + jumin[0:6])
print('주민번호 뒷자리 : ' + jumin[7:])
# 음수 인덱스는 제일 마지막이 -1
print('주민번호 뒷자리(뒤에서부터) : ' + jumin[-7:])
# 문자열 함수
p = 'Python is Amazing and Amazing'
print(p.lower())
print(p.upper())
print(p[0].isupper())
print(p[1:3].islower())
print(p.replace('Python', 'Java')) 
# 처음 a가 있던 인덱스
print(p.index('a'))
# 2번째~12번째까지 중 처음 a가 있던 인덱스. 없으면 프로그램 종료
print(p.index('a', 2, 13))
print(p.count('Amazing'))
print(p.find('Java')) # 없으면 -1 출력
print(len(p)) # 공백 포함, 변수가 함수의 매개변수로 온다
# 문자열 포매팅 print('문자열 서식지정자 문자열' % 값)
print('나는 %d살 입니다' % 20)
print('나는 %s를 좋아합니다' % '자바')
print('Apple은 %c로 시작해요' % 'A')
print('나는 %s살 입니다' % 20)
print('i am %ccc.' % 'A')
print('나는 %s과 %s을 좋아합니다'%('파랑색', '빨강색'))
age = 20
lang = 'python'
startsWith = 'A'
print('나는 %d살 입니다.' % age)
print('나는 %s을 좋아합니다.' % lang)
print('Apple은 %s로 시작해요' % startsWith)
print('나는 {}살 입니다.'.format(age))
print('나는 {}을 좋아합니다.'.format(lang))
print('Apple은 {}로 시작해요'.format(startsWith))
print('나는 {}색과 {}색을 좋아해요'.format('파란','빨간'))
# 인덱스를 이용하기
print('나는 {0}색과 {1}색을 좋아해요'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란','빨간'))
# f문자열 : 직관적으로 출력 결과 확인 가능
print(f'나는 {age}살 입니다.')
print(f'나는 {lang}을 좋아합니다.')
print(f'Apple은 {startsWith}로 시작해요')
# 탈출 문자
print('백문이 불여일견\n백견이 불여일타')
print('저는 \'나도코딩\'입니다')
print("저는 \"나도코딩\"입니다")
print('C:\\Users\\')
print(r'C:\Users\programfiles')
print('Red\tApple')
# p.117 실습문제 : 비밀번호 만들기
# 사이트별로 비밀번호 생성하는 프로그램 작성
# http://naver.com
# 조건 : http:// 제외, 처음 만나는 점(.) 이후도 제외, 남은 글자 중 세자리 + 글자 개수 + 글자 내 'e'개수 + ! 로 구성
# 실행결과 : http://naver.com의 비밀번호는 nav51!입니다 로 출력
url = 'http://naver.com'
# url = 'http://daum.net'
# url = 'http://google.com'
# url = 'http://youtube.com'
state = url.replace('http://','')
state = state[:state.index('.')]
password = state[:3]+str(len(state))+str(state.count('e'))+'!'
print(f'{url}의 비밀번호는 {password}입니다.')
# p. 121 셀프체크
# 영어 문장이 주어졌을 때 첫 번째 글자는 대문자로, 나머지 글자는 모두 소문자로 변환하는 프로그램
# 주어진 문장 : the early bird catches the worm
sentence = 'the early bird catches the worm'
# print(sentence.capitalize())
sentence = sentence[0].upper()+sentence[1:].lower()
print(sentence)