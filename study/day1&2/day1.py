a=4.2E7
print(a)
a=4.2E-7
print(a)
print (7/4)
print(7//4)
print (7%4)

msg ="""
Life is \ntoo short
"""

print(msg)

print ("-"*100)
a="Life"
print (a[-2])
print (a[1:3])

print ("I eat {0} apples.so I was sick for {1} days".format(3,5))

pi=3.14
print ("{0:10.4f}".format(pi))

a=","
print (a.join('abcd'))
msg = msg.replace("Life","Your leg")
print (msg)
print (msg.split())
msg2="Life:is:too:short"
print (msg2.split(":"))

a=[1,2,3,['a','b','c']]
print (a[-1])
print ("="*50)
a=[4,5,6]
a[2]=7
print (a)
print (a[1:2])
a[1]=['a','b','c']
print (a)

del a[1:3]
print (a)

def sum2(*v):
    sum=0
    for i in v:
        sum+=i
    return sum
print (sum2(1,2))

f=open("test.txt","w")
#파일처리
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

# f=open("test.txt","r")
# # while True:
# #     line=f.readline()
# #     if not line:break
# #     print(line)
# # f.close()

f=open("test.txt","r")
lines=f.readlines()
print(lines)

s=open("input.txt","r")
line=s.readlines()
s.close()
print(line)
sum=0
for k in line:
    sum= sum+int(k)
print(sum)
avg=sum/len(line)
print(avg)

s=open("result.txt","w")
s.write(str(avg))
s.close()