# 클래스
name = '보병'
hp = 40
damage = 5
print('{} 유닛을 생성했습니다'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

tank_name = '탱크'
tank_hp = 150
tank_damage = 35
print('{} 유닛을 생성했습니다'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

def attack(name, location, damage):
    print('{0} : {1}방향 적군을 공격. [공격력 {2}]'.format(name, location, damage))
attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

tank2_name = '탱크'
tank2_hp = 150
tank2_damage = 35
print('')
attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)
attack(tank2_name, '1시', tank_damage)

# 위와 같은 방법으로 유닛을 관리하는 건 무리
# 이럴 때 필요한 것이 클래스
# 메서드 : 클래스 안에 작성하는 함수
# 인스턴스 변수 : 메서드 안에 정의한 변수
# 생성자 : 클래스에 정의한 __init__ 메서드, 따로 호출하지 않아도 객체 생성시 자동 호출

#생성자 예시
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{} 유닛을 생성했습니다'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
        
# 기본 생성자를 가진 클래스
class Unit2:            # 초기화
    def __init__(self) -> None:
        pass
    
# 값을 준 상태
print('생성자 예시 2(값을 메서드에 미리 입력함)')
class Unit3:
    def __init__(self, name = 'marine', hp : int = 10, damage : int = 0) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
unit = Unit3()
print('이 유닛은 {0}이고, 체력은 {1}, 공격력은 {2}입니다'.format(unit.name, unit.hp, unit.damage))

# 호출할 때 값을 줌
print('\n생성자 예시 2(호출할 때 값을 줌)')
soldier1 = Unit('보병', 40, 5)
soldier2 = Unit('보병', 40, 5)
tank = Unit('탱크', 150, 35)

class Unit4:
    def __init__(self, name: str, hp: int, damage: int) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛을 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')
marin = Unit4('마린', 40, 5)

# 인스턴스 변수는 외부에서 직접 정의 가능
stealth1 = Unit('전투기', 80, 5)
print('유닛이름 : {0}, 공격력 : {1}'.format(stealth1.name, stealth1.damage))
print('\n생성자 예시 3(인스턴스 변수를 외부에서 직접 정의)')
stealth2 = Unit4('업그레이드한 전투기', 80, 5)
# cloaking이라고 추가해줌
stealth2.cloaking = True
if stealth2.cloaking == True:
    print('{0}는 현재 은폐 상태입니다'.format(stealth2.name))

# stealth1으로 시도하면 error 발생
# 공격 유닛만을 위한 클래스 정의
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):     # 코드가 길면 아래처럼 역슬래시를 쓰고 다음 줄에 이어갈 수 있다
        print('{0} : {1} 방향 적을 공격 [공격력{2}]'\
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        # 피해 정보 출력
        print('{0} : {1}만큼의 피해를 입었습니다'.format(self.name, damage))
        self.hp -= damage
        # 남은 체력 출력
        print('{0} : 남은 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp<=0:
            print('{0} : 파괴됐습니다'.format(self.name))
            
# 파이어뱃 생성 후 공격
print('\n새로운 유닛 생성 및 공격')
firebat = AttackUnit('파이어뱃', 50, 16)
firebat.attack('5시')

# 마린 생성 후 피해받기 및 파괴
print('\n마린 생성 후 피해받기 및 파괴')
marine = AttackUnit('마린', 40, 5)
marine.damaged(16)
marine.damaged(16)
marine.damaged(16)