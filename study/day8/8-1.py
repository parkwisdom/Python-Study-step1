from bs4 import BeautifulSoup
import urllib.request as req

OUTPUT_FILE_NAME='output.txt'
URL="https://news.naver.com/main/read.nhn?mode=LS2D&mid=sec&sid1=103&sid2=248&oid=056&aid=0010610228"

# 1. 오늘의 날씨 스크랩(네이버)
# 2. 날씨 본문 내용을 텍스트 파일로 저장(output.txt)
#크롤링 함수:
def get_text(URL):
    sourceFromURL=req.urlopen(URL)
    soup=BeautifulSoup(sourceFromURL,'lxml', from_encoding='utf-8')
    text=""
    for item in soup.find_all('div', id='articleBodyContents'):
        # print(item.find_all(text=True))
        text=text+str(item.find_all(text=True))
    print(text)
    return text

#메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME,"w")
    # get_text(URL)
    res=get_text(URL)
    open_output_file.write(res)
    open_output_file.close()

if __name__ =='__main__': #다른곳에서 불러올 때 이아랫부분은 제외하고 윗쪽 함수만 불러오게함
    main()