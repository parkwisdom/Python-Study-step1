from bs4 import BeautifulSoup
import urllib.request as req
import re


def ngram(s,num):
    res=[]
    slen=len(s)-num+1
    for i in range(slen):
        ss=s[i:i+num]
        res.append(ss)
    return res
def diff_ngram(sa,sb,num):
    a=ngram(sa,num)
    b=ngram(sb,num)
    cnt=0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    return cnt/len(a),r


#연합뉴스 기사=text1로 출력
url1="http://www.yonhapnews.co.kr/bulletin/2018/08/14/0200000000AKR20180814075800003.HTML?input=1195m"
news1=req.urlopen(url1).read()
# print(news1)
soup1=BeautifulSoup(news1,'html.parser')
r1=soup1.select("#articleWrap > div.article > p" )
a=str(r1)
# print("="*200)

#아주경제 기사=text2로 출력
url2="http://news.hankyung.com/article/201808140286g"
news2=req.urlopen(url2).read()
soup2=BeautifulSoup(news2,'html.parser')
r2=str(soup2.select("#newsView")[0])
t2=re.compile('[^가-힣BMW]+',re.M)
b=t2.sub(' ',r2)


res, word=diff_ngram(a,b,3)
print("3-gram",res, word)
