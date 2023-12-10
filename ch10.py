# 예외 처리 : try-except
print('나누기 전용 계산기')
'''
num1 = int(input('첫 번째 수 입력 :'))
num2 = int(input('두 번째 수 입력 :'))
print('{0}/{1} = {2}'.format(num1, num2, int(num1/num2)))

try:
    print('나누기 전용 계산기')
    nums = []
    nums.append(int(input('첫 번째 수 입력 :')))
    nums.append(int(input('두 번째 수 입력 :')))
    nums.append(int(nums[0]/nums[1]))
    print('{0}/{1} = {2}'.format(nums[0], nums[1], int(nums[0]/nums[1])))
except ValueError:
    print('오류 : 잘못된 값 입력')
except ZeroDivisionError as err0:
    print(err0)
except Exception as errAll:
    print('알 수 없는 오류 발생')
    print(errAll)
'''
'''
# 모든 예외 처리 => Exception
try:
    print('나누기 전용 계산기')
    nums = []
    nums.append(int(input('첫 번째 수 입력 :')))
    nums.append(int(input('두 번째 수 입력 :')))
    # nums.append(int(nums[0]/nums[1]))
    print('{0}/{1} = {2}'.format(nums[0], nums[1], nums[2]))
except Exception as errAll:
    print('알 수 없는 오류 발생')
    print(errAll)
# 오류 발생시키기
print('한자리 숫자 전용 나누기')
try:
    num1 = int(input('첫 번째 숫자 : '))
    num2 = int(input('두 번째 숫자 : '))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print('{0}/{1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('한자리 숫자만 입력해라')
'''
'''
# 사용자 정의 예외 처리하기
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):      # print함수로 객체를 호출할 때 호출됨
        return '[오류코드 001]' + self.msg
try:   
    print('한자리 숫자 전용 나누기')
    num1 = int(input('첫 번째 숫자 : '))
    num2 = int(input('두 번째 숫자 : '))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f'입력값 : {num1}, {num2}')
    print(f'{num1}/{num2} = {int(num1/num2)}')
except ValueError:
    print('잘못된 값. 한 자리 숫자만 입력해라')
except BigNumberError as err10:  # 사용자가 정의한 예외 처리
    print('오류 발생. 한 자리 숫자만 입력해라')
    print(err10)
'''
# 오류와 상관없이 무조건 실행하기 : finally => try를 빠져나가면 무조건 실행
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):      # print함수로 객체를 호출할 때 호출됨
        return '[오류코드 001]' + self.msg
try:   
    print('한자리 숫자 전용 나누기')
    num1 = int(input('첫 번째 숫자 : '))
    num2 = int(input('두 번째 숫자 : '))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f'입력값 : {num1}, {num2}')
    print(f'{num1}/{num2} = {int(num1/num2)}')
except ValueError:
    print('잘못된 값. 한 자리 숫자만 입력해라')
except BigNumberError as err10:  # 사용자가 정의한 예외 처리
    print('오류 발생. 한 자리 숫자만 입력해라')
    print(err10)
finally:
    print('계산기 이용 감사합니다.')

# p.346 실습문제
# 다음 코드를 확인하고 적절한 예외 처리 구문 추가하기
'''
chicken = 10 # 남은 치킨 수
waiting = 1 # 대기번호, 1부터
while True:
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('몇 마리 주문하실건가요?'))
        if order > chicken:     # 남은 치킨보다 주문량이 많을 때
            print('재료 부족')
        else:
            print('[대기 번호 : {0}]주문 수량 : {1}마리'.format(waiting, order))
            waiting += 1    # 대기 번호 증가
            chicken -= order    # 주문 수 만큼 남은 치킨 감소
'''
# 조건 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때 ValueError 처리(잘못된 값). 최대주문수량=10, 매진이면 SoldOutError(매진)
class SoldOutError(Exception):
    pass
chicken = 10 # 남은 치킨 수
waiting = 1 # 대기번호, 1부터
while True:
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('몇 마리 주문하실건가요?'))
        if order > chicken:     # 남은 치킨보다 주문량이 많을 때
            print('재료 부족')
        elif order <= 0:
            raise ValueError
        else:
            print('[대기 번호 : {0}]주문 수량 : {1}마리'.format(waiting, order))
            waiting += 1    # 대기 번호 증가
            chicken -= order    # 주문 수 만큼 남은 치킨 감소
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값')
    except SoldOutError as err0:
        print(err0)
        break

# p.350 셀프체크 : 배터리 관리 프로그램
# 조건
# save_battery 함수 생성
# 배터리 잔량 정보 : level을 전달값으로 받고 반환값은 없음
# 함수 호출하면 잔량 출력 뒤 잔량에 따라 동작 수행. 비정상적 종료 불가능하게끔 함수 안에 예외 처리
# 잔량에 따른 동작
# 30% 초과 : 일반 모드
# 5%~30% : 절전 모드
# 5% 이하 : 종료. 종료메세지를 담은 Exception 객체 생성하여 오류 발생. 오류 처리하는 곳에서 메세지 출력
# 테스트 코드
def save_battery(level):
    try:
        print(f'배터리 잔량 : {level}%')
        if level > 30:
            print('일반 모드로 사용')
        elif level > 5:
            print('절전 모드로 사용')
        else:
            raise Exception('배터리가 부족해 종료합니다')
    except Exception as e:
        print(e)
save_battery(75)
save_battery(25)
save_battery(3)