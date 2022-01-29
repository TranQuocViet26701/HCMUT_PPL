// My ID: 1915919
// My name: Tran Quoc Viet

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

@members{
global countName
countName = 0
global countValue 
countValue = 0
}

program: class_declare+ EOF;

/**********************************************************************/
/*							  Program structure						  */
/**********************************************************************/

/**** Class ****/
class_declare: CLASS ID ( COLON ID)? LP memberlist RP;									// Class ID (: ID)? {...}
memberlist: members | ;							
members: member members | member;
member: attribute_declare | method_declare;

/**** Attribute ****/
// Val/Var $?My1stCons, $?My2ndCons: Int (= 1 + 5, 2)?;
attribute_declare: (VAL | VAR) identifier (CM identifier)*  COLON data_type SEMI
				| {countName,countValue=0,0} (VAL | VAR) identifier (CM identifier {countName+=1})*  COLON data_type ASSIGN expr (CM expr {countValue+=1})*  {countName==countValue}? SEMI;


// fixed list attribute names
attr_names: (identifier CM attr_names | identifier);	
identifier: ID | DOLLAR_ID;																// $?My1stCons, $?My2ndCons: Int
exprlist: expr CM exprlist | expr;				

/**** Method ****/
method_declare: CONSTRUCTOR LB paramlist RB block_statement
				| DESTRUCTOR LB RB block_statement
				| identifier LB paramlist RB block_statement;  
paramlist: params | ;
params: param SEMI params | param;
param: instance_attr_names COLON data_type;	

/**********************************************************************/
/*							  Expression						   	  */
/**********************************************************************/
expr: expr1 CONCATE expr1 | expr1 COMPARE_STRING expr1 | expr1;						// +., ==. none
expr1: expr2 EQUAL expr2 | expr2 NOT_EQUAL expr2 | expr2 LT expr2					// ==, !=, <, >, <=, >=  none
	| expr2 LTE expr2 | expr2 GT expr2 | expr2 GTE expr2 
	| expr2;
expr2: expr2 AND expr3 | expr2 OR expr3 | expr3;									// &&, || left
expr3: expr3 ADD expr4 | expr3 SUB expr4 | expr4;									// +, - left
expr4: expr4 MUL expr5 | expr4 DIV expr5 | expr4 MOD expr5 | expr5;					// *, /, % left
expr5: NOT expr5 | expr6;															// ! right
expr6: SUB expr6 | expr7;															// - right

expr7: expr7 index_operators | expr8;												// [,] left
index_operators: LSB expr RSB | LSB expr RSB index_operators;

expr8: expr8 DOT ID | expr8 DOT ID LB list_of_expr RB | expr9;						// . left

expr9: ID TWOCOLON DOLLAR_ID | ID TWOCOLON DOLLAR_ID LB list_of_expr RB | expr10;	// :: none

expr10: NEW ID LB list_of_expr RB | expr11;											// New right
expr11: LB expr RB | ID | SELF | literal;											// method_call ????????? DOLLAR_ID ?????

list_of_expr: exprlist | ;
literal: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | array_lit ;
/**********************************************************************/
/*							  Statement						   	  	  */
/**********************************************************************/
statement: declaration_statement
		| assignment_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| return_statement
		| method_invocation_statement
		| block_statement;

instance_attr_names: ID CM instance_attr_names | ID ;
declaration_statement: (VAL | VAR) ID (CM ID)*  COLON data_type SEMI
				| {countName,countValue=0,0} (VAL | VAR) ID (CM ID {countName+=1})*  COLON data_type ASSIGN expr (CM expr {countValue+=1})*  {countName==countValue}? SEMI;

assignment_statement: lhs ASSIGN expr SEMI;
lhs: ID | expr7;

if_statement: IF expr block_statement elseif_statement_list  else_statement;
elseif_statement_list: elseif_statements | ;
elseif_statements: elseif_statement elseif_statements | elseif_statement;
elseif_statement: ELSEIF expr block_statement;
else_statement: ELSE block_statement |;

