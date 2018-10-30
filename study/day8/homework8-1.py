from bs4 import BeautifulSoup
import urllib.request as req

OUTPUT_FILE_NAME='hw_output.txt'
URL="http://news.hankyung.com/article/2018081680497"

def get_text(URL):
    sourceFromURL=req.urlopen(URL)
    soup=BeautifulSoup(sourceFromURL,'lxml',from_encoding='utf-8')
    text=""
    for item in soup.find_all('div',id='newsView'):
        text=text+str(item.find_all(text=True))
    print(text)
    return text

def main():
    open_output_file=open(OUTPUT_FILE_NAME,"w")
    res=get_text(URL)
    open_output_file.write(res)
    open_output_file.close()

if __name__ =='__main__':
    main()