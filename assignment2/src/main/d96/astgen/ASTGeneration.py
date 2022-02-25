from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from main.d96.utils.AST import *

class ASTGeneration(D96Visitor):
    # program: classdecl+ EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    # classdecl: CLASS ID (COLON ID)? LP memlist RP | CLASS ID (COLON ID)? LP RP;;
    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        if ctx.COLON():
            if ctx.memlist():
                return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memlist()), Id(ctx.ID(1).getText()))
            return ClassDecl(Id(ctx.ID(0).getText()), [], Id(ctx.ID(1).getText()))
        if ctx.memlist():
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memlist()))
        return ClassDecl(Id(ctx.ID(0).getText()), [])
    
    # memlist: member memlist | member;	
    def visitMemlist(self, ctx: D96Parser.MemlistContext):
        if ctx.getChildCount == 2:
            member = self.visit(ctx.member())
            memlist = self.visit(ctx.memlist())
            return member + memlist
        return self.visit(ctx.member())
    
    # member: attribute_declare | method_declare;
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.attribute_declare():
            return self.visit(ctx.attribute_declare())
        return [self.visit(ctx.method_declare())]
        
    # attribute_declare: immutable_declare | mutable_declare;
    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):  
        if ctx.immutable_declare():
            constants = self.visit(ctx.immutable_declare())
            return list(map(lambda x: AttributeDecl(Static() if '$' in x.constant.name else Instance(), x), constants))
        variables = self.visit(ctx.mutable_declare())
        return list(map(lambda x: AttributeDecl(Static() if '$' in x.variable.name else Instance(), x), variables))
    
    # immutable_declare: VAL identifier (CM identifier)* COLON data_type SEMI
	#                   | VAL identifier (CM identifier)* COLON data_type ASSIGN expr (CM expr)* SEMI;
    def visitImmutable_declare(self, ctx: D96Parser.Immutable_declareContext): 
        if ctx.ASSIGN():
            ids = [self.visit(x) for x in ctx.identifier()] # => list(identifier)
            exprs = [self.visit(x) for x in ctx.expr()] # => list(expr)
            typ = self.visit(ctx.data_type())
            return list(map(lambda x: ConstDecl(x[0], typ, x[1]), zip(ids, exprs)))
        ids = [self.visit(x) for x in ctx.identifier()] # => list(identifier)
        typ = self.visit(ctx.data_type())
        return list(map(lambda x: ConstDecl(x, typ)), ids)
    
    # mutable_declare: VAR identifier (CM identifier)*  COLON data_type SEMI
    #				| VAR identifier (CM identifier)*  COLON data_type ASSIGN expr (CM expr)* SEMI;
    def visitMutable_declare(self, ctx: D96Parser.Mutable_declareContext): 
        if ctx.ASSIGN():
            ids = [self.visit(x) for x in ctx.identifier()] # => list(identifier)
            exprs = [self.visit(x) for x in ctx.expr()] # => list(expr)
            typ = self.visit(ctx.data_type())
            return list(map(lambda x: VarDecl(x[0], typ, x[1]), zip(ids, exprs)))
        ids = [self.visit(x) for x in ctx.identifier()] # => list(identifier)
        typ = self.visit(ctx.data_type())
        return list(map(lambda x: VarDecl(x, typ), ids))

    # identifier: ID | DOLLAR_ID;
    def visitIdentifier(self, ctx: D96Parser.IdentifierContext):
         return Id(ctx.getChild(0).getText())
    
    #--------------METHODS-----------------------#
    
    # method_declare: CONSTRUCTOR LB paramlist RB block_statement
	# 			| CONSTRUCTOR LB RB block_statement
	# 			| DESTRUCTOR LB RB block_statement
	# 			| identifier LB paramlist RB block_statement
	# 			| identifier LB RB block_statement;  
    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        if ctx.CONSTRUCTOR():
            if ctx.paramlist():
                return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paramlist()), self.visit(ctx.block_statement()))
            return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), [], self.visit(ctx.block_statement()))
        if ctx.DESTRUCTOR():
            return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], self.visit(ctx.block_statement()))
        if ctx.paramlist():
            return MethodDecl(Instance(), self.visit(ctx.identifier()), self.visit(ctx.paramlist()), self.visit(ctx.block_statement()))
        return MethodDecl(Instance(), self.visit(ctx.identifier()), [], self.visit(ctx.block_statement()))
    
    # paramlist: param SEMI paramlist | param; => list(Vardecl)
    def visitParamlist(self, ctx: D96Parser.ParamlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        return self.visit(ctx.param()) + self.visit(ctx.paramlist())

    # param: instance_attr_names COLON data_type;  => list(Vardecl)
    def visitParam(self, ctx: D96Parser.ParamContext): 
        instance_attr_names = self.visit(ctx.instance_attr_names())
        typ = self.visit(ctx.data_type())
        return [VarDecl(x, typ) for x in instance_attr_names]
        
    # instance_attr_names: ID CM instance_attr_names | ID ; => list(Id)
    def visitInstance_attr_names(self, ctx: D96Parser.Instance_attr_namesContext):
        if ctx.getChildCount() == 1: 
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.instance_attr_names())
                 
    #**********************************************************************#
    #*							  Statement						   	  	  *#
    #**********************************************************************#
    
    # statement: declaration_statement
	# 	| assignment_statement
	# 	| if_statement
	# 	| for_statement
	# 	| break_statement
	# 	| continue_statement
	# 	| return_statement
	# 	| method_invocation_statement
	# 	| block_statement;
    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.method_invocation_statement():
            return self.visit(ctx.method_invocation_statement())
        else:
            return self.visit(ctx.block_statement())
        
    # declaration_statement: (VAL | VAR) ID (CM ID)*  COLON data_type SEMI
	# 			| (VAL | VAR) ID (CM ID)*  COLON data_type ASSIGN expr (CM expr)* SEMI;
    def visitDeclaration_statement(self, ctx: D96Parser.Declaration_statementContext):
        if ctx.ASSIGN():
            ids = [Id(x.getText()) for x in ctx.ID()] # => list(Id())
            exprs = [self.visit(x) for x in ctx.expr()] # => list(expr)
            typ = self.visit(ctx.data_type())
            if ctx.VAL(): # Constant
                return list(map(lambda x: ConstDecl(x[0], typ, x[1])), zip(ids, exprs))
            else: # Variable
                return list(map(lambda x: VarDecl(x[0], typ, x[1])), zip(ids, exprs))
        ids = [Id(x.getText()) for x in ctx.ID()] # => list(Id())
        typ = self.visit(ctx.data_type())
        if ctx.VAL(): # Constant
            return list(map(lambda x: ConstDecl(x, typ), ids))
        else:   # Variable
            return list(map(lambda x: VarDecl(x, typ), ids))
        
    # assignment_statement: lhs ASSIGN expr SEMI;
    def visitAssignment_statement(self, ctx: D96Parser.Assignment_statementContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    
    # lhs: expr7;
    def visitLhs(self, ctx: D96Parser.LhsContext):
        return self.visit(ctx.expr7())
    
    # if_statement: IF LB expr RB block_statement
	# 		| IF LB expr RB block_statement else_statement
	# 		| IF LB expr RB block_statement elif_else_statement;
    def visitIf_statement(self, ctx: D96Parser.If_statementContext):
        if ctx.getChildCount() == 5: 
            return If(self.visit(ctx.expr()), self.visit(ctx.block_statement()))
        if ctx.else_statement(): 
            return If(self.visit(ctx.expr()), self.visit(ctx.block_statement()), self.visit(ctx.else_statement()))
        return If(self.visit(ctx.expr()), self.visit(ctx.block_statement()), self.visit(ctx.elif_else_statement()))
        
    # elif_else_statement: (ELSEIF LB expr RB block_statement)+ else_statement | (ELSEIF LB expr RB block_statement)+;
    def visitElif_else_statement(self, ctx: D96Parser.Elif_else_statementContext):
        exprs = [self.visit(x) for x in ctx.expr()]
        block_statements = [self.visit(x) for x in ctx.block_statement()]
        else_stmt = self.visit(ctx.else_statement()) if ctx.else_statement() else None
        for i in range(len(exprs)):
            expr = exprs[len(exprs) - 1 - i]
            block_stmt = block_statements[len(exprs) - 1 - i]
            else_stmt = If(expr, block_stmt, else_stmt)
        return else_stmt
    
    # else_statement: ELSE block_statement;
    def visitElse_statement(self, ctx: D96Parser.Else_statementContext):
        return self.visit(ctx.block_statement())
    
    # for_statement: FOREACH LB identifier IN expr TWODOT expr RB block_statement
	# 		| FOREACH LB identifier IN expr TWODOT expr BY expr RB block_statement;
    def visitFor_statement(self, ctx: D96Parser.For_statementContext):
        if ctx.BY():
            return For(self.visit(ctx.identifier()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.block_statement()))
        return For(self.visit(ctx.identifier()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.block_statement()))
    
    # break_statement: BREAK SEMI;
    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return Break()
    
    # continue_statement: CONTINUE SEMI;
    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return Continue()
    
    # return_statement: RETURN SEMI | RETURN expr SEMI;
    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        if ctx.getChildCount() == 2:
            return Return()
        return Return(self.visit(ctx.expr()))
    
    # method_invocation_statement: (instance_method_invocation | static_method_invocation ) SEMI;
    def visitMethod_invocation_statement(self, ctx: D96Parser.Method_invocation_statementContext):
        return self.visit(ctx.getChild(0))
    
    # instance_method_invocation: expr DOT ID LB exprlist RB;
    def visitInstance_method_invocation(self, ctx: D96Parser.Instance_method_invocationContext):
        return CallStmt(self.visit(ctx.expr()), Id(ctx.ID().getText()), self.visit(ctx.exprlist()))
    
    # static_method_invocation: ID TWOCOLON DOLLAR_ID LB exprlist RB;
    def visitStatic_method_invocation(self, ctx: D96Parser.Static_method_invocationContext):
        return CallStmt(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exprlist()))
    
    # block_statement: LP statementlist RP | LP RP;
    def visitBlock_statement(self, ctx: D96Parser.Block_statementContext):
        if ctx.getChildCount() == 2:
            return Block([])
        return Block(self.visit(ctx.statementlist()))
    
    # statementlist: statement statementlist | statement;
    def visitStatementlist(self, ctx: D96Parser.StatementlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.statementlist())
    
    #**********************************************************************#
    #*							  Expression						   	  *#
    #**********************************************************************#
    
    # expr: expr1 CONCATE expr1 | expr1 COMPARE_STRING expr1 | expr1;	
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        
        if ctx.CONCATE():
            op = ctx.CONCATE().getText()
        else:
            op = ctx.COMPARE_STRING().getText()
            
        return BinaryOp(op, left, right)
      
    # expr1: expr2 EQUAL expr2 | expr2 NOT_EQUAL expr2 | expr2 LT expr2
	#       | expr2 LTE expr2 | expr2 GT expr2 | expr2 GTE expr2 
	#       | expr2;
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))  

        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))  
        
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            op = ctx.NOT_EQUAL().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        else:
            op = ctx.GTE().getText()
        
        return BinaryOp(op, left, right) 
    
    # expr2: expr2 AND expr3 | expr2 OR expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3()) 

        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())  
        
        if ctx.AND():
            op = ctx.AND().getText()
        else:
            op = ctx.OR().getText()
        
        return BinaryOp(op, left, right)
    
    # expr3: expr3 ADD expr4 | expr3 SUB expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4()) 

        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())  
        
        if ctx.ADD():
            op = ctx.ADD().getText()
        else:
            op = ctx.SUB().getText()
        
        return BinaryOp(op, left, right)
    
    # expr4: expr4 MUL expr5 | expr4 DIV expr5 | expr4 MOD expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5()) 

        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())  
        
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        else:
            op = ctx.MOD().getText()
        
        return BinaryOp(op, left, right)
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.expr6())
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
    
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expr6()))
    
    # expr7: expr7 index_operators | expr8;
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        return ArrayCell(self.visit(ctx.expr7()), self.visit(ctx.index_operators())) # use arraycell ???
            
    # index_operators: LSB expr RSB | LSB expr RSB index_operators;
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.index_operators())
    
    # expr8: expr8 DOT ID | expr8 DOT ID LB exprlist RB | expr9;
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        if ctx.getChildCount() == 3: 
            return FieldAccess(self.visit(ctx.expr8()), Id(ctx.ID().getText()))
        return CallExpr(self.visit(ctx.expr8()), Id(ctx.ID().getText()), self.visit(ctx.exprlist()) )

    # expr9: ID TWOCOLON DOLLAR_ID | ID TWOCOLON DOLLAR_ID LB exprlist RB | expr10;
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        if ctx.getChildCount() == 3: 
            return FieldAccess(self.visit(ctx.expr8()), Id(ctx.DOLLAR_ID().getText()))
        return CallExpr(self.visit(ctx.expr8()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exprlist()) )
    
    # expr10: NEW ID LB exprlist RB | expr11;
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())
        return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exprlist()))
    
    # expr11: LB expr RB | ID | SELF | NULL | literal;    // có thêm null literal
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.expr())
    
    # exprlist: exprs | ;
    def visitExprlist(self, ctx: D96Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprs())
        return []
    
    # exprs: expr CM exprs | expr;
    def visitExprs(self, ctx: D96Parser.ExprsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprs())
    
    #****************************************************************************#
    #*								Type										*#
    #****************************************************************************#
    
    # data_type: primitive_type | arr_type | class_type;
    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.arr_type():
            return self.visit(ctx.arr_type())
        return self.visit(ctx.class_type())
    
    # primitive_type: INT | FLOAT | BOOLEAN | STRING;
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        return StringType()
    
    # arr_type: ARRAY LSB element_type CM arr_size RSB;
    def visitArr_type(self, ctx: D96Parser.Arr_typeContext):
        return ArrayType(self.visit(ctx.arr_size()), self.visit(ctx.element_type()))
    
    # element_type: primitive_type | arr_type;
    def visitElement_type(self, ctx: D96Parser.Element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        return self.visit(ctx.arr_type())
    
    # arr_size: INTLIT;	
    def visitArr_size(self, ctx: D96Parser.Arr_sizeContext):		
        return int(ctx.INTLIT().getText())                      # should be IntLiteral ???										
        
    # class_type: ID; 
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):    # nên rút gọn ??? in element_type
        return ClassType(Id(ctx.ID().getText()))
    
    #****************************************************************************#
    #*								Literals								    *#
    #****************************************************************************#

    # literal: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | array_lit ; 
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "True")
        return self.visit(ctx.array_lit())
    
    # array_lit: ARRAY LB RB | ARRAY LB arraylist RB;
    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        if ctx.arraylist():
            return ArrayLiteral(self.visit(ctx.arraylist()))
        return ArrayLiteral([])
    
    # arraylist: expr CM arraylist | expr;
    def visitArraylist(self, ctx: D96Parser.ArraylistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.arraylist())

