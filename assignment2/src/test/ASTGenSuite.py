import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """Class Program {}"""
        expect = str(Program([ClassDecl(Id("Program"),[])]))
        self.assertTrue(TestAST.test(input,expect,301))
    def test2(self):
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,302))
    def test3(self):
        input = """Class Rectangle {
                        Var length: Int;
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,303))
    def test4(self):
        input = """Class Rectangle {
                        Val $x: Int = 10;
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,304))
   