from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager,rc
import platform

if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font',family=font_name)
matplotlib.rcParams['axes.unicode_minus']=False

f=open("hw_output_final.txt","r")
i=1
news_word=[]
word_cnt=[]
while True:
    line=f.readline()
    word, count = line.split(" ")
    news_word.append(word)
    word_cnt.append(int(count[0]))
    if i==10 :break
    i+=1
f.close()
print(news_word)
print(word_cnt)

xs=[i for i, _ in enumerate(news_word)]
plt.bar(xs,word_cnt)
plt.ylabel('단어 사용 빈도수')
plt.title('김동연부총리 방문 기념 과제')
plt.xticks([i for i, _ in enumerate(news_word)],news_word)
plt.show()
