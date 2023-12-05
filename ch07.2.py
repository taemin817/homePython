# 함수 호출
def profile(name, age, main_lang):
    print('이름 : {0}\t나이 : {1}, \t주 사용 언어 : {2}'.format(name, age, main_lang))    
profile('찰리', 20, '파이썬')
profile('루시', 25, '자바')
# 기본값 설정
def profile(name, age=20, main_lang='파이썬'):
    print('이름: {0}\t나이:{1}\t주 사용언어:{2}'.format(name, age, main_lang))
profile('찰리')
profile('루시')
def profile(name, age=20, main_lang='파이썬'):
    print('이름: {0}\t나이: {1}\t주 사용 언어: {2}'.format(name, age, main_lang))
profile('찰리')
profile('찰리', 22)
profile('찰리', 24, '자바')
# 전달값 작성 순서 : 함수를 정의할 때 일반 전달값과 기본값이 있는 전달값을 혼용할 경우 일반 전달값을 먼저 작성
def buy(item1, item2='음료수'):
    print(item1, item2)
buy('빵')
'''def buy(item1='음료수', item2):
    print(item1, itemz)
buy(빵)'''
# 키워드 인자 사용
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name='찰리', main_lang='파이썬', age=20)
profile(main_lang='자바', age=25, name='루시')
def profile(name, age, main_lang):
    print(name, age, main_lang)
# 일반 전달값을 먼저 작성
profile('찰리', age=20, main_lang='파이썬')
# 일반 전달값을 나중에 작성. 오류
'''profile(name='루시', 25, '파이썬')'''
# end를 이용해 한줄로 표현하기
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# 한 줄 print가 끝나고 마지막에 ''이 온 다음 print가 온다
    print('이름: {0}\t나이: {1}\t'.format(name, age), end='')
    print(lang1, lang2, lang3, lang4, lang5)
profile('루시', 25, '코틀린', '스위프트', '', '', '')
# 가변인자
def profile(name, age, *lang):
    print('이름: {0}\t나이: {1}\t'.format(name, age))
    print(lang, type(lang))
profile('찰리', 20, '파이썬', '자바', 'c', 'c++', 'c#')
def profile(name, age, *lang):
    print('이름: {0}\t나이: {1}\t'.format(name, age), end='')
    print(lang, type(lang))
profile('루시', 25, '코틀린', '스위프트', '자바스크립트')
# 튜플이 아니라 기존의 출력 형태로 출력하기
def profile(name, age, *lang):
    print('이름: {0}\t나이: {1}\t'.format(name, age), end='')
    for i in lang:
        print(i, end=' ')
    print('')
profile('루시', 25, '코틀린', '스위프트', '자바스크립트')
def profile(name, age, *lang):
    print('이름: {0}\t나이: {1}\t'.format(name, age), end='')
    print(*lang)
profile('찰리', 20, '파이썬', '자바', 'c', 'c++', 'c#')
# 지역변수와 전역변수
glasses = 10
def rent(people):
    global glasses  # 전역변수 glasses를 가져오겠다
    glasses = glasses-people
    print('[함수내부] 남은 3D안경 개수: {0}'.format(glasses))
print('전체 3D 안경 개수: {0}'.format(glasses))
rent(2)
print('남은 3D 안경 개수: {0}'.format(glasses))
print('')
glasses = 10
def rent_return(glasses, people):
    glasses = glasses-people
    print('[함수내부] 남은 3D안경 개수: {0}'.format(glasses))
    return glasses
print('전체 3D 안경 개수: {0}'.format(glasses))
rent_return(glasses, 3)
print('남은 3D 안경 개수: {0}'.format(glasses))
# p.216 실습문제 : 표준 체중 구하기
# 조건 : 표준 체중은 별도 함수로 계산, 키는 미터단위, 소수점이하 둘째자리까지
# 함수명 : std_weight, 전달값: height, weight
constantM = 22
constantF = 21
def std_weight(height, gender):
    if gender == '남자':
        weight = height*height*constantM
        return weight
    else: 
        weigth = height*height*constantF
        return weight
height=170
gender='남자'
weigth=(round(std_weight(height/100, gender), 2))
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다'.format(height, gender, weigth))
# p.220 셀프체크 : 미세먼지 수치로 대기 상태 출력
# 조건 : ger_air_quality 이름의 함수. 전달값으로 미세먼지수치, 대기질 상태 반환
# 수치에 따른 대기질 상태
# 좋음:0~30, 보통:31~80, 나쁨:81~150, 매우나쁨:151 이상
def get_air_quality(dust):
    if 0<=dust<=30:
        return '좋음'
    elif 30<dust<=80:
        return '보통'
    elif 80<dust<=150:
        return '나쁨'
    else:
        return '매우 나쁨'
print(get_air_quality(77))