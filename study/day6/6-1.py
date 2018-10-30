from konlpy.tag import Twitter
import codecs
from bs4 import BeautifulSoup
#
# twitter= Twitter()
# mlist=twitter.pos("나는 공부하고 있습니다. 한국어 처리 관련 학습을.,..재미있엌ㅋㅋㅋ",norm=True,stem=True) #품사 구분하기
# # mlist=twitter.pos("아버지가방에들어가신다")
# print(mlist)

# ############################## ↓토지 파일 형태소 분석 작업 코드

fp=codecs.open("TOJI.txt","r",encoding="utf-8")
# print(fp)
soup=BeautifulSoup(fp,"html.parser")
# print(soup)
text=soup.getText()
print(text)
#
# twitter=Twitter()
# lines=text.split("\r\n")
# # print(len(lines))
#
# word_dic={}
#
# for line in lines:
#     malist= twitter.pos(line)
#     for word in malist:
#         # print(word[1])
#         if word[1]=="Noun":#명사라면...
#             if not word[0] in word_dic:
#                 word_dic[word[0]]=0
#             word_dic[word[0]]+=1
# # print(word_dic)
# # print(word_dic.items)
# keys=sorted(word_dic.items(),key=lambda x:x[1], reverse=True)
# print("="*100)
# # print(keys)
# for word,count in keys[:50]:
#     print("{0}({1})".format(word,count),end="")
# print()
#
