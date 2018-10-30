#N-GRAM : 문장 유사도 분석
#레벤슈타인거리 : 두개의 문자열이 어느 정도 다른가(=편집거리 알고리즘) / DNA배열 유사성 조사
#ex)가나다라, 가마바라 의 두개의 다름의 정도 비교.

# def calc_distance(a,b):
#     if a==b: return 0
#     a_len=len(a)
#     b_len=len(b)
#     if a=="":return b_len
#     if b=="":return a_len
#
#     matrix=[[] for i in range(a_len+1)]
#     # print(matrix) #[[], [], [], [], []]
#     for i in range(a_len+1): #5번 반복 :0~4
#         matrix[i]=[0 for j in range(b_len+1)]
#     # for j in range:
#     # print(matrix)
#
#     for i in range(a_len+1):
#         matrix[i][0]=i
#     for j in range(b_len+1):
#         matrix[0][j]=j
#     print(matrix)
#     #return a와 b사이의 거리
#
#     for i in range(1,a_len+1):
#         ac=a[i-1] #"가나다라"에서 "가"
#         for j in range(1,b_len+1):
#             bc=b[j-1] #"가마바라"에서 "가"
#             cost = 0 if(ac==bc) else 1 # matrix[i][j]에는 문자 삽입, 제거, 변경중 가장 작은값을 대입..
#
#             matrix[i][j]=min(
#                 matrix[i-1][j]+1, #문자 삽입
#                 matrix[i][j-1]+1, #문자 제거
#                 matrix[i-1][j-1]+cost #문자 변경
#             )
#     return matrix[a_len][b_len]
#
#
# # print(calc_distance("가나다라","가마바라"))#출력
# samples= ["신촌역","화곡역","동대문입구역","신발","상공회의소"]
# base=samples[0]
# r= sorted(samples, key=lambda n: calc_distance(base,n)) #samples를 정렬해라_정렬은 calc_distance함수 수행 결과(두 문자열의 편집거리)에 대한 오름차순.
# for n in r:
#     print(calc_distance(base, n),n) #레벤슈타인거리_

# for n in range(len(samples)):
#     calc_distance(base, samples[n])
# n-gram: 두 문장 사이의 유사도를 조사하는 방법//n? 이웃한 문자의 수
# ex) "오늘 상공회의소에서 문자 비교 알고리즘을 배웠다" --> n을 2로 한경우.-->['오늘', '늘 ', '상공', '공회', ....,'배웠', '웠다']
# ex) "문자 비교 알고리즘을 오늘 상공회의소에서 배웠습니다" --> n을 2로 한경우.-->['문자', '자 ', '비교','비 ',...,'니다']

def ngram(s,num):
    res=[]
    #res의 길이는 얼마나 나올까?
    slen=len(s)-num+1
    for i in range(slen):
        ss=s[i:i+num]
        res.append(ss)
    print(res)
#리턴: ['오늘','늘 ',' 상'....]
    return res

def diff_ngram(sa,sb,num):
    a=ngram(sa,num)
    b=ngram(sb,num)
    cnt=0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    return cnt/len(a),r

a="오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
b="문자간 비교하는 알고리즘을 오늘 상공회의소에서 배웠다"

#2-gram
res, word=diff_ngram(a,b,3)
print("2-gram",res, word)

#3-gram
# res=diff_ngram(a,b,3)
# print("3-gram",res)