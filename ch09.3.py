# 게임 만들기
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 생성'.format(name))
    def move(self, location):
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))
    def damaged(self, damage):
        print('{0} : {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴됐습니다.'.format(self.name))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print('{0}: {1}방향 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
# 보병
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 5, 1) # 이름, 체력, 공격력, 이동속도
    
    # 스팀팩
    def booster(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩 사용(hp 10감소)'.format(self.name))
        else :
            print('{0} : 체력이 부족해 불가능합니다'.format(self.name))
# 탱크
class Tank(AttackUnit):
    # 시즈모드
    siege_developed = False # 개발여부를 클래스 변수로 정의
    
    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 35, 1)
        self.siege_mode = False # 시즈모드 해제 상태를 인스턴스 변수로 정의
    def set_siege_mode(self):
        if Tank.siege_developed == False:   # 개발되지 않았으면 바로 반환
            return
        # 일반모드
        if self.siege_mode == False:
            print('{0} : 시즈모드로 전환'.format(self.name))
            self.damage *= 2
            self.siege_mode = True
        # 시즈모드
        else:
            print('{0} : 시즈모드 해제'.format(self.name))
            self.damage //= 2   # 데미지 절반 감소
            self.siege_mode = False     # 시즈모드 해제
# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{0}: {1}방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)      # 지상 이동속도 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)
# 전투기
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '전투기', 80, 20, 5)
        self.cloaked = False
    def cloaking(self):
        # 현재 클로킹 모드
        if self.cloaked == True:
            print('{0} : 클로킹 off'.format(self.name))
            self.cloaked = False
        else:
            print('{0} : 클로킹 on'.format(self.name))
            self.cloaked = True
# 게임 실행
# 수행할 동작 : 게임 시작, 유닛 생성(마린 3, 탱크 2, 전투기 1), 전부 1시로 이동, 시즈모드 개발, 스팀팩, 시즈모드, 클로킹, 1시 공격, 피해, 종료
# 게임 시작 및 유닛 생성
def game_start():
    print('[알림]게임 시작')
def game_over():
    print('Player : GG')
    print('[Player]님이 게임에서 퇴장했습니다')

game_start()
s1 = Soldier()
s2 = Soldier()
s3 = Soldier()
t1 = Tank()
t2 = Tank()
a1 = Stealth()
# 유닛 부대 지정(리스트에 담기)
attack_units = []
attack_units.append(s1)
attack_units.append(s2)
attack_units.append(s3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(a1)
# 전부 1시로 이동 및 시즈모드 개발
for unit in attack_units:
    unit.move('1시')
Tank.siege_developed = True
print('[알림]시즈모드 개발 완료')
# 공격 준비 및 공격(리스트로 관리되는 유닛들이 서로 다른 기술 사용해야함.
# 구분하려면 isinstance(객체명, 클래스명) 사용
# 공격 준비(스팀팩, 시즈모드, 클로킹)
for unit in attack_units:
    if isinstance(unit, Soldier):
        unit.booster()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):
        unit.cloaking()
# 공격
for unit in attack_units:
    unit.attack('1시')
# 피해
from random import *
for unit in attack_units:
    unit.damaged(randint(5,20))
# 게임 종료
game_over()