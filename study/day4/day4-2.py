from bs4 import BeautifulSoup
fp=open("fruits.html",mode="r",encoding="utf-8")
soup=BeautifulSoup(fp,"html.parser")

# print(soup)

# print(soup.select_one("li").string)
# print(soup.select_one("li:nth-of-type(2)").string)


# pos1="li:nth-of-type("
# pos2=")"
# for i in range(9):
#     pos=pos1+str(i+1)+pos2
#     print(soup.select_one(pos).string)
#
#
# myList=soup.select("li")
# for li in myList:
#     # myList=soup.select_one("li:nth-of-type(i)").string
#     print("li=",li.string)


# myList=soup.select("#ve-list > li")
# # print(len(myList))
# for i in range(len(myList)):
#     print(soup.select("#ve-list > li")[i].string)

#
# print(soup.select("#ve-list > li:nth-of-type(3)"))
# print(soup.select("#ve-list > li:nth-of-type(3)")[0].string)
# #select함수는 라턴 결과가 리스트이므로, string함수는 사용할 수 없음.
# # 따라서 select()[0]와 같이 인덱스를 주어 접근한 후 string함수를 적용.


# print(soup.select("#ve-list > li[data-lo='us']" )[0].string)
# # print(soup.select("#ve-list > li.'us'" ))--->사용자가 임의로 만든 클래스라서 "."으로는 못찾음.
#
# print(soup.select("#ve-list > li[class='black']"))
# print(soup.select("#ve-list > li.'black'"))
#
# cond={"data-lo":"us","class":"black"}
# print(soup.find("li",cond).string)
# # print(soup.find(id="ve-list",cond).string)

