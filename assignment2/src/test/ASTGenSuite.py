import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test1(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program {}"""
    #     expect = str(Program([ClassDecl(Id("Program"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    # def test2(self):
    #     input = """Class Rectangle : Shape {}"""
    #     expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
    #     self.assertTrue(TestAST.test(input,expect,302))
    # def test3(self):
    #     input = """Class Rectangle {
    #                     Var length: Int;
    #                 }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
    #     self.assertTrue(TestAST.test(input,expect,303))
    # def test4(self):
    #     input = """Class Rectangle {
    #                     Val $x: Int = 10;
    #                 }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
    #     self.assertTrue(TestAST.test(input,expect,304))
    # def test5(self):
    #     input = """Class secondary : main { }"""
    #     expect = "Program([ClassDecl(Id(secondary),Id(main),[])])"
    #     self.assertTrue(TestAST.test(input, expect, 305))
    # def test6(self):
    #     input = """ Class main { 
    #                     Val My1stCons, My2ndCons: Int = 6, 2;
    #                     Var $x, $y : Int = 0, 0;
                 
    #                 }
    #             """
    #     expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0)))])])"
    #     self.assertTrue(TestAST.test(input, expect, 306))
    # def test7(self):
    #     input = """ Class secondary : main { 
    #                     Constructor () {}
    #                 }
    #             """
    #     expect = "Program([ClassDecl(Id(secondary),Id(main),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 307))
    # def test8(self):
    #     input = """ 
    #                 Class Shape {
    #                     Val $numOfShape: Int = 0;
    #                     Val immutableAttribute: Int = 0;
    #                     Var length, width: Int;
                        
    #                     $getNumOfShape() {}
    #                     }
    #             """
    #     expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input,expect,308))
        
#     def test9(self):
#         input = """ 
#                     Class Shape {
#                         Val $numOfShape: Int = 0;
#                         Val immutableAttribute: Int = 0;
#                         Var length, width: Int;
#                         $getNumOfShape() {
#                         Return Rectangle::$numOfShape;
#                         }
#                     }
#                     Class Rectangle: Shape {
#                         getArea() {
#                         Return Self.length * Self.width;
#                         }
#                     }
#                     Class Program {
#                         main() {
#                         Return Shape::$numOfShape;
#                         }
#                     }
#                 """
#         expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Rectangle),Id($numOfShape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))]))])])"
#         self.assertTrue(TestAST.test(input,expect,309))

#     def test10(self):
#         input = """ 
#                     Class Shape {
#                         Val $numOfShape: Int = 5+2;
#                         Val immutableAttribute: Int = 10*6/8;
                        
#                         }
#                 """
#         expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,BinaryOp(+,IntLit(5),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,BinaryOp(/,BinaryOp(*,IntLit(10),IntLit(6)),IntLit(8))))])])"
#         self.assertTrue(TestAST.test(input,expect,310))
    
#     def test11(self):
#         input = """ 
#                     Class arr_test {
#                         Var arr: Array[Int, 5] = Array(1, 5, 7, 12);
#                         Var arr2: Array[Int, 3] = Array(!25, arr[0], (5/3)*10, (arr[2]/2)%2);
#                         Var arr3: Array[Array[Int, 3], 1] = Array(arr2);
                        
#                         }
#                 """
#         expect = "Program([ClassDecl(Id(arr_test),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(1),IntLit(5),IntLit(7),IntLit(12)])),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(3,IntType),[UnaryOp(!,IntLit(25)),ArrayCell(Id(arr),[IntLit(0)]),BinaryOp(*,BinaryOp(/,IntLit(5),IntLit(3)),IntLit(10)),BinaryOp(%,BinaryOp(/,ArrayCell(Id(arr),[IntLit(2)]),IntLit(2)),IntLit(2))])),AttributeDecl(Instance,VarDecl(Id(arr3),ArrayType(1,ArrayType(3,IntType)),[Id(arr2)]))])])"
#         self.assertTrue(TestAST.test(input,expect,311))
    
#     def test12(self):
#         input = """ 
#                     Class Rectangle: Shape {
#                         getArea(){
#                             Return Self.length * Self.width;
#                         }
#                     }
#                 """
#         expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
#         self.assertTrue(TestAST.test(input,expect,312))
    
#     def test13(self):
#         input = """ 
#                 Class Person {
#                         Val firstName, lastName: String; ## property ##
#                         Var age: Int;          ## property ##
                        
#                         c(){
#                             s = a + b + c * d;
#                             d = a && b;
#                             e = !a;
#                         }
#                 }
#                 """
#         expect = "Program([ClassDecl(Id(Person),[AttributeDecl(Instance,ConstDecl(Id(firstName),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(lastName),StringType,None)),AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id(c),Instance,[],Block([AssignStmt(Id(s),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d)))),AssignStmt(Id(d),BinaryOp(&&,Id(a),Id(b))),AssignStmt(Id(e),UnaryOp(!,Id(a)))]))])])"
#         self.assertTrue(TestAST.test(input,expect,313))

#     def test14(self):
#         input = """ 
# Class Test {
#         abc(){}
#         $abc(){}
#         abc(){}
#         print(){}
#         abc(){}
#         low2up(){}
# }
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id($abc),Static,[],Block([])),MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(print),Instance,[],Block([])),MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(low2up),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input,expect,314))
        
