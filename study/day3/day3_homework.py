import re

emails =[
'python@mail.example.com', 'python+kr@example.com',
         'python-dojang@example.co.kr', 'python_10@example.info','python.dojang@e-xample.com',
            '@example.com', 'python@example', 'python@example-com'
]
hw=re.compile('[a-zA-Z0-9-_+.]+@[a-zA-Z0-9.-]+\.[a-zA-Z{2,4}]+')

for r in range(0,len(emails)):
    res = hw.match(emails[r])
    if res !=None:
        print(True)
    else:
        print(False)


