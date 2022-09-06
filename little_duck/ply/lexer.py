# ------------------------------------------------------------
# lexer.py
#
# tokenizer for Little Duck language
# ------------------------------------------------------------
from ply.lex import TOKEN
import ply.lex as lex

# Reserved words
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
}
# List of token names
tokens = (
   'CTE_I', 'CTE_F', 'CTE_STRING', 'ID','DIFFERENT'
   ) + list(reserved.values())

# literal symbols
literals = [';', ',', '{', '}', '=', '>', '<', '(', ')', '+', '-', '*', '/']

# helper RegExs
digit = r'([0-9])'
letter = r'([A-Za-z])'
regex_CTE_I = digit + r'+'
regex_CTE_F = digit + r'*\.' + digit + r'+'
regex_ID = r'(\_*' + letter + r'(' + letter + r'|' + digit + r')*)'

# Token regular expressions
t_CTE_STRING = r'\"(' + digit + r'|' + letter + r')*\"'
t_DIFFERENT = r'\<\>'

# Complex tokens
def t_CTE_I(t):
    regex_CTE_I
    t.value = int(t.value)
    return t

def t_CTE_F(t):
    regex_CTE_F
    t.value = float(t.value)
    return t

def t_ID(t):
    regex_ID
    if t.value not in reserved:
        t.type = 'ID'
    else:
        t.type = reserved[t.value]
        print("Illegal usage of reserved word as identifier") 
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