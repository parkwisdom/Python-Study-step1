a=[1,2,3,4]
res=[]
for num in a:
    res.append(num*2)
print(res)

#리스트 내포 이용한 코드
res=[num*2 for num in a]
print(res)

#a리스트의 요소값에 대해 짝수인 경우에는 2배를 해서 res
res=[num*2 for num in a if num%2==0]
print(res)

res=[x*y for x in range(2,5)
     for y in range(1,10)]
print(res)
#[표현식 for 항목 in 반복객체 if 조건문...]

a=[1,2,3,4,5]
res=[n*2 if n%2==1 else n for n in a ]
print(res)

a=[1,2,3,4,5]
res=[]
for n in a:
    if n%2==1:
        res.append(n*2)
    else:
        res.append(n)
print(res)

msg="How are you? fine thank. you and you?"
#리스트 내포를 이용하여 모음(aeiou)을 제거한 후 msg출력
v='aeiou'
print(''.join([a for a in msg if a not in v]))

