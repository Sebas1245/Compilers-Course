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
    '''vars : VAR vars_p'''

def p_vars_p(p):
    '''vars_p : identifier ':' type ';' vars_p
                | identifier ':' type ';' '''

def p_identifier(p):
    '''identifier : ID ',' identifier 
                  | ID'''

def p_type(p):
    '''type : INT 
            | FLOAT'''

def p_block(p):
    '''block : '{' block_p '}' 
            | '{' '}' '''

def p_block_p(p):
    '''block_p : statement block_p
        | statement'''

def p_statement(p):
    '''statement : assignment
                 | condition
                 | write'''

def p_assignment(p):
    '''assignment : ID '=' expression ';' '''

def p_expression(p):
    '''expression : exp
                  | exp '>' exp
                  | exp '<' exp
                  | exp DIFFERENT exp '''

def p_exp(p):
    '''exp : term 
            | term '+' term
            | term '-' term'''

def p_term(p):
    '''term : factor 
            | factor '*' factor
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
    '''condition : IF '(' expression ')' block ';' 
                | IF '(' expression ')' block ELSE block ';' '''

def p_write(p):
    '''write : PRINT '(' write_p ')' ';' '''

def p_write_p(p):
    '''write_p : write_p2
                | write_p2 ',' write_p'''

def p_write_p2(p):
    '''write_p2 : expression
                | CTE_STRING'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    raise Exception(p)


ld_parser = yacc.yacc(debug=True)

