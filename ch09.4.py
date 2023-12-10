# p.321 실습문제 : 부동산 프로그램 만들기
# 조건 : 생성자로 인스턴스 변수 정의.
# 매물 정보 표시 show_detail(메서드). 실행결과의 3가지 매물로 객체 만들고 매물 수 출력 뒤 각 정보 표시
# 실행결과
'''
총 3가지 매물이 있습니다.
강남 아파트 매매 10억 원 2010년
마포 오피스텔 전세 5억 원 2007년
송파 빌라 월세 500/50만 원 2000년
'''
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
houses = []
house1 = House('강남', '아파트', '매매', '10억 원', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억 원', '2007년')
house3 = House('송파', '빌라', '월세', '500/50만 원', '2000년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {0}가지 매물이 있습니다.'.format(len(houses)))
for house in houses:
    house.show_detail()
    
# p.324 셀프체크 : 주차 차량 등록 관리 프로그램 작성
# 조건
# 총 주차 가능 대수 capacity. 객체 생성할 때 전달받아 인스턴스 변수로 정의
# 현재 등록된 차량 수를 관리하는 count는 객체 생성할 때 0으로 정의
# 객체 생성할 때 등록 가능한 대수를 출력
# 차를 신규 등록하는 register() 정의
# 신규 등록 시 등록 현황을 출력
# 총 주차 가능 대수를 초과하는 경우 "등록 불가 : 대수 초과" 출력
print('')
class ParkingManager:
    # 주차 정보 초기화 : 총 주차 가능 대수
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f'총 {capacity}대를 등록할 수 있습니다')
    def register(self):
        if self.count >= self.capacity:
            print('등록 불가 : 대수 초과')
            return
        self.count += 1
        print(f'차량 신규 등록 ({self.count}/{self.capacity})')
        
manage = ParkingManager(6)
for i in range(7):
    manage.register()