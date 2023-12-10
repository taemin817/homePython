# 클래스 상속
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
# 공격 유닛만을 위한 클래스 정의
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name    # 같은 부분 쳐내기
        self.hp = hp    # 같은 부분 쳐내기
        self.damage = damage
# __init__의 self.name=name, self.hp=hp가 겹친다. 상속으로 처리
class AttackUnit(Unit):     # Unit 클래스 상속  class 클래스명(부모 클래스명):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # 부모 클래스의 생성자 호출
        self.damage = damage
class Unit :
    def __init__(self, name:str, hp:int) -> None:
        self.name = name
        self.hp = hp
class AttackUnit(Unit):
    def __init__(self, name:str, hp:int, damage:int) -> None:
        super().__init__(name, hp)   # 부모 클래스의 생성자 호출
        self.damage = damage
    def attack(self, location):
        print('{0} : {1} 방향 적을 공격. [공격력 {2}]'.format(self.name, location, self.damage))
    def damaged(self, damaged):
        print('{0} : {1}만큼 피해를 입었습니다'.format(self.name, damaged))
        self.hp -= damaged
        print('{0} : 현재 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴됐습니다'.format(self.name))
# 파이어뱃 생성 후 공격
print('새로운 유닛 생성 및 공격')
firebat = AttackUnit('파이어뱃', 50, 16)
firebat.attack('5시\n')
# 마린 생성 후 피해받기 및 파괴
marine = AttackUnit('마린', 40, 5)
            # 확인할 개체, 확인할 클래스
print(isinstance(marine, Unit))
marine.damaged(16)
marine.damaged(16)
marine.damaged(16)
# 다중 상속
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('\n{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
interceptor = FlyableAttackUnit('인터셉터', 200, 6, 5)
interceptor.fly(interceptor.name, '3시')
# 메서드 오버라이딩 : 메서드를 재정의하는 것
class Unit:                     #speed : 지상 이동 속도
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print('\n[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다 [속도 {2}]'.format(self.name, location, self.speed))
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print('{0} : {1} 방향 적을 공격. [공격력 {2}]'.format(self.name, location, self.damage))
    def damaged(self, damaged):
        print('{0} : {1}만큼 피해를 입었습니다'.format(self.name, damaged))
        self.hp -= damaged
        print('{0} : 현재 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴됐습니다'.format(self.name))
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상이동속도 = 0
        Flyable.__init__(self, flying_speed)
# 벌처 : 지상 유닛, 속도 빠름
hoverbike = AttackUnit('벌처', 80, 20, 10)
# 배틀크루저 : 공중 유닛, 체력 공격력 좋음
battlecruiser = FlyableAttackUnit('배틀 크루저', 500, 25, 3)
hoverbike.move('1시')
battlecruiser.fly(battlecruiser.name, '10시')
# 메서드 오버라이딩 실습
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init(self, flying_speed)
    def move(self, location):
        print('[공중 이동 유닛]')
        self.fly(self.name,location)
hoverbike.move('4시')
battlecruiser.move('6시')
# 다이아몬드 상속을 지양하며 코딩하기!
# 동작없이 넘어가기 : pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
supply_depot = BuildingUnit('서플라이 디팟', 500, '7시')

def game_start():
        print('[알림]새로운 게임을 시작합니다')
def game_over():
        pass
    
game_start()
game_over()
# 부모 클래스 호출하기 : super()
class BuildUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        self.location = location
# super()를 사용하는 문장에서 self는 사용하지 않음
class BuildUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location
