from functools import reduce

class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class Binary(Expr):
    #op:string: 
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "Binary(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class Id(Expr):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Id(" + self.value + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class IntLiteral(Expr):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class BooleanLiteral(Expr):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)


class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.exp()))
    # exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ASSIGN():
            left = self.visit(ctx.term())
            right = self.visit(ctx.exp())
            return Binary(ctx.ASSIGN().getText(), left, right)
        return self.visit(ctx.term())
    
    # term: factor COMPARE factor | factor
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(ctx.COMPARE().getText(), left, right)
        return self.visit(ctx.factor(0))
    
    # factor: factor ANDOR operand | operand;
    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ANDOR():
            left = self.visit(ctx.factor())
            right = self.visit(ctx.operand())
            return Binary(ctx.ANDOR().getText(), left, right)
        return self.visit(ctx.operand())

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
            