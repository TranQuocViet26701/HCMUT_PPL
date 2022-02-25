from functools import reduce


class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda prev , curr: prev + self.visit(curr), ctx.vardecl(), []))
    
    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ = self.visit(ctx.mptype())  
        ids = self.visit(ctx.ids())
        return [VarDecl(i, typ) for i in ids]
    
    # mptype: INTTYPE | FLOATTYPE;  
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]