for_statement: FOREACH LB (ID | DOLLAR_ID) IN expr TWODOT expr by_expr_in_for RB block_statement;
by_expr_in_for: BY expr | ;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

return_statement: RETURN SEMI | RETURN expr SEMI;

method_invocation_statement: (instance_method_invocation | static_method_invocation ) SEMI;		
instance_method_invocation: expr DOT ID LB list_of_expr RB;
static_method_invocation: ID TWOCOLON DOLLAR_ID LB list_of_expr RB;

block_statement: LP statementlist RP;
statementlist:  statements | ;
statements: statement statements | statement;
/****************************************************************************/
/*								Type										*/
/****************************************************************************/
data_type: primitive_type | arr_type | class_type;
primitive_type: INT | FLOAT | BOOLEAN | STRING;

arr_type: ARRAY LSB element_type CM arr_size RSB;								
element_type: primitive_type | arr_type;
arr_size: {self.getCurrentToken().text not in ['0', '00', '0b0', '0B0', '0x0', '0X0']}? INTLIT;																	// required "The lower bound is always 1", but maybe 0 now !!

class_type: ID; 

/**********************************************************************/
/*							  Lexer						   			  */
/**********************************************************************/

/**** COMMENT ****/
BLOCK_COMMENT: '##' .*? '##' -> skip;

/**** LITERALS ****/
INTLIT: ('0' | '00' | '0'[bB]'0' | '0'[xX]'0'
		| NONEZERO_BINARY | NONEZERO_DECIMAL
		| NONEZERO_HEXADECIMAL | NONEZERO_OCTAL
		) {self.text = self.text.replace("_", "")};

FLOATLIT: ( ( '0' | NONEZERO_DECIMAL) '.' DIGIT*							// 1. OR 1.2
		| ( '0' | NONEZERO_DECIMAL) ('.' DIGIT*)? [eE] [+-]? DIGIT+ 		// 1E10 OR 1.E1 1.01E10
		| '.' DIGIT* [eE] [+-]? DIGIT+ 										// .e-10
		) {self.text = self.text.replace("_", "")} ;

BOOLLIT: TRUE | FALSE ;

STRINGLIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};

array_lit: ARRAY LB arraylist RB;
arraylist: array_elements | ;
array_elements: expr CM array_elements | expr;

/**** KEYWORD ****/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';

INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';

RETURN: 'Return';
SELF: 'Self';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

/**** OPERATORS ****/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOT_EQUAL: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
COMPARE_STRING: '==.';
CONCATE: '+.';
TWOCOLON: '::';

/**** SEPERATORS ****/
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';';
COLON: ':';
TWODOT: '..';
DOT: '.'; 
CM: ',';

/**** IDENTIFIERS ****/
ID: [a-zA-Z_][a-zA-Z0-9_]*;
DOLLAR_ID: '$'[a-zA-Z0-9_]+;


/**** FRAGMENTS ****/
fragment DIGIT: [0-9];

fragment NONEZERO_DECIMAL: [1-9]DIGIT*('_'DIGIT+)*;

fragment NONEZERO_HEXADECIMAL: '0'[xX][1-9A-F][0-9A-F]*('_'[0-9A-F]+)*;	

fragment NONEZERO_OCTAL: '0'[1-7][0-7]*('_'[0-7]+)*;							

fragment NONEZERO_BINARY: '0'[bB]'1'[01]*('_'[01]+)*;					

fragment STR_CHAR: ESC_SEQ | ~[\\"\b\f\r\n\t] | '\'"';

fragment ESC_SEQ: '\\' [btnfr'\\];

fragment ESC_ILLEGAL: '\\' ~[btnfr'\\];

WS: [ \t\r\f\n]+ -> skip; // skip spaces, tabs, form feed, newlines
NEWLINE: '\n'+ -> skip;

UNCLOSE_STRING: '"' STR_CHAR* EOF { raise UncloseString(self.text[1:])}
				| '"' STR_CHAR* [\\\b\f\t\n\r] { raise UncloseString(self.text[1:-1]) };

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL { raise IllegalEscape(self.text[1:] )};
ERROR_CHAR: . { raise ErrorToken(self.text) };
