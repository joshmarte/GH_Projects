#Strings, Bytes and Character Encoding: ut-8, strict
import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #calling the same function within the function to create a loop, the if statement prevents it running to infinity


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=error)
    cooked_string = raw_bytes.decode(encoding, errors=error)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
