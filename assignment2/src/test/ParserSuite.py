import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """Class Program {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test2(self):
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestParser.test(input,expect,202))
    def test3(self):
        input = """Class Rectangle {
                        Var length: Int;
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestParser.test(input,expect,203))
    def test4(self):
        input = """Class Rectangle {
                        Val $x: Int = 10;
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestParser.test(input,expect,204))
    def test5(self):
        input = """Class secondary : main { }"""
        expect = "Program([ClassDecl(Id(secondary),Id(main),[])])"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self):
        input = """ Class main { 
                        Val My1stCons, My2ndCons: Int = 6, 2;
                        Var $x, $y : Int = 0, 0;
                 
                    }
                """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0)))])])"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test7(self):
        input = """ Class secondary : main { 
                        Constructor () {}
                    }
                """
        expect = "Program([ClassDecl(Id(secondary),Id(main),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test8(self):
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        
                        $getNumOfShape() {}
                        }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Instance,[],Block([]))])])"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test9(self):
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        $getNumOfShape() {
                        Return Rectangle::$numOfShape;
                        }
                    }
                    Class Rectangle: Shape {
                        getArea() {
                        Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                        Return Shape::$numOfShape;
                        }
                    }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Rectangle),Id($numOfShape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))]))])])"
        self.assertTrue(TestParser.test(input,expect,209))

    def test10(self):
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 5+2;
                        Val immutableAttribute: Int = 10*6/8;
                        
                        }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,BinaryOp(+,IntLit(5),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,BinaryOp(/,BinaryOp(*,IntLit(10),IntLit(6)),IntLit(8))))])])"
        self.assertTrue(TestParser.test(input,expect,210))
    
#     def test11(self):
#         input = """ 
#                     Class arr_test {
#                         Var arr: Array[Int, 5] = Array(1, 5, 7, 12);
#                         Var arr2: Array[Int, 3] = Array(!25, arr[0], (5/3)*10, (arr[2]/2)%2);
#                         Var arr3: Array[Array[Int, 3], 1] = Array(arr2);
                        
#                         }
#                 """
#         expect = "Program([ClassDecl(Id(arr_test),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(1),IntLit(5),IntLit(7),IntLit(12)])),AttributeDecl(Instance,VarDecl(Id(arr2),ArrayType(3,IntType),[UnaryOp(!,IntLit(25)),ArrayCell(Id(arr),[IntLit(0)]),BinaryOp(*,BinaryOp(/,IntLit(5),IntLit(3)),IntLit(10)),BinaryOp(%,BinaryOp(/,ArrayCell(Id(arr),[IntLit(2)]),IntLit(2)),IntLit(2))])),AttributeDecl(Instance,VarDecl(Id(arr3),ArrayType(1,ArrayType(3,IntType)),[Id(arr2)]))])])"
#         self.assertTrue(TestParser.test(input,expect,311))
    
#     def test12(self):
#         input = """ 
#                     Class Rectangle: Shape {
#                         getArea(){
#                             Return Self.length * Self.width;
#                         }
#                     }
#                 """
#         expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
#         self.assertTrue(TestParser.test(input,expect,312))
    
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
#         self.assertTrue(TestParser.test(input,expect,313))

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
#         self.assertTrue(TestParser.test(input,expect,314))
        
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
#         self.assertTrue(TestParser.test(input,expect,315))
        
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
#         self.assertTrue(TestParser.test(input,expect,316))
        
#     def test17(self):
#         input = """ 
# Class Test {
#         square (x: Float)   ## function definition ##
# {
#     Var x : Float;
#     p = x * x ;
#     Return  p  ;
# }
# }
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(square),Instance,[param(Id(x),FloatType)],Block([VarDecl(Id(x),FloatType),AssignStmt(Id(p),BinaryOp(*,Id(x),Id(x))),Return(Id(p))]))])])"
#         self.assertTrue(TestParser.test(input,expect,317))
        
#     def test18(self):
#         input = """ 
# Class Test {
#    swap(a, b: Boolean)
# {
#     Var tmp : Boolean;
#     tmp = a;
#     a = b;
#     b = tmp;
#     Other.printf(a, b);
#     ##Return True;
#     ##
#     Return;
# }
#     main(){
#     Var a, b : Int;
#     Var result: Boolean;
#     result = Test.swap(a,b);
#     Other.print(result);
# }
# }
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(swap),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],Block([VarDecl(Id(tmp),BoolType),AssignStmt(Id(tmp),Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(tmp)),Call(Id(Other),Id(printf),[Id(a),Id(b)]),Return()])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(result),BoolType),AssignStmt(Id(result),CallExpr(Id(Test),Id(swap),[Id(a),Id(b)])),Call(Id(Other),Id(print),[Id(result)])]))])])"
#         self.assertTrue(TestParser.test(input,expect,318))
        
#     def test19(self):
#         input = """ 
# Class Test {
#      a(abc : Int; xyz : Float){}
#         a(a : Array[Int, 5]){}
# }
       
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(a),Instance,[param(Id(abc),IntType),param(Id(xyz),FloatType)],Block([])),MethodDecl(Id(a),Instance,[param(Id(a),ArrayType(5,IntType))],Block([]))])])"
#         self.assertTrue(TestParser.test(input,expect,319))

#     def test20(self):
#         input = """ 
# Class Test {
#     main()
#         {
#             Foreach (i In 1 .. 100 By -1) {}
#         }
# }
    
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),Block([]),UnaryOp(-,IntLit(1))])]))])])"
#         self.assertTrue(TestParser.test(input,expect,320))
        
#     def test21(self):
#         input = """ 
# Class Test {
#     main()
#         {
#             Foreach (i In 1 .. 5 + 1) {
#                 IO.printf(i);
#             }
#         }
# }
    
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),BinaryOp(+,IntLit(5),IntLit(1)),Block([Call(Id(IO),Id(printf),[Id(i)])]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input,expect,321))
    
#     def test22(self):
#         input = """ 
# Class Test {
#     main()
#         {
#             Var x: Int;
#             IO.input(x);
#             Foreach (i In 1 .. x) {
#                 If (i%2==1) {IO.print(i);}
#                 If (i==4) {Break;}
#             }
#         }
# }
    
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),IntType),Call(Id(IO),Id(input),[Id(x)]),For(Id(i),IntLit(1),Id(x),Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(1)),Block([Call(Id(IO),Id(print),[Id(i)])])),If(BinaryOp(==,Id(i),IntLit(4)),Block([Break]))]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input,expect,322))
    
#     def test23(self):
#         input = """ 
# Class Test {
#     main()
#         {
#             Var x: Int;
#             IO.input(x);
#             Foreach (i In 1 .. x) {
#                 If (i%2==1) {IO.print(i);}
#                 If (i==(x/2)) {
#                     i = i + 5;
#                     Continue;
#                     }
#             }
#         }
# }
    
#                 """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),IntType),Call(Id(IO),Id(input),[Id(x)]),For(Id(i),IntLit(1),Id(x),Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(1)),Block([Call(Id(IO),Id(print),[Id(i)])])),If(BinaryOp(==,Id(i),BinaryOp(/,Id(x),IntLit(2))),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(5))),Continue]))]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input,expect,323))
        
#     def test24(self):
#         input = """
#         Class testFor {
#             testFor() {
#                 Foreach (i In 1 .. 10) {a=a+1;}
#             ##}##}
#             callFor() {
#                 Foreach (i In 25 .. 5 By 2) {
#                     a = a + 1;
#                     Foreach (i In 5 .. 25 By 2) {
#                         a.Pi[5] = 1 + 2;
#                     }
#                 }
                
#                 Return a;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testFor),[MethodDecl(Id(testFor),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),IntLit(1)])])),MethodDecl(Id(callFor),Instance,[],Block([For(Id(i),IntLit(25),IntLit(5),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),For(Id(i),IntLit(5),IntLit(25),Block([AssignStmt(ArrayCell(FieldAccess(Id(a),Id(Pi)),[IntLit(5)]),BinaryOp(+,IntLit(1),IntLit(2)))]),IntLit(2)])]),IntLit(2)]),Return(Id(a))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 324))
        
#     def test25(self):
#         input = """
#         Class testFor {
#             testFor() {
#                 Foreach (i In 1 .. 10) {a=a+1;}
#             }
#             callFor(a : Int) {
#                 Foreach (a In 1 .. 10) {
#                     a = a + 1;
#                     Foreach (a In -10 .. 10 By 5) {
#                         a.Pi[5] = 1 + 2;
#                         If (a.v < z[2]) {
#                             If (a == 1) {
#                                 If (a == 1) {
                                    
#                                 }
#                             }
#                             Else {
#                                 If (a > b) {a = 2;} Elseif (a == -5) {a = 2;}
#                             }
#                         }
#                     }
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testFor),[MethodDecl(Id(testFor),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),IntLit(1)])])),MethodDecl(Id(callFor),Instance,[param(Id(a),IntType)],Block([For(Id(a),IntLit(1),IntLit(10),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),For(Id(a),UnaryOp(-,IntLit(10)),IntLit(10),Block([AssignStmt(ArrayCell(FieldAccess(Id(a),Id(Pi)),[IntLit(5)]),BinaryOp(+,IntLit(1),IntLit(2))),If(BinaryOp(<,FieldAccess(Id(a),Id(v)),ArrayCell(Id(z),[IntLit(2)])),Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([]))]),Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),UnaryOp(-,IntLit(5))),Block([AssignStmt(Id(a),IntLit(2))])))]))]))]),IntLit(5)])]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 325))
        
#     def test26(self):
#         input = """
#         Class testFor : _parentTest {
#             testFor(i: Float) {
#                 Foreach (i In 1 .. 10) {a=a+1;}
                
#                 Return _123;
#             }
#             $callFor() {
#                 Foreach (i In (10-5) .. 10 By -5) {
#                     a = a + 1;
#                     Foreach (i In 1 .. 10 By (10-5)) {
#                         a.Pi[5] = 1 + 2;
                        
#                     }
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testFor),Id(_parentTest),[MethodDecl(Id(testFor),Instance,[param(Id(i),FloatType)],Block([For(Id(i),IntLit(1),IntLit(10),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),IntLit(1)]),Return(Id(_123))])),MethodDecl(Id($callFor),Static,[],Block([For(Id(i),BinaryOp(-,IntLit(10),IntLit(5)),IntLit(10),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),For(Id(i),IntLit(1),IntLit(10),Block([AssignStmt(ArrayCell(FieldAccess(Id(a),Id(Pi)),[IntLit(5)]),BinaryOp(+,IntLit(1),IntLit(2)))]),BinaryOp(-,IntLit(10),IntLit(5))])]),UnaryOp(-,IntLit(5))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 326))
        
