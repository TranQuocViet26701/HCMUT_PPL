
"""
 * @author nhphung
"""
from array import ArrayType
from mailbox import NotEmptyError
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        

class GetEnvironment(BaseVisitor):
    
    def __init__(self):
        self.globalEnv = {}
        
    def visitProgram(self, ast: Program, o: object):
        o = self.globalEnv
        for decl in ast.decl:
            self.visit(decl, o)
        return o
    
    def visitClassDecl(self, ast: ClassDecl, o: object):
        name = ast.classname.name
        if name in o:
            raise Redeclared(Class(), name)
        o[name] = {}
        for decl in ast.memlist:
            self.visit(decl, o[name])
            
    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        if type(ast.kind) is Instance:
            self.visit(ast.decl, ('instance', o))
        if type(ast.kind) is Static:
            self.visit(ast.decl, ('static', o))
            
    def visitVarDecl(self, ast: VarDecl, o: object):
        kind, env = o
        name = ast.variable.name
        if name in env:
            raise Redeclared(Attribute(), name)
        env[name] = ('mutable', self.visit(ast.varType, env), kind)
        return ('mutable', self.visit(ast.varType, env), kind)
    
    def visitConstDecl(self, ast: ConstDecl, o: object):
        kind, env = o
        name = ast.constant.name 
        if name in env: 
            raise Redeclared(Attribute(), name)
        env[name] = ('immutable', self.visit(ast.constType, env), kind)
        # chổ này khác Đạt
        return ('immutable', self.visit(ast.constType, env), kind)
    
    def visitMethodDecl(self, ast: MethodDecl, o: object):
        name = ast.name.name
        if type(ast.kind) is Instance:
            kind = 'instance'
        if type(ast.kind) is Static:
            kind = 'static'
        if name in o:
            raise Redeclared(Method(), name)
        params = list(map(lambda x: self.visit(x, (None, {})), ast.param))
        o[name] = ('method', kind, params, VoidType())
        
    def visitIntType(self, ast, param):
          return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()
    
    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, param):
        name = ast.classname.name
        env = self.globalEnv
        if name in env:
            return ClassType(ast.classname)
        raise Undeclared(Class(), name)
    
class HelpUtils:
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

