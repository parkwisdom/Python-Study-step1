"""
1.정규식
search():문자열 전체 검색,정규식 매치 조사
match():문자열 왼쪽부터 검색, 정규식 매치 조사
findall():정규식 매치되는 모든 문자열을 리스트로 리턴
finditer():정규식 매치되는 모든 문자열을 iterator객체로

2,컴파일 옵션1
1) re.I 옵션(Ignore case) : 대소문자 관계없이 매칭
2) .옵션 : 모든 문자와 매치(\n 제외)
    re.DOTALL 또는 re.s 옵션:\n을 포함시킬때
3) re.M(Multiline) : ^(문자열의 처음), $(문자열의 마지막)
4) re.X(Verbose)

한글 코드
가~힣
"""
#
import re
p=re.compile('[a-z]+')
m=p.match("9 java")
print(m)

m2=p.search("9 java 7")
print(m2)

res=p.findall("How are you?")
print(res)

res2=p.finditer("How are you?")
print(res2)
#res2에는 how,are,you라는 3개의 문자열 리스트가 객체로 저장되어 있음.

for r in res2:
    print(r.group())
    print(r.start())
    print(r.end())
    print(r.span())
print("1.=================================================================")

# import re
# pat = re.compile('a.k',re.DOTALL)
# #여러줄로 구성된 문자열에서 \n에 상관없이 검색하고자 할때/
# # res=pat.match('a1k')
# # res=pat.match('ak')
# # res=pat.match('asak')
# res=pat.match('a\nk')
# print(res)
#
# import re
# # pat = re.compile("python\s\w+")
# # pat = re.compile("^python\s\w+",re.M)
# pat = re.compile("\w+\spython$",re.M)#$의 앞은 문자로 끝나는 경우.
# text="""python java
# python c ruby r
# seoul gangseo python
# one two three
# """
# print(pat.findall(text))
#
# import re
# def hangulTest():
#     s="大韓민국에서 살고 있어요. 한국은 very nice해요. English 싫어요.ㅋㅋㅋ"
#     hangul=re.compile('[^ㄱ-ㅎ | 가-힣]+')#한글, 뛰어쓰기를 제외한 모든 글자
#     res2=hangul.sub('',s)#한글, 뛰어쓰기를 제외한 모든 글자 지우기
#     print(res2)
#     res=hangul.findall(s)
#     print(res)
# hangulTest()

import re
# pat = re.compile('&[#](0[0-7]+);')
pat = re.compile("""
&[#]
(
0[0-7]+
)
;
""",re.VERBOSE)#정규화식 여러줄로 표현하여 가독성 높임

