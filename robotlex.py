#-----------------------------------------
#		robotlex.py
#	tokenizer for an expression evaluator for words of my formal language
#	to depict actions of a robot which can destroy some walls, yeah baby
#-----------------------------------------

from ply import *

tokens = [	'DATA', 'PRINT', 'MATERIALS', 'STRING_VAR', 'NUMERIC_VAR', 'ELLIPSIS',
		'EQUAL', 'PLUS', 'MINUS', 'COMPARE',
		'INDEX',  'EXIT', 'OPEN_SC', 'CLOSE_SC','COMMA', 'LT', 'GT', 'EQUALS', 'NE', 'ID', 'NEWLINE' ]

reserved = {	'rotate_right' : 'ROTATE_RIGHT', 'function' : 'FUNCTION', 'rotate_left' :'ROTATE_LEFT', 
		'application' : 'APPLICATION', 'undefined' : 'UNDEFINED', 'vector' : 'VECTOR', 'boolean' : 'BOOLEAN', 
		'reflect' : 'REFLECT', 'integer' : 'INTEGER', 'forward' : 'FORWARD', 'return' : 'RETURN', 'string' : 'STRING', 
		'false' : 'FALSE', 'drill' : 'DRILL', 'begin' : 'BEGIN', 'front' : 'FRONT', 'until' : 'UNTIL', 'right' : 'RIGHT', 
		'finish' : 'FINISH', 'robot' : 'ROBOT',
		'true' : 'TRUE', 'then' : 'THEN', 'else' : 'ELSE', 'push' : 'PUSH', 'back' : 'BACK', 'left' :'LEFT', 
		'pop' : 'POP', 'end' : 'END', 'lms' : 'LMS', 'do' : 'DO', 'to' : 'TO', 'if' : 'IF', 'of' : 'OF' }

#List of token names
tokens +=  reserved.values() 

#A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

#A regular expression rule with some action code
def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

#Regular expression rules for simple tokens
t_MATERIALS = r'CONCRETE|PLASTIC|STEEL|WOOD'
t_NUMERIC_VAR = r'[0-9]+'
t_ELLIPSIS = r'\.\.\.'
t_STRING_VAR = r'(\"[a-zA-Z0-9^\w]*\")|(\'[a-zA-Z0-9^\w]*\')' # with a non-word character
t_EQUAL = r':='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_INDEX = r'\[\d+\]'
t_EXIT = r'EXIT'
t_OPEN_SC = r'\('
t_CLOSE_SC = r'\)'
t_COMMA = r'\,'
t_LT = r'<'
t_GT = r'>'
t_EQUALS = r'='
t_NE = r'<>'


#A newline rule 
def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

#Error handling rule
def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

#lex.lex(debug=0)

#Building the lexer
lexer = lex.lex(debug=0)
