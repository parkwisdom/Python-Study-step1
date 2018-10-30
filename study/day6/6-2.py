import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp=codecs.open("BEXX0003.txt","r",encoding="utf-16")
soup=BeautifulSoup(fp,"html.parser")
# print(soup)
body=soup.select_one("body > text")
# print(body)
text=body.getText()
# print(text)

twitter=Twitter()
lines = text.split("\r\n")
# print(lines)
results=[]
for line in lines:
    malist = twitter.pos(line,norm=True,stem=True)
    res=[]
    for word in malist:
        if not word[1] in ["Josa","Eomi","Foreign","Punctuation"]:
            # print(word)
            res.append(word[0])

    r1=(" ".join(res))
    results.append(r1)
    # print(r1)

###########워드->벡터화 == 워드임베딩 ################################


toji_file="toji.data"
with open(toji_file,"w",encoding="utf-8")as fp:
    fp.write("\n".join(results))

#아래 문장은 toji_file의 모든 내용을 읽어서 data 저장
data=word2vec.LineSentence(toji_file)
# print(data)
model=word2vec.Word2Vec(data,size=200, window=10 ,min_count=5, iter=10,sg=1)#word2vec은 임포트한거고 Word2Vec은 클래스 / size:벡터의 차원 /window:앞뒤로 참조하는 단어 개수
#min : 최소 30번 이상 등장한 단어들에 대해서만 임베딩
#sg : CBOW(sg=0) 아니면 Skip-Gram(sg=1)중 택일 //알고리즘..

#모델 저장하기
# model.save("toji.model")
# print("모델이 만들어졌습니다.")

#모델 불러오기
model1=word2vec.Word2Vec.load("toji.model")
print(model.most_similar(negative=["땅","집"]))
