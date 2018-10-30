#1. 정규식 특수 문자
# \d : 숫자 =[0-9]=[0123456789]
# \D :(대문자는 소문자의 반대) 숫자가 아닌것 = [^0-9]
# \w :문자+숫자 = [0-9A-Za-z]
# \W :문자+숫자가 아닌것 = [^0-9A-Za-z]
#  \s : space문자 = [ \t\n]
# \S : space문자가 아닌것 = [^ \t\n]

# 2. 정규식 기호
# 1) .
# 의미:모든 문자(줄바꿈 문자 \n는 제외)
# ex)t.y t와y 사이에 어떤 문자가 와도 매치가 된다; try매치, t9y매치, tya매치안됨
#
# 2) *
# 의미:여러 번 반복, *앞에 있는 문자를 0번 이상 반복
# ex)bu*s(u가 0번이상 반복); bs매치, bus매치, buuuuuuuus매치
#
# 3) +
# 의미:여러 번 반복, +앞에 있는 문자를 1번 이상 반복
# ex)bu+s(u가 1번이상 반복);  bs매치가 안됨, bus매치, buuuuus매친
#
# 4) {}
# 의미:반복 횟수 제한
# {1,} :최소 1번 이상 반복(+와 같아짐)
# {0,} :최소 0번 이상 반복(*과 같아짐)
# {3} : 무조건 3번 반복; bu{3}s(반드시 u문자가 3번 반복); bus매치안됨, buuus매치, buuuuuuus매치안됨
# {2,5} : 2번~5번 반복; bu{2,5}s;  bus매치안됨, buus매치, buuuuu매치
#
# 5) ?
# 의미:있어도 없어도 됨 ={0,1}
# ex)bu?s; bs매치, bus매치
#
# 3.정규식 사용
import re
pat=re.compile('bu*s')

import re
pat=re.compile('[a-z]')
res=pat.match("compu4ter")
print(res)

text="에러 1004: 레퍼런스 에러\n 에러 1247:코드오류"
regex=re.compile("에러 12437")
res=regex.search(text)
print(res)

if res !=None:
    print(res.group())
else:
    print("매칭안됨")


text2="기타사항은 전화번호:02-1234-5678로 연락주세요"
regex2=re.compile("\d\d-\d\d\d\d-\d\d\d\d")
res2=regex2.search(text2)
pNumber=res2.group()
print(pNumber)


text3="에러 1347:레퍼런스 에러\n 에러 232323:코드오류"
regex3=re.compile("에러\s\d+")
res3=regex3.findall(text3)
print(res3)

# 정규식 그룹
# (): 그룹
# ex)전화번호 정규식을 '\d{3}-\d{3}-\d{4}'
# 지역번호,전화번호를 그룹으로 나누고자 한다면,'(\d{3})-(\d{3}-\d{4})'으로 표현하면 됨.
# 첫번째 그룹은 group(1),두번째 그룹은 group(2)로 사용. 전체 전화번호를 모두 가지고 올때는 group() or group(0)으로 표현/

text4="기타사항은 전화번호:02-1234-5678로 연락주세요"
# regex4=re.compile("\d{2}-\d{4}-\d{4}")
regex4=re.compile("(\d{2})-(\d{4}-\d{4})")
res4=regex4.search(text4)
pNumber=res4.group()
print(pNumber)
print(res4.group(1),res4.group(2))

text5="기타사항은 전화번호:02-4321-8765로 연락주세요"
regex5=re.compile("(?P<area>\d{2})-(?P<number>\d{4}-\d{4})")
res5=regex5.search(text5)
print(res5.group("area"),res5.group("number"))