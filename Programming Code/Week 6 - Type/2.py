class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = {}
        for decl in ctx.decl:
            self.visit(decl, o)
        self.visit(ctx.exp, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = ctx.typ

    def visitBinOp(self,ctx:BinOp,o): 
        op = ctx.op
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if op in ["+", "-", "*"]:
            if type(e1) is BoolType or type(e2) is BoolType:
                raise TypeMismatchInExpression(ctx)
            if (type(e1) is IntType and type(e2) is IntType):
                return IntType()
            else:
                return FloatType()
        elif op == "/":
            if type(e1) is BoolType or type(e2) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif op in ["&&", "||"]:
            if type(e1) is BoolType and type(e2) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        elif op in [">", "<", "==", "!="]:
            if type(e1) is type(e2):
                return BoolType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        e = self.visit(ctx.e, o)
        if op == "!" and type(e) is BoolType:
            return BoolType()
        elif op == "-" and (type(e) is IntType or type(e) is FloatType):
            return e
        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o): 
        return IntType()

    def visitFloatLit(self,ctx,o): 
        return FloatType()

    def visitBoolLit(self,ctx,o): 
        return BoolType()

    def visitId(self,ctx,o): 
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)