#     def test15(self):
#         input = """ 
# Class Test : TestParent{
#         abc__bc_ab(c : Int){
#         }
#         print(a : String){
#             Return "hello" + a;
#         }
# }
#                 """
#         expect = "Program([ClassDecl(Id(Test),Id(TestParent),[MethodDecl(Id(abc__bc_ab),Instance,[param(Id(c),IntType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(a),StringType)],Block([Return(BinaryOp(+,StringLit(hello),Id(a)))]))])])"
#         self.assertTrue(TestAST.test(input,expect,315))
        
#     def test16(self):
#         input = """ 
# Class Test {
#         main(arg : Array[Int, 5]){}
#         $goo (x : Array[Float, 5]) {
#     Val y : Array[Float, 10];
#     Val x : Array[Float, 10];
#     Val z : Array[Float, 10];
#     a.foo( z ) ;
#      a.foo( x ) ;
#       a.foo( y ) ;
#     Return y;
# }
# }
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[param(Id(arg),ArrayType(5,IntType))],Block([])),MethodDecl(Id($goo),Static,[param(Id(x),ArrayType(5,FloatType))],Block([ConstDecl(Id(y),ArrayType(10,FloatType),None),ConstDecl(Id(x),ArrayType(10,FloatType),None),ConstDecl(Id(z),ArrayType(10,FloatType),None),Call(Id(a),Id(foo),[Id(z)]),Call(Id(a),Id(foo),[Id(x)]),Call(Id(a),Id(foo),[Id(y)]),Return(Id(y))]))])])"
#         self.assertTrue(TestAST.test(input,expect,316))
        
    def test17(self):
        input = """ 
Class Test {
        square (x: Float)   ## function definition ##
{
    Var x : Float;
    p = x * x ;
    Return  p  ;
}
}
                """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(square),Instance,[param(Id(x),FloatType)],Block([VarDecl(Id(x),FloatType),AssignStmt(Id(p),BinaryOp(*,Id(x),Id(x))),Return(Id(p))]))])])"
        self.assertTrue(TestAST.test(input,expect,317))
        
    def test18(self):
        input = """ 
Class Test {
   swap(a, b: Boolean)
{
    Var tmp : Boolean;
    tmp = a;
    a = b;
    b = tmp;
    Other.printf(a, b);
    ##Return True;
    ##
    Return;
}
    main(){
    Var a, b : Int;
    Var result: Boolean;
    result = Test.swap(a,b);
    Other.print(result);
}
}
                """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(swap),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],Block([VarDecl(Id(tmp),BoolType),AssignStmt(Id(tmp),Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(tmp)),Call(Id(Other),Id(printf),[Id(a),Id(b)]),Return()])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(result),BoolType),AssignStmt(Id(result),CallExpr(Id(Test),Id(swap),[Id(a),Id(b)])),Call(Id(Other),Id(print),[Id(result)])]))])])"
        self.assertTrue(TestAST.test(input,expect,318))
        
    def test19(self):
        input = """ 
Class Test {
     a(abc : Int; xyz : Float){}
        a(a : Array[Int, 5]){}
}
       
                """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(a),Instance,[param(Id(abc),IntType),param(Id(xyz),FloatType)],Block([])),MethodDecl(Id(a),Instance,[param(Id(a),ArrayType(5,IntType))],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test20(self):
        input = """ 
Class Test {
    main()
        {
            Foreach (i In 1 .. 100 By -1) {}
        }
}
    
                """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),Block([]),UnaryOp(-,IntLit(1))])]))])])"
        self.assertTrue(TestAST.test(input,expect,320))