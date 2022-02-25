from functools import reduce

class ASTGenerator(CSELVisitor):
    
    # program: decl+ EOF;
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return Program(list(reduce(lambda x, y: x + self.visit(y), ctx.decl(), [])))

    # cseltype: INT | FLOAT | BOOLEAN;
    def visitCseltype(self, ctx:CSELParser.CseltypeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        return BooleanType()

    # decl: vardecl decltail | constdecl decltail | funcdecl decltail;
    def visitDecl(self, ctx:CSELParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        if ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        # if ctx.funcdecl():
        return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())

    # decltail: vardecl decltail | constdecl decltail | funcdecl decltail | ; 
    def visitDecltail(self, ctx:CSELParser.DecltailContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        if ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())
        return []

    # vardecl: LET single_vardecls SEMI;
    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visit(ctx.single_vardecls())

    # single_vardecls: single_vardecl single_vardecltail;
    def visitSingle_vardecls(self, ctx:CSELParser.Single_vardeclsContext):
        return self.visit(ctx.single_vardecl()) + self.visit(ctx.single_vardecltail())

    # single_vardecl: ID COLON cseltype;
    def visitSingle_vardecl(self, ctx:CSELParser.Single_vardeclContext):
        return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.cseltype()))]

    # single_vardecltail: COMMA single_vardecl single_vardecltail | ;
    def visitSingle_vardecltail(self, ctx:CSELParser.Single_vardecltailContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.single_vardecl()) + self.visit(ctx.single_vardecltail())

    # constdecl: CONST single_constdecl SEMI;
    def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
        return self.visit(ctx.single_constdecl())

    # single_constdecl: ID COLON cseltype EQ expr;
    def visitSingle_constdecl(self, ctx:CSELParser.Single_constdeclContext):
        return [ConstDecl(Id(ctx.ID().getText()), self.visit(ctx.cseltype()), self.visit(ctx.expr()))]

    # expr: INTLIT | FLOATLIT | BOOLEANLIT;
    def visitExpr(self, ctx:CSELParser.ExprContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        return BooleanLit(True if ctx.BOOLEANLIT().getText() == 'True' else False)

    # funcdecl: FUNCTION ID LR paramlist RR SEMI;
    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        return [FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paramlist()))]
    
    # paramlist: single_vardecls | ;
    def visitParamlist(self, ctx:CSELParser.ParamlistContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.single_vardecls())
        return []