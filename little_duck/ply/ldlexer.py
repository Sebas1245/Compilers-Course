# ------------------------------------------------------------
# ldlexer.py
#
# tokenizer for Little Duck language
# ------------------------------------------------------------
import ply.lex as lex

# Reserved words
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT'
}
# List of token names
tokens = (
   'CTE_I', 'CTE_F', 'CTE_STRING', 'ID', 'DIFFERENT'
) + tuple(reserved.values())

# literal symbols
literals = [';', ',', ':', '{', '}', '=', '>', '<', '(', ')', '+', '-', '*', '/']


# Token regular expressions
t_CTE_STRING = r'\"[0-9A-Za-z_ ]*\"'
t_DIFFERENT = r'\<\>'

# Complex tokens
def t_CTE_I(t):
    r'([0-9])+'
    t.value = int(t.value)
    return t

def t_CTE_F(t):
    r'([0-9])*\.([0-9])+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'(\_)*[A-Za-z]([A-Za-z] | [0-9] | \_)*'
    if t.value not in reserved:
        t.type = 'ID'
    else:
        t.type = reserved[t.value]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
program hello; var p1, p2 : int;
{
    if (p1 <> p2)
        print("hello world");
    else
        print("world");
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)