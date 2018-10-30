import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

search_addr="http://book.daum.net/search/bookSearch.do?query="

search_word=["파이썬","자바","자바스크립트"]

for i in range(0,len(search_word)):
    search_word_enc=urllib.parse.quote(search_word[i])
    print(search_word_enc)

        # print(search_word_enc)
    url=search_addr+search_word_enc

        # request=req.Request(url)
        # print(request)

    response=req.urlopen(url)
    print(response)

    html_data=response.read()
    print(html_data)

    data=BeautifulSoup(html_data, 'html.parser')
    res=data.select("#page_body > form > ul > li > dl > dd.price > div > span.prc > strong")
    for r in res:
        print(r.string)
    # print(res)
    print("="*70)
