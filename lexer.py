import sys
import re

new1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
new2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lex(teks, token_exprs):
    line = 1 #posisi baris saat ini
    pos = 0 #posidi karakter pada seluruh potongan teks (absolut)
    cur_pos = 1 #posisi karakter relatif terhadap baris tempat dia berada
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            line += 1
            cur_pos = 1
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            if line == 1:
                if pattern == new1:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == new2:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = tag
                    tokens.append(token)
                break
        if not match:
            print()
            print("SYNTAX ERROR")
            # print("Illegal character %s at line %d and column %d" % (characters[pos], line, cur_pos))
            sys.exit(1)
        else:
            pos = match.end(0)
        cur_pos += 1
    return tokens
