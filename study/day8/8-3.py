from konlpy.tag import Twitter
from collections import Counter

# colors=['r','b','r','g','b','b']
# num=[1,2,3,3,3,4,4,4,4,5]
# cnt = Counter(colors)
# print(cnt)
# #Counter는 리스트 또는 튜플에 저장된 데이터를 딕셔너리 형태로 데이터가 등장한 횟수를 출력
# n=Counter(num)
# print(n.most_common())
# print(n.most_common(3))
#=============================counter함수 연습↑==

# 5. 정제된 파일을 읽어서 형태소 분석 -> 명사 추출 -> 빈도수
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(output_final.txt)

#명사를 추출하는 함수
def get_tags(gtext,ntags=30):
    twitter=Twitter()
    nouns=twitter.nouns(gtext)
    # print(nouns)
    count=Counter(nouns)
    # print(count)
    # print(count.most_common(ntags))
    return_list=[]
    for word, cnt in count.most_common(ntags):
        temp={'tag':word,'count':cnt}
        return_list.append(temp)
    return return_list
        # print(temp)

def main():
    text_file_name ="output_cleaned.txt"
    noun_count=30
    output_file_name="output_final.txt"
    open_text_file=open(text_file_name,"r")
    text=open_text_file.read()
    res=get_tags(text,noun_count)
    open_text_file.close()

    open_output_file=open(output_file_name,"w")
    for data in res:
        noun=data['tag']
        count=data['count']
        open_output_file.write("{} {}\n".format(noun,count))


if __name__=='__main__':
    main()