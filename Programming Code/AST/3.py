class ASTGeneration(MPVisitor):
    #program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))
    # vadecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        vardecl = self.visit(ctx.vardecl()) # list
        vardecltail = self.visit(ctx.vardecltail()) #list
        return vardecl + vardecltail
        
    # vadecltail : vardecl vardecltail |; 
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 2:
            vardecl = self.visit(ctx.vardecl()) # list
            vardecltail = self.visit(ctx.vardecltail()) #list
            return vardecl + vardecltail
        else: return []
    # vardecl: mptype ids ';';
    # int a, b, c; => VarDecl()
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ = self.visit(ctx.mptype())  #IntType()
        ids = self.visit(ctx.ids())     #[Id(a), Id(b), Id(c)]
        # For statement
        res = []
        for x in ids: 
            res += [VarDecl(x, typ)]
        return res
        # return [VarDecl(x, typ) for x in ids]
        # return [map(lambda x: VarDecl(x, typ), ids)]
    # mptype: INTTYPE | FLOATTYPE
    def visitMptype(self,ctx:MPParser.MptypeContext):
        # if ctx.INTTYPE(): return IntType()
        # else: return FloatType()
        return IntType() if ctx.INTTYPE() else FloatType()
    # ids: ID ',' ids | ID
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            t_id = Id(ctx.ID().getText())
            ids = self.visit(ctx.ids()) # list [Id(b), Id(c)]
            return [t_id] + ids