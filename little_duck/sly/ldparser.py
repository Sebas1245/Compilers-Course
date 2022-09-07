# ------------------------------------------------------------
# ldparser.py
#
# parser for Little Duck language using SLY
# ------------------------------------------------------------

from sly import Parser
from ldlexer import LDLexer

class LDParser(Parser):
    debugfile = 'parser.out'

    # Get token set
    tokens = LDLexer.tokens

    # Grammar rules
    @_('PROGRAM ID ";" vars block ',
        'PROGRAM ID ";" block')
    def programa(self, p):
        pass

    @_('VAR vars_p')
    def vars(self, p):
        pass
    
    @_('identifier ":" type ";" vars_p',
        'identifier ":" type ";"')
    def vars_p(self, p):
        pass

    @_('ID',
        'ID "," identifier')
    def identifier(self, p):
        pass 

    @_('INT',
        'FLOAT')
    def type(self, p):
        pass

    @_(' "{" block_p "}" ',
        ' "{" "}" ')
    def block(self, p):
        pass
    
    @_('statement block_p',
        'statement')
    def block_p(self, p):
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

    @_('IF "(" expression ")" block ";"',
        'IF "(" expression ")" block ELSE block ";"')
    def condition(self, p):
        pass

    @_('PRINT "(" write_p ")" ";"') 
    def write(self, p):
        pass

    @_('write_p2 ',
        'write_p2 "," write_p')
    def write_p(self, p):
        pass

    @_('expression',
        'CTE_STRING')
    def write_p2(self, p):
        pass

     # Error handling rule
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        raise Exception(t)

