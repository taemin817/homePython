class Unit:
    def __init__(self):
        print('Unit 생성자')
class Flyable:
    def __init__(self):
        print('Flyable 생성자')
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
# 드랍십
dropship = FlyableUnit()
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()
dropship = FlyableUnit()
# 부모 클래스 생성자 모두 부르고 싶을 때
print('부모 클래스 생성자 모두 부르고 싶을 때')
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)
dropship = FlyableUnit()