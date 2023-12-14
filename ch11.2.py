# 패키지 설치 url https://pypi.org
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
print(soup.find(string='bad'))
print(soup.i)
# 설치한 패키지의 자세한 정보 확인하려면 터미널에서 pip show beautifulsoup4 입력
'''
# 내장 함수 사용
language = input('어떤 언어를 좋아하세요?')
print(f'{language}은/는 좋은 언어입니다')
# dir()로 현재 소스코드 안에서 사용할 수 있는 모듈, 객체 출력
print('dir()')
print(dir())
import random
import pickle
print('\nimport 이후')
print(dir())
print('dir(random)')
print(dir(random))
# 리스트 만들어서 사용 가능한 변수와 함수 확인
lst = [1, 2, 3]
print('\nlist에 사용 가능한')
print(dir(lst))
# 문자열에사용 가능한 변수와 함수 확인
name = 'james'
print('\nstring에 사용 가능한')
print(dir(name))
# string에서 사용할 수 있는 유용한 메서드
# split()
s1 = 'abc def'
print(s1.split())   # 공백을 기준으로 list형식으로 반환
s1 = 'a,b,cdef'
print(s1.split(','))
a,b = input('\n공백을 기준으로 나누고싶은 문자열을 입력하세요').split()
print('a : ' + a)
print('b : ' + b)
print('')
# strip()
s2 = '  abc  '
s2 = s2.strip()
print(s2)
print(len(s2))
'''
# 외장 함수 사용
import glob
print(glob.glob('*.py'))    # 확장자가 py인 모든 파일 출력
# 다른 경로에 있는 확장자가 py인 모든 파일 출력
print(glob.glob("./travel/*.py"))
import os
print(os.getcwd())      # 현재 파이썬 파일을 실행하는 경로 정보를 출력  cwd=current working directory
folder = 'sample_dir'
if os.path.exists(folder):  # folder라는 이름의 폴더가 존재하면
    print('이미 존재하는 폴더입니다')
    os.rmdir(folder)    # 폴더 삭제
    print(folder, '폴더 삭제')
else:
    os.makedirs(folder)     # 폴더 생성
    print(folder, '폴더 생성')
print(os.listdir())     # 현재 작업 폴더 안의 폴더와 파일 목록 출력
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
import datetime
today = datetime.date.today()
print('오늘 날짜는', today)
td = datetime.timedelta(days=100)
print('오늘부터 100일 뒤는 ', today + td, '입니다')
print('오늘부터 100일 전은 ', today - td, '입니다')

# p.395 실습 문제
import byme
byme.sign()
import greeting
greeting.say_hello('파이썬')