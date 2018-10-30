#웹의 컨텐츠를 가져오기 위한 라이브러리
import urllib.request as req

url="http://www.kccistc.net/images/layout/logo_09000_1.png"
savename="test2.png"
mem=req.urlopen(url).read()
with open(savename,mode="wb") as f:#f=open(savename,mode="wb"),f.close 와 같음
    f.write(mem)
    print("저장했습니다.")
# print(type(mem))



# req.urlretrieve(url,"test.png")
# print("이미지가 저장되었습니다.")