import ply.lex as lex
import sys

tokens = [
    'CHARACTER',
    'DIGIT',
    #'DELIMITER',
    #'OPERATOR',
    'PRIMWORDS',
    'IF',
    'THEN',
    'ELSE',
    'LET',
    'MAP',
    'IN',
    'TO',
    'WAVE',
    'LEFTPAREN',
    'RIGHTPAREN',
    'BOOLEANS',
    'COMA',
    'SEMICOLON',
    'ASSIGN',
    'SIGNS',
    'BINOPS'


]

t_CHARACTER = r'[a-z]|[A-Z]|\?|\_'
t_DIGIT = r'[0-9]'
#t_DELIMITER = r'\(|\)|\[|\]|\,|\;'
#t_OPERATOR = r'\+ | \- | \~ | \* | \/ | \:\= | \!\= | \<\= | \>\= | \< | \> | \& | \| | \='
t_PRIMWORDS = r' number\? | function\? | list\? | empty\? | cons\? | cons | first | rest | arity'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_LET = r'let'
t_MAP = r'map'
t_IN = r'in'
t_TO = r'to'
t_BOOLEANS = r'true | false'
t_WAVE = r'\~'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_COMA = r'\,'
t_SEMICOLON = r'\;'
t_ASSIGN = r'\:\='
t_SIGNS = r'\+ | \-'
t_BINOPS = r'\* | \/ | \!\= | \<\= | \>\= | \< | \> | \& | \| | \='
t_ignore = ' \t\n'


def t_error(t):
    print("Lexer Error: Illegal Character!")
    t.lexer.skip(1)

lexer = lex.lex()

# Test Lexer
# lexer.input("")
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
