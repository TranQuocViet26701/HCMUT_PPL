grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : ID ;

// Question 1
ID: [a-z][a-z0-9]*;

// Question 2
IPV4: ('0' | [1-9][0-9] | [1-9][0-9][0-9])'.'
      ('0' | [1-9][0-9] | [1-9][0-9][0-9])'.'
      ('0' | [1-9][0-9] | [1-9][0-9][0-9])'.'
      ('0' | [1-9][0-9] | [1-9][0-9][0-9]);

// Question 3
REAL: '-'?DECIMAL('.'[0-9]+)?('e''-'?[1-9][0-9]*);
fragment DECIMAL: [0-9] | [1-9][0-9]+;

// Question 4
STRING: ['] ((~[']) | (['][']))* ['];

// Question 5
INT_PHP: [1-9][0-9]*('_'[0-9]+)* {self.text = self.text.replace('_', '')} | '0';



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;