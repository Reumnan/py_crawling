# Section03-2
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(2) - RSS

import urllib.request
import urllib.parse

# 행정 안전부 : https://www.mois.go.kr
# 행정 안전부 RSS API URL
API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c)
    # URL 완성
    url = API + "?" + param
    # URL 출력
    print("url=", url)
    # 요청
    res_data = urllib.request.urlopen(url).read()
    # 수신 후 디코딩
    contents = res_data.decode("utf-8")
    # 출력
    print(contents)
