class Eval:
    def visit(self, x):
        return x.accept(self)

    def visitIntLit(self, x: IntLit):
        return x.value
        
    def visitFloatLit(self, x: FloatLit):
        return x.value
    
    def visitUnExp(self, x:UnExp):
        e = self.visit(x.operand)
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

    def visitIntLit(self, x: IntLit):
        return str(x.value)
        
    def visitFloatLit(self, x: FloatLit):
        return str(x.value)
    
    def visitUnExp(self, x:UnExp):
        e = self.visit(x.operand)
        return '-. ' + e if x.op == '-' else '+. ' + e
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '-': return x.op + ' ' + e1 + ' ' + e2
        elif x.op == '+': return '+' + ' ' + e1 + ' ' + e2
        elif x.op == '*': return '*' + ' ' + e1 + ' ' + e2
        elif x.op == '/': return '/' + ' ' + e1 + ' ' + e2

class PrintPostfix:
    def visit(self, x):
        return x.accept(self)

    def visitIntLit(self, x: IntLit):
        return str(x.value) + ' '
        
    def visitFloatLit(self, x: FloatLit):
        return str(x.value) + ' '
    
    def visitUnExp(self, x:UnExp):
        e = self.visit(x.operand)
        return e + x.op + '. '
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        return e1 + e2 + x.op + ' ' 
