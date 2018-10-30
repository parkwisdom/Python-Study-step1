# print(abs(-2))
# print(all([2,5,-7]))#전부참이냐?
# print(any([1,2,0]))#하나라도 참으면 참
# print(any([0,""]))
#
for n in ['gildong','sunsin','sejong']:
    print(n)
#
# for n in enumerate(['gildong','sunsin','sejong']):
#     print(n)
#
for i,n in enumerate(['gildong','sunsin','sejong']):
    print(i,n)
# #문자열로된 수식 계산
# print(eval('1+2'))
# print(eval('int(3.14)'))

print(len("today"))
print(len([3,4,5]))
print(type(['t','o','d','a','y']))
print(list("today"))
a=list("today")
print(type(a))

#map(적용함수,데이터) 데이터를 함수에 적용

def two_times(num):
    res=[]
    for n in num:
        print(n)
        res.append(num*2)
    return res
print(two_times([1,2,3]))

def two_times(num):return num*2
print(list(map(two_times,[1,2,3])))

#lambda :함수 구분을 간략화

print(list(map(lambda x:x*2,[1,2,3])))