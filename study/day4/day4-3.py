from bs4 import BeautifulSoup
import urllib.request as req

# fp = open("color.html",encoding="utf-8")
# soup = BeautifulSoup(fp,'html.parser')
#
# # print(soup)
#
# print(soup.select_one("#gr").string)
#
# sel = lambda q:print(soup.select_one(q).string)
# sel("#gr")
# sel("li#gr")
# sel("ul > li#gr")
# sel("#mycolor #gr")
# sel("#mycolor > #gr")
# sel("ul#mycolor > li#gr")
# sel("ul#mycolor > li#gr")
# sel("li[id='gr']")
# sel("li:nth-of-type(4)")
# sel("li:nth-of-type(4)")
#
# print(soup.select("li")[3].string)
# print(soup.find_all("li")[3].string)

# url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
# res=req.urlopen(url).read()
# print(res)
# soup=BeautifulSoup(res,'html.parser')
# # print(soup)
#
# #mw-content-text > div > ul > li
# #mw-content-text > div > ul:nth-child(6) > li > ul > li
# alist=soup.select("#mw-content-text > div > ul > li > ul > li > a")
# for a in alist:
#     print(a.string)

# url2="http://www.fntimes.com/html/view.php?ud=20180809111647466b93a47988c_18"
# res2=req.urlopen(url2).read().decode('utf-8')
# soup2=BeautifulSoup(res2,'html.parser')
#
# newslist=soup2.select("body > div.con.mt30 > div.con_wrap > div.con_lt > div > div.vcon_con > div > div.vcon_con_in > div.vcon_con_intxt")
# # print(newslist)
# import re
# pat=re.compile('[^ 가-힣]+')
# result=pat.sub('',res2)
# print(result)

#contents_layer_0
#qna_detail_question > div.end_question._end_wrap_box > div.end_tit
#qna_detail_question > div.end_question._end_wrap_box
url3="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=3&search_sort=0&spq=1"
res3=req.urlopen(url3).read().decode('utf-8')
soup3=BeautifulSoup(res3,'html.parser')
naverIn=soup3.select("#qna_detail_question > div.end_question._end_wrap_box")
# print(naverIn)
import re
han=re.compile('[^ ㅏ-ㅣㄱ-ㅎ가-힣]+')
result3=han.sub('',res3)
print(result3)