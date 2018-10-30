#웹의 컨텐츠를 가져오기 위한 라이브러리
import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

api="http://www.weather.go.kr/weather/forecast/mid-term-rss.jsp"
values={
    'stnId':'108'
}
params=urllib.parse.urlencode(values)
print(params)
url=api+"?"+params
# print("url=",url)
data=req.urlopen(url).read().decode("utf-8")
# print(data)

soup=BeautifulSoup(data,'html.parser')
# print(soup)

wf=soup.find("tmn").string
print(wf)
#
# url="http://www.kccistc.net/"
# mem=req.urlopen(url).read()
# text=mem.decode("utf-8")
# print(text)