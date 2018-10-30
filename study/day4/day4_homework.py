
f=open("words.txt","r")
word=f.readlines()
# print(word)
a=0
for i in word:
    # print(i)
    if len(i)<=11:
        a=a+1
print("출력:", a)

#========================================================


n = int(input("출력 단어수 : "))
text = input("문장을 입력 : ")
words = text.split()

if (len(words) < n):
    print('wrong')
else:
    for i in range(len(words) - (n - 1)):
        for j in range(n):
            print(words[i + j], end=' ')
        print(' ')





#=============================================================
from bs4 import BeautifulSoup
import urllib.request as req
url3="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=3&search_sort=0&spq=1"
res3=req.urlopen(url3).read().decode('utf-8')
soup3=BeautifulSoup(res3,'html.parser')
naverIn=soup3.select("#contents_layer_0 > div.end_content._endContents")
# print(naverIn)
import re
han=re.compile('[^ ㅏ-ㅣㄱ-ㅎ가-힣]+')
result3=han.sub('',res3)
print(result3)
