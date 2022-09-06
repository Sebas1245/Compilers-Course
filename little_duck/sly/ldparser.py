# ------------------------------------------------------------
# ldparser.py
#
# parser for Little Duck language using SLY
# ------------------------------------------------------------

from sly import Parser
from ldlexer import LDLexer

class LDParser(Parser):
    # Get token set
    tokens = LDLexer.tokens

    # Grammar rules
    @_('PROGRAM ID ";" vars block ',
        'PROGRAM ID ";" block')
    def programa(self, p):
        pass

    @_('VAR identifier',
        'VAR identifier ":" type ";"  identifier')
    def vars(self, p):
        pass

    @_('ID "," identifier',
        'ID',
        'empty')
    def identifier(self, p):
        pass 

    @_('INT',
        'FLOAT')
    def type(self, p):
        pass

    @_('"{" e "}"')
    def block(self, p):
        pass
    
    @_('statement e',
        'empty')
    def e(self, p):
        pass
    
    @_('assignment',
        'condition',
        'write')
    def statement(self, p):
        pass

    @_('ID "=" expression ";"')
    def assignment(self, p):
        pass
    
    @_('exp',
        'exp ">" exp',
        'exp "<" exp',
        'exp DIFFERENT exp')
    def expression(self, p):
        pass
    
    @_('term',
        'exp_p')
    def exp(self, p):
        pass
    
    @_('term "+" term',
        'term "-" term')
    def exp_p(self, p):
        pass
    
    @_('factor',
        'term_p')
    def term(self, p):
        pass
    
    @_('factor "*" factor',
        'factor "/" factor')
    def term_p(self, p):
        pass

    @_('"(" expression ")"',
        '"+" const_var',
        '"-" const_var',
        'const_var')
    def factor(self, p):
        pass

    @_('ID',
        'CTE_I',
        'CTE_F')
    def const_var(self, p):
        pass

    @_('IF "(" expression ")" block condition_p')
    def condition(self, p):
        pass

    @_('";"',
        'ELSE block')
    def condition_p(self, p):
        pass

    @_('PRINT "(" write_p ")" ";"') 
    def write(self, p):
        pass

    @_('expression "," write_p',
        'CTE_STRING "," write_p',
        'expression ","',
        'CTE_STRING ","',
        'expression',
        'CTE_STRING')
    def write_p(self, p):
        pass

    @_('')
    def empty(self, sp):
        pass

