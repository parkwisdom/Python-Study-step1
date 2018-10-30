

print(range(5))
print(list(range(5)))
print(list(range(3,8)))
print(list(range(3,8,2)))
print(list(range(8,-5,-2)))

#sorted함수: 값을 정렬 ->결과를 리스트로 리턴하는 함수
#sort함수: 리턴값이 없음

print(sorted([5,3,4]))
print(sorted(['k','i','m']))
print(sorted("seoul"))

data=[5,3,4]
print(sorted(data))
print(data)

data2=[5,3,4]
print(data2.sort())
data2.sort()
print(data2)

#zip:자료들을 묶어주는 함수
print(list(zip([1,2,3])))
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))

print(list(zip("xyz","ijk")))
print('-'*30,"↑내장함수↑",'-'*30)


print('-'*30,"↓외장함수↓",'-'*30)
#pickle:객체 상태를 유지하면서 파일 입출력 모듈
#dump함수를 이용...
import pickle

f=open("sleep.txt","wb")
data={1:"big",2:"data"}
#f.write(data)
pickle.dump(data,f)
f.close()

f=open("sleep.txt","rb")
data=pickle._load(f)
print(data)

import glob
print(glob.glob("d*"))

import random
print(random.random())
for i in range(1,7):
    print(random.randint(1,46))

# a=set([1,2,2,3,2])
# print(len(a))

#정규표현식:일정 규칙을 갖는 문자열을 표현하는 방법,(정규식)
#REGular EXpression;REDEX
# 복잡한 문자열에서 특정 규칙을 만족하는 문자열을 검색한다음 전처리(치환,삽입 등).주어진 문자열이 규칙에 맞는지 확인하고자 하는 경우.

jumin="""
kim 980102-1234567
park 970807-2345678
"""
#정규식
import re
pattern=re.compile("(\d{6})[-]\d{7}")
print(pattern.sub("\g<1>-*******",jumin))

# print(jumin)
for line in jumin.split("\n"):
    word_res=[]
    for word in line.split(" "):
        # print(word)
        if len(word)==14:
            word=word[0:6]+"-"+"*******"
            # print(word)
        word_res.append(word)
    print(word_res)

#메타문자 :[]{}.()|\등..
#문자메타 :[],[]사이에는 모든 문자가 들어갈수 있음
#ex)정규식이 [xyz]라면,x,y,z중 한개의 문자와 매치
#   =>"a"는 정규식에 매치가 안됨
#   =>"text"는 정규식에 일치하는 'x'문자 있음=매치
#   =>"y"는 정규식 매치
#ex)정규식이 [a-zA-Z]라면 알파벳 전체!
#ex)[0-9]라면 숫자가 전체!
p=re.compile('a.b')
m=p.match("abcd")
print(m)

p=re.compile('a[.]b')
m=p.match("a.baabb")
print(m)