class StaticChecker(BaseVisitor):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast
   
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        env = GetEnvironment().visit(ast, None)
        if not ('Program' in env and 'main' in env['Program'] and len(env['Program']['main'][2]) == 0):
            raise NoEntryPoint()
        return [self.visit(x, env) for x in ast.decl]
    
    def visitClassDecl(self, ast: ClassDecl, o: object):
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o
        if ast.parentname is not None:
            parentname = ast.parentname.name
            if parentname in env['global']:
                env['parent'] = parentname
            else:
                raise Undeclared(Class(), parentname)
        else: 
            env['parent'] = None
        for decl in ast.memlist:
            self.visit(decl, env)
            
    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        env = o
        if type(ast.decl) is VarDecl:
            self.visit(ast.decl, (Variable(), env))
        if type(ast.decl) is ConstDecl:
            self.visit(ast.decl, (Constant(), env))
            
    def visitMethodDecl(self, ast: MethodDecl, o: object):
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]
        env['current'] = o['current']
        env['parent'] = o['parent']
        [self.visit(param, (Parameter(), env)) for param in ast.param]
        
        for inst in ast.body.inst:
            if type(inst) is VarDecl:
                self.visit(inst, (Variable(), env))
            elif type(inst) is ConstDecl: 
                self.visit(inst, (Constant(), env))
            elif type(inst) is Return:
                if ast.name.name == 'main': 
                    self.visit(inst, ('main', env))
                else :
                    kind = env['global'][env['current']][ast.name.name][1]
                    params = env['global'][env['current']][ast.name.name][2]
                    env['global'][env['current']][ast.name.name] = ('method', kind , params, self.visit(inst, (False, env)))
            else: self.visit(inst, (False, env))
                
    def visitBlock(self, ast: Block, o: object):
        inLoop, env1 = o
        env = {}
        env['global'] = env1['global']
        env['local'] = [{}] + env1['local']
        env['current'] = env1['current']
        env['parent'] = env1['parent']
        
        for inst in ast.inst:
            if type(inst) is VarDecl:
                self.visit(inst, (Variable(), env))
            elif type(inst) is ConstDecl: 
                self.visit(inst, (Constant(), env))
            else:
                # stmt
                self.visit(inst, (inLoop, env))
                
    def visitVarDecl(self, ast: VarDecl, o: object):
        kind, env = o
        name = ast.variable.name
        varType = self.visit(ast.varType, env)
        if ast.varInit is not None:
            value = self.visit(ast.varInit, env)
            # Kiểm tra truy cập global scope
            if value[0] in ['mutable', 'immutable', 'method']:
                if HelpUtils.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)
            if type(varType) is ArrayType and type(value[1]) is ArrayType:
                if varType.size != value[1].size:
                    raise TypeMismatchInStatement(ast)
                if type(varType.eleType) is not type(value[1].eleType):
                    if not (type(varType.eleType) is FloatType and type(value[1].eleType) is IntType):
                        raise TypeMismatchInStatement(ast)
            if type(varType) is not type(value[1]):
                if not (type(varType) is FloatType and type(value[1]) is IntType):
                    raise TypeMismatchInStatement(ast)
        if env.get('local') is not None:
            if name in env['local'][0]:
                raise Redeclared(kind, name)
            env['local'][0][name] = ('var', varType, None)
    
    def visitConstDecl(self, ast: ConstDecl, o: object):
        kind, env = o
        name = ast.constant.name
        if ast.value is None or HelpUtils.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value)
        
        valueCheck = self.visit(ast.value, (True, env))
        if valueCheck[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.value):
                raise Undeclared(Identifier(), ast.value.name)
        if valueCheck[0] in ['mutable', 'var']:
            raise IllegalConstantExpression(ast.value)
        
        value = self.visit(ast.value, env)[1]
        constType = self.visit(ast.constType, env)
        if env.get('local') is not None:
            if name in env['local'][0]:
                raise Redeclared(kind, name)
        if type(constType) is ArrayType and type(value) is ArrayType:
            if constType.size != value.size:
                raise TypeMismatchInConstant(ast)
            if type(constType.eleType) is not type(value.eleType):
                if not (type(constType.eleType) is FloatType and type(value.eleType) is IntType):
                    raise TypeMismatchInConstant(ast)
        if type(constType) is not type(value):
            if not (type(constType) is FloatType and type(value) is IntType):
                raise TypeMismatchInConstant(ast)
        if env.get('local') is not None:
            env['local'][0][name] = ('const', constType, None)       
            
    def visitId(self, ast: Id, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        
        if env.get('local') is not None:
            for local in env['local']:
                if ast.name in local:
                    return local[ast.name]
        if ast.name in env['global'][env['current']]:
            return env['global'][env['current']][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
              return env['global'][env['parent']][ast.name]
        raise Undeclared(Identifier(), ast.name)
    
    def visitAssign(self, ast, o):
        inLoop, env = o
        
        lhs = self.visit(ast.lhs, env)
        exp = self.visit(ast.exp, env)
        
        kindLhs = lhs[0]
        typeLhs = lhs[1]
        kindExp = exp[0]
        typeExp = exp[1]
        
        if kindLhs in ['const', 'immutable']:
            raise CannotAssignToConstant(ast)
        if kindLhs in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        if kindExp in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ast)
            if type(typeLhs.eleType) is not type(typeExp.eleType):
                if not (type(typeLhs.eleType) is FloatType and type(typeExp.eleType) is IntType):
                    raise TypeMismatchInStatement(ast)
        if not ((type(typeLhs) is type(typeExp)) or (type(typeLhs) is FloatType and type(typeExp) is IntType)):
            raise TypeMismatchInStatement(ast)
        
    def visitIf(self, ast: If, o):
        inLoop, env = o
        
        expr = self.visit(ast.expr, env)
        kindExpr = expr[0]
        typeExpr = expr[1]
        
        if kindExpr in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(typeExpr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, (inLoop, env))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, (inLoop, env))

    def visitFor(self, ast: For, o):
        inLoop, env = o

        idType = self.visit(ast.id, env)
        # Check Type Expression
        exp1Type = self.visit(ast.expr1, env)
        exp2Type = self.visit(ast.expr2, env)
        

        if idType[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.id):
                raise Undeclared(Identifier(), ast.id.name)
        if exp1Type[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.expr1):
                raise Undeclared(Identifier(), ast.expr1.name)
        if exp2Type[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.expr2):
                raise Undeclared(Identifier(), ast.expr2.name)
        
        if idType[0] in ['const', 'immutable']:
            raise CannotAssignToConstant(ast.expr1)
        if False in [type(x) is IntType for x in [idType[1], exp1Type[1], exp2Type[1]]]:
            raise TypeMismatchInStatement(ast)
        if HelpUtils.isNaNType(idType[1]):
            raise TypeMismatchInStatement(ast)
            
        if ast.expr3 is not None:
            exp3Type = self.visit(ast.expr3, env)
            if exp3Type[0] in ['mutable', 'immutable', 'method']:
              if HelpUtils.isNotAccess(ast.expr3):
                raise Undeclared(Identifier(), ast.expr3.name)
            if type(exp3Type[1]) is not IntType:
                raise TypeMismatchInStatement(ast)
        
        # Visit statements
        self.visit(ast.loop, (True, env))

    def visitContinue(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o):
        nameMethod, env = o
        # kiểm tra có phải main không
        if nameMethod == 'main':
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
            
        if ast.expr is not None: 
            typeReturn = self.visit(ast.expr, env)
            if typeReturn[0] in ['mutable', 'immutable', 'method']:
                if HelpUtils.isNotAccess(ast.expr):
                    raise Undeclared(Identifier(), ast.expr.name)
            return typeReturn[1]
        else: 
            return VoidType()

    def visitBinaryOp(self, ast: BinaryOp, o):
        if type(o) is tuple:
            if HelpUtils.isNotConst(ast.left) or HelpUtils.isNotConst(ast.right):
                raise IllegalConstantExpression(ast)
            
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
            if lType[0] in ['var', 'mutable'] or rType[0] in ['var', 'mutable']:
                raise IllegalConstantExpression(ast)
        else:
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
        if lType[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
        if rType[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)
        op = str(ast.op)
        if op in ["+", "-", "*"]:
            if HelpUtils.isNaNType(lType[1]) or HelpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            if type(lType[1]) is FloatType or type(rType[1]) is FloatType:
                return (None, FloatType(), None)
            return (None, IntType(), None)
        if op in ["/"]:
            if HelpUtils.isNaNType(lType[1]) or HelpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, FloatType(), None)
        if op in ["%"]:
            if not (type(lType[1]) is IntType) or not (type(rType[1]) is IntType):
                raise TypeMismatchInExpression(ast)
            return (None, IntType(), None)
        if op in ["==", "!="]:
            if type(lType[1]) is type(rType[1]):
                if (type(lType[1]) is IntType) or (type(rType[1]) is BoolType):
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in [">", "<", ">=", "<="]:
            if HelpUtils.isNaNType(lType[1]) or HelpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, BoolType(), None)
        if op in ["&&", "||"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is BoolType:
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in ["==.", "+."]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is StringType:
                    return (None, StringType(), None)
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        if type(o) is tuple:
            if HelpUtils.isNotConst(ast.body):
                raise IllegalConstantExpression(ast.body)
            expr = self.visit(ast.body, o)
            if expr[0] in ['var', 'mutable']:
                raise IllegalConstantExpression(ast.body)
            exprType = expr
        else:
            exprType = self.visit(ast.body, o)
        if exprType[0] in ['mutable', 'immutable', 'method']:
            if HelpUtils.isNotAccess(ast.body):
                raise Undeclared(Identifier(), ast.body.name)
        op = str(ast.op)
        if (op == '-' and HelpUtils.isNaNType(exprType[1])) or (op == '!' and type(exprType[1]) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return (None, exprType[1], None)

    # chưa xử lý
    def visitArrayCell(self, ast, o):
        arrType = self.visit(ast.arr, o)
        if type(arrType[1]) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        listIdxType = [self.visit(x, o) for x in ast.idx]
        for idxType in listIdxType:
            if type(idxType[1]) is not IntType:
                raise TypeMismatchInExpression(ast)
        return (None, arrType[1], None)

    def visitCallExpr(self, ast, o):
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(ast.method, (Method(), o, o['current']))
            if method[1] == 'static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  o)
            except:
                if ast.obj.name in o['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                method = self.handleAccess(ast.method, (Method(), o, nameClass[1].classname.name))
                if method[1] == 'static':
                    raise IllegalMemberAccess(ast)
                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                method = self.handleAccess(ast.method, (Method(), o, nameClass))
                if method[1] == 'instance':
                    raise IllegalMemberAccess(ast)
                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)
        paramCall = list(map(lambda x: self.visit(x, o), ast.param))
        if len(paramCall) != len(method[2]):
            raise TypeMismatchInExpression(ast)
        for i in range(len(paramCall)):
            if type(paramCall[i][1]) is not type(method[2][i][1]):
                if not (type(method[2][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                    raise TypeMismatchInExpression(ast)
        return (None, method[3], None)

    def visitCallStmt(self, ast, o):
        inLoop, env = o
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(ast.method, (Method(), env, env['current']))
            if method[1] == 'static':
                raise IllegalMemberAccess(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInStatement(ast)
                method = self.handleAccess(ast.method, (Method(), env, nameClass[1].classname.name))
                if method[1] == 'static':
                    raise IllegalMemberAccess(ast)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)
            if type(nameClass) is str:
                method = self.handleAccess(ast.method, (Method(), env, nameClass))
                if method[1] == 'instance':
                    raise IllegalMemberAccess(ast)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
        if len(paramCall) != len(method[2]):
            raise TypeMismatchInStatement(ast)
        for i in range(len(paramCall)):
            if type(paramCall[i][1]) is not type(method[2][i][1]):
                if not (type(method[2][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                    raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if type(ast.obj) is SelfLiteral:
            fieldname = self.handleAccess(ast.fieldname, (Attribute(), env, env['current']))
            if fieldname[2] == 'static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                fieldname = self.handleAccess(ast.fieldname, (Attribute(), env, nameClass[1].classname.name))
                if fieldname[2] == 'static':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                fieldname = self.handleAccess(ast.fieldname, (Attribute(), env, nameClass))

                if fieldname[2] == 'instance':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)
        return (fieldname[0], fieldname[1], None)

    def handleAccess(self, ast, o):
        kind, env, name = o
        if ast.name in env['global'][name]:
            return env['global'][name][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(kind, ast.name)

    def visitNewExpr(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            classType = (None, ClassType(ast.classname), None)
        else:
            raise Undeclared(Class(), ast.classname.name)
        if (len(ast.param) != 0):
            if "<init>" in env['global'][ast.classname.name]:
                constructor = env['global'][ast.classname.name]["<init>"]
            else:
                raise Undeclared(Method(), "<init>")
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(constructor[2]):
                raise TypeMismatchInExpression(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(constructor[2][i][1]):
                    if not (type(constructor[2][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInExpression(ast)
        return classType

    def visitIntLiteral(self, ast, param):
        return (None, IntType(), None)

    def visitFloatLiteral(self, ast, param):
        return (None, FloatType(), None)

    def visitBooleanLiteral(self, ast, param):
        return (None, BoolType(), None)

    def visitStringLiteral(self, ast, param):
        return (None, StringType(), None)

    def visitNullLiteral(self, ast, param):
        return (None, NullLiteral(), None)

    def visitSelfLiteral(self, ast, param):
        return (None, SelfLiteral(), None)

    def visitArrayLiteral(self, ast, param):
        temp = list(map(lambda x: self.visit(x, param), ast.value))
        default = temp[0][1]
        for typeOfElement in temp:
            if type(typeOfElement[1]) is not type(default):
                raise IllegalArrayLiteral(ast)
        return (None,  ArrayType(len(temp), default), None)

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            return ast
        raise Undeclared(Class(), ast.classname.name)
    

