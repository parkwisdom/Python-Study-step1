# from bs4 import BeautifulSoup
# html="""
# <html><body>
#     <ul>
#         <li>
#         <a href="http://www.naver.com">naver</a>
#         </li>
#         <li>
#         <a href="http://www.daum.net">daum</a>
#         </li>
#     </ul>
# </body></html>
# """
# soup=BeautifulSoup(html,'html.parser')
# # print(soup)
# link=soup.find_all("a")
# print(link)
#
# for i in link:
#     # print(i)
#     myhref=i.attrs['href']
#     # print(myhref)
#     text=i.string
#     print(text,"-->",myhref)
##==========================================================

# from bs4 import BeautifulSoup
# html="""
# <html><body>
# <h1>빅데이터 분석</h1>
# <p>데이터 수집</p>
# <p>데이터 전처리</p>
# <p>데이터 마이닝</p>
# </body></html>
# """
#
# soup=BeautifulSoup(html,'html.parser')
# h1=soup.html.body.h1
# print(h1)
#
# p1=soup.html.body.p
# print(p1.string)
# p2=soup.html.body.p
# # print(p2.string)------>이렇게 작성하면 첫번째것만 찾아짐.

# p2=p1.next_sibling#---->p1다음 \n문자 인식
# p2=p1.next_sibling.next_sibling
# print(p2.string)
# p3=p2.next_sibling.next_sibling
# print(p3.string)
## ==============================================================
#
from bs4 import BeautifulSoup
import urllib.request as req
#
# url="https://finance.naver.com/marketindex/"
# res=req.urlopen(url).read()
# soup=BeautifulSoup(res,'html.parser')
# # print(soup)
# p=soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
# print("usd/krw=",p.string)
##============================================================================

html="""
<html><body>
<div id="test">
<h1>빅데이터 분석</h1>
<ul class="lec">
<li>파이썬</li>
<li>머신러닝</li>
<li>통계분석</li>
</ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')
# print(soup)
# res=soup.select_one("h1").string
# res=soup.select_one("div#test > h1").string
# res=soup.select_one("body > div#test > h1").string
# res=soup.select_one("html > body > div#test > h1").string
# res=soup.select_one("div#test > ul.lec > li").string

# res=soup.li
# res2=res.next_sibling.next_sibling
# res3=res2.next_sibling.next_sibling
# print(res.string)
# print(res2.string)
# print(res3.string)

# myList = soup.select("div#test > ul.lec > li")
# # myList=soup.select("div > ul > li")
# for li in myList:
#     print(li.string)

test = soup.find(id="test")
print(test)