#     def test27(self):
#         input = """
#         Class testData : PPL {
#             $loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#             Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                     If (a > f-1) {Break;}
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),Id(PPL),[MethodDecl(Id($loopTest),Static,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([Break]))]),BinaryOp(-,IntLit(10),IntLit(5))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 327))
        
#     def test28(self):
#         input = """
#         Class testData : PPL {
#             loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),Id(PPL),[MethodDecl(Id(loopTest),Instance,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([]))])])"
#         self.assertTrue(TestParser.test(input, expect, 328))
        
#     def test29(self):
#         input = """
#         Class testData : PPL {
#             $loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#                 Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                     ## in loop ##
#                 }
#             }
#             loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#                 Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                     If (a > f-1) {Break;} Else {Continue;}
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),Id(PPL),[MethodDecl(Id($loopTest),Static,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([]),BinaryOp(-,IntLit(10),IntLit(5))])])),MethodDecl(Id(loopTest),Instance,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([Break]),Block([Continue]))]),BinaryOp(-,IntLit(10),IntLit(5))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 329))
        
#     def test30(self):
#         input = """
#         Class testData : PPL {
#             loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#                  Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                     If (a > f-1) {Break;} Else {Continue;}
#                     Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                     If (a > f-1) {
#                         Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
#                         If (a > f-1) {Out.print(10);} 
#                         }
#                     } Else {Continue;}
#                     }
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),Id(PPL),[MethodDecl(Id(loopTest),Instance,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([Break]),Block([Continue])),For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([Call(Id(Out),Id(print),[IntLit(10)])]))]),BinaryOp(-,IntLit(10),IntLit(5))])]),Block([Continue]))]),BinaryOp(-,IntLit(10),IntLit(5))])]),BinaryOp(-,IntLit(10),IntLit(5))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 330))
        
#     def test31(self):
#         input = """
#         Class testData{
#             loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
#                 Foreach (i In (a + c -d == f) .. a+(a >=d)/32) {
#                         If (a > f-1) {Out.print(10);} 
#                         Elseif (a <= 10) {Return Tester::$number;}
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),[MethodDecl(Id(loopTest),Instance,[param(Id(a),IntType),param(Id(v),IntType),param(Id(c),FloatType),param(Id(d),FloatType),param(Id(a),BoolType),param(Id(s),BoolType),param(Id(str1),StringType),param(Id(str2),StringType),param(Id(r1),ClassType(Id(Room))),param(Id(r2),ClassType(Id(Room)))],Block([For(Id(i),BinaryOp(==,BinaryOp(-,BinaryOp(+,Id(a),Id(c)),Id(d)),Id(f)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(>=,Id(a),Id(d)),IntLit(32))),Block([If(BinaryOp(>,Id(a),BinaryOp(-,Id(f),IntLit(1))),Block([Call(Id(Out),Id(print),[IntLit(10)])]),If(BinaryOp(<=,Id(a),IntLit(10)),Block([Return(FieldAccess(Id(Tester),Id($number)))])))]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 331))

#     def test32(self):
#         input = """
#         Class testData : PPL {
#             _LoopTest() {
#                 Foreach (incre In -10 .. (22+a) By -(22+5)) {
#                     Return (a!=10 && !a);
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(testData),Id(PPL),[MethodDecl(Id(_LoopTest),Instance,[],Block([For(Id(incre),UnaryOp(-,IntLit(10)),BinaryOp(+,IntLit(22),Id(a)),Block([Return(BinaryOp(!=,Id(a),BinaryOp(&&,IntLit(10),UnaryOp(!,Id(a)))))]),UnaryOp(-,BinaryOp(+,IntLit(22),IntLit(5)))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 332))
        
#     def test33(self):
#         input = """
#         Class School {
#             cloneStudent(stu: Student){
#                 Var clone : Student = "qwerty\\n";
#                 If (clone != nil) {
#                     Return clone;
#                 }
#                 Else {
#                     Return null;
#                 }
#             }
#         }"""
#         expect = r"""Program([ClassDecl(Id(School),[MethodDecl(Id(cloneStudent),Instance,[param(Id(stu),ClassType(Id(Student)))],Block([VarDecl(Id(clone),ClassType(Id(Student)),StringLit(qwerty\n)),If(BinaryOp(!=,Id(clone),Id(nil)),Block([Return(Id(clone))]),Block([Return(Id(null))]))]))])])"""
#         self.assertTrue(TestParser.test(input, expect, 333))
        
#     def test34(self):
#         input = """Class Res {
#             add (a,b : Array[Int, 1]) {
#                 Val res : Array[Int, 6] = Array(a,b,res);
#                 If (res.size() != 0) {
#                     Return res;
#                 }
#                 Else
#                     {Return Array();}
#             }
#             getA() {
#                 Self.PrintA();
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Res),[MethodDecl(Id(add),Instance,[param(Id(a),ArrayType(1,IntType)),param(Id(b),ArrayType(1,IntType))],Block([ConstDecl(Id(res),ArrayType(6,IntType),[Id(a),Id(b),Id(res)]),If(BinaryOp(!=,CallExpr(Id(res),Id(size),[]),IntLit(0)),Block([Return(Id(res))]),Block([Return([])]))])),MethodDecl(Id(getA),Instance,[],Block([Call(Self(),Id(PrintA),[])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 334))
        
#     def test35(self):
#         input = """
#         Class C1 {
#             Val $a : Int = 10;
#             C1(a : Int) {
#                 Self.a = a;
#                 If (Self.CheckA() == True ) {Self.PrintA();}
#                 Else {Self.getA();}
#             }
#             getA() {
#                 Foreach (i In 1 .. 10) {
#                     Var a : Int = io.getInt();
#                     If (a > 0)  {
#                         Self.a = a;
#                         Break;
#                     }
#                 }
#                 Self.PrintA();
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(C1),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(10))),MethodDecl(Id(C1),Instance,[param(Id(a),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),If(BinaryOp(==,CallExpr(Self(),Id(CheckA),[]),BooleanLit(True)),Block([Call(Self(),Id(PrintA),[])]),Block([Call(Self(),Id(getA),[])]))])),MethodDecl(Id(getA),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),Block([VarDecl(Id(a),IntType,CallExpr(Id(io),Id(getInt),[])),If(BinaryOp(>,Id(a),IntLit(0)),Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),Break]))]),IntLit(1)]),Call(Self(),Id(PrintA),[])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 335))
        
#     def test36(self):
#         input = """
#         Class C3 : C2 {
#             Val string : String;
#             Constructor(self, name : String) {
#                 Return "Name of C3: " +. name;
#             }
#             CheckName(n1 : String) {
#                 Return string == self.name;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(C3),Id(C2),[AttributeDecl(Instance,ConstDecl(Id(string),StringType,None)),MethodDecl(Id(Constructor),Instance,[param(Id(self),StringType),param(Id(name),StringType)],Block([Return(BinaryOp(+.,StringLit(Name of C3: ),Id(name)))])),MethodDecl(Id(CheckName),Instance,[param(Id(n1),StringType)],Block([Return(BinaryOp(==,Id(string),FieldAccess(Id(self),Id(name))))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 336))

#     def test37(self):
#         input = """Class Rectangle {
#             Var numOfShape: Int = 0;
#             }"""
#         expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(numOfShape),IntType,IntLit(0)))])])"
#         self.assertTrue(TestParser.test(input,expect,337))
        
#     def test38(self):
#         input = """
#         Class checkExp {
#             $_check1(a,b,c : Bolen) {
#                 a1 = a > (b > c);
#                 a2 = ((a==b)!=c)==123;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(checkExp),[MethodDecl(Id($_check1),Static,[param(Id(a),ClassType(Id(Bolen))),param(Id(b),ClassType(Id(Bolen))),param(Id(c),ClassType(Id(Bolen)))],Block([AssignStmt(Id(a1),BinaryOp(>,Id(a),BinaryOp(>,Id(b),Id(c)))),AssignStmt(Id(a2),BinaryOp(==,BinaryOp(!=,BinaryOp(==,Id(a),Id(b)),Id(c)),IntLit(123)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 338))
        
#     def test39(self):
#         input = """
#         Class C3 : C2 {
#             Val name : Car = New Car("Mazda", 2019);
            
#             Constructor(name : String; year : Int) {
#                 Self.name = name;
#                 Self.year = year;
#             }
            
#             C3(n : String;c : C1) {
#                 Self.name = n;
#             }
            
#             getName() {
#                 Return "Name of C3: " +. name;
#             }
#             checkName(n1 : String) {
#                 Return n1 ==. name;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(C3),Id(C2),[AttributeDecl(Instance,ConstDecl(Id(name),ClassType(Id(Car)),NewExpr(Id(Car),[StringLit(Mazda),IntLit(2019)]))),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(year),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(year)),Id(year))])),MethodDecl(Id(C3),Instance,[param(Id(n),StringType),param(Id(c),ClassType(Id(C1)))],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(n))])),MethodDecl(Id(getName),Instance,[],Block([Return(BinaryOp(+.,StringLit(Name of C3: ),Id(name)))])),MethodDecl(Id(checkName),Instance,[param(Id(n1),StringType)],Block([Return(BinaryOp(==.,Id(n1),Id(name)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 339))
        
#     def test40(self):
#         input = """
#         Class mainClass {
#             main() {
#                 Val c3 : C3 = New C3("abc",c1);
#                 c3.checkName("abcd");
#                 io.Print(c3.getName());
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c3),ClassType(Id(C3)),NewExpr(Id(C3),[StringLit(abc),Id(c1)])),Call(Id(c3),Id(checkName),[StringLit(abcd)]),Call(Id(io),Id(Print),[CallExpr(Id(c3),Id(getName),[])])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 340))

