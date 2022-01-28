class Exp: pass

class IntLit(Exp): 
    def __init__(self, value):
        self.value = value

class FloatLit(Exp): 
    def __init__(self, value):
        self.value = value

class UnExp(Exp): 
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    
class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.o1 = o1
        self.op = op
        self.o2 = o2
		
class Eval:
    def visit(self, x):
        if type(x) is IntLit:
            return x.value
        elif type(x) is FloatLit:
            return x.value
        elif type(x) is UnExp:
            e = self.visit(x.operand)
            if x.op == '+': return e
            elif x.op == '-': return -e
        elif type(x) is BinExp:
            e1 = self.visit(x.o1)
            e2 = self.visit(x.o2)
            if x.op == '-': return e1 - e2
            elif x.op == '+': return e1 + e2
            elif x.op == '*': return e1 * e2
            elif x.op == '/': return e1 / e2
            
class PrinPrefix:
    def visit(self, x):
        if type(x) is IntLit:
            return str(x.value) + ' '
        elif type(x) is FloatLit:
            return str(x.value) + ' '
        elif type(x) is UnExp:
            e = self.visit(x.operand)
            if x.op == '+': return '+.' + ' ' + e
            elif x.op == '-': return '-.' + ' ' + e
        elif type(x) is BinExp:
            e1 = self.visit(x.o1)
            e2 = self.visit(x.o2)
            if x.op == '-': return '-' + ' ' + e1 + e2
            elif x.op == '+': return '+' + ' ' + e1 + e2
            elif x.op == '*': return '*' + ' ' + e1 + e2
            elif x.op == '/': return '/' + ' ' + e1 + e2
        



	
if __name__ == '__main__':
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
    v1 = Eval()
    v2 = PrinPrefix()
    print(v1.visit(x5))
    print(v2.visit(x5))