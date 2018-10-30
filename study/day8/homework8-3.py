from konlpy.tag import Twitter
from collections import Counter

def get_tags(gtext,ntags=30):
    twitter=Twitter()
    nouns=twitter.nouns(gtext)
    count=Counter(nouns)

    return_list=[]
    for word,cnt in count.most_common(ntags):
        temp={'tag':word,'count':cnt}
        return_list.append(temp)
    return return_list

def main():
    text_file_name="hw_output_cleaned.txt"
    noun_count=30
    output_file_name="hw_output_final.txt"
    open_text_file=open(text_file_name,"r")
    text=open_text_file.read()
    res=get_tags(text,noun_count)
    open_text_file.close()

    open_output_file=open(output_file_name,"w")
    for data in res:
        noun=data['tag']
        count=data['count']
        open_output_file.write("{} {}\n".format(noun,count))

if __name__=="__main__":
    main()
