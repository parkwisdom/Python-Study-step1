# 1) 텍스트->학습->모델
# 2) 모델->새로운 텍스트 입력 

import math,sys
from konlpy.tag import Twitter
from konlpy.tag import Okt
class BayesianFilter:
#학습
    def __init__(self):
        # print("생성자 함수")
        #init의 self가 붙은 함수 사용시 풀네임 사용
        self.words=set()
        self.word_dict={}
        self.category_dict={}

    def fit(self, text, category):
        word_list=self.split(text)
        # print(word_list[0],category)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    def split(self,text):
        twitter=Twitter()
        malist=twitter.pos(text, norm=True,stem=True)
        # print(malist)
        results=[]
        for word in malist:
            if not word[1] in ["Josa","Eomi","Punctuation"]:
                results.append(word[0])
        # print(results)
        return results

    # 단어를 카테고리에 추가
    def inc_word(self,word, category):
        # print(word, category)     #파격 광고 30% 광고
        if not category in self.word_dict:
            self.word_dict[category]={}
        if not word in self.word_dict[category]:
            self.word_dict[category][word]=0
        self.word_dict[category][word] +=1
        self.words.add(word)
        # print('='*50)
        # print(self.word_dict)
        # print('='*50)
        # print(self.words)

    #카테고리 계산
    def inc_category(self,category):
        # print("inc카테고리;")
        if not category in self.category_dict:
            self.category_dict[category]=0
        self.category_dict[category]+=1
        # print(self.category_dict)

#예측
    def predict(self,text):
        best_category=None
        words=self.split(text)
        # print(words)   #['재고', '정리', '할인', '무료', '배송']
        score_list=[]
        max_score=-sys.maxsize
        for category in self.category_dict.keys():
            score=self.score(words,category)
            score_list.append((category,score))
            if score > max_score:
                best_category=category
        return best_category, score_list


    def category_prob(self,category):
        sum_categories = sum(self.category_dict.values())   #카테고리 전체 개수 : 10개
        category_v=self.category_dict[category]     #광고 카테고리에 속하는 문장의 개수 : 5개
        return category_v / sum_categories  #'광고'=>5/10이 리턴, '중요'=>5/10이 리턴됨.

    def score(self,words,category):
        score = math.log(self.category_prob(category))
        print('스코어',score)
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    def word_prob(self,word,category):
        n=self.get_word_count(word, category)+1
        # print(n)
        d=sum(self.word_dict[category].values())+len(self.words)
        #광고 카테고리에 속하는 단어들의 등장 횟수의 총합+분류 대상
        print(n/d)
        return n/d

    def get_word_count(self,word,category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0




