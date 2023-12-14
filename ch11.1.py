# 모듈 만들기 : theater_module이라는 파일을 작성(서로 같은 경로에 있어야 함)
'''
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)
print('')
# 모듈에 별명 붙여 사용하기
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
print('')
# 모듈의 모든 기능 가져와 사용하기
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)
'''
# 필요한 기능만 사용하기
from theater_module import price, price_morning
price(3)
price_morning(4)
# price_soldier(5) # 정의된 함수가 아니라는 오류 출력
print('')
# 만든 패키지 사용하기
import travel.thai  # import만 사용할 때는 대상이 모듈이나 패키지만 가능
trip_to = travel.thai.ThaiPackage()
trip_to.detail()
from travel.thai import ThaiPackage
trip_to = ThaiPackage()
trip_to.detail()
# 모듈 공개 설정
from travel import *
trip_to = vietnam.VietPackage()
trip_to.detail()
# 패키지와 모듈 위치 확인
import inspect
import random
print("위치 : " + inspect.getfile(random))
from travel import *
print("위치 : " + inspect.getfile(travel))
# 함수 시그니처 확인
import inspect
from greeting import *
print(inspect.signature(greet))