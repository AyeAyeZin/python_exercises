import sys
script, input_encoding, error=sys.argv
def main(language_file, encoding, error):
    line=language_file,readline()
    if line:
        print_line(line,encoding,error)
        return main(language_file,encoding, error)
    def print_line(line,encoding,error):
        next_lang=line.script()
        raw_butes=next_lang.encoding(encoding,erroe=error)
        cooked_string=raw_bytes.decode(enciding,error=error)
        print(raw_bytes,"<===>",cooked_string)
        languages=open("languages.txt",encoding="utf-8")
        main(languages,input_encoding,error)
