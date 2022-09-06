from ldparser import LDParser
from ldlexer import LDLexer

if __name__ == '__main__':
    file = open('hello_world.ld')
    data = file.read()
    file.close()
    lexer = LDLexer()
    parser = LDParser()
    tokens = lexer.tokenize(data)
    parser.parse(tokens)
    print('Code OK')
