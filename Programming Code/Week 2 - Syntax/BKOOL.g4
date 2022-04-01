grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// Question 1
// program: (vardecl | funcdecl)+ EOF;

// vardecl: 'vardecl' ;

// funcdecl: 'funcdecl' ;

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

// ------------------------------------------------------------
// Question 2
// EBNF -> * + ?
// program: (vardecl | funcdecl)+ EOF;

// vardecl: typ (ID (CM ID)*) SM;
// funcdecl: typ ID paramdecl body;
// paramdecl: LP (param (SM param)*)? RP;
// param: typ (ID (CM ID)*);
// typ: INT | FLOAT;

// BNF
program: decls EOF;
decls: decl decls | decl;
decl: vardecl | funcdecl;

vardecl: typ idlist SM;
idlist: ID CM idlist | ID;

funcdecl: typ ID paramdecl body;
paramdecl: LP paramlist RP;
paramlist: params | ;
params: param SM params | param;
param: typ idlist;

typ: INT | FLOAT;

// ------------------------------------------------------------
// Question 3
body: LB stmts RB ;

stmts: stmt stmts | ;

stmt: vardecl | stmt_assign | stmt_call | stmt_return;

stmt_assign: ID EQ expr SM ;

stmt_call: func_call SM ;

stmt_return: RETURN expr SM ;

func_call: ID LP exprlists RP;
exprlists: exprlist | ;
exprlist: expr CM exprlist | expr;


// expr: 'expr';
// ------------------------------------------------------------
// Question 4
expr: term ADD expr | term;
term: term SUB fact | fact;
fact: fact MUL factor | fact DIV factor | factor;
factor: LP expr RP | INTNUMBER | FLOATNUMBER | func_call;

//And some other rules for variable declaration, function declaration and other rules
// body: 'body';

// Lexer
FLOAT: 'float'; 
INT: 'int';
RETURN: 'return';

CM: ',';
SM: ';';
LP: '(';
RP: ')';
LB: '{';
RB: '}';

EQ: '=';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

fragment INTPART: '0' | [1-9][0-9]*;
fragment FRACPART: '.'[0-9]+;

ID: [a-zA-Z]+;
INTNUMBER: INTPART;
FLOATNUMBER: INTPART FRACPART;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};