#     def test41(self):
#         input = """
#         Class BinExp : Exp {
#             Val op : String;
#             Val left, right : Float;
#             BinExp(op : String; l, r : Float) {
#                 Self.op = op;
#                 Self.r = r;
#             }
#             eval() {
#                 If (op == "+") {Return left + right;}
#                 Elseif (op == "-") {Return lef - right;}
#                 Elseif (op == "/") {Return lef / right;}
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(BinExp),Id(Exp),[AttributeDecl(Instance,ConstDecl(Id(op),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(left),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(right),FloatType,None)),MethodDecl(Id(BinExp),Instance,[param(Id(op),StringType),param(Id(l),FloatType),param(Id(r),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(op)),Id(op)),AssignStmt(FieldAccess(Self(),Id(r)),Id(r))])),MethodDecl(Id(eval),Instance,[],Block([If(BinaryOp(==,Id(op),StringLit(+)),Block([Return(BinaryOp(+,Id(left),Id(right)))]),If(BinaryOp(==,Id(op),StringLit(-)),Block([Return(BinaryOp(-,Id(lef),Id(right)))]),If(BinaryOp(==,Id(op),StringLit(/)),Block([Return(BinaryOp(/,Id(lef),Id(right)))]))))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 341))
#     def test42(self):
#         input = """Class follow_mouse {
#     FixedUpdate () {
#         ## Get the Screen positions of the object ##
#         Val angle : Float = system.AngleBetweenTwoPoints(positionOnScreen, mouseOnScreen);
#         transform.rotation =  Quaternion.Euler(New Vector3(0,0,angle - 180));
#     }
#     changeState() {
#         checkRun = !checkRun;
#     }
#     ## FUNCTION FOR SKILL AND FIRE BULLET
#     create_button_skill() {
#         system.Instantiate(button_skill, new Vector3(-6.5,-4,0), transform.rotation);
#     }
#     float AngleBetweenTwoPoints(Vector3 a, b) {
#          return Math.Atan2(a.y - b.y, a.x - b.x) * Math.Rad2Deg;
#     }##
# }"""
#         expect = "Program([ClassDecl(Id(follow_mouse),[MethodDecl(Id(FixedUpdate),Instance,[],Block([ConstDecl(Id(angle),FloatType,CallExpr(Id(system),Id(AngleBetweenTwoPoints),[Id(positionOnScreen),Id(mouseOnScreen)])),AssignStmt(FieldAccess(Id(transform),Id(rotation)),CallExpr(Id(Quaternion),Id(Euler),[NewExpr(Id(Vector3),[IntLit(0),IntLit(0),BinaryOp(-,Id(angle),IntLit(180))])]))])),MethodDecl(Id(changeState),Instance,[],Block([AssignStmt(Id(checkRun),UnaryOp(!,Id(checkRun)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 342))

#     def test43(self):
#         input = """
# Class skill_check {
#     FixedUpdate()
#     {
#         If (Input.GetKeyDown("s")) {
#         }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(skill_check),[MethodDecl(Id(FixedUpdate),Instance,[],Block([If(CallExpr(Id(Input),Id(GetKeyDown),[StringLit(s)]),Block([]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 343))
        
#     def test44(self):
#         input = """
# Class virus_move {
#     Var myEffect : GameObject;
#     Val speed_virus : Float = -0.15E10;
#     FixedUpdate()
#     {
#     }
#     OnTriggerEnter2D(col : Col2) {
        
#         If ((col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_water_skill"))
#         {
#             system.Destroy(Self);
#             system.Instantiate(myEffect, transform.position, transform.rotation);
#         }
#         If ((col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water")) 
#         {
#             system.Destroy(col.gameObject);
#         }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(virus_move),[AttributeDecl(Instance,VarDecl(Id(myEffect),ClassType(Id(GameObject)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(speed_virus),FloatType,UnaryOp(-,FloatLit(1500000000.0)))),MethodDecl(Id(FixedUpdate),Instance,[],Block([])),MethodDecl(Id(OnTriggerEnter2D),Instance,[param(Id(col),ClassType(Id(Col2)))],Block([If(BinaryOp(||,BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_water)),BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_water_skill))),Block([Call(Id(system),Id(Destroy),[Self()]),Call(Id(system),Id(Instantiate),[Id(myEffect),FieldAccess(Id(transform),Id(position)),FieldAccess(Id(transform),Id(rotation))])])),If(BinaryOp(||,BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_mask)),BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_water))),Block([Call(Id(system),Id(Destroy),[FieldAccess(Id(col),Id(gameObject))])]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 344))
        
#     def test45(self):
#             input = """
#     Class control_victim {
#         Val victim_die :GameObject ;
#         Val eff :GameObject ;
#         Val speed_human : Float = -0.15;

#          Constructor()
#         {
#             transform.position = transform.position + New Vector3(speed_human, 0, 0);
#         }
#          OnTriggerEnter2D(col : Collider2D) {  
#             If ((col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water_skill")) 
#             {
#                 system.Destroy(Self);
#                 system.Instantiate(eff, transform.position, transform.rotation);
#                 system.Instantiate(victim_die, transform.position, transform.rotation);
#             }
#             If (!checkRun)  {
#                 ## UPDATE PLAYER'S HP ##
#                 txt.text = myHP.ToString();
#                 If ((transform.position.y > 6) || (transform.position.y < -6))  {Self.GameOver();}
#                 ## CONTROLL JUMP AND DROP OF PLAYER ##
#                 If (Input.GetButtonDown("Jump") && !isJump) {
#                     jumpAudio.Play(0);
#                     countJump = 4;
#                     isJump = true;
#                     counting = 3;
#                     Self.outSmoke();
#                     Self.jumpUp(jumping / 2);
#                 }
#                 Elseif (countJump != 0) {
#                     If (countJump > 3) { Self.jumpUp(jumping); }
#                     Else { Self.jumpUp(jumping / 3); }
#                 }
#                 Else {
#                     Self.dropDown();
#                     If (counting == 0) { isJump = False; }
#                 }
#             }
#             If ((col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_mask")) 
#             { system.Destroy(col.gameObject); }
#         }
#     }"""
#             expect = "Program([ClassDecl(Id(control_victim),[AttributeDecl(Instance,ConstDecl(Id(victim_die),ClassType(Id(GameObject)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(eff),ClassType(Id(GameObject)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(speed_human),FloatType,UnaryOp(-,FloatLit(0.15)))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(transform),Id(position)),BinaryOp(+,FieldAccess(Id(transform),Id(position)),NewExpr(Id(Vector3),[Id(speed_human),IntLit(0),IntLit(0)])))])),MethodDecl(Id(OnTriggerEnter2D),Instance,[param(Id(col),ClassType(Id(Collider2D)))],Block([If(BinaryOp(||,BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_mask)),BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_water_skill))),Block([Call(Id(system),Id(Destroy),[Self()]),Call(Id(system),Id(Instantiate),[Id(eff),FieldAccess(Id(transform),Id(position)),FieldAccess(Id(transform),Id(rotation))]),Call(Id(system),Id(Instantiate),[Id(victim_die),FieldAccess(Id(transform),Id(position)),FieldAccess(Id(transform),Id(rotation))])])),If(UnaryOp(!,Id(checkRun)),Block([AssignStmt(FieldAccess(Id(txt),Id(text)),CallExpr(Id(myHP),Id(ToString),[])),If(BinaryOp(||,BinaryOp(>,FieldAccess(FieldAccess(Id(transform),Id(position)),Id(y)),IntLit(6)),BinaryOp(<,FieldAccess(FieldAccess(Id(transform),Id(position)),Id(y)),UnaryOp(-,IntLit(6)))),Block([Call(Self(),Id(GameOver),[])])),If(BinaryOp(&&,CallExpr(Id(Input),Id(GetButtonDown),[StringLit(Jump)]),UnaryOp(!,Id(isJump))),Block([Call(Id(jumpAudio),Id(Play),[IntLit(0)]),AssignStmt(Id(countJump),IntLit(4)),AssignStmt(Id(isJump),Id(true)),AssignStmt(Id(counting),IntLit(3)),Call(Self(),Id(outSmoke),[]),Call(Self(),Id(jumpUp),[BinaryOp(/,Id(jumping),IntLit(2))])]),If(BinaryOp(!=,Id(countJump),IntLit(0)),Block([If(BinaryOp(>,Id(countJump),IntLit(3)),Block([Call(Self(),Id(jumpUp),[Id(jumping)])]),Block([Call(Self(),Id(jumpUp),[BinaryOp(/,Id(jumping),IntLit(3))])]))]),Block([Call(Self(),Id(dropDown),[]),If(BinaryOp(==,Id(counting),IntLit(0)),Block([AssignStmt(Id(isJump),BooleanLit(False))]))])))])),If(BinaryOp(||,BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_water)),BinaryOp(==,FieldAccess(FieldAccess(Id(col),Id(gameObject)),Id(tag)),StringLit(bullet_mask))),Block([Call(Id(system),Id(Destroy),[FieldAccess(Id(col),Id(gameObject))])]))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 345))
            
#     def test46(self):
#         input = """
# Class Shape {
#             $getNumOfShape() {
#                 Return A::$numOfShape;
#                 }
#             }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(A),Id($numOfShape)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 346))

#     def test47(self):
#             input = """
#     Class move {
        

#         ## FIRE
#         Transform fire_point;
#         GameObject bullet_water;
#         GameObject bullet_mask;
#         AudioSource shoot_Audio;
#         float num_bullet = 1.;
#         float count_trigger = 0;
#         # special skill ##
        

#         Val Heart : GameObject;
#         Val count_kira : Float = -1.0e12;
#          Update() {
#             If (Input.GetKeyDown("f"))  {
#                 Self.changeState();
#             }
            
#         }
#          shootMask() {
#             Foreach ( i In 0 .. Num_bulle By -1) {
#                 system.Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
#                 shoot_Audio.Play(0);       
#             }
#         }
#         ## FUNCTION CONTROLL UFO AND EFFECT WHEN JUMPING ##
#          outSmoke() {
#             system.Instantiate(smoke_pre, smoke_point.position, smoke_point.rotation);
#         }
#          jumpUp(upSize : Float) {
#             system.transform.position = transform.position + New Vector3(0, upSize, 0);
#         }
#          dropDown() {
#             system.transform.position = transform.position + New Vector3(0, falling, 0);
#         }
#         GameOver() {
#             SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
#         }
#     }"""
#             expect = "Program([ClassDecl(Id(move),[AttributeDecl(Instance,ConstDecl(Id(Heart),ClassType(Id(GameObject)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(count_kira),FloatType,UnaryOp(-,FloatLit(1000000000000.0)))),MethodDecl(Id(Update),Instance,[],Block([If(CallExpr(Id(Input),Id(GetKeyDown),[StringLit(f)]),Block([Call(Self(),Id(changeState),[])]))])),MethodDecl(Id(shootMask),Instance,[],Block([For(Id(i),IntLit(0),Id(Num_bulle),Block([Call(Id(system),Id(Instantiate),[Id(bullet_mask),FieldAccess(Id(fire_point),Id(position)),FieldAccess(Id(fire_point),Id(rotation))]),Call(Id(shoot_Audio),Id(Play),[IntLit(0)])]),UnaryOp(-,IntLit(1))])])),MethodDecl(Id(outSmoke),Instance,[],Block([Call(Id(system),Id(Instantiate),[Id(smoke_pre),FieldAccess(Id(smoke_point),Id(position)),FieldAccess(Id(smoke_point),Id(rotation))])])),MethodDecl(Id(jumpUp),Instance,[param(Id(upSize),FloatType)],Block([AssignStmt(FieldAccess(FieldAccess(Id(system),Id(transform)),Id(position)),BinaryOp(+,FieldAccess(Id(transform),Id(position)),NewExpr(Id(Vector3),[IntLit(0),Id(upSize),IntLit(0)])))])),MethodDecl(Id(dropDown),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(system),Id(transform)),Id(position)),BinaryOp(+,FieldAccess(Id(transform),Id(position)),NewExpr(Id(Vector3),[IntLit(0),Id(falling),IntLit(0)])))])),MethodDecl(Id(GameOver),Instance,[],Block([Call(Id(SceneManager),Id(LoadScene),[BinaryOp(-,FieldAccess(CallExpr(Id(SceneManager),Id(GetActiveScene),[]),Id(buildIndex)),IntLit(1))])]))])])"
#             self.assertTrue(TestParser.test(input, expect, 347))
            
#     def test48(self):
#             input = """
#     Class PlayerMoment : MonoBehaviour{

#         Var speed : Int = 12;
#         Val  gravity : Float = -9.81* 10;
#         ## Update is called once per frame ##
#          Update()
#         {
#             isGrounded = Physics.CheckSphere(groundCheck::$position, groundDistance, groundMask);

#             If (isGrounded && velocity.y < 0) {
#                 velocity.y = -2;
#             }
#         }
#     }"""
#             expect = "Program([ClassDecl(Id(PlayerMoment),Id(MonoBehaviour),[AttributeDecl(Instance,VarDecl(Id(speed),IntType,IntLit(12))),AttributeDecl(Instance,ConstDecl(Id(gravity),FloatType,BinaryOp(*,UnaryOp(-,FloatLit(9.81)),IntLit(10)))),MethodDecl(Id(Update),Instance,[],Block([AssignStmt(Id(isGrounded),CallExpr(Id(Physics),Id(CheckSphere),[FieldAccess(Id(groundCheck),Id($position)),Id(groundDistance),Id(groundMask)])),If(BinaryOp(<,BinaryOp(&&,Id(isGrounded),FieldAccess(Id(velocity),Id(y))),IntLit(0)),Block([AssignStmt(FieldAccess(Id(velocity),Id(y)),UnaryOp(-,IntLit(2)))]))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 348))
            
#     def test49(self):
#             input = """
#     Class PlayerMoment : MonoBehaviour{
#         Var speed : Int= 12;
#         Val gravity : Float= -9.81 * 10;
#         Val jumpHeight: Float = 7;
#         Val velocity : Victory;
#         Var isGrounded : Boolean;
#         ## Update is called once per frame ##
#          Update()
#         {
#             move = transform.right * x + transform.forward * z;
#             ctrller.Move(move  * speed * Time.deltaTime);

#             If (Input.GetButtonDown("Jump") && isGrounded) {
#                 velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
#             }
#             io.getInt(num);
#                 sLec = num;
#             velocity.y = velocity.y + gravity * Time.deltaTime;
#             ctrller.Move(velocity * Time.deltaTime);
#         }
#     }"""
#             expect = "Program([ClassDecl(Id(PlayerMoment),Id(MonoBehaviour),[AttributeDecl(Instance,VarDecl(Id(speed),IntType,IntLit(12))),AttributeDecl(Instance,ConstDecl(Id(gravity),FloatType,BinaryOp(*,UnaryOp(-,FloatLit(9.81)),IntLit(10)))),AttributeDecl(Instance,ConstDecl(Id(jumpHeight),FloatType,IntLit(7))),AttributeDecl(Instance,ConstDecl(Id(velocity),ClassType(Id(Victory)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(isGrounded),BoolType)),MethodDecl(Id(Update),Instance,[],Block([AssignStmt(Id(move),BinaryOp(+,BinaryOp(*,FieldAccess(Id(transform),Id(right)),Id(x)),BinaryOp(*,FieldAccess(Id(transform),Id(forward)),Id(z)))),Call(Id(ctrller),Id(Move),[BinaryOp(*,BinaryOp(*,Id(move),Id(speed)),FieldAccess(Id(Time),Id(deltaTime)))]),If(BinaryOp(&&,CallExpr(Id(Input),Id(GetButtonDown),[StringLit(Jump)]),Id(isGrounded)),Block([AssignStmt(FieldAccess(Id(velocity),Id(y)),CallExpr(Id(Mathf),Id(Sqrt),[BinaryOp(*,BinaryOp(*,Id(jumpHeight),UnaryOp(-,IntLit(2))),Id(gravity))]))])),Call(Id(io),Id(getInt),[Id(num)]),AssignStmt(Id(sLec),Id(num)),AssignStmt(FieldAccess(Id(velocity),Id(y)),BinaryOp(+,FieldAccess(Id(velocity),Id(y)),BinaryOp(*,Id(gravity),FieldAccess(Id(Time),Id(deltaTime))))),Call(Id(ctrller),Id(Move),[BinaryOp(*,Id(velocity),FieldAccess(Id(Time),Id(deltaTime)))])]))])])"
#             self.assertTrue(TestParser.test(input, expect, 349))
            
#     def test50(self):
#             input = """
#     Class Faculty {
#             Val name : String;
#             Faculty(m : String) {}
#             getNameFaculty() { Return name;  }
#              setNameFaculty(n : Int) { name = n;  }
#     }"""
#             expect = "Program([ClassDecl(Id(Faculty),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),MethodDecl(Id(Faculty),Instance,[param(Id(m),StringType)],Block([])),MethodDecl(Id(getNameFaculty),Instance,[],Block([Return(Id(name))])),MethodDecl(Id(setNameFaculty),Instance,[param(Id(n),IntType)],Block([AssignStmt(Id(name),Id(n))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 350))
            
#     def test51(self):
#         input = """Class a {
#                 Val x, y: Float = 1.0, 2e-1 + 0.2;
#             }"""
#         expect = "Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(x),FloatType,FloatLit(1.0))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,BinaryOp(+,FloatLit(0.2),FloatLit(0.2))))])])"
#         self.assertTrue(TestParser.test(input,expect,351))
    
#     def test52(self):
#             input = """

#     Class Student {
#             findSubject(name : String) {
#                 If (subs.getNameSubject() == name) { Return 1; }
#                 Return 0;
#             }
#             checkLec() {
#                     io.print("\\n----------\\n");
#                     subs.checkLect();
#             }
#             checkFacuSub(facu : String; sub : String) {
#                 If (facul.getNameFaculty() != facu) {Return 0;}
#                 Return self.findSubject(sub);
#             }
#     }"""
#             expect = r"""Program([ClassDecl(Id(Student),[MethodDecl(Id(findSubject),Instance,[param(Id(name),StringType)],Block([If(BinaryOp(==,CallExpr(Id(subs),Id(getNameSubject),[]),Id(name)),Block([Return(IntLit(1))])),Return(IntLit(0))])),MethodDecl(Id(checkLec),Instance,[],Block([Call(Id(io),Id(print),[StringLit(\n----------\n)]),Call(Id(subs),Id(checkLect),[])])),MethodDecl(Id(checkFacuSub),Instance,[param(Id(facu),StringType),param(Id(sub),StringType)],Block([If(BinaryOp(!=,CallExpr(Id(facul),Id(getNameFaculty),[]),Id(facu)),Block([Return(IntLit(0))])),Return(CallExpr(Id(self),Id(findSubject),[Id(sub)]))]))])])"""
#             self.assertTrue(TestParser.test(input, expect, 352))

#     def test53(self):
#         input =  """
# Class mainClass {
#     main() {
    
#     ##=========================ClassROOM===========================//##
#     io.print("\\n=============================================================\\n");
#     io.print("How many Classroom? ");
#     io.getInt(n);
#     sRoom = n;
#     Foreach (i In 1 .. n) {
#         Val name : String;
#         io.print("---------------------------------\\n");
#         io.print("Input details for Classroom " +.  ":\\n");
#         io.print("Input name of Classroom: ");
#         io.fflush(stdin);
#         io.getline(name);
#         ClassR.setNameClassroom(name);
#     }
# }

# }"""
#         expect = r"""Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([Call(Id(io),Id(print),[StringLit(\n=============================================================\n)]),Call(Id(io),Id(print),[StringLit(How many Classroom? )]),Call(Id(io),Id(getInt),[Id(n)]),AssignStmt(Id(sRoom),Id(n)),For(Id(i),IntLit(1),Id(n),Block([ConstDecl(Id(name),StringType,None),Call(Id(io),Id(print),[StringLit(---------------------------------\n)]),Call(Id(io),Id(print),[BinaryOp(+.,StringLit(Input details for Classroom ),StringLit(:\n))]),Call(Id(io),Id(print),[StringLit(Input name of Classroom: )]),Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getline),[Id(name)]),Call(Id(ClassR),Id(setNameClassroom),[Id(name)])]),IntLit(1)])]))])])"""
#         self.assertTrue(TestParser.test(input, expect, 353))
        
#     def test54(self):
#         input = """
# Class mainClass {
#     main() {
#     io.print("\\n=============================================================\\n");
#     io.print("How many Classroom? ");
#     io.getInt(n);
#     sRoom = n;
#     Foreach (i In 1 .. 10 By -b+a) {
#         io.print("---------------------------------\\n");
#         io.print("Input details for Classroom " +. ":\\n");
#         io.print("Input name of Classroom: ");
#         io.fflush(stdin);
#         io.getline(name);
#         ClassR.setNameClassroom(name);
#     }
# }

# }"""
#         expect = r"""Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([Call(Id(io),Id(print),[StringLit(\n=============================================================\n)]),Call(Id(io),Id(print),[StringLit(How many Classroom? )]),Call(Id(io),Id(getInt),[Id(n)]),AssignStmt(Id(sRoom),Id(n)),For(Id(i),IntLit(1),IntLit(10),Block([Call(Id(io),Id(print),[StringLit(---------------------------------\n)]),Call(Id(io),Id(print),[BinaryOp(+.,StringLit(Input details for Classroom ),StringLit(:\n))]),Call(Id(io),Id(print),[StringLit(Input name of Classroom: )]),Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getline),[Id(name)]),Call(Id(ClassR),Id(setNameClassroom),[Id(name)])]),BinaryOp(+,UnaryOp(-,Id(b)),Id(a))])]))])])"""
#         self.assertTrue(TestParser.test(input, expect, 354))
        
#     def test55(self):
#         input = """
# Class display {
#     Val $dis_instance : Float;
#     Var txt : Text;
#     Start()
#     {
#         If (display::$dis_instance == null)  {
#             dis_instance = Self;
#         }
#     }
#     $Display(str: String) {
#         txt.text = str;
#     }
# }"""
#         expect = "Program([ClassDecl(Id(display),[AttributeDecl(Static,ConstDecl(Id($dis_instance),FloatType,None)),AttributeDecl(Instance,VarDecl(Id(txt),ClassType(Id(Text)),NullLiteral())),MethodDecl(Id(Start),Instance,[],Block([If(BinaryOp(==,FieldAccess(Id(display),Id($dis_instance)),Id(null)),Block([AssignStmt(Id(dis_instance),Self())]))])),MethodDecl(Id($Display),Static,[param(Id(str),StringType)],Block([AssignStmt(FieldAccess(Id(txt),Id(text)),Id(str))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 355))
        
#     def test56(self):
#         input = """
# Class skill{
#     Val name : String = "";
#     skill(){
#         If (Self.name == "") 
#            { Self.name = "Skill";}
#     }
#     getName() {
#         Return Self.name;
#     }
#     displayData() {}
# }
# Class factory_skil{
#     $get_skill( i :all_skill ) {
#         If (i == all_skill.FireBall) 
#                 {Return New FireBall();}
#         Elseif (i == all_skill.WaterHealing) 
#                 {Return New WaterHealing();}
#         Elseif (i == all_skill.RockShield )
#                 {Return New RockShield();}
#         Else
#                 {Return New skill();}
#     }
# }
# Class WaterHealing : skill{
#     WaterHealing(){ Self.name = "WaterHealing";}
#     displayData() {
#         display.dis_instance.Display(Self.name);
#     }
# }"""
#         expect = "Program([ClassDecl(Id(skill),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,StringLit())),MethodDecl(Id(skill),Instance,[],Block([If(BinaryOp(==,FieldAccess(Self(),Id(name)),StringLit()),Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(Skill))]))])),MethodDecl(Id(getName),Instance,[],Block([Return(FieldAccess(Self(),Id(name)))])),MethodDecl(Id(displayData),Instance,[],Block([]))]),ClassDecl(Id(factory_skil),[MethodDecl(Id($get_skill),Static,[param(Id(i),ClassType(Id(all_skill)))],Block([If(BinaryOp(==,Id(i),FieldAccess(Id(all_skill),Id(FireBall))),Block([Return(NewExpr(Id(FireBall),[NullLiteral()]))]),If(BinaryOp(==,Id(i),FieldAccess(Id(all_skill),Id(WaterHealing))),Block([Return(NewExpr(Id(WaterHealing),[NullLiteral()]))]),If(BinaryOp(==,Id(i),FieldAccess(Id(all_skill),Id(RockShield))),Block([Return(NewExpr(Id(RockShield),[NullLiteral()]))]),Block([Return(NewExpr(Id(skill),[NullLiteral()]))]))))]))]),ClassDecl(Id(WaterHealing),Id(skill),[MethodDecl(Id(WaterHealing),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(WaterHealing))])),MethodDecl(Id(displayData),Instance,[],Block([Call(FieldAccess(Id(display),Id(dis_instance)),Id(Display),[FieldAccess(Self(),Id(name))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 356))
    
#     def test57(self):
#         input = """
# Class ButtonRun {
#     Var my_skill : skill;
#     InitButton(input_skill : Skill) {
#         Self.my_skill = input_skill;
#         txt.text = my_skill.getName();
#     }
#     clickButton() {
#         my_skill.displayData();
#     }
# }
# Class manager_skill {
#     Val list_button :ButtonRun;
#     manager_skill(all_skill : i) {
#         list_button.InitButton(factory_skill.get_skill(i));
#     }
# }"""
#         expect = "Program([ClassDecl(Id(ButtonRun),[AttributeDecl(Instance,VarDecl(Id(my_skill),ClassType(Id(skill)),NullLiteral())),MethodDecl(Id(InitButton),Instance,[param(Id(input_skill),ClassType(Id(Skill)))],Block([AssignStmt(FieldAccess(Self(),Id(my_skill)),Id(input_skill)),AssignStmt(FieldAccess(Id(txt),Id(text)),CallExpr(Id(my_skill),Id(getName),[]))])),MethodDecl(Id(clickButton),Instance,[],Block([Call(Id(my_skill),Id(displayData),[])]))]),ClassDecl(Id(manager_skill),[AttributeDecl(Instance,ConstDecl(Id(list_button),ClassType(Id(ButtonRun)),NullLiteral())),MethodDecl(Id(manager_skill),Instance,[param(Id(all_skill),ClassType(Id(i)))],Block([Call(Id(list_button),Id(InitButton),[CallExpr(Id(factory_skill),Id(get_skill),[Id(i)])])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 357))
        
#     def test58(self):
#         input = """
#         Class a {
#                 Var r, s: Int;
#                 x() {
#                     a = 2.0;
#                     Var a, b: Array[Int, 5];
#                     s = r * r * Self.myPI;
#                     a[0] = s;
#                     }
#         }"""
#         expect = "Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),MethodDecl(Id(x),Instance,[],Block([AssignStmt(Id(a),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
#         self.assertTrue(TestParser.test(input,expect,358))
#     def test59(self):
#         input = """
# Class Bank {
#     Val bankName : String;

#     doSomething()
#     {
#         ####
#     }
# } 
# Class Vietcombank : Bank{
#     Student(ID : Int; name: String) {
#             Self.studentID = ID;
#             Self.name = name;
#             numOfGrade = 0;
#             sumMark = 0;
#         }
#         insertGrade( nameOfCourse: String;  mark : Int) {
#             grades.setName(nameOfCourse);
#             grades.setMark(mark);
#             numOfGrade = numOfGrade+1;
#             sumMark = sumMark+ mark;
#         }
#         setName(name : String) { Self.nameOfCourse = name; }
#         setMark()  { Self.mark = mark;}
#         getMark()      { Return mark; }
# }"""
#         expect = "Program([ClassDecl(Id(Bank),[AttributeDecl(Instance,ConstDecl(Id(bankName),StringType,None)),MethodDecl(Id(doSomething),Instance,[],Block([]))]),ClassDecl(Id(Vietcombank),Id(Bank),[MethodDecl(Id(Student),Instance,[param(Id(ID),IntType),param(Id(name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(studentID)),Id(ID)),AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(Id(numOfGrade),IntLit(0)),AssignStmt(Id(sumMark),IntLit(0))])),MethodDecl(Id(insertGrade),Instance,[param(Id(nameOfCourse),StringType),param(Id(mark),IntType)],Block([Call(Id(grades),Id(setName),[Id(nameOfCourse)]),Call(Id(grades),Id(setMark),[Id(mark)]),AssignStmt(Id(numOfGrade),BinaryOp(+,Id(numOfGrade),IntLit(1))),AssignStmt(Id(sumMark),BinaryOp(+,Id(sumMark),Id(mark)))])),MethodDecl(Id(setName),Instance,[param(Id(name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(nameOfCourse)),Id(name))])),MethodDecl(Id(setMark),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(mark)),Id(mark))])),MethodDecl(Id(getMark),Instance,[],Block([Return(Id(mark))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 359))

#     def test360(self):
#         input = """
# Class io {
#     $getInt() {
#         data = (system.checkIntLitForm(system.getIO())).toInt();
#         a = data;
#     }
#     getFloat(a : Float) {
#         data = (system.checkFloatLitForm(system.getIO())).toFloat();
#         a = data;
#     }    
# }"""
#         expect = "Program([ClassDecl(Id(io),[MethodDecl(Id($getInt),Static,[],Block([AssignStmt(Id(data),CallExpr(CallExpr(Id(system),Id(checkIntLitForm),[CallExpr(Id(system),Id(getIO),[])]),Id(toInt),[])),AssignStmt(Id(a),Id(data))])),MethodDecl(Id(getFloat),Instance,[param(Id(a),FloatType)],Block([AssignStmt(Id(data),CallExpr(CallExpr(Id(system),Id(checkFloatLitForm),[CallExpr(Id(system),Id(getIO),[])]),Id(toFloat),[])),AssignStmt(Id(a),Id(data))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 360))
#     def test61(self):
#         input = """
# Class heap {
# minWaitingTime(n : Int;arrvalTime : Array[Int, 1]) {
#     Val curTime : Int = 0;
#     Var totalWaitTime : Int = 0;

#     Return totalWaitTime;   
# }
# }"""
#         expect = "Program([ClassDecl(Id(heap),[MethodDecl(Id(minWaitingTime),Instance,[param(Id(n),IntType),param(Id(arrvalTime),ArrayType(1,IntType))],Block([ConstDecl(Id(curTime),IntType,IntLit(0)),VarDecl(Id(totalWaitTime),IntType,IntLit(0)),Return(Id(totalWaitTime))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 361))

#     def test62(self):
#         input = """
# Class makeSchool {
#      main() {
#         Foreach (i In 10 .. 1 By 2) {
#             Val new_Class : String;
#             io.fflush(stdin);
#             io.getline(new_Class);
#             If (new_Class != "-1") 
#                 { School.updateClass(new_Class); }
#             Else { Break; }
#         }
#     }
#      getNext() {
#         Return next;
#     }
    
# }"""
#         expect = "Program([ClassDecl(Id(makeSchool),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(10),IntLit(1),Block([ConstDecl(Id(new_Class),StringType,None),Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getline),[Id(new_Class)]),If(BinaryOp(!=,Id(new_Class),StringLit(-1)),Block([Call(Id(School),Id(updateClass),[Id(new_Class)])]),Block([Break]))]),IntLit(2)])])),MethodDecl(Id(getNext),Instance,[],Block([Return(Id(next))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 362))

#     def test63(self):
#         input = """
#                 Class a {
#                 Var r, s: Int = 1, 0;
                
#                 main(){
#                     Val a, b: Float = 1.5E10, -10.;
#                 }
               
#         }
#                 """
#         expect = "Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(r),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(s),IntType,IntLit(0))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),FloatType,FloatLit(15000000000.0)),ConstDecl(Id(b),FloatType,UnaryOp(-,FloatLit(10.0)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 363))
#     def test64(self):
#         input = """
# Class linked_list {
#     Val $node : start;
#     linked_list(node: s) {
#         Self.start = s;
#     }
#     $getNode(index: Int; node : n) {
#         If (index == 0) 
#             { Return n; }
#         Else
#            { Return Self.getNode(index - 1, n.getNext()); }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(linked_list),[AttributeDecl(Static,ConstDecl(Id($node),ClassType(Id(start)),NullLiteral())),MethodDecl(Id(linked_list),Instance,[param(Id(node),ClassType(Id(s)))],Block([AssignStmt(FieldAccess(Self(),Id(start)),Id(s))])),MethodDecl(Id($getNode),Static,[param(Id(index),IntType),param(Id(node),ClassType(Id(n)))],Block([If(BinaryOp(==,Id(index),IntLit(0)),Block([Return(Id(n))]),Block([Return(CallExpr(Self(),Id(getNode),[BinaryOp(-,Id(index),IntLit(1)),CallExpr(Id(n),Id(getNext),[])]))]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 364))
#     def test65(self):
#         input = """
# Class mainFuncion {
#     insert () {
#         If (index == 0) 
#            { n.setNext(root.getNext());}
#         Else 
#            { Self.insert(index - 1, root.getNext(), n)[Math.ceil(10, 5)[iphone.get()]] = 1; }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(mainFuncion),[MethodDecl(Id(insert),Instance,[],Block([If(BinaryOp(==,Id(index),IntLit(0)),Block([Call(Id(n),Id(setNext),[CallExpr(Id(root),Id(getNext),[])])]),Block([AssignStmt(ArrayCell(CallExpr(Self(),Id(insert),[BinaryOp(-,Id(index),IntLit(1)),CallExpr(Id(root),Id(getNext),[]),Id(n)]),[ArrayCell(CallExpr(Id(Math),Id(ceil),[IntLit(10),IntLit(5)]),[CallExpr(Id(iphone),Id(get),[])])]),IntLit(1))]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 365))
#     def test66(self):
#         input = """
# Class tesster {
#     getCaculatorInt() {
#         arr = Array(1, a - b, a * bb);
#     }
# }"""
#         expect = "Program([ClassDecl(Id(tesster),[MethodDecl(Id(getCaculatorInt),Instance,[],Block([AssignStmt(Id(arr),[IntLit(1),BinaryOp(-,Id(a),Id(b)),BinaryOp(*,Id(a),Id(bb))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 366))
#     def test67(self):
#         input = """
# Class tesster {
#     getCaculatorInt() {
#         arr1sd = Array(a + b, a - b, a * b, a % b, a / b);
#     }
# }"""
#         expect = "Program([ClassDecl(Id(tesster),[MethodDecl(Id(getCaculatorInt),Instance,[],Block([AssignStmt(Id(arr1sd),[BinaryOp(+,Id(a),Id(b)),BinaryOp(-,Id(a),Id(b)),BinaryOp(*,Id(a),Id(b)),BinaryOp(%,Id(a),Id(b)),BinaryOp(/,Id(a),Id(b))])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 367))
#     def test68(self):
#         input = """
# Class tesster {
#     $getCaculatorInt(a,b : Int) {
#         a132 = a + b;
#         a2 = a- b;
#         arr = Array(a1,a2,a3,a4,a5);
#     }
# }"""
#         expect = "Program([ClassDecl(Id(tesster),[MethodDecl(Id($getCaculatorInt),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(Id(a132),BinaryOp(+,Id(a),Id(b))),AssignStmt(Id(a2),BinaryOp(-,Id(a),Id(b))),AssignStmt(Id(arr),[Id(a1),Id(a2),Id(a3),Id(a4),Id(a5)])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 368))
#     def test69(self):
#         input = """
# Class mainFuncion {
#      insert () {
#         If (index == 0) {
#             root.setNext(n);
#             If (index == 0)
#            { n.setNext(root.getNext());}
#         Else 
#             { test.insert(index - 1, root.getNext(), n); }
#         }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(mainFuncion),[MethodDecl(Id(insert),Instance,[],Block([If(BinaryOp(==,Id(index),IntLit(0)),Block([Call(Id(root),Id(setNext),[Id(n)]),If(BinaryOp(==,Id(index),IntLit(0)),Block([Call(Id(n),Id(setNext),[CallExpr(Id(root),Id(getNext),[])])]),Block([Call(Id(test),Id(insert),[BinaryOp(-,Id(index),IntLit(1)),CallExpr(Id(root),Id(getNext),[]),Id(n)])]))]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 369))
#     def test70(self):
#         input = """
# Class getStudent {
#      main() {
#         io.getInt(n);
#         Foreach (i In 0 .. n) {
#             io.fflush(stdin);
#             io.getBoolean(option);
#             new_student = (School.getNameClass(range.random() % School.num_Class)).getStudent(name,id,option);
#             lass.updateStudent(new_student);
#         }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(getStudent),[MethodDecl(Id(main),Instance,[],Block([Call(Id(io),Id(getInt),[Id(n)]),For(Id(i),IntLit(0),Id(n),Block([Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getBoolean),[Id(option)]),AssignStmt(Id(new_student),CallExpr(CallExpr(Id(School),Id(getNameClass),[BinaryOp(%,CallExpr(Id(range),Id(random),[]),FieldAccess(Id(School),Id(num_Class)))]),Id(getStudent),[Id(name),Id(id),Id(option)])),Call(Id(lass),Id(updateStudent),[Id(new_student)])]),IntLit(1)])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 370))

#     def test71(self):
#         input = """
#         Class x {
#             x() {
#                 If (b < a[2][4*b]) {}
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(x),[MethodDecl(Id(x),Instance,[],Block([If(BinaryOp(<,Id(b),ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[BinaryOp(*,IntLit(4),Id(b))])),Block([]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,371))
#     def test72(self):
#         input = """
# Class special_student : student {
#     Val list_skill_special : Array[String, 100];
#     Val num_skill : Int;
#     special_student(c : Classssss) {
#         Self.student(name, id, c);
#         num_skill = 0;
#         }
#     updateSkill(skill : String) {
#         Self.list_skill_special[123] = skill; 
#         num_skill = num_skill + 1;
#     }
    
# }"""
#         expect = "Program([ClassDecl(Id(special_student),Id(student),[AttributeDecl(Instance,ConstDecl(Id(list_skill_special),ArrayType(100,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(num_skill),IntType,None)),MethodDecl(Id(special_student),Instance,[param(Id(c),ClassType(Id(Classssss)))],Block([Call(Self(),Id(student),[Id(name),Id(id),Id(c)]),AssignStmt(Id(num_skill),IntLit(0))])),MethodDecl(Id(updateSkill),Instance,[param(Id(skill),StringType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(list_skill_special)),[IntLit(123)]),Id(skill)),AssignStmt(Id(num_skill),BinaryOp(+,Id(num_skill),IntLit(1)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 372))
#     def test73(self):
#         input = """
# Class  Classs {
    
#     getdStudent() {
#         If (option == True) 
#             { Return New special_student(name,id,c);}
#     }
# }"""
#         expect = "Program([ClassDecl(Id(special_student),Id(student),[AttributeDecl(Instance,ConstDecl(Id(list_skill_special),ArrayType(100,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(num_skill),IntType,None)),MethodDecl(Id(special_student),Instance,[param(Id(c),ClassType(Id(Classssss)))],Block([Call(Self(),Id(student),[Id(name),Id(id),Id(c)]),AssignStmt(Id(num_skill),IntLit(0))])),MethodDecl(Id(updateSkill),Instance,[param(Id(skill),StringType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(list_skill_special)),[IntLit(123)]),Id(skill)),AssignStmt(Id(num_skill),BinaryOp(+,Id(num_skill),IntLit(1)))]))])])"
#     def test74(self):
#         input = """
# Class School {
#     Val  $Class_name : Array[Int, 20];
#     $getNumClass() {
#         Return num_Class;
#     }
#     $updateClass(name : String) {
#         Class_name[num_Class] = name;
#         num_Class = num_Class + 1;
#     }
#     setData(data : Int) {    }
# }"""
#         expect = "Program([ClassDecl(Id(School),[AttributeDecl(Static,ConstDecl(Id($Class_name),ArrayType(20,IntType),None)),MethodDecl(Id($getNumClass),Static,[],Block([Return(Id(num_Class))])),MethodDecl(Id($updateClass),Static,[param(Id(name),StringType)],Block([AssignStmt(ArrayCell(Id(Class_name),[Id(num_Class)]),Id(name)),AssignStmt(Id(num_Class),BinaryOp(+,Id(num_Class),IntLit(1)))])),MethodDecl(Id(setData),Instance,[param(Id(data),IntType)],Block([]))])])"
#         self.assertTrue(TestParser.test(input, expect, 374))
#     def test75(self):
#         input = """
# Class makeSchool {
#         secondary(a : Int) {
#             io.fflush(stdin);
#             io.getline(lass);
#             If (lass != "-1") 
#                 {School.updateClass(lass);}
#             Else { Break;}
#         }
#     setNext(next : Node) {
#         Self.next = next;
#     }
# }"""
#         expect = "Program([ClassDecl(Id(makeSchool),[MethodDecl(Id(secondary),Instance,[param(Id(a),IntType)],Block([Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getline),[Id(lass)]),If(BinaryOp(!=,Id(lass),StringLit(-1)),Block([Call(Id(School),Id(updateClass),[Id(lass)])]),Block([Break]))])),MethodDecl(Id(setNext),Instance,[param(Id(next),ClassType(Id(Node)))],Block([AssignStmt(FieldAccess(Self(),Id(next)),Id(next))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 375))
        
#     def test76(self):
#         input = """
# Class heap {
#  minWaitingTime(arr: Array[Int, 10]) {
#      curTime = 0;

#     Return totalWaitTime;   

     
#             If ((curTime >= arrvalTime[i]) && ((serCos == -1) || (serTime > completeTime[i]))) {
#                     serCos = i;
#                     serTime = completeTime[i];
#             }
#             If ((min == -1) || (min > arrvalTime[i])) { min = arrvalTime[i]; }
#         Else    { curTime = min; }
#         If (n < 0) { Break; }
    
# }

# }"""
#         expect = "Program([ClassDecl(Id(heap),[MethodDecl(Id(minWaitingTime),Instance,[param(Id(arr),ArrayType(10,IntType))],Block([AssignStmt(Id(curTime),IntLit(0)),Return(Id(totalWaitTime)),If(BinaryOp(&&,BinaryOp(>=,Id(curTime),ArrayCell(Id(arrvalTime),[Id(i)])),BinaryOp(||,BinaryOp(==,Id(serCos),UnaryOp(-,IntLit(1))),BinaryOp(>,Id(serTime),ArrayCell(Id(completeTime),[Id(i)])))),Block([AssignStmt(Id(serCos),Id(i)),AssignStmt(Id(serTime),ArrayCell(Id(completeTime),[Id(i)]))])),If(BinaryOp(||,BinaryOp(==,Id(min),UnaryOp(-,IntLit(1))),BinaryOp(>,Id(min),ArrayCell(Id(arrvalTime),[Id(i)]))),Block([AssignStmt(Id(min),ArrayCell(Id(arrvalTime),[Id(i)]))]),Block([AssignStmt(Id(curTime),Id(min))])),If(BinaryOp(<,Id(n),IntLit(0)),Block([Break]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 376))
        
#     def test77(self):
#         input = """
# Class heap {
#  minWaitingTime() {
#      curTime = 0;
#     Return totalWaitTime;   
# }
#  main() {
#     {
#          n = 3;
#         arrvalTime = Array();
#         completeTime = Array(3, 9, 6, 10, 8);

#         io.pr(this.minWaitingTime(n, arrvalTime, completeTime));
#     }
#     io.pr(endl);
# }
# }"""
#         expect = "Program([ClassDecl(Id(heap),[MethodDecl(Id(minWaitingTime),Instance,[],Block([AssignStmt(Id(curTime),IntLit(0)),Return(Id(totalWaitTime))])),MethodDecl(Id(main),Instance,[],Block([Block([AssignStmt(Id(n),IntLit(3)),AssignStmt(Id(arrvalTime),[]),AssignStmt(Id(completeTime),[IntLit(3),IntLit(9),IntLit(6),IntLit(10),IntLit(8)]),Call(Id(io),Id(pr),[CallExpr(Id(this),Id(minWaitingTime),[Id(n),Id(arrvalTime),Id(completeTime)])])]),Call(Id(io),Id(pr),[Id(endl)])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 377))
#     def test78(self):
#         input = """
# Class student {
#     Val $num_student: Int;
#     Var $name : String;
#     getSkill() {
#         Return list_skill_special;
#     }
#     getNumStudent() {
#         Return CLASS::$num_student;
#     }
# }"""
#         expect = "Program([ClassDecl(Id(student),[AttributeDecl(Static,ConstDecl(Id($num_student),IntType,None)),AttributeDecl(Static,VarDecl(Id($name),StringType)),MethodDecl(Id(getSkill),Instance,[],Block([Return(Id(list_skill_special))])),MethodDecl(Id(getNumStudent),Instance,[],Block([Return(FieldAccess(Id(CLASS),Id($num_student)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 378))
#     def test79(self):
#         input = """
# Class mainClass {
#  main() {
  
#     io.print("Enter number of Students? ");
#     io.getInt(n);
#         ## GET INFORMATION ##
#         io.print("Input details for Student " +. ":\\n");
#         students.insertGrade(nameMark, mark);
#     n = 1;
#     ## GET AVERAGE  ##
    
#     Return 0;
# }
# }"""
#         expect = r"""Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([Call(Id(io),Id(print),[StringLit(Enter number of Students? )]),Call(Id(io),Id(getInt),[Id(n)]),Call(Id(io),Id(print),[BinaryOp(+.,StringLit(Input details for Student ),StringLit(:\n))]),Call(Id(students),Id(insertGrade),[Id(nameMark),Id(mark)]),AssignStmt(Id(n),IntLit(1)),Return(IntLit(0))]))])])"""
#         self.assertTrue(TestParser.test(input, expect, 379))
#     def test80(self):
#         input = """
# Class mainClass {
#     $getline(a : String) {
#         test = system.getIO();
#         a = "";
#         Foreach (i In 1 .. (a+b) ) {
#             a = a+.test;
#             test = system.getIO();
#             If (test == "\\n") { Break; }
#             Else  { Continue; }
#         }
#     }
#     $fflush(s : typeIO) {
#         If (s == stdin) {system.clear_console(); }
#     }
# $main() {
#     io.print("Enter number of Students? ");
#     io.getInt(n);
#         ##GET INFORMATION ##
#         io.print("Input details for Student " +. ":\\n");
#         students.push(New Student(ID, name));

    
#     Return 0;
# }
# }"""
#         expect = r"""Program([ClassDecl(Id(mainClass),[MethodDecl(Id($getline),Static,[param(Id(a),StringType)],Block([AssignStmt(Id(test),CallExpr(Id(system),Id(getIO),[])),AssignStmt(Id(a),StringLit()),For(Id(i),IntLit(1),BinaryOp(+,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+.,Id(a),Id(test))),AssignStmt(Id(test),CallExpr(Id(system),Id(getIO),[])),If(BinaryOp(==,Id(test),StringLit(\n)),Block([Break]),Block([Continue]))]),IntLit(1)])])),MethodDecl(Id($fflush),Static,[param(Id(s),ClassType(Id(typeIO)))],Block([If(BinaryOp(==,Id(s),Id(stdin)),Block([Call(Id(system),Id(clear_console),[])]))])),MethodDecl(Id($main),Static,[],Block([Call(Id(io),Id(print),[StringLit(Enter number of Students? )]),Call(Id(io),Id(getInt),[Id(n)]),Call(Id(io),Id(print),[BinaryOp(+.,StringLit(Input details for Student ),StringLit(:\n))]),Call(Id(students),Id(push),[NewExpr(Id(Student),[Id(ID),Id(name)])]),Return(IntLit(0))]))])])"""
#         self.assertTrue(TestParser.test(input, expect, 380))
        
#     def test81(self):
#         input = """
# Class Grade {
        
#         Grade() {
#             nameOfCourse = "";
#             mark = 0;
#         }
#         Grade() {
#             Val num : Int = 10;
#         }
# }"""
#         expect = "Program([ClassDecl(Id(Grade),[MethodDecl(Id(Grade),Instance,[],Block([AssignStmt(Id(nameOfCourse),StringLit()),AssignStmt(Id(mark),IntLit(0))])),MethodDecl(Id(Grade),Instance,[],Block([ConstDecl(Id(num),IntType,IntLit(10))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 381))
#     def test82(self):
#         input = """
# Class Student {
#         Val studentID : Int;
#         getAverage()  {
#             Return sumMark / numOfGrade;
#         }
# }"""
#         expect = "Program([ClassDecl(Id(Student),[AttributeDecl(Instance,ConstDecl(Id(studentID),IntType,None)),MethodDecl(Id(getAverage),Instance,[],Block([Return(BinaryOp(/,Id(sumMark),Id(numOfGrade)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 382))
#     def test83(self):
#         input = """
#         Class a : _class {
#             Var $x: Float = 1.03;
#         }"""
#         expect = "Program([ClassDecl(Id(a),Id(_class),[AttributeDecl(Static,VarDecl(Id($x),FloatType,FloatLit(1.03)))])])"
#         self.assertTrue(TestParser.test(input,expect,383))
#     def test84(self):
#             input = """
#     ## LECTURER ##

#     Class Lecturer {
           
# Lecturer(n : String)  { name=n; }
#             Lecturer(n : String; f : Faculty) { name = n; lecFaculty = f; }
#             getNameFacultyOfLecturer() { Return lecFaculty.getNameFaculty(); }
#             setNameFacultyOfLecturer(n : String) { lecFaculty.setNameFaculty(n); }
#     }

#     ## ClassROOM ##

#     Class Classroom {
#             Constructor(n : String) { nameRoom=n;}
#              getNameClassroom() { Return nameRoom; }
#              setNameClassroom(n : String) { nameRoom = n; }
#     }"""
#             expect = "Program([ClassDecl(Id(Lecturer),[MethodDecl(Id(Lecturer),Instance,[param(Id(n),StringType)],Block([AssignStmt(Id(name),Id(n))])),MethodDecl(Id(Lecturer),Instance,[param(Id(n),StringType),param(Id(f),ClassType(Id(Faculty)))],Block([AssignStmt(Id(name),Id(n)),AssignStmt(Id(lecFaculty),Id(f))])),MethodDecl(Id(getNameFacultyOfLecturer),Instance,[],Block([Return(CallExpr(Id(lecFaculty),Id(getNameFaculty),[]))])),MethodDecl(Id(setNameFacultyOfLecturer),Instance,[param(Id(n),StringType)],Block([Call(Id(lecFaculty),Id(setNameFaculty),[Id(n)])]))]),ClassDecl(Id(Classroom),[MethodDecl(Id(Constructor),Instance,[param(Id(n),StringType)],Block([AssignStmt(Id(nameRoom),Id(n))])),MethodDecl(Id(getNameClassroom),Instance,[],Block([Return(Id(nameRoom))])),MethodDecl(Id(setNameClassroom),Instance,[param(Id(n),StringType)],Block([AssignStmt(Id(nameRoom),Id(n))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 384))
#     def test85(self):
#             input = """
#             Class Test{
#                Var ins: Int;
#                Var $static: Int;
               
#                Test(){
#                   Var a: Int= Self.ins;
#                   Var b: Int= A::$static;
#                }
#             }
#       """
#             expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(ins),IntType)),AttributeDecl(Static,VarDecl(Id($static),IntType)),MethodDecl(Id(Test),Instance,[],Block([VarDecl(Id(a),IntType,FieldAccess(Self(),Id(ins))),VarDecl(Id(b),IntType,FieldAccess(Id(A),Id($static)))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 385))
#     def test86(self):
#             input = """
#     Class Subject {
            
#             Subject(n : String; number: Int) { name=n; sLec=0;}
#             getNameSubject() { Return name; }
#             setNameSubject(n : String) { name = n; }
#             inputData() {
               
#                 io.print("---------------\\n");
#                 io.print("Input name of Subject: ");
#                 io.fflush(stdin);
#                 io.getline(n);
#                 name = n;
#             }
           
#     }"""
#             expect = r"""Program([ClassDecl(Id(Subject),[MethodDecl(Id(Subject),Instance,[param(Id(n),StringType),param(Id(number),IntType)],Block([AssignStmt(Id(name),Id(n)),AssignStmt(Id(sLec),IntLit(0))])),MethodDecl(Id(getNameSubject),Instance,[],Block([Return(Id(name))])),MethodDecl(Id(setNameSubject),Instance,[param(Id(n),StringType)],Block([AssignStmt(Id(name),Id(n))])),MethodDecl(Id(inputData),Instance,[],Block([Call(Id(io),Id(print),[StringLit(---------------\n)]),Call(Id(io),Id(print),[StringLit(Input name of Subject: )]),Call(Id(io),Id(fflush),[Id(stdin)]),Call(Id(io),Id(getline),[Id(n)]),AssignStmt(Id(name),Id(n))]))])])"""
#             self.assertTrue(TestParser.test(input, expect, 386))

#     def test87(self):
#             input = """
#     Class drop_victim {
#         Var count_time : Float = 0;
#     changeState() {
#             checkRun = !checkRun;
#         }
#         ## FUNCTION FOR SKILL AND FIRE BULLET ##
#          create_button_skill() {
#             system.Instantiate(button_skill, New Vector3(-6.5,-4,0), transform.rotation);
#         }
#          create_skill() {
#             can_skill = false;
#             have_button = false;
#             system.Instantiate(water_skill, New Vector3(-10,0,0), transform.rotation);  
#             skill_Audio.Play(0);   
#         }
#          shootWater() {
#             Foreach (i In 0 .. num_bullet) {
#                 system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
#                 shoot_Audio.Play(0);       
#             }
#         }
#         Update()
#         {
#             If (count_time < 5) { transform.position = transform.position + New Vector3(0.5, 0.2, 0);}
#             Else { transform.position = transform.position + New Vector3(0.5, -0.1, 0);}
#         }
#     }       """
#             expect = "Program([ClassDecl(Id(drop_victim),[AttributeDecl(Instance,VarDecl(Id(count_time),FloatType,IntLit(0))),MethodDecl(Id(changeState),Instance,[],Block([AssignStmt(Id(checkRun),UnaryOp(!,Id(checkRun)))])),MethodDecl(Id(create_button_skill),Instance,[],Block([Call(Id(system),Id(Instantiate),[Id(button_skill),NewExpr(Id(Vector3),[UnaryOp(-,FloatLit(6.5)),UnaryOp(-,IntLit(4)),IntLit(0)]),FieldAccess(Id(transform),Id(rotation))])])),MethodDecl(Id(create_skill),Instance,[],Block([AssignStmt(Id(can_skill),Id(false)),AssignStmt(Id(have_button),Id(false)),Call(Id(system),Id(Instantiate),[Id(water_skill),NewExpr(Id(Vector3),[UnaryOp(-,IntLit(10)),IntLit(0),IntLit(0)]),FieldAccess(Id(transform),Id(rotation))]),Call(Id(skill_Audio),Id(Play),[IntLit(0)])])),MethodDecl(Id(shootWater),Instance,[],Block([For(Id(i),IntLit(0),Id(num_bullet),Block([Call(Id(system),Id(Instantiate),[Id(bullet_water),FieldAccess(Id(fire_point),Id(position)),FieldAccess(Id(fire_point),Id(rotation))]),Call(Id(shoot_Audio),Id(Play),[IntLit(0)])]),IntLit(1)])])),MethodDecl(Id(Update),Instance,[],Block([If(BinaryOp(<,Id(count_time),IntLit(5)),Block([AssignStmt(FieldAccess(Id(transform),Id(position)),BinaryOp(+,FieldAccess(Id(transform),Id(position)),NewExpr(Id(Vector3),[FloatLit(0.5),FloatLit(0.2),IntLit(0)])))]),Block([AssignStmt(FieldAccess(Id(transform),Id(position)),BinaryOp(+,FieldAccess(Id(transform),Id(position)),NewExpr(Id(Vector3),[FloatLit(0.5),UnaryOp(-,FloatLit(0.1)),IntLit(0)])))]))]))])])"
#             self.assertTrue(TestParser.test(input, expect, 387))
            
#     def test88(self):
#         input = """
# Class smoke_run : MonoBehaviour{
#     Val speed : Int = 5;
#     Var counter : Float = 0;
#     Var scaleChange : Vector3;
#     $FixedUpdate()
#     {
#         transform.localScale = transform.localScale + scaleChange;
#         If (counter == 100) {
#         }
#     }
# }"""
#         expect = "Program([ClassDecl(Id(smoke_run),Id(MonoBehaviour),[AttributeDecl(Instance,ConstDecl(Id(speed),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(counter),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(scaleChange),ClassType(Id(Vector3)),NullLiteral())),MethodDecl(Id($FixedUpdate),Static,[],Block([AssignStmt(FieldAccess(Id(transform),Id(localScale)),BinaryOp(+,FieldAccess(Id(transform),Id(localScale)),Id(scaleChange))),If(BinaryOp(==,Id(counter),IntLit(100)),Block([]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 388))
        
#     def test89(self):
#         input = """
#         Class UnExp : Exp {
#             Val op : String;
#             Val value : Float;
#             UnExp(op : String;value : Float) {
#                 Self.value = value;
#             }
#             eval() {
#                 If (op == "+") {Return value; }
#                 Else {Return value * (-1);}
#             }
#             create_skill() {
#         can_skill = false;
#         have_button = false;
#         system.Instantiate(water_skill, New Vector3(-10,0,0), transform::$rotation);  
#         skill_Audio.Play(0);   
#     }
#      shootWater() {
        
#     }
#         }"""
#         expect = "Program([ClassDecl(Id(UnExp),Id(Exp),[AttributeDecl(Instance,ConstDecl(Id(op),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(value),FloatType,None)),MethodDecl(Id(UnExp),Instance,[param(Id(op),StringType),param(Id(value),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(value)),Id(value))])),MethodDecl(Id(eval),Instance,[],Block([If(BinaryOp(==,Id(op),StringLit(+)),Block([Return(Id(value))]),Block([Return(BinaryOp(*,Id(value),UnaryOp(-,IntLit(1))))]))])),MethodDecl(Id(create_skill),Instance,[],Block([AssignStmt(Id(can_skill),Id(false)),AssignStmt(Id(have_button),Id(false)),Call(Id(system),Id(Instantiate),[Id(water_skill),NewExpr(Id(Vector3),[UnaryOp(-,IntLit(10)),IntLit(0),IntLit(0)]),FieldAccess(Id(transform),Id($rotation))]),Call(Id(skill_Audio),Id(Play),[IntLit(0)])])),MethodDecl(Id(shootWater),Instance,[],Block([]))])])"
#         self.assertTrue(TestParser.test(input, expect, 389))
        
#     def test90(self):
#         input = """
#         ## class parent ##
#         Class Exp {
#             eval() {}
#         }
#         ## class intlit and floatlit ##
#         Class IntLit : Exp {
#             Val value : Int;
#             Intlit(a : Int) {
#                 Self.value = a;
#             }
#             eval() {
#                 Return Self.value;
#             }
#         }
#         ## Class floatlit and floatlit##
#         Class FloatLit : Exp {
#             Val value : Float;
#             Constructor(a : Float) {
#                 Self.value = a;
#             }
#             eval() {
#                 Return Self.value;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Exp),[MethodDecl(Id(eval),Instance,[],Block([]))]),ClassDecl(Id(IntLit),Id(Exp),[AttributeDecl(Instance,ConstDecl(Id(value),IntType,None)),MethodDecl(Id(Intlit),Instance,[param(Id(a),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(value)),Id(a))])),MethodDecl(Id(eval),Instance,[],Block([Return(FieldAccess(Self(),Id(value)))]))]),ClassDecl(Id(FloatLit),Id(Exp),[AttributeDecl(Instance,ConstDecl(Id(value),FloatType,None)),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(value)),Id(a))])),MethodDecl(Id(eval),Instance,[],Block([Return(FieldAccess(Self(),Id(value)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 390))
        
#     def test91(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = b + 1.2e12 + 0X1232_32_3;}
#                 Else{
#                     Val a: Float = 1.2;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(b),FloatLit(1200000000000.0)),IntLit(19079971)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(1.2))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,391))
#     def test92(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = 0b0 + 0x0 + 0X1232_32_3;}
#                 Else{
#                     Val a: Float = 1.2;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(19079971)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(1.2))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,392))
#     def test93(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = 00 + 0124 + 0xAFFF;}
#                 Else{
#                     Val a: Float = 1.2;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(84)),IntLit(45055)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(1.2))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,393))
#     def test94(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = 0B0 + 0b1010100 + 0b1010111111111111;}
#                 Else{
#                     Val a: Float = 1.2;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(84)),IntLit(45055)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(1.2))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,394))
#     def test95(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = 0B0 + 0 + 0b0 + 0x0 + 0X0 + 00;}
#                 Else{
#                     Val a: Float = 1.2;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(1.2))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,395))
#     def test96(self):
#         input = """
#         Class Shape {
#             Shape(length: Float){
#                 If (True) {a = 0b1000_0001_00 - 0XABCDEF + 052746757;}
#                 Else{
#                     Val a: Float = 2_12414_5.e1;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType)],Block([If(BooleanLit(True),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,IntLit(516),IntLit(11259375)),IntLit(11259375)))]),Block([ConstDecl(Id(a),FloatType,FloatLit(21241450.0))]))]))])])"
#         self.assertTrue(TestParser.test(input,expect,396))

#     def test97(self):
#         input = """
#         Class mainClass {
#             main() {
#                 Var c1 : C1 = New C1();
#                 Var c3 : C3 = New C3("abc" +. c1);
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(c1),ClassType(Id(C1)),NewExpr(Id(C1),[NullLiteral()])),VarDecl(Id(c3),ClassType(Id(C3)),NewExpr(Id(C3),[BinaryOp(+.,StringLit(abc),Id(c1))]))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 397))
#     def test98(self):
#         input = """
#         Class mainClass {
#             main() {
#                 Val c3 : C3 = New C3("abc",c1, 123_000.e-1, 0XA123);
#                 c3.checkName("abcd");
#                 io.Print(c3.getName(0.e10));
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(mainClass),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c3),ClassType(Id(C3)),NewExpr(Id(C3),[StringLit(abc),Id(c1),FloatLit(12300.0),IntLit(41251)])),Call(Id(c3),Id(checkName),[StringLit(abcd)]),Call(Id(io),Id(Print),[CallExpr(Id(c3),Id(getName),[FloatLit(0.0)])])]))])])"
#         self.assertTrue(TestParser.test(input, expect, 398))

