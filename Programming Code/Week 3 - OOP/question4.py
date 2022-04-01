class Exp: pass

class IntLit(Exp): 
    def __init__(self, value):
        self.value = value
    
    def accept(self,v): return v.visitIntLit(self)

class FloatLit(Exp): 
    def __init__(self, value):
        self.value = value
        
    def accept(self,v): return v.visitFloatLit(self)

class UnExp(Exp): 
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
        
    def accept(self,v): return v.visitUnExp(self)
    
class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.left = o1
        self.op = op
        self.right = o2
    
    def accept(self,v): return v.visitBinExp(self)
		
class Eval:
    def visit(self, x):
        return x.accept(self)
    # IntLit(1) -> 1
    def visitIntLit(self, x: IntLit):
        return x.value
        
    def visitFloatLit(self, x: FloatLit):
        return x.value
    
    def visitUnExp(self, x:UnExp):
        e = self.visit(x.operand)
        # if x.op == '-': return -e
        # else: return e
        return -e if x.op == '-' else e
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '+': return e1 + e2
        elif x.op == '-': return e1 - e2
        elif x.op == '*': return e1 * e2
        elif x.op == '/': return e1 / e2
            
class PrintPrefix:
    def visit(self, x):
        return x.accept(self)
    # IntLit(1) -> 1
    def visitIntLit(self, x: IntLit):
        return str(x.value)
        
    def visitFloatLit(self, x: FloatLit):
        return str(x.value)
    
    def visitUnExp(self, x:UnExp):
        e = self.visit(x.operand)
        # if x.op == '-': return -e
        # else: return e
        return '-. ' + e if x.op == '-' else '+. ' + e
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '-': return x.op + ' ' + e1 + ' ' + e2
        elif x.op == '+': return '+' + ' ' + e1 + ' ' + e2
        elif x.op == '*': return '*' + ' ' + e1 + ' ' + e2
        elif x.op == '/': return '/' + ' ' + e1 + ' ' + e2
        



	
if __name__ == '__main__':
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
    v1 = Eval()
    v2 = PrintPrefix()
    print(v1.visit(x5))
    print(v2.visit(x5))