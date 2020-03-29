# Regex version of strip()

import re

string = '   apples and oranges    '
strip_string = string.strip()


def stripper(words, key = None):

    if key == None:
        string_Regex = re.compile(r'^\s*|\s*$')
        new = string_Regex.sub('', words)
    else:
        string_Regex = re.compile(r'^' + key + '|' + key + '$')
        new = string_Regex.sub('', words)

    return print(new), new



