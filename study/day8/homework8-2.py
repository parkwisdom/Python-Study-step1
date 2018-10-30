import re

INPUT_FILE_NAME= "hw_output.txt"
OUTPUT_FILE_NANE= "hw_output_cleaned.txt"

def clean_text(text):
    cleaned_text=re.sub('[a-zA-Z]','',text)
    cleaned_text=re.sub('[\\\@\'\"ⓒ\[\],.\(\)]','',cleaned_text)
    return cleaned_text

def main():
    read_file=open(INPUT_FILE_NAME,"r")
    write_file=open(OUTPUT_FILE_NANE,"w")
    text=read_file.read()
    cleaned_text=clean_text(text)
    print(cleaned_text)

    write_file.write(cleaned_text)
    read_file.close()
    write_file.close()

if __name__ =="__main__":
    main()