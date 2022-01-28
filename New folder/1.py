class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls()) + 1

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() == 0: return 0
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return typ + ids + 1

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1: return 1
        else: return self.visit(ctx.ids()) + 2