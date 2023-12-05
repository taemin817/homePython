# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(10000000000000)
print(3+5)
print(3/3)
print(4-490)
print(3*10)
print(3*(3+2))
# 문자열 자료형
print('ㅁ')
print("사랑해")
print('고마워')
print("2020")
print("pyton "*3)
print("머릿속으로 '학교 가기 싫다'라고 생각했다")
print(5>10)
print(5<10)
# 불린 자료형 1 = True, 0 = False @binary
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
# 변수
print('반려동물을 소개해 주세요')
print('우리 집 반려동물은 개인데, 이름이 연탄이에요')
print('연탄이는 4살이고, 산책을 좋아해요')
print('연탄이는 수컷인가요?')
print('네')
# 변수 정의
name='연탄이'
animal='개'
age=4
hobby='산책'
is_male=True
# 변수 사용
print('반려동물을 소개해 주세요')
print('우리 집 반려동물은 ' + animal + '인데, 이름이 ' + name + '이에요/예요')
print('우리 집 반려동물은 ',animal,'인데, 이름이 ',name,'이에요/예요')
                        #형변환
print(name + '은/는 ' + str(age) + '살이고, ' + hobby + '을/를 좋아해요')
                    #형변환 하지 않아도 됨
print(name + '은/는 ',age,'살이고, ',hobby,'을/를 좋아해요')
print(name + '은/는 수컷인가요?')
print(is_male)
'''여러줄 주석 사용
print
('반려동물을 소개해 주세요')'''
print('우리 집 반려동물은 ' + animal + '인데, 이름이 ' + name + '이에요/예요')
print(name + '은/는 ' + str(age) + '살이고, ' + hobby + '을/를 좋아해요')
print(name + '은/는 수컷인가요?')
print(is_male)
# 형변환
age=20
print('이제 ' + str(age) + '살이다!')
print(float(age))
age=15
print(age + float(age))
# p.64 실습문제 : 역 이름 출력하기
# 변수명은 station, 값은 변수에 '사당, 신도림, 인천공항' 순으로 저장
# 변수가 '사당'
station='사당'
print(station+'행 열차가 들어오고 있습니다')
# 변수가 '신도림'
station='신도림'
print(station+'행 열차가 들어오고 있습니다')
# 변수가 '인천공항'
station='인천공항'
print(station+'행 열차가 들어오고 있습니다')
# p.67 셀프체크
# 변수명은 status, 값은 변수에 '상품 준비, 배송 중, 배송 완료' 순으로 저장
# 변수가 '상품 준비'
status = '상품 준비'
print('주문상태 : ' + status)
# 변수가 '배송 중'
status = '배송 중'
print('주문상태 : ' + status)
# 변수가 '배송 완료'
status = '배송 완료'
print('주문상태 : ' + status)