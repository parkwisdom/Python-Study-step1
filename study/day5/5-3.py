# filename="a.bin"
# data=100
# with open(filename,"wb") as f:
#     f.write(bytearray([data]))
#
# =========================================================================

# http://www.kma.go.kr/weather/froecast/mid-term-rss3.jsp?stnId=108

from bs4 import BeautifulSoup
import urllib.request as req
import os.path #경로와 관련된 함수 모듈

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename="forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print("서버로부터 날씨 정보 XML문서를 가져오쟈")

xml=open(savename, mode="r",encoding="utf-8").read()
print(xml)
soup=BeautifulSoup(xml,'html.parser')
print(soup)
loc=soup.find_all("location")
print(loc)

info={}

for location in soup.find_all("location"):
    name=location.find('city').string
    weather=location.find('wf')
    if not (weather in info):
        info[weather]=[]#info={'구름조금':[]}
    info[weather].append(name)

for locW in info:
    print("+",locW)
    for name in info[locW]:
        print("|-",name)

# info={'구름조금':'서울','구름많음':'인천','구름조금':'부산'}
# for i in info:
#     print(i,info[i])