#     def test99(self):
#         input = """
#         Class checkExp {
#             check1(a,b,c : Boolean ) {
#                 a1 = ((a > b) > c) == "True";
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(checkExp),[MethodDecl(Id(check1),Instance,[param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType)],Block([AssignStmt(Id(a1),BinaryOp(==,BinaryOp(>,BinaryOp(>,Id(a),Id(b)),Id(c)),StringLit(True)))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 399))
        
#     def test100(self):
#         input = """
#         Class checkExp {
#             check1(boolean, a,b,c : Boolean) {
#                 a1 = (a > (b > c)) <= boolean;
#                 a = 00;
#                 b = 0707;
#                 c = 0xAF12;
#                 d = 0b10110101;
#                ## b2 = 00 + 0707 + 0xAF12 + 0b00110101;##
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(checkExp),[MethodDecl(Id(check1),Instance,[param(Id(boolean),BoolType),param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType)],Block([AssignStmt(Id(a1),BinaryOp(<=,BinaryOp(>,Id(a),BinaryOp(>,Id(b),Id(c))),Id(boolean))),AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(455)),AssignStmt(Id(c),IntLit(44818)),AssignStmt(Id(d),IntLit(181))]))])])"
#         self.assertTrue(TestParser.test(input, expect, 400))
        
        
#         # note: .e10
        


   