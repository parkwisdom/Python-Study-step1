# 입력: output.txt -> 데이터 크리닝 -> output.
# 3. 데이터 정제(크리닝)-영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)

import re

INPUT_FILE_NAME = "output.txt"
OUTPUT_FILE_NAME = "output_cleaned.txt"

#정제 함수
def clean_text(text):
    cleaned_text=re.sub('[a-zA-Z]','',text)
    cleaned_text=re.sub('[\{\}\[\]\(\)\\\▶_.,\'\"//ⓒ!]','',cleaned_text)
    return cleaned_text



#메인 함수
def main():
    read_file=open(INPUT_FILE_NAME,"r")
    write_file=open(OUTPUT_FILE_NAME,"w")
    text=read_file.read()
    # print(text)
    cleaned_text=clean_text(text)
    print(cleaned_text)
    # clean_text(text)
    write_file.write(cleaned_text)
    read_file.close()
    write_file.close()


if __name__ =="__main__":
    main()