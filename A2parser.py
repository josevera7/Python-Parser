import ply.yacc as yacc
import sys
from lex import tokens

#Profesor, por alguna razon, algunos tokens no los accepta. Si encuentra algo al corregirlo, notifiquelo en los comentarios
def p_Exp(p):
    """
    Exp : Term Binop Exp
    | Term
    | IF Exp THEN Exp ELSE Exp
    | LET DefPlus IN Exp
    | MAP IdList TO Exp
    """
    #print('IsExp')


def p_Term(p):
    """
    Term : Bool
         | Unop Term
         | Factor LEFTPAREN ExpList RIGHTPAREN
         | Factor
         | Int
         | empty
    """

def p_Factor(p):
    '''
    Factor : LEFTPAREN Exp RIGHTPAREN
           | Prim
           | Id
    '''
    #print("isFactor")


def p_ExpList(p):
    '''
    ExpList : PropExpList
            | empty
    '''


def p_PropExpList(p):
    '''
    PropExpList : Exp COMA PropExpList
                | Exp
    '''


def p_IdList(p):
    '''
    IdList : PropIdList
           | empty
    '''


def p_PropIdList(p):
    '''
    PropIdList : Id COMA PropIdList
               | Id
    '''


def p_Def(p):
    '''
    Def : Id ASSIGN Exp SEMICOLON
    '''
   # print('is Def')

def p_DefPlus(p):
    '''
    DefPlus : DefPlus Def
            | Def
    '''



def p_Bool(p):
    '''
    Bool : BOOLEANS
    '''
    #print('isBool')


def p_Unop(p):
    '''
    Unop : Sign
         | WAVE
    '''
   # print("isUnop")


def p_Sign(p):
    '''
    Sign : SIGNS
    '''


def p_Binop(p):
    '''
    Binop : Sign
          | BINOPS
    '''


def p_Prim(p):
    '''
    Prim : PRIMWORDS
    '''
    #print('isPrim')


def p_Id(p):
    '''
    Id : CHARACTER Chagit
       | CHARACTER
    '''
    #print("isID")


def p_Chagit(p):
    '''
    Chagit : Chagit CHARACTER
           | Chagit DIGIT
           | CHARACTER
           | DIGIT
           | empty
    '''


def p_Int(p):
    '''
    Int : DigitPlus
    '''
    #print("is Int")


def p_Digit(p):
    '''
    DigitPlus : DIGIT DigitPlus
              | DIGIT
    '''


def p_empty(p):
    '''
    empty :
    '''

def p_error(p):
    print('Parsing Error!',p)


parser = yacc.yacc()