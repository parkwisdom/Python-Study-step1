import re
from bs4 import BeautifulSoup


# html="""
# <ul>
#     <li><a href="www.naver.com">naver</a></li>
#     <li><a href="https://www.naver.com">naver</a></li>
#     <li><a href="https://www.daum.net">daum</a></li>
#     <li><a href="http://www.naver.com">naver</a></li>
# </ul>
# """
# soup=BeautifulSoup(html,'html.parser')
# #정규식으로 href속성이 https인 것만 추출
# li=soup.find_all(href=re.compile("^https://"))
# # print(li)
# for e in li:
#     print(e.attrs['href'])

#상대 경로로 웹 주소를 지정하는 방법
# from urllib.parse import urljoin
# base="http://example.com/html/a.html"
# print(urljoin(base, "b.html"))
# print(urljoin(base, "sub/c.html"))
# print(urljoin(base, "../index.html"))
# print(urljoin(base, "../img/sky.png"))
#
# print(urljoin(base, "http://other.com/test"))
# print(urljoin(base, "//other.com/test"))

# 파이써응로 사이트 로그인->개인정보 추출->화면 출력
import requests
USER="park4164"
PASS="wisdom0!"
session=requests.session()#세션 객체 생성(송화기-통신선-수화기 연결해두는 느낌)

# 클라이언트에서 서버에 데이터를 전달하기 위한 목적으로 연결할 때는 SESSION을 사용.
# 세션은 서버와 클라이언트의 연결

login_info={"m_id":USER,"m_passwd":PASS}

url_login="http://www.hanbit.co.kr/member/login_proc.php"

res=session.post(url_login,data=login_info)
# print(res)

url_mypage="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res=session.get(url_mypage)
# print(res)
# print(res.text)
soup=BeautifulSoup(res.text, 'html.parser')
mileage=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").string
print("마일리지 : "+mileage)
ecoin=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").string
print("한빛이코인 : "+ecoin)



