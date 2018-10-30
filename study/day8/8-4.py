# 7. 상위 10개에 해당하는 단어를 시각화

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

#시각화시 한글 깨짐 방지를 위해 작성↓(아래 4줄)
if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font',family=font_name)
matplotlib.rcParams['axes.unicode_minus']=False

f=open("output_final.txt","r")
i=1
news_word=[]
word_cnt=[]
while True:
    line=f.readline()
    word,count=line.split(" ") #공백문자로 분류해서 word,count추출
    news_word.append(word)
    word_cnt.append(int(count[0]))
    if i==10 :break
    i+=1
f.close()
print(news_word)
print(word_cnt)

xs=[i for i, _ in enumerate(news_word)] # '_' 차트에 제외하고 싶은 부분을 _로 표시한다.
print(xs)


plt.bar(xs,word_cnt)
plt.ylabel('등장 단어의 수')
plt.title('오늘의 날씨 키워드')
plt.xticks([i for i, _ in enumerate(news_word)],news_word)
plt.show()