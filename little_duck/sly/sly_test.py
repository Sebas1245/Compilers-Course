from ldparser import LDParser
from ldlexer import LDLexer

if __name__ == '__main__':
    print('Enter file name to be tested (with .ld extension)')
    filename = input()
    file = open(filename)
    data = file.read()
    file.close()
    lexer = LDLexer()
    parser = LDParser()
    tokens = lexer.tokenize(data)
    parser.parse(tokens)
    print('Code OK')
