class ThaiPackage:
    def detail(self):
        print('[태국 3박 5일 패키지]방콕, 파타야 여행(야시장 투어) 50만 원')
# 모듈을 직접 실행하는 경우
if __name__ == "__main__":    # __name__이 __main__일 때
    print('thai 모듈 직접 실행(할 때만 이 문장 출력)')
    trip_to = ThaiPackage()     # ThaiPackage 클래스를 객체로 만들어 
    trip_to.detail()    # detail() 메서드를 호출
else:   # 외부에서 모듈 호출
    print('외부에서 thai 모듈 호출')
    
