class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())
    
    # exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        terms = [self.visit(x) for x in ctx.term()]
        assigns = [x.getText() for x in ctx.ASSIGN()]
        right = terms[-1]
        for i in range(len(assigns)):
            op = assigns[len(assigns) - 1 - i]
            left = terms[len(terms) - 2 - i]
            right = Binary(op, left, right)
        return right
    
    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(ctx.COMPARE().getText(), left, right)
        return self.visit(ctx.factor(0))
        
    # factor: operand (ANDOR operand)*; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        operands = [self.visit(x) for x in ctx.operand()]
        andors = [x.getText() for x in ctx.ANDOR()]
        left = operands[0]
        for i in range(len(andors)):
            op = andors[i]
            right = operands[i+1]
            left = Binary(op, left, right)
        return left

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): 
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == "True" else False)
        else: 
            return self.visit(ctx.exp())