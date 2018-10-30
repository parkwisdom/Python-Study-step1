import re
# re.compile('\\white')#\white
pat = re.compile('Java|Python')
res=pat.match('Python')
print(res)
res=pat.match('Java')
print(res)
res=pat.match('PythonJava')
print(res)
res=pat.match('PythonRuby')
print(res)
res=pat.match('RubyPython')
print(res)

print(re.search('How','How are you'))
print(re.search('are','How are you'))
print(re.match('are','How are you'))
print(re.search('^How','How are you'))
print(re.search('^are','How are you'))

print(re.search('you$','How are you'))
print(re.search('you$','How are you.Hi'))

re.compile('(ABC)+')#ABC가 계속 반복되는 경우
res=pat.search('ABCABCABCABCABCABCDABCD ok?')
print(res)
# print(res.group(1))

pat=re.compile('(\w+)\s+((\d+)[-](\d+)[-](\d+))')
res=pat.search("kim 010-1234-5678")
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.group(4))
print(res.group(5))


pat=re.compile('(어제|오늘|내일)')
print(pat.sub('DAY','어제 날씨 그리고 오늘 날씨'))
"""
웹텍스트 스크래핑 ->치환/삭제(sub)->형태소 분석기(형태소 단위로 분해, 8개 품사)->ex)오늘 뉴스 사건 사고
{'오늘':5,'뉴스':1,'사건':10,....}
"""
pat=re.compile('(어제|오늘|내일)')
print(pat.sub('DAY','어제 날씨 그리고 오늘 날씨',count=1))

pat=re.compile("(?P<name>\w+)\s+(?P<phone>(\d+)[-](\d+)[-](\d+))")
print(pat.sub("\g<phone> \g<name>","kim 010-1234-5678"))
print(pat.sub("\g<2> \g<1>","kim 010-1234-5678"))

"""
정규 표현식 예 : 의미
^Test : Test로 시작하는 문자열
test$ : test로 끝나는 문자열
^xyz$ : xyz로 시작하고 xyz로 끝나는 문자열(xyz도 해당
abc : abc가 들어가는 문자열
ab* : a뒤에 b가 0개 이상 있는 문자열(a,ab,abbbbbb)
ab+ : a뒤에 b가 1개 이상 있는 문자열(ab, abbbbb)
ab? : b가 1개 있을 수도 있고 없을 수도 있다(ab,a)
a?b+$ : a는 있을수도 없을수도 있고, 그뒤에 반드시 한개 이상의 b로 끝나는 문자열

ab{2} : a 뒤에 b가 2개있는 문자열(abb)
ab{3,} : a뒤에 b가 3개 이상 있는 문자열(abbb,abbbbbb)
ab{2,4} : a뒤에 2개 이상 4개 이하의 b가 있는 문자열(abb,abbb,abbbb)

a(bc)* : a뒤에 bc가 0번 이상 반복되는 문자열
a(bc){1,3}: a뒤에 bc가 1번 이상 3번 이하 반복되는 문자열

hi|bye : hi 또는 bye가 있는 문자열
(a|bc)de : ade 또는 bcde문자열
(a|b)*c : a와 b가 뒤섞여서 0번 이상 반복되며, 그뒤에 c가 오는 문자열(aababaaac)
. : 한 문자
.. : 두문자
... : 세문자
a.[0-9] : a뒤에 문자가 1개 있으며, 그 뒤에 숫자가 붙는 문자열
^.{3}$ : 반드시 3문자

[ab] : a또는 b(a|b와 같음)
[a-d] : 소문자 a~d(a|b|c|d 또는 [abcd]와 같음
^[a-zA-Z]: 영문자로 시작하는 문자열
[0-9]% :%문자앞에 하난의 숫자가 있는 문자열
[a-zA-Z0-9]$ : 숫자,영문자로 끝나는 문자열

XML 확장가능한 

"""