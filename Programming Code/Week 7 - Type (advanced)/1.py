class StaticCheck(Visitor):
  
    def visitProgram(self,ctx:Program,o):
      o = {}
      for decl in ctx.decl: self.visit(decl, o)
      for stmt in ctx.stmts: self.visit(stmt, o)

    def visitVarDecl(self,ctx:VarDecl,o):
      o[ctx.name] = 0

    def visitAssign(self,ctx:Assign,o): 
      rtype = self.visit(ctx.rhs, o)
      ltype = self.visit(ctx.lhs, o)
      
      if rtype == 0 and ltype == 0:
        raise TypeCannotBeInferred(ctx)
      elif rtype == 0 and ltype != 0:
        o[ctx.rhs.name] = ltype
      elif ltype == 0 and rtype != 0:
        o[ctx.lhs.name] = rtype
      elif rtype != ltype:
        raise TypeMismatchInStatement(ctx)
      
      

    def visitBinOp(self,ctx:BinOp,o): 
      t1 = self.visit(ctx.e1, o)
      t2 = self.visit(ctx.e2, o)
      
      if ctx.op in ['+', '-', '*', '/']:
        if t1 == 0:
          o[ctx.e1.name] = 1
          t1 = 1
        if t2 == 0:
          o[ctx.e2.name] = 1
          t2 = 1
        if t1 != 1 or t2 != 1: 
          raise TypeMismatchInExpression(ctx)
        return 1
        
      if ctx.op in ['+.', '-.', '*.', '/.']:
        if t1 == 0:
          o[ctx.e1.name] = 2
          t1 = 2
        if t2 == 0:
          o[ctx.e2.name] = 2
          t2 = 2
        if t1 != 2 or t2 != 2: 
          raise TypeMismatchInExpression(ctx)
        return 2
      
      if ctx.op in [">","="]:
          if t1 == 0:
              o[ctx.e1.name] = 1
              t1 = 1
          if t2 == 0:
              o[ctx.e2.name] = 1
              t2 = 1
          if t1 == 1 and t2 == 1:
              return 3
          raise TypeMismatchInExpression(ctx)
        
      if ctx.op in [">.", "=."]:
          if t1 == 0:
              o[ctx.e1.name] = 2
              t1 = 2
          if t2 == 0:
              o[ctx.e2.name] = 2
              t2 = 2
          if t1 == 2 and t2 == 2:
              return 3
          raise TypeMismatchInExpression(ctx)
        
      if ctx.op in ["&&", "||", ">b", "=b"]:
          if t1 == 0:
              o[ctx.e1.name] = 3
              t1 = 3
          if t2 == 0:
              o[ctx.e2.name] = 3
              t2 = 3
          if t1 == 3 and t2 == 3:
              return 3
          raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
      typ = self.visit(ctx.e,o)
      if ctx.op == "-":
          if typ == 0:
              o[ctx.e.name] = 1
              typ = 1
          if typ == 1:
              return 1
          raise TypeMismatchInExpression(ctx)
      if ctx.op == "-.":
          if typ == 0:
              o[ctx.e.name] = 2
              typ = 2
          if typ == 2:
              return 2
          raise TypeMismatchInExpression(ctx)
      if ctx.op == "!":
          if typ == 0:
              o[ctx.e.name] = 3
              typ = 3
          if typ == 3:
              return 3
          raise TypeMismatchInExpression(ctx)
      if ctx.op == "i2f":
          if typ == 0:
              o[ctx.e.name] = 1
              typ = 1
          if typ == 1:
              return 2
          raise TypeMismatchInExpression(ctx)
      if ctx.op == "floor":
          if typ == 0:
              o[ctx.e.name] = 2
              typ = 2
          if typ == 2:
              return 1
          raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o): return 1 

    def visitFloatLit(self,ctx,o): return 2

    def visitBoolLit(self,ctx,o): return 3

    def visitId(self,ctx,o): 
      if ctx.name in o:
        return o[ctx.name]
      raise UndeclaredIdentifier(ctx.name)