# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

# 테스트 html (response data 또는 파일에서 읽어온 data로 가정)
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<h1>this is h1 area</h1>
<h2>this is h2 area</h2>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
</p>
<p class="story">story...</p>
</body>
</html>
"""

# 예제1(Beautiful 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))

# 코드 정리
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print('p2', p2)

# 텍스트 출력1
print("h1 >> ", h1.string)

# 텍스트 출력2
print("p >> ", p1.string)

# 함수 확인
print(dir(p2))

# 다음 엘리먼트 확인
print(list(p2.next_elements))

# 반복 출력 확인
for v in p2.next_elements:
    print(v)

# 예제2(Find, Find_all)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
links1 = soup.find_all("a")  # limit=2
# 타입 확인
print('links', type(links1))
# 리스트 요소 확인
print(links1)
# dir 확인
print(dir(links1))

links2 = soup.find_all("a", class_='sister')  # id="link2" , string="Tillie" , string=["Elsie","Tillie"] , {} 다중 조건
print(links2)

for t in links1:
    print("link1 >> ", t.text)

# 처음 발견한 a 태그 선택
link1 = soup.find("a")  # find 연결 가능
print('links', type(link1))
# 리스트 요소 확인
print(link1)
# dir 확인
print(dir(link1))
# 태그 텍스트 출력
print(link1.string)
print(link1.text)

# 다중 조건
link2 = soup.find("a", {"class": "sister", "data-io": "link3"})
# 출력
print(link2)

# 예제3(Select, Select_one)
# CSS 선택자 중요
# 태그 + 클래스 + 자식 선택자
link1 = soup.select_one("p.title > b")
# 태그 + id 선택자
link2 = soup.select_one("a#link1")
# 태그 + 속성 선택자
link3 = soup.select_one("a[data-io='link3']")

# 전체 구조 및 텍스트 출력
print(link1)
print(link1.string)
print(link2)
print(link2.string)
print(link3)
print(link3.string)

# 선택자에 맞는 전체 선택
# 태그 + 클래스 + 자식
link4 = soup.select("p.story > a")
# 태그 + 클래스 + 자식 + 태그 + 순서
link5 = soup.select("p.story > a:nth-of-type(2)")
# 태그 + 클래스
link6 = soup.select("p.story")

# 전체 구조 및 텍스트 출력
print(link4)
print(link5)
print(link6[1])
