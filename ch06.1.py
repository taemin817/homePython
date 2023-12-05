# 조건문
# 파이썬은 콜론(:), 스페이스바(빈칸) 4개 혹은 탭으로 들여쓰기하여 실행구간을 정의
# if문
weather = '비'
if weather == '비':
    print('우산을 챙기세요')
# elif문
weather = '미세먼지'
if weather == '비':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
# else문
weather = '맑음'
if weather == '비':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물이 필요 없어요')
# input()으로 입력 받기 : 항상 문자열로 저장함
weather = input('오늘 날씨는 어때요')
print(weather)
weather = input('오늘 날씨 어때')
if weather == '비' or '눈':
    print('우산 챙겨')
elif weather == '미세먼지':
    print('마스크 챙겨')
else:
    print('날씨를 즐겨')
# 문자열로 저장한다는 증거
a = input('숫자 입력하세요')
b = input('숫자 입력하세요')
print('a+b = ' + (a+b))  # 3 아니라 12 출력
# input()을 int()로 감싸기
temp = int(input('오늘 기온 몇도야?'))
if 30<=temp:
    print('너무 덥다')
elif 10<=temp<30:
    print('딱 좋은데?')
elif 0<=tmep<10:
    print('외투 챙겨')
else:
    print('너무 추엉')
# 간단하게 바꾸기
temp = int(input('오늘 최고기온은?'))
if temp>=30:
    print('엄청 덥네')
elif temp>=10:
    print('딱 좋아')
elif temp>=0:
    print('외투 입어')
else:
    print('개추워')
# 멘토노트
grade = 80
if grade >= 95:
    print("A+")
elif grade >= 90:
    print("A")
elif grade >= 85:
    print("B+")
elif grade >= 80:
    print("B")
elif grade >= 75:
    print("C+")
elif grade >= 70:
    print("C")
else:
    print("F")
