# ------------------------------------------------------------
# ldparser.py
#
# parser for Little Duck language
# ------------------------------------------------------------

import ply.yacc as yacc

from ldlexer import tokens

def p_programa(p):
    '''programa : PROGRAM ID ';' vars block 
                | PROGRAM ID ';' block'''

def p_vars(p): 
    '''vars : VAR identifier
            | VAR identifier ':' type ';'  identifier'''

def p_identifier(p):
    '''identifier : ID ',' identifier 
                  | ID
                  | empty'''

def p_type(p):
    '''type : INT 
            | FLOAT'''

def p_block(p):
    '''block : '{' e '}' '''

def p_e(p):
    '''e : statement e
        | empty'''

def p_statement(p):
    '''statement : assignment
                 | condition
                 | write'''

def p_assignment(p):
    '''assignment : ID '=' expression'''

def p_expression(p):
    '''expression : exp
                  | exp '>' exp
                  | exp '<' exp
                  | exp DIFFERENT exp'''

def p_exp(p):
    '''exp : term 
            | exp_p'''

def p_exp_p(p):
    '''exp_p : term '+' term
            | term '-' term'''

def p_term(p):
    '''term : factor 
            | term_p'''

def p_term_p(p):
    '''term_p : factor '*' factor
            | factor '/' factor'''

def p_factor(p):
    '''factor : '(' expression ')'
              | '+' const_var 
              | '-' const_var
              | const_var '''

def p_const_var(p):
    '''const_var : ID 
                | CTE_I 
                | CTE_F'''

def p_condition(p):
    '''condition : IF '(' expression ')' block condition_p'''

def p_condition_p(p):
    '''condition_p : ';' 
                   | ELSE block'''

def p_write(p):
    '''write : PRINT '(' CTE_STRING ')' ';' 
             | PRINT '(' write_p ')' ';' '''

def p_write_p(p):
    '''write_p : expression ',' expression'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    raise Exception(p)

def p_empty(p):
    'empty :'
    pass

ld_parser = yacc.yacc()

