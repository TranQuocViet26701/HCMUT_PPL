import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """Class main { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test_simple_program1(self):
        """Simple program"""
        input = """Class Main : { }"""
        expect = "Error on line 1 col 13: {"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program1(self):
        """Simple program"""
        input = """Class secondary : main { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_more_complex_program(self):
        """More complex program"""
        input = """ Class main { 
                        Val My1stCons, My2ndCons: Int = 6, 2;
                        Var $x, $y : Int = 0, 0;
                 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_more_complex_program2(self):
        """More complex program"""
        input = """ Class secondary : main { 
                        Constructor () {}
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_more_complex_program3(self):
        """More complex program"""
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        
                        $getNumOfShape() {}
                        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    
    def test_wrong_miss_close(self):
        """Miss } Class"""
        input = """Class missing_close {"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_more_complex_program4(self):
        """More complex program"""
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 5+2;
                        Val immutableAttribute: Int = 10*6/8;
                        
                        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test_more_complex_program5(self):
        """More complex program"""
        input = """ 
                    Class arr_test {
                        Var arr: Array[Int, 5] = Array(1, 5, 7, 12);
                        Var arr2: Array[Int, 3] = Array(!25, arr[0], (5/3)*10, (arr[2]/2)%2);
                        Var arr3: Array[Array[Int, 3], 1] = Array(arr2);
                        
                        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    
    def test_more_complex_program6(self):
        """More complex program"""
        input = """ 
                    Class Rectangle: Shape {
                        getArea(){
                            Return Self.length * Self.width;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test_more_complex_program7(self):
        """More complex program"""
        input = """ 
                    Class Shape {
                        $getNumberOfShape( {
                            Return Self.lenght * Self.width;
                        }
                    }
                """
        expect = "Error on line 3 col 43: {"
        self.assertTrue(TestParser.test(input,expect,211))
    
    def test_more_complex_program8(self):
        """More complex program"""
        input = """ 
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {
    Return $numOfShape;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    
    def test_more_complex_program9(self):
        """More complex program"""
        input = """ 
    Class Shape {
        ## This is a class for shape ##
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    ##
    CLASS Rectangle: Shape {
        getArea() {
            Return Self.length * Self.width;
        }
    }
    ##
    Class Program {
        main() {
            Return Shape::$numOfShape;
        }
    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    
    def test_more_complex_program10(self):
        """More complex program"""
        input = """ 
Class Person {
    Var $numOfPerson: Int = 0;
    Val firstname: String = "Your";
    Val lastname: String = "Name";
    
    Constructor(firstname, lastname : String){
        $numberOfPerson = $getNumberOfPerson() + 1;
        setFirstName(firstname);
        setLastName(lastname);
    }
    
    $getNumberOfPerson() {
        Return $numOfPerson;
    }
    
    setFirstName(string: String){
        firstname = string;
    }
    
    setLastName(string: String){
        lastname = string;
    }
}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_more_complex_program11(self):
        """More complex program"""
        input = """ 
 Class Person {
        Val firstName, lastName: String; ## property ##
        Var age: Int;          ## property ##
        
        c(){
            s = a + b + c * d;
            d = a && b;
            e = !a;
        }
}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_more_complex_program12(self):
        """More complex program"""
        input = """ 
Class Test {
        abc(){}
        $abc(){}
        abc(){}
        print(){}
        abc(){}
        low2up(){}
}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_more_complex_program13(self):
        """More complex program"""
        input = """ 
Class Test : TestParent{
        abc__bc_ab(c : Int){
        }
        print(a : String){
            Return "hello" + a;
        }
}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_more_complex_program14(self):
        """More complex program"""
        input = """ 
Class Test {
        main(arg : Array[Int, 5]){}
        $goo (x : Array[Float, 5]) {
    Val y : Array[Float, 10];
    Val x : Array[Float, 10];
    Val z : Array[Float, 10];
    a.foo( z ) ;
     a.foo( x ) ;
      a.foo( y ) ;
    Return y;
}
}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_more_complex_program15(self):
        """More complex program"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_more_complex_program16(self):
        """More complex program"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_more_complex_program17(self):
        """More complex program"""
        input = """ 
Class Test {
     a(abc : Int; xyz : Float){}
        a(a : Array[Int, 5]){}
}
       
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
#====================================  For/In statement ====================================#
    def test_more_complex_program18(self):
        """More complex program"""
        input = """ 
Class Test {
    main()
        {
            Foreach (i In 1 .. 100 By -1) {}
        }
}
    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    
    def test_more_complex_program19(self):
        """More complex program"""
        input = """ 
Class Test {
    main()
        {
            Foreach (i In 1 .. 5 + 1) {
                IO.printf(i);
            }
        }
}
    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    
    def test_more_complex_program20(self):
        """More complex program"""
        input = """ 
Class Test {
    main()
        {
            Var x: Int;
            IO.input(x);
            Foreach (i In 1 .. x) {
                If (i%2==1) {IO.print(i);}
                If (i==4) {Break;}
            }
        }
}
    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    
    def test_more_complex_program21(self):
        """More complex program"""
        input = """ 
Class Test {
    main()
        {
            Var x: Int;
            IO.input(x);
            Foreach (i In 1 .. x) {
                If (i%2==1) {IO.print(i);}
                If (i==(x/2)) {
                    i = i + 5;
                    Continue;
                    }
            }
        }
}
    
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    
    def test_more_complex_program21(self):
        """More complex program"""
        input = """ 
Class Test {
        main()
        {
            Foreach (i In 1 .. x {
                
            }
        }
}
    
                """
        expect = "Error on line 5 col 33: {"
        self.assertTrue(TestParser.test(input,expect,225))