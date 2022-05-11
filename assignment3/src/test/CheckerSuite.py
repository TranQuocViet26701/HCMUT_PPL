import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
   
    def test_1(self):
        input = """
            Class Program{
                
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_2(self):
        input = """
            Class Program{
                main(x : Int){
                    
                }
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_3(self):
        input = """
            Class Program{
                main(){
                    Return 2;
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_4(self):
        input = """
            Class Program{
                main(){
                    Return;
                }
            }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_5(self):
        input = """
            Class Program{
                main(){
                }
            }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_6(self):
        input = """
            Class Program{
                main(){
                }
            }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_7(self):
        input = """
            Class Program {
                Val numOfShape : Int = 0;
                Var immuAttribute : Int = 0;
                test(n : Int){
                    Var a : Int;
                        Val y : Int = 5;
                        Var a : Int = 6;
                }
                
                main(){
                    Return;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        input = """
            Class B{}
            Class A {
                Val c : C;
            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        input = """
            Class B{}
            Class Program {
                main(){
                    Val c : C;
                    Return;
                }
            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        input = """
            Class B{}
            Class Program {
                main(){
                    {
                        {
                            {
                                {
                                    Val c : C;
                                    
                                }
                            }
                        }
                    }
                    Return;
                }
            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_11(self):
        input = """
            Class B{}
            Class Program {
                main(){
                    Val a : Int = 0;
                    a = 1;
                    
                    Return;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        input = """
            Class B{}
            Class Program {
                main(){
                    Var test : B = New B();
                    test.access();
                    
                    Return;
                }
            }
        """
        expect = "Undeclared Method: access"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
        Class A{}
            Class Program{
                main(){
                    Var a : Float;
                    a =5;
                    
                    Return;
                }
            }
        """
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        input = """
            Class B{}
            Class Program {
                main(){
                    Var a : Int;
                    a = 5.1;
                    Return;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(5.1))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        input = """
            Class B{}
            Class Program {
                Val a : Int;
                main(){
                    Return;
                }
            }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 414))   

    def test_16(self):
        input = """Class A {} Class A {}"""
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        input = """
            Class B{
                Var b : Int;
            }
            
            Class Program : B{
                Var a : Int;
                main(){
                    b=1;
                    Return;
                }
            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_18(self):
        input = Program([ClassDecl(Id("a"), [], Id("b"))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_19(self):
        input = """
        Class Program{
            Val x : Int = 10.0;
            
            main(){
                Return;
            }
            
            }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_20(self):
        input = """
            Class Program {
                Var a : Int = 3.5;
                
                getValue(){
                    Return 10;
                }
                
                main(){
                    Var x: Int;
                    x = Self.a;
                    Return;
                }
            }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_21(self):
        input = """
            Class Program {
                Var x : Array[Int , 3] = Array(2, 1.2, 10.0);
                main(){
                    Return;
                }
            }
        """
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),FloatLit(10.0)]"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_22(self):
        input = """
            Class Program {
                getValue(){
                    Return 10;
                }
                
                main(){
                    Var x: Int = Self.getValue();
                    Return;
                }
            }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_23(self):
        input = """
            Class B{}
            Class Program {
                Var a : Int;
                Val b : Int = a+1;
                
                main(){
                }
            }
         """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_24(self):
        input = """
            Class B{
                Val b : String = "b";
            }
            
            Class Program : B{
                Val $a : String = "test";
                main(){
                    Var b : String = Self.c;
                }
            }
         """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_25(self):
        input = """
            Class B{
                Val $a : String ="test";
            }
            Class Program{
                main(){
                    Var obj : B = New B();
                    Var a : String = obj::$a;
                }
            }
         """
        expect = "Illegal Member Access: FieldAccess(Id(obj),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_26(self):
        input = """Class Program {
            printInt(i: Int){
                Return;
            }
            
            main() {
                Var i: Int;
                Foreach (i In 1 .. 100 By 2) {
                    Self.printInt(i);
                }
                Return;
            }
        }"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_27(self):
        input = """
            Class Program {
            main(){
                Var x : Int = y;
                Var y : Int;
            Return;
            }
        }
         """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_28(self):
        input = """
            Class A {
                foo(){
                    Return 1;
                }
            }
            Class Program : A{
                Var a : A = New A();
               main(){
                    a.foo();
                }
            }
         """
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_29(self):
        input = """
            Class A {
                $foo(){
                    Return 7.8;
                }
            }
            Class Program : A{
                Var $a : A = New A();
                main(){
                    Var i : Int = A::$foo();
                }
            }
         """
        expect = "Type Mismatch In Statement: VarDecl(Id(i),IntType,CallExpr(Id(A),Id($foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_30(self):
        input = """
            Class A {
            }
            Class Program : A{
                Var a : A = New A();
                main(){
                    Var a : Int;
                    Var b : Int = 1;
                    If (b) {
                        a = 1;
                    } 
                    Else {
                        a = 2;
                    }
                }
            }
         """
        expect = "Type Mismatch In Statement: If(Id(b),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(2))]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_31(self):
        input = """
            Class A {
            }
            Class Program : A{
                Var a : A = New A();
                main(){
                    Var a : Int = 0;
                    Var i : A = New A();
                    Foreach (i In 1 .. 100){
                        a = a + 1;
                    }
                }
            }
         """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_32(self):
        input = """
            Class A {
            }
            Class Program{
                main(){
                    Var a : Array[Float, 2];
                    a = Array(1, 2, 3);
                }
            }
         """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_33(self):
        input = """
            Class A {
            }
            Class Program{
                test(){
                    Var a : Array[Float, 4] = Array(1, 2, 3, 4);
                    Var sum : Int = 0;
                    Var i : Int;
                    Foreach (i In 0 .. 3){
                        sum = sum + a[i];
                    }
                }
                main(){}
            }
         """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(sum),ArrayCell(Id(a),[Id(i)]))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_34(self):
        input = """
           
            Class Program{
                main(){
                    Var a : Array[Float, 4] = Array(1.5, 2.2, 3.10, 4.0);
                    Var sum : Int = 0;
                    Var i : Int;
                    Foreach (i In 0 .. 3){
                        sum = "5" + a[i];
                    }
                }
            }
         """
        expect = """Type Mismatch In Expression: BinaryOp(+,StringLit(5),ArrayCell(Id(a),[Id(i)]))"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_35(self):
        input = """
            Class A {
                Val value :Int = 5;
            }
            Class Program{
                main(){
                    Var a : Int = 5;
                    Var b : A = New A();
                    Var c : String;
                    
                    If (a < b) {
                        c = "a";
                    } 
                    Else {
                        c = "b";
                    }
                }
            }
         """
        expect = """Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_36(self):
        input = """
            Class B{
                $test(a, b, c : Int){
                }
            }
            Class Program{
                main(){
                    B::$test(1.1,2,3);
                }
            }
         """
        expect = "Type Mismatch In Statement: Call(Id(B),Id($test),[FloatLit(1.1),IntLit(2),IntLit(3)])" 
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_37(self):
        input = """ Class A{} Class B : A{} Class C : A{} Class F{} Class A : F{}"""
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_38(self):
        input = """ Class Program {Var a: Int; Var $a : Float; main(){}}"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_39(self):
        input = """ Class Program { Val a : Int; main(){}}"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_40(self):
        input = """ Class Program {Val a : Int = 10; Val $a : Float = 2.2; main(){}}"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_41(self):
        input = """ Class Program{ Val a : A = New A(); main(){}}"""
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_42(self):
        input = """ Class Program {a() {} $a() {} main(){}}"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_43(self):
        input = """ Class Program {Val a : Int; a(){} main(){}}"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_44(self):
        input = """ Class Program {a(){} Val a : Int; main(){}}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        input = """ Class Program { C(){} C(a : Int){} main(){}}"""
        expect = "Redeclared Method: C"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_46(self):
        input = """ Class Program {
            main() { Break;}
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_47(self):
        input = """ Class Program{
            main() {
                Var i : Int;
                Foreach (i In 1 .. 2){
                    Break;
                }
                Continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_48(self):
        input = """ Class Program{
            main() {
                Var i : Int;
                Foreach (i In 1 .. 2){
                    If ( i == 1) {
                        Break;
                    }
                    Else {
                        Continue;
                    }
                }
                Continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_49(self):
        input = """ Class Program{
            Var a : Int = Self.b;
            main(){}
        }"""
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_50(self):
        input = """ Class Program {
            Var a : Int;
            Var b : Int = Self.a;
            Var c : Int = a;
            main(){}
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_51(self):
        input = """
        Class Program {
            main(){
                Var a: Boolean;
                If(a) {Break;}
            }
        }
        Class A{
            Val $c: Int = 3;
            
            greet(){
                Return "hello";
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_52(self):
        input = """
        Class Program {
            main(){
                If("True") {Break;}
            }
        }
        Class A{
            Val $c: Int = 3;
            
            greet(){
                Return "hello";
            }
        }
        """
        expect = "Type Mismatch In Statement: If(StringLit(True),Block([Break]))"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_53(self):
        input = """
        Class Program {
            main(){
                If(a) {Break;}
            }
        }
        Class A{
            Val $c: Int = 3;
            
            greet(){
                Return "hello";
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_54(self):
        input = """
        Class Program {
            
             main(){
            }
            Factorial(n: Int){
                If (n == 0) {Return 1;} 
                Else {Return n * Self.Factorial(n - 1);}
            }
           
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(n),CallExpr(Self(),Id(Factorial),[BinaryOp(-,Id(n),IntLit(1))]))"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test_55(self):
        input = """
        Class A{
            Val $c: Int = 3;
            
            greet(){
                Return "hello";
            }
        }
        
        Class Program {   
            main(){
                A::$c = 2;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(A),Id($c)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_56(self):
        input = """
        Class A{
            Var $c: Int = 3;
            test(){
                Return;
            }
        }
        
        Class Program {   
            main(){
                Var a: Int = A::$b;
            }
        }"""
        expect = "Undeclared Attribute: $b"
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test_57(self):
        input = """
        Class Program {   
            Var $b: Int = 3;
            main(){
                Var a: Int = A::$b;
            }
        }"""
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_58(self):
        input = """
        Class A{
            Var $b: Int = 100;
            x(a:Int; b:Int){
                Return a / b + 20;
            }
        }
        Class Program {   
            main(){
                Var a: Int = A::$b;
            }
        }"""
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 457)) 
        
    def test_59(self):
        input = """
        Class A{
            Var $b: Int = 3;
            x(a:Int; b:Int){
                Return b - a + a;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: Int = c::$b;
            }
        }"""
        expect = "Illegal Member Access: FieldAccess(Id(c),Id($b))"
        self.assertTrue(TestChecker.test(input, expect, 458)) 
    
    def test_60(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return a + b;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: Int = c.x(1.2,2.3);
                Return;
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(c),Id(x),[FloatLit(1.2),FloatLit(2.3)])"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test_61(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return b - a;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: Int = c.x(1,2);
            }
        }"""
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_62(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return a*b;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: String = c.x(1,2);
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,CallExpr(Id(c),Id(x),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_63(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return  b * a;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: String = c.x(1);
            }
            
            
            
            
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(c),Id(x),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_64(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return a + b;
            }
        }
        Class Program {   
            main(){
                Var c: A = New A();
                Var a: String = A.x(1);
                Return;
            }
        }"""
        expect = "Illegal Member Access: CallExpr(Id(A),Id(x),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_65(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return a - b;
            }
        }
        Class Program {   
            main(){
                Var c: A;
                Var a: String = A.x(1,2);
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(c),ClassType(Id(A)),NullLiteral())"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_66(self):
        input = """
        Class A{
            x(a:Int; b:Int){
                Return a + b;
            }
        }
        Class Program {   
            main(){
                Var B: Array[Int,5];
                Var a: String = Self.x(1,2);
                Return;
            }
        }"""
        expect = "Undeclared Method: x"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_67(self):
        input = """
        Class Program {   
            x(a:Int; b:Int){
                Return b + a;
            }
            y(){}
            
            main(){
                Var B: Array[Int,5];
                Var a: String =Self.x(1,2);
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,CallExpr(Self(),Id(x),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test_68(self):
        input = """
        Class Program {   
        y(){
            Return 10;
        }
            x(a:Int; b:Int){
                Return b+a;
            }
            
            main(){
                Var B: Array[Int,5];
                Var a: Int= Self.x(1,2);
            }
        }"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test_69(self):
        input = """
        Class Program {   
        y(){
            Return 10;
        }
            x(a:Int; b:Int){
                Var x: Int = a + b;
                Return x;
            }
            
            main(){
                Var B: Array[Int,5];
                Var a: Int = Self.x(1);
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(x),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_70(self):
        input = """
        Class Program { 
        second()     {}
            main(){
                Var B: Array[Int,5];
                Var a: Boolean = !3.2;
            }
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLit(3.2))"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_71(self):
        input = """
        Class A {}
        Class Program {    
        test()  {}
            main(){
                Var B: Array[Int,5];
                Var a: Int = !True;
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,UnaryOp(!,BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_72(self):
        input = """
        Class Program {    
                test(){}
          
            main(){
                Var B: Array[Int,5];
                Var a: Int = 1.2 % 3;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.2),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_73(self):
        input = """
        Class Program {      
        test()   {}
            main(){
                Var B: Array[Int,5];
                Var a: Boolean = "abc" ==. 123 ;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==.,StringLit(abc),IntLit(123))"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_74(self):
        input = """
        Class Program {   
        test()   {}
            main(){
                Var B: Array[Int,5];
                Var a: Boolean = "abc" == "abc" ;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,StringLit(abc),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_75(self):
        input = """
        Class Program {     
        
        test(){} 
            main(){
                Var B: Array[Int,5] = Array(1,2);
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(B),ArrayType(5,IntType),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        
    def test_76(self):
        input = """
        
        Class A{
            x(){
                Return 15;
            }
        }
        Class Program {      
            main(){
                Var B: A = New A();
                Var c: String = "2";
                c = c +. B.x();
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+.,Id(c),CallExpr(Id(B),Id(x),[]))"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_77(self):
        input = """
        
        Class A{
            x(){
                Return "1251255";
            }
        }
        Class Program {    
        
        clone()  {}
            main(){
                Var B: A = New A();
                Var c: String = "2";
                c = c +. B.x();
            }
        }"""
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 476))
           
    def test_78(self):
        input = """
        Class A{
            x(){
                Return "123456";
            }
        }
        Class Program {      
            main(){
                Var B: A = New A();
                Var c: String = "2";
                c = c + B.x();
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(c),CallExpr(Id(B),Id(x),[]))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_79(self):
        input = """
        Class A{
            x(){
                Return "10";
            }
        }
        Class Program {      
            main(){
                Var B: A = New A();
            }
        }"""
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test_80(self):
        input = """
        Class Parent{}
        Class Program {
            main(){
                Var a: Int = Self.x();
                Return;
            }
            x(){
                Return "3";
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,CallExpr(Self(),Id(x),[]))"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
    def test_81(self):
        input = """
        Class Test {}
        Class Program {
            x(){
                Return "3";
            }
             
             test(){}
            main(){
                Var a: String = Self.x();
                Return;
            }
            
        }"""
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test_82(self):
        input = """
        
        Class Parent{}
        Class Program {
            
            main(){
                Var b: Int;
                b = 3;
                Val a: Float = 5.0;
                b = b + a;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(+,Id(b),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 481))
            
    def test_83(self):
        input = """
        Class Parent{}
        Class Program {
            main(){
                Var b: Int;
                Val a: Float = 5.0 + "3";
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,FloatLit(5.0),StringLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test_84(self):
        input = """
        Class Parent{}
        Class Program {
            main(){
                Var b: Int;
                Val a: Int = 1 + b;
            }
        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,IntLit(1),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test_85(self):
        input = """
        Class Parent {}
        Class Program {
            
            main(){
                Val a: Int;
            }
        }"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_86(self):
        input = """
        Class Parent {}
        Class Program {
            
            main(){
                Val a: Int = 5;
                a = 6;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(6))"
        self.assertTrue(TestChecker.test(input, expect, 485))
         
    def test_87(self):
        input = """
        Class Program {
            Shape(left,right: Float){
                Var a: Array[String, 3];
                a = Array("Volvo", "22", "18");
                Var b: Int= a[1];
            }

            main(){}
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),IntType,ArrayCell(Id(a),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test_88(self):
        input = """
        Class Program {
            Shape(left,right: Float){
                Var a: Array[String, 3];
                a = Array("Volvo", "22", "18");
                Var b: String = a[1.5];
            }

            main(){}
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[FloatLit(1.5)])"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_89(self):
        input = """
        Class Program {
            Shape(left,right: Float){
                Var a: Array[Array[String,3],3];
                a = Array(
                    Array("Volvo", 22, 18),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                );
            }
            
            
            main(){}
        }"""
        expect = "Illegal Array Literal: [StringLit(Volvo),IntLit(22),IntLit(18)]"
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test_90(self):
        input = """
        Class Program {
            Shape(left,right: Float){
                Var a: Array[Array[String,3],3];
                a = Array(
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                );
            }
            main(){            }
        }"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 489))
        
    def test_91(self):
        input = """
        Class Program {
            Shape(l,w: Float){
                Var a: Int = 10;
                a = Array(
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                );
            }
            main(){}
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])"
        self.assertTrue(TestChecker.test(input, expect, 490))
        
    def test_92(self):
        input = """
        Class Program {
            
            Shape(l,w: Float){
                a = Array(
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                );
            }
            main(){}
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 491))
            
    def test_93(self):
        input = """Class Program {
            main() {
                Var i: Int;
                Foreach (i In 1 .. 100 By 2) {
                    If (i % 2 == 0) {
                        Continue; 
                        }
                }
            }
        }"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_94(self):
        input = """Class Program {
            printInt(){
                Return;
            }
            
            main() {
                Var i: Int = 200;
                Foreach (i In 1 .. 100 By 2) {
                    Self.printInt();
                }
                Continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))
        
    def test_95(self):
        input = """Class Program {
            printInt(){
                Return;
            }
            main() {
                Var i: Int = 100;
                Foreach (i In 1 .. 100 By 2) {
                    Self.printInt();
                }
                Break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test_96(self):
        input = """ 
        Class Program {
            main() {
                Var i: Int = 20;
                Foreach (i In 1 .. 100 By 2) {
                    Self.printInt(i);
                }
            }
        }"""
        expect = "Undeclared Method: printInt"
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_97(self):
        input = """Class Program {
            main() {
                Var i: Int = 1;
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Undeclared Class: Out"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test_98(self):
        input = """Class Program {
            main() {
                Var i: Int;
                Foreach (i In 1.0 .. 100.5 By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(i),FloatLit(1.0),FloatLit(100.5),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])"
        self.assertTrue(TestChecker.test(input, expect, 497))
        
    def test_99(self):
        input = """    Class Program {
            main() {
                
                
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test_100(self):
        input = """
        
        Class Program {
            
                Val $numOfShape: Int = 2.5;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                main(){
                }
            }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id($numOfShape),IntType,FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input, expect, 499))
    