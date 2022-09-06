# ------------------------------------------------------------
# ldparser.py
#
# parser for Little Duck language
# ------------------------------------------------------------

import ply.yacc as yacc

from ldlexer import tokens

def p_programa(p):
    '''programa : program ID ';' vars block 
                | program ID ';' block'''
    if len(p) == 5:
        p[0] = p[4] + p[5]
    else:
        p[0] = p[4]

def p_vars(p): 
    '''vars : var identifier
            | var identifier ':' type ';'  identifier'''
    p[0] = p[2]

def p_identifier(p):
    '''identifier : ID ',' identifier 
                  | ID
                  | empty'''
    if len(p) == 3:
        p[0] = p[3]
    else:
        p[0] = p[1]

def p_type(p):
    'type : INT | FLOAT'
    p[0] = p[1]

def p_block(p):
    '''b''lock : '{' e '}' '''
    p[0] = p[2]

def p_e(p):
    '''e : statement e
        | empty'''
    if len(p) == 2:
        p[0] = p[1] + p[2]
    else: 
        p[0] = p[1]

def p_statement(p):
    '''statement : assignment
                 | condition
                 | write'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : ID '=' expression'''
    p[0] = p[3]

def p_expression(p):
    '''expression : exp
                  | exp '>' exp
                  | exp '<' exp
                  | exp DIFFERENT exp'''
    if len(p) == 3:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]

def p_exp(p):
    'exp : term | exp_p'
    p[0] = p[1]

def p_exp_p(p):
    '''exp_p : term '+' term
             | term '-' term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

def p_term(p):
    'term : factor | term_p'
    p[0] = p[1]

def term_p(p):
    '''term_p : factor '*' factor
            | factor '/' factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]
def p_factor(p):
    '''factor: ( expression )
             | '+' const_var 
             | '-' const_var
             | const_var '''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 2:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_const_var(p):
    '''const_var : ID | CTE_I | CTE_F'''
    p[0] = p[1]

def p_condition(p):
    '''condition : IF '(' expression ')' block condition_p'''
    p[0] = p[3] + p[5] + p[6]

def p_condition_p(p):
    '''condition_p : ';' 
                   | ELSE block'''
    if len(p) == 2:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_write(p):
    '''write : PRINT '(' CTE_STRING ')' ';' 
             | PRINT '(' write_p ')' ';' '''
    p[0] = p[3]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def p_empty(p):
    'empty :'
    pass

ld_parser = yacc.yacc()

