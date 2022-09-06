# ------------------------------------------------------------
# ldlexer.py
#
# tokenizer for Little Duck language using SLY
# ------------------------------------------------------------

from sly import Lexer

class LDLexer(Lexer):
    tokens = {'CTE_I', 'CTE_F', 'CTE_STRING', 'ID', 'DIFFERENT',
                'PROGRAM', 'IF', 'ELSE', 'VAR', 'INT', 'FLOAT', 'PRINT'}

    literals = {';', ',', ':', '{', '}', '=', '>', '<', '(', ')', '+', '-', '*', '/'}

    # Reserved words
    PROGRAM = r'program'
    IF = r'if'
    ELSE = r'else'
    VAR = r'var'
    INT = r'int'
    FLOAT = r'float'
    PRINT = r'print'
    # Token RegEx
    ID = r'\_*[A-Za-z][A-Za-z0-9_]*'
    CTE_STRING = r'\"[0-9A-Za-z_ ]*\"'
    DIFFERENT = r'\<\>'

    @_(r'\d+\.\d+')
    def CTE_F(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def CTE_I(self, t):
        t.value = int(t.value)
        return t
    

    # ignored characters
    ignore = ' \t'

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1




    
if __name__ == '__main__':
    file = open('hello_world.ld')
    data = file.read()
    file.close()
    lexer = LDLexer()
    for tok in lexer.tokenize(data):
        print(tok)
