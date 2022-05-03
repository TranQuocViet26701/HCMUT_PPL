class StaticCheck(Visitor):
  
    def visitProgram(self,ctx:Program,o):
        o = [{}]
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        n = ctx.name
        if n in o[0]:
            raise Redeclared(ctx)
        else:
            o[0][ctx.name] = 0
            
    def visitBlock(self,ctx:Block,o):
        block = [{}]
        for decl in ctx.decl:
           self.visit(decl, block + o)
        for stmt in ctx.stmts:
           self.visit(stmt, block + o)
           
    def visitAssign(self,ctx:Assign,o):
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs, o)
        if lhs == 0:
            if rhs == 0:
                raise TypeCannotBeInferred(ctx)
            for a in o:
                if ctx.lhs.name in a:
                   a[ctx.lhs.name]=rhs
                   break
            lhs = rhs
        if rhs == 0:
            if lhs == 0:
                raise TypeCannotBeInferred(ctx)
            for a in o:
                if ctx.rhs.name in a:
                    a[ctx.rhs.name]=lhs
                    break
            rhs = lhs
        if lhs != rhs:
            raise TypeMismatchInStatement(ctx)


    def visitBinOp(self,ctx:BinOp,o):
        ltype = self.visit(ctx.e1,o)
        rtype = self.visit(ctx.e2,o)

        if ctx.op in ["+", "-", "*", "/"]:
            if ltype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=1
                        break
                ltype == 1
            if rtype == 0:
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]=1
                        break
                rtype == 1
            if ltype == 1 and rtype == 1:
                return 1
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if ltype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=2
                        break
                ltype == 2
            if rtype == 0:
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]=2
                        break
                rtype == 2
            if ltype == 2 and rtype == 2:
                return 2
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">","="]:
            if ltype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=1
                        break
                ltype == 1
            if rtype == 0:
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]=1
                        break
                rtype == 1
            if ltype == 1 and rtype == 1:
                return 3
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">.", "=."]:
            if ltype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=2
                        break
                ltype == 2
            if rtype == 0:
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]=2
                        break
                rtype == 2
            if ltype == 2 and rtype == 2:
                return 3
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if ltype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=3
                        break
                ltype == 3
            if rtype == 0:
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]=3
                        break
                rtype == 3
            if ltype == 3 and rtype == 3:
                return 3
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == "-":
            if typ == 0:
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]=1
                        break
                typ == 1
            if typ == 1:
                return 1
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "-.":
            if typ == 0:
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]=2
                        break
                typ == 2
            if typ == 2:
                return 2
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "!":
            if typ == 0:
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]=3
                        break
                typ == 3
            if typ == 3:
                return 3
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "i2f":
            if typ == 0:
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]=1
                        break
                typ == 1
            if typ == 1:
                return 2
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "floor":
            if typ == 0:
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]=2
                        break
                typ == 2
            if typ == 2:
                return 1
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return 1

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3

    def visitId(self,ctx,o):
        n = ctx.name
        for a in o:
            if n in a:
                return a[n]
        raise UndeclaredIdentifier(n)