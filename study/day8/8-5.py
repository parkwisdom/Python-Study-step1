# myName=['Kim','Park','Lee']
# v=[name for _, name in enumerate(myName)]
# print(v)

# r=[i for i in range(5)]

import json
from collections import defaultdict
path = 'example.txt'
# print(open(path).readline())
rec=[json.loads(line) for line in open(path, encoding='utf-8')] #json어서 읽어진 문서를 줄단위로 읽어라.

# print(rec[3]['tz'])
time_zones=[myRec['tz']for myRec in rec if 'tz' in myRec]
#만약에 myRec에'tz'키가 있다면,'tz'키에 해당하는 값을 추출하여 time_zoons리스트의 요소로 집어넣어라...
#자세한 해석...↓
#1) for myRec in rec : rec에서 3560개의 라인이 있고,rec로 부터 한줄씩 읽어라.
#2) if 'tz' in myRec : 만약 myRec에 'tz'키에 해당하는 값을 추출하
#3) time_zones=[myRec['tz'] : 'tz'키에해당하는 값을 추출하여 time_zoons리스트의 요소로 집어넣어라.

# print(len(time_zones)) #3440개
print(time_zones[:20])

def get_counts2(sequence):
    counts=defaultdict(int) #0으로 초기화
    for x in sequence:
        counts[x]+=1
    return counts
counts=get_counts2(time_zones)
print(counts)

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts
        # print(x)

# counts=get_counts(time_zones)
# print(counts['America/Denver'])