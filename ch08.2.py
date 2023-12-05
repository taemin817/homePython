# 파일 입출력
# 파일 열고 닫기 : open(), close()
# open('파일명', '모드', encoding='인코딩 형식')
'''
모드
r(read) : 파일 내용을 읽어오기 위한 모드
w(write) : 파일에 내용을 쓰기 위한 모드, 같은 이름의 파일이 있으면 해당 파일을 덮어 써서 기존 내용은 삭제
a(append) : 파일에 내용을 쓰기 위한 모드, 같은 이름의 파일이 있으면 기존 내용 끝에 이어서 씀
'''
# 쓰기(w) 모드로 열기
score_file = open('score.txt', 'w', encoding='utf8')
print('수학 : 0', file=score_file) # score_file에 출력
print('영어 : 50', file=score_file)
score_file.close()
# 쓰기(a) 모드로 열기
score_file = open('score.txt', 'a', encoding='utf8')
score_file.write('과학 : 80\n') # write는 자동 줄바꿈하지 않기 때문에 \n 사용
score_file.write('코딩 : 100\n')
score_file.close()
# 읽기(r) 모드로 열기
# read(전체)
score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.read())
score_file.close()
# readline(1줄씩)
score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline(), end='')
score_file.close()
print('')
# while문으로 전체 출력
score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
print('')
# readlines : 파일 전체를 읽고 lines에 저장, 전체를 읽기 때문에 용량이 큰 파일은 부담
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines()
for line in lines:
    print(line, end='')
print('')
score_file.close()
# 데이터를 파일로 저장하기 : pickle 모듈, 저장형식은 t(text), b(binary)
# dump(저장할 데이터, 저장할 파일명)
import pickle
# 텍스트 파일의 읽기는 rt, 쓰기는 wt. t생략 가능
# 바이너리 파일의 읽기는 rb, 쓰기는 wb
profile_file = open('profile.pickle', 'wb')
profile = {'이름':'스누피', '나이':30, '취미':['축구', '골프', '코딩']}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()
# import할 때 같은 경로에 있는 파일을 먼저 인식하므로 사용하려는 모듈과 같은 이름으로 파일을 생성하면 안됨
profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
# 파일 한 번에 열고 닫기 : with, 수동(close())로 닫지 않아도 된다
# 위의 53~67줄을 아래 코드로 바꿀 수 있다
profile = {'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}
with open('profile.pickle', 'wb') as profile_file:
    print(profile)
    pickle.dump(profile, profile_file)
# 위의 59~62줄을 아래코드로 바꿀 수 있다
with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))
with open('study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')
with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())
# p.251 실습문제 : 보고서 파일 만들기
# 조건 : 1~50주차까지, 소스코드와 동일 위치에 'n주차.txt'파일 생성
'''
- n주차 주간보고 -
부서 :
이름 :
업무요약 :

for i in range(1,51):
    with open(str(i)+'주차.txt', 'w', encoding='utf8') as report_file:
        report_file.write('-{0}주차 주간보고-\n부서:\n이름:\n업무요약:'.format(i))
'''
# p.255 셀프체크 : 파일 내용을 읽어와 각 반의 정보를 출력하는 프로그램
# 조건
# 텍스트파일명 = class.txt, 파일내용 = 초록반 5세 20명, 파랑반 6세 18명, 노랑반 7세 22명
# 생성한 파일을 읽어와 내용을 각각 빈칸으로 구분하여 split(), endswitch('명')사용해 출력

with open('class.txt', 'r', encoding='utf8') as f:
    txt = f.read()
    words = txt.split()
    for word in words:
        print(word, end='')
        if word.endswith('명'):
            print()
