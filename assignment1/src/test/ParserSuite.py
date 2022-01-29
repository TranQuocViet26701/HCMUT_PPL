import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program201(self):
        """Simple program"""
        input = """Class main { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test_simple_program202(self):
        """Simple program"""
        input = """Class Main : { }"""
        expect = "Error on line 1 col 13: {"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program203(self):
        """Simple program"""
        input = """Class secondary : main { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_more_complex_program204(self):
        """More complex program"""
        input = """ Class main { 
                        Val My1stCons, My2ndCons: Int = 6, 2;
                        Var $x, $y : Int = 0, 0;
                 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_more_complex_program205(self):
        """More complex program"""
        input = """ Class secondary : main { 
                        Constructor () {}
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_more_complex_program206(self):
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
    
    def test_wrong_miss_close207(self):
        """Miss } Class"""
        input = """Class missing_close {"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_more_complex_program208(self):
        """More complex program"""
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 5+2;
                        Val immutableAttribute: Int = 10*6/8;
                        
                        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test_more_complex_program209(self):
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
    
    def test_more_complex_program210(self):
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
    
    def test_more_complex_program211(self):
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
    
    def test_more_complex_program212(self):
        """More complex program"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    
    def test_more_complex_program213(self):
        """More complex program"""
        input = """ 
    Class Shape {
        ## Self is a class for shape ##
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
        expect = "Error on line 8 col 19: $numOfShape"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_more_complex_program214(self):
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
        
    def test_more_complex_program215(self):
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
        
    def test_more_complex_program216(self):
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
        
    def test_more_complex_program217(self):
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
        
    def test_more_complex_program218(self):
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
        
    def test_more_complex_program219(self):
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
        
    def test_more_complex_program220(self):
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
    def test_more_complex_program221(self):
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
    
    def test_more_complex_program222(self):
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
    
    def test_more_complex_program223(self):
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
    
    def test_more_complex_program224(self):
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
    
    def test_more_complex_program225(self):
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
    def test_for_stmt_226(self):
        input = """
        Class testFor {
            testFor() {
                Foreach (i In 1 .. 10) {a=a+1;}
            }
            callFor() {
                Foreach (i In 25 .. 5 By 2) {
                    a = a + 1;
                };
            }
        }"""
        expect = "Error on line 9 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_for_stmt_227(self):
        input = """
        Class testFor {
            testFor() {
                Foreach (i In 1 .. 10) {a=a+1;}
            ##}##}
            callFor() {
                Foreach (i In 25 .. 5 By 2) {
                    a = a + 1;
                    Foreach (i In 5 .. 25 By 2) {
                        a.Pi[5] = 1 + 2;
                    }
                }
                
                Return a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_for_stmt_228(self):
        input = """
        Class testFor {
            testFor() {
                Foreach (i In 1 .. 10) {a=a+1;}
            }
            callFor(a : Int) {
                Foreach (a In 1 .. 10) {
                    a = a + 1;
                    Foreach (a In -10 .. 10 By 5) {
                        a.Pi[5] = 1 + 2;
                        If (a.v < z[2]) {
                            If (a == 1) {
                                If (a == 1) {
                                    
                                }
                            }
                            Else {
                                If (a > b) {a = 2;} Elseif (a == -5) {a = 2;}
                            }
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_for_stmt_229(self):
        input = """
        Class testFor : _parentTest {
            testFor(i: Float) {
                Foreach (i In 1 .. 10) {a=a+1;}
                
                Return _123;
            }
            $callFor() {
                Foreach (i In (10-5) .. 10 By -5) {
                    a = a + 1;
                    Foreach (i In 1 .. 10 By (10-5)) {
                        a.Pi[5] = 1 + 2;
                        
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        # Test special
    def test_special230(self):
        input = """
        Class _childTest : _parentTest {
            Destructor(a : Int){
                Return;
            }
        }"""
        expect = "Error on line 3 col 23: a"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_special231(self):
        input = """
        Class _childTest : _parentTest {
            Constructor(){
                Var arr : Array[Int, 0];
            }
        }"""
        expect = "Error on line 4 col 37: 0"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_break_con_232(self):
        input = """
        Class testData : PPL {
            $loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
            Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                    If (a > f-1) {Break;}
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_break_con_233(self):
        input = """
        Class testData : PPL {
            loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_break_con_234(self):
        input = """
        Class testData : PPL {
            $loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
                Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                    ## in loop ##
                }
            }
            loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
                Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                    If (a > f-1) {Break;} Else {Continue;}
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_break_con_235(self):
        input = """
        Class testData : PPL {
            loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
                 Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                    If (a > f-1) {Break;} Else {Continue;}
                    Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                    If (a > f-1) {
                        Foreach (i In (a + c -d == f) .. a+(a >=d)/32 By (10-5)) {
                        If (a > f-1) {Out.print(10);} 
                        }
                    } Else {Continue;}
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_break_con_236(self):
        input = """
        Class testData{
            loopTest(a, v : Int; c, d: Float; a, s: Boolean; str1, str2 : String; r1, r2: Room) {
                Foreach (i In (a + c -d == f) .. a+(a >=d)/32) {
                        If (a > f-1) {Out.print(10);} 
                        Elseif (a <= 10) {Return Tester::$number;}
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_break_con_237(self):
        input = """
        Class testData : PPL {
            $loopTestTest(int a,v; float c,d; boolean a,s; string str1,str2; Room r1,r2) {
                for i = (a + c -d == f) downto a+(a >=d)/32 do {
                    If ((a > f-1)&&(a||1)) {Break;}
                    If (a > f-1) {Break;}
                }
            }
        }"""
        expect = "Error on line 3 col 30: a"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_break_con_238(self):
        input = """
        Class testData : PPL {
            _LoopTest() {
                Foreach (incre In -10 .. (22+a) By -(22+5)) {
                    Return (a!=10 && !a);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_return_239(self):
        input = """
        Class School {
            cloneStudent(stu: Student){
                Var clone : Student = "qwerty\\n";
                If (clone != nil) {
                    Return clone;
                }
                Else {
                    Return null;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    # #======================================= 40-49 ==========================================
    def test_return_240(self):
        input = """Class Res {
             Add(a, b: Int) {
                Return a + b;
            }
            Add(a,b : Float) {
                Return a + b ==. c % 2 / 1 * a;
            }
            Add(a,b : Boolean) {
                Return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            Add (a : String; "abcd") {
                return;
            }
            doctor makeNew(int a; float b) {
                if a== 0 then
                return new doctor(a,b,c,d,1./2);
                else {
                    if a<1 then
                        return this.doctor;
                    else
                        return nil;
                }
            }
        }"""
        expect = '''Error on line 11 col 29: abcd'''
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_return_241(self):
        input = """Class Res {
            Add(a, b : Int) {
                Return a + b;
            }
            Add(a,b : Float) {
                Return a + b || c % 2 / 1 * a;
            }
            Add(a,b : Boolean) {
                Return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            Add (a : String) {
                Self.Add(10);
            }
            makeNew(a : Int; b : Float) {
                If ( a== 0) {
                
            }
        }"""
        expect = "Error on line 18 col 9: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_return_242(self):
        input = """Class Res {
            add (a,b : Array[Int, 1]) {
                Val res : Array[Int, 6] = Array(a,b,res);
                If (res.size() != 0) {
                    Return res;
                }
                Else
                    {Return Array();}
            }
            getA() {
                Self.PrintA();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_stmt_243(self):
        input = """
        Class C1 : C2_C2C2 {
            Var $a : Int = 10;
            C1(a : Int) {
                Self.a = a;
                If (Self.CheckA() == True ) {Self.PrintA();}
                Else {Self.getA();}
            }
            CheckA(10) {
                if this.a <= 0 then return false;
                else return true;
            }
             PrintA() {
                io.print("Data of list" ==. str.makeStr(a));
            }
            
        }"""
        expect = "Error on line 9 col 19: 10"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_stmt_244(self):
        input = """
        Class C1 {
            Val $a : Int = 10;
            C1(a : Int) {
                Self.a = a;
                If (Self.CheckA() == True ) {Self.PrintA();}
                Else {Self.getA();}
            }
            getA() {
                Foreach (i In 1 .. 10) {
                    Var a : Int = io.getInt();
                    If (a > 0)  {
                        Self.a = a;
                        Break;
                    }
                }
                Self.PrintA();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_stmt_245(self):
        input = """
        Class C2 {
            Val $_11 : c;
            Var arr : Array[String, 15];
            C2(C1 c) {
                Self.c = c;
                C1.PrintA();
            }
             create_skill() {
        can_skill := false;
        have_button := false;
        system.Instantiate(water_skill, new Vector3(-10,0,0), transform.rotation);  
        skill_Audio.Play(0);   
    }
            int[5] getArr() {
                return arr;
            }
        }"""
        expect = "Error on line 5 col 18: c"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_stmt_246(self):
        input = """
        Class C3 : C2 {
            Val string : String;
            Constructor(self, name : String) {
                Return "Name of C3: " +. name;
            }
            CheckName(n1 : String) {
                Return string == self.name;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_stmt_247(self):
        input = """
        Class checkExp {
            check1(a,b,c : Boolean ) {
                a1 = a > b > c;
            }
        }"""
        expect = "Error on line 4 col 27: >"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_stmt_248(self):
        input = """
        Class checkExp {
            check1(boolean, a,b,c : Boolean) {
                a1 = a > (b > c) <= boolean;
            }
        }"""
        expect = "Error on line 4 col 33: <="
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_stmt_249(self):
        input = """
        Class checkExp {
            $_check1(a,b,c : Bolen) {
                a1 = a > (b > c);
                a2 = ((a==b)!=c)==123;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_stmt_250(self):
        input = """
        Class C3 : C2 {
            Val name : Car = New Car("Mazda", 2019);
            
            Constructor(name : String; year : Int) {
                Self.name = name;
                Self.year = year;
            }
            
            C3(n : String;c : C1) {
                Self.name = n;
            }
            
            getName() {
                Return "Name of C3: " +. name;
            }
            checkName(n1 : String) {
                Return n1 ==. name;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_stmt_251(self):
        input = """
        Class mainClass {
            main() {
                Var c1 : C1 = New C1();
                Val c2 = New C2(c1);
                Var c3 : C3 = New C3("abc
                ",c1);
            }
        }"""
        expect = """abc"""
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_stmt_252(self):
        input = """
        Class mainClass {
            main() {
                Val c3 : C3 = New C3("abc",c1);
                c3.checkName("abcd");
                io.Print(c3.getName());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_only_EOF253(self):
        input = """##no have class
        *****************
        ******************##
        ## only have cmt ##"""
        expect = "Error on line 4 col 27: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_random_254(self):
        input = """
        ## class parent ##
        Class Exp {
            eval() {}
        }
        ## class intlit and floatlit ##
        Class IntLit : Exp {
            Val value : Int;
            Intlit(a : Int) {
                Self.value = a;
            }
            eval() {
                Return Self.value;
            }
        }
        ## Class floatlit and floatlit
        Class FloatLit : Exp {
            Val value : Float;
            Constructor(a : Float) {
                Self.value = a;
            }
            eval() {
                Return Self.value;
            }
        }
        """
        expect = "#"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_random_255(self):
        input = """
        Class UnExp : Exp {
            Val op : String;
            Val value : Float;
            UnExp(op : String;value : Float) {
                Self.value = value;
            }
            eval() {
                If (op == "+") {Return value; }
                Else {Return value * (-1);}
            }
            create_skill() {
        can_skill = false;
        have_button = false;
        system.Instantiate(water_skill, New Vector3(-10,0,0), transform.$rotation);  
        skill_Audio.Play(0);   
    }
     shootWater() {
        for i = 0  to num_bullet do {
            system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
            shoot_Audio.Play(0);       
        }
    }
        }"""
        expect = "Error on line 15 col 72: $rotation"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_random_256(self):
        input = """
        Class BinExp : Exp {
            Val op : String;
            Val left, right : Float;
            BinExp(op : String; l, r : Float) {
                Self.op = op;
                Self.r = r;
            }
            eval() {
                If (op == "+") {Return left + right;}
                Elseif (op == "-") {Return lef - right;}
                Elseif (op == "/") {Return lef / right;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_random_257(self):
        input = """Class follow_mouse {
    FixedUpdate () {
        ## Get the Screen positions of the object ##
        Val angle : Float = system.AngleBetweenTwoPoints(positionOnScreen, mouseOnScreen);
        transform.rotation =  Quaternion.Euler(New Vector3(0,0,angle - 180));
    }
    changeState() {
        checkRun = !checkRun;
    }
    ## FUNCTION FOR SKILL AND FIRE BULLET
    create_button_skill() {
        system.Instantiate(button_skill, new Vector3(-6.5,-4,0), transform.rotation);
    }
    float AngleBetweenTwoPoints(Vector3 a, b) {
         return Math.Atan2(a.y - b.y, a.x - b.x) * Math.Rad2Deg;
    }##
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_random_258(self):
        input = """
Class smoke_run : MonoBehaviour{
    Val speed : Int = 5f;
    Var counter : Float = 0;;
    Var scaleChange : Vector3;
    $FixedUpdate()
    {
        transform.localScale = transform.localScale + scaleChange;
        if (counter == 100) {
        }
    }
}"""
        expect = "Error on line 3 col 23: f"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_random_259(self):
        input = """
Class skill_check {
    FixedUpdate()
    {
        If (Input.GetKeyDown("s")) {
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_random_260(self):
        input = """
Class virus_move {
    Var myEffect : GameObject;
    Val speed_virus : Float = -0.15E10;
    FixedUpdate()
    {
    }
    OnTriggerEnter2D(col : Col2) {
        
        If ((col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_water_skill"))
        {
            system.Destroy(Self);
            system.Instantiate(myEffect, transform.position, transform.rotation);
        }
        If ((col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water")) 
        {
            system.Destroy(col.gameObject);
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_random_261(self):
            input = """
    Class drop_victim {
        Var count_time : Float = 0;
    changeState() {
            checkRun = !checkRun;
        }
        ## FUNCTION FOR SKILL AND FIRE BULLET ##
         create_button_skill() {
            system.Instantiate(button_skill, New Vector3(-6.5,-4,0), transform.rotation);
        }
         create_skill() {
            can_skill = false;
            have_button = false;
            system.Instantiate(water_skill, New Vector3(-10,0,0), transform.rotation);  
            skill_Audio.Play(0);   
        }
         shootWater() {
            Foreach (i In 0 .. num_bullet) {
                system.Instantiate(bullet_water, fire_point.position, fire_point.rotation);  
                shoot_Audio.Play(0);       
            }
        }
        static  Update()
        {
            if (count_time < 5) then transform.position := transform.position + new Vector3(0.5, 0.2, 0);
            else transform.position := transform.position + new Vector3(0.5, -0.1, 0);
        }
    }       """
            expect = "Error on line 23 col 16: Update"
            self.assertTrue(TestParser.test(input, expect, 261))
            
    def test_random_262(self):
            input = """
    Class control_victim {
        Val victim_die :GameObject ;
        Val eff :GameObject ;
        Val speed_human : Float = -0.15;

         Constructor()
        {
            transform.position = transform.position + New Vector3(speed_human, 0, 0);
        }
         OnTriggerEnter2D(col : Collider2D) {  
            If ((col.gameObject.tag == "bullet_mask") || (col.gameObject.tag == "bullet_water_skill")) 
            {
                system.Destroy(Self);
                system.Instantiate(eff, transform.position, transform.rotation);
                system.Instantiate(victim_die, transform.position, transform.rotation);
            }
            If (!checkRun)  {
                ## UPDATE PLAYER'S HP ##
                txt.text = myHP.ToString();
                If ((transform.position.y > 6) || (transform.position.y < -6))  {Self.GameOver();}
                ## CONTROLL JUMP AND DROP OF PLAYER ##
                If (Input.GetButtonDown("Jump") && !isJump) {
                    jumpAudio.Play(0);
                    countJump = 4;
                    isJump = true;
                    counting = 3;
                    Self.outSmoke();
                    Self.jumpUp(jumping / 2);
                }
                Elseif (countJump != 0) {
                    If (countJump > 3) { Self.jumpUp(jumping); }
                    Else { Self.jumpUp(jumping / 3); }
                }
                Else {
                    Self.dropDown();
                    If (counting == 0) { isJump = False; }
                }
            }
            If ((col.gameObject.tag == "bullet_water") || (col.gameObject.tag == "bullet_mask")) 
            { system.Destroy(col.gameObject); }
        }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 262))
    def test_random_263(self):
            input = """
    Class move {
        

        ## FIRE
        Transform fire_point;
        GameObject bullet_water;
        GameObject bullet_mask;
        AudioSource shoot_Audio;
        float num_bullet = 1.;
        float count_trigger = 0;
        # special skill ##
        

        Val Heart : GameObject;
        Val count_kira : Float = -1.0e12;
         Update() {
            If (Input.GetKeyDown("f"))  {
                Self.changeState();
            }
            
        }
         shootMask() {
            Foreach ( i In 0 .. Num_bulle By -1) {
                system.Instantiate(bullet_mask, fire_point.position, fire_point.rotation);  
                shoot_Audio.Play(0);       
            }
        }
        ## FUNCTION CONTROLL UFO AND EFFECT WHEN JUMPING ##
         outSmoke() {
            system.Instantiate(smoke_pre, smoke_point.position, smoke_point.rotation);
        }
         jumpUp(upSize : Float) {
            system.transform.position = transform.position + New Vector3(0, upSize, 0);
        }
         dropDown() {
            system.transform.position = transform.position + New Vector3(0, falling, 0);
        }
        GameOver() {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
        }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 263))
    def test_random_264(self):
            input = """
    Class PlayerMoment : MonoBehaviour{

        Var speed : Int = 12;
        Val  gravity : Float = -9.81* 10;
        ## Update is called once per frame ##
         Update()
        {
            isGrounded = Physics.CheckSphere(groundCheck::$position, groundDistance, groundMask);

            If (isGrounded && velocity.y < 0) {
                velocity.y = -2;
            }
        }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 264))
    def test_random_265(self):
            input = """
    Class PlayerMoment : MonoBehaviour{
        Var speed : Int= 12;
        Val gravity : Float= -9.81 * 10;
        Val jumpHeight: Float = 7;
        Val velocity : Victory;
        Var isGrounded : Boolean;
        ## Update is called once per frame ##
         Update()
        {
            move = transform.right * x + transform.forward * z;
            ctrller.Move(move  * speed * Time.deltaTime);

            If (Input.GetButtonDown("Jump") && isGrounded) {
                velocity.y = Mathf.Sqrt(jumpHeight * -2 * gravity);
            }
            io.getInt(num);
                sLec = num;
            velocity.y = velocity.y + gravity * Time.deltaTime;
            ctrller.Move(velocity * Time.deltaTime);
        }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 265))
    def test_random_266(self):
            input = """
    Class Faculty {
            Val name : String;
            Faculty(m : String) {}
            getNameFaculty() { Return name;  }
             setNameFaculty(n : Int) { name = n;  }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 266))
    def test_random_267(self):
            input = """
    ## LECTURER ##

    Class Lecturer {
           
Lecturer(n : String)  { name=n; }
            Lecturer(n : String; f : Faculty) { name = n; lecFaculty = f; }
            getNameFacultyOfLecturer() { Return lecFaculty.getNameFaculty(); }
            setNameFacultyOfLecturer(n : String) { lecFaculty.setNameFaculty(n); }
    };

    ## ClassROOM ##

    Class Classroom {
            Constructor(n : String) { nameRoom=n;}
             getNameClassroom() { Return nameRoom; }
             setNameClassroom(n : String) { nameRoom = n; }
    }"""
            expect = "Error on line 10 col 5: ;"
            self.assertTrue(TestParser.test(input, expect, 267))
    def test_random_268(self):
            input = """
            Class Test{
               Var ins: Int;
               Var $static: Int;
               
               Test(){
                  Var a: Int= Self::ins;
                  Var b: Int= Self::$static;
               }
            }
      """
            expect = "Error on line 7 col 34: ::"
            self.assertTrue(TestParser.test(input, expect, 268))
    def test_random_269(self):
            input = """
    Class Subject {
            
            Subject(n : String; $number: Int) { name=n; sLec=0;}
            getNameSubject() { Return name; }
            setNameSubject(n : String) { name = n; }
            inputData() {
               
                io.print("---------------\\n");
                io.print("Input name of Subject: ");
                io.fflush(stdin);
                io.getline(n);
                name = n;
            }
           
    }"""
            expect = "Error on line 4 col 32: $number"
            self.assertTrue(TestParser.test(input, expect, 269))
    def test_random_270(self):
            input = """

    Class Student {
            findSubject(name : String) {
                If (subs.getNameSubject() == name) { Return 1; }
                Return 0;
            }
            checkLec() {
                    io.print("\\n----------\\n");
                    subs.checkLect();
            }
            checkFacuSub(facu : String; sub : String) {
                If (facul.getNameFaculty() != facu) {Return 0;}
                Return self.findSubject(sub);
            }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 270))
            
    def test271(self):
        input = """
        Class a : _class {
            Var $x: Float = 1.0, y: Int = 3;
        }"""
        expect = "Error on line 3 col 34: :"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_random_272(self):
        input =  """
Class mainClass {
    main() {
    
    ##=========================ClassROOM===========================//##
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom = n;
    Foreach (i In 1 .. n) {
        Val name : String;
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " +.  ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        ClassR.setNameClassroom(name);
    }
}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_random_273(self):
        input = """
Class mainClass {
    main() {
    io.print("\\n=============================================================\\n");
    io.print("How many Classroom? ");
    io.getInt(n);
    sRoom = n;
    Foreach (i In 1 .. 10 By -b+a) {
        io.print("---------------------------------\\n");
        io.print("Input details for Classroom " +. ":\\n");
        io.print("Input name of Classroom: ");
        io.fflush(stdin);
        io.getline(name);
        ClassR.setNameClassroom(name);
    }
}

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_random_274(self):
        input = """
Class display {
    Val $dis_instance : Float;
    Var txt : Text;
    Start()
    {
        If (display::$dis_instance == null)  {
            dis_instance = Self;
        }
    }
    $Display(str: String) {
        txt.text = str;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_random_275(self):
        input = """
Class skill{
    Val name : String = "";
    skill(){
        If (Self.name == "") 
           { Self.name = "Skill";}
    }
    getName() {
        Return Self.name;
    }
    displayData() {}
}
Class factory_skil{
    $get_skill( i :all_skill ) {
        If (i == all_skill.FireBall) 
                {Return New FireBall();}
        Elseif (i == all_skill.WaterHealing) 
                {Return New WaterHealing();}
        Elseif (i == all_skill.RockShield )
                {Return New RockShield();}
        Else
                {Return New skill();}
    }
}
Class WaterHealing : skill{
    WaterHealing(){ Self.name = "WaterHealing";}
    displayData() {
        display.dis_instance.Display(Self.name);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_random_276(self):
        input = """
Class ButtonRun {
    Var my_skill : skill;
    InitButton(input_skill : Skill) {
        Self.my_skill = input_skill;
        txt.text = my_skill.getName();
    }
    clickButton() {
        my_skill.displayData();
    }
}
Class manager_skill {
    Val list_button :ButtonRun;
    manager_skill(all_skill : i) {
        list_button.InitButton(factory_skill.get_skill(i));
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_random_277(self):
        input = """
Class Bank {
    Val bankName : String;

    doSomething()
    {
        ####
    }
} 
Class Vietcombank : Bank{
    Student(ID : Int; name: String) {
            Self.studentID = ID;
            Self.name = name;
            numOfGrade = 0;
            sumMark = 0;
        }
        insertGrade( nameOfCourse: String;  mark : Int) {
            grades.setName(nameOfCourse);
            grades.setMark(mark);
            numOfGrade = numOfGrade+1;
            sumMark = sumMark+ mark;
        }
        setName(name : String) { Self.nameOfCourse = name; }
        setMark()  { Self.mark = mark;}
        getMark()      { Return mark; }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_random_278(self):
        input = """
Class Grade {
        
        Grade() {
            nameOfCourse = "";
            mark = 0;
        }
        Grade() {
            Val $num : Int = 10;
        }
}"""
        expect = "Error on line 9 col 16: $num"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_random_279(self):
        input = """
Class Student {
        Val studentID : Int;
        getAverage()  {
            Return (float)sumMark / numOfGrade;
        }
};"""
        expect = "Error on line 5 col 26: sumMark"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test_random_280(self):
        input = """
Class mainClass {
 main() {
  
    io.print("Enter number of Students? ");
    io.getInt(n);
        ## GET INFORMATION ##
        io.print("Input details for Student " +. (i + 1) +. ":\\n");
        students.insertGrade(nameMark, mark);
    n = 1;
    ## GET AVERAGE 
    for i = true to 1.234E-12 do {
        ##
        io.print("Which student average grade? ");
        io.getInt(n);
        If (n > 0) && (n <= students.size()) 
            {io.print("Average grade for student " +. n +. ": " +. students.getAverage());}
        Else
            {io.print("Don't have student " +. n +. endl); }         
        io.print("Mark of Grade " +. (j + 1) +. ": ");
        io.getInt(mark);
        students.insertGrade(nameMark, mark);
    n = 1;
        
        If (n == 1) {   io.print("-----\\n");}
    ##} ##
    Return 0;
}
}"""
        expect = "Error on line 8 col 57: +."
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_random_281(self):
        input = """
Class mainClass {
    $getline(a : String) {
        test = system.getIO();
        a = "";
        Foreach (i In 1 .. (a+b) ) {
            a = a+.test;
            test = system.getIO();
            If (test == "\\n") { Break; }
            Else  { Continue; }
        }
    }
    $fflush(s : typeIO) {
        If (s == stdin) {system.clear_console(); }
    }
$main() {
    io.print("Enter number of Students? ");
    io.getInt(n);
        ##GET INFORMATION ##
        io.print("Input details for Student " +. (1+2) +. ":\\n");
        students.push(New Student(ID, name));
       
   
 
  
        if (n == 1)    io.print("-----\\n");
    }
    Return 0;
}
}"""
        expect = "Error on line 20 col 55: +."
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_random_282(self):
        input = """
Class io {
    $getInt() {
        data = (system.checkIntLitForm(system.getIO())).toInt();
        a = data;
    }
    getFloat(a : Float) {
        data = (system.checkFloatLitForm(system.getIO())).toFloat();
        a = data;
    }    
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_random_283(self):
        input = """
Class heap {
minWaitingTime(n : Int;arrvalTime : Array[Int, 1]) {
    Val curTime : Int = 0;
    Var totalWaitTime : Int = 0;

    Return totalWaitTime;   
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_random_284(self):
        input = """
Class heap {
 minWaitingTime(arr: Array[]) {
     curTime = 0;

    return totalWaitTime;   
for i=((-1!=true||false)==(22/15)) downto xyz do {
        for i = 0 to n do {
            if ((curTime >= arrvalTime[i]) && ((serCos == -1) || (serTime > completeTime[i]))) then {
                    serCos = i;
                    serTime = completeTime[i];
            }
            if (min == -1) || (min > arrvalTime[i])    min = arrvalTime[i];
        }
        else    curTime = min;
        if n < 0 then break;
    }
}

}"""
        expect = "Error on line 3 col 27: ]"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_random_285(self):
        input = """
Class heap {
 minWaitingTime() {
     curTime = 0;
    Return totalWaitTime;   
}
 main() {
    {
         n = 3;
        arrvalTime = Array();
        completeTime = Array[3, 9, 6, 10, 8];

        io.pr(this.minWaitingTime(n, arrvalTime, completeTime));
    }
    io.pr(endl);
    Val var : Constructor;
}
}"""
        expect = "Error on line 11 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_random_286(self):
        input = """
Class student {
    $num_student: Int;
    $name : String;
    getSkill() {
        Return list_skill_special;
    }
    getNumStudent() {
        Return CLASS::$num_student;
    }
}"""
        expect = "Error on line 3 col 16: :"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_random_287(self):
        input = """
Class special_student : student {
    VAl list_skill_special : Array[String, 100];
    Val num_skill : Int;
    special_student(c : Classssss) {
        Self.student(name, id, c);
        num_skill = 0;
        updateSkill(skill : String) {
        Self.list_skill_special[123] = skill; 
        num_skill = num_skill + 1;
    }
    }
}"""
        expect = "Error on line 3 col 8: list_skill_special"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_random_288(self):
        input = """
Class  Class {
    
    student getdStudent() {
        if (option == True) 
            { Return New special_student(name,id,c);}
    }
}"""
        expect = "Error on line 2 col 7: Class"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_random_289(self):
        input = """
Class School {
    Val  $Class_name : Array[Int, -20];
    $getNumClass() {
        Return num_Class;
    }
    $updateClass(string name) {
        Class_name[num_Class] = name;
        num_Class = num_Class + 1;
    }
    setData(data : Int) {    }
}"""
        expect = "Error on line 3 col 34: -"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_random_290(self):
        input = """
Class makeSchool {
     main() {
        secondary(a : int) {
            io.fflush(stdin);
            io.getline(Class);
            If (Class != "-1") 
                School.updateClass(Class);
            else break;
        }
    }
    setNext(next : Node) {
        Self.next = next;
    }
}"""
        expect = "Error on line 4 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_random_291(self):
        input = """
Class makeSchool {
     main() {
        Foreach (i In 10 .. 1 By 2) {
            Val new_Class : String;
            io.fflush(stdin);
            io.getline(new_Class);
            If (new_Class != "-1") 
                { School.updateClass(new_Class); }
            Else { Break; }
        }
    }
     getNext() {
        Return next;
    }
    
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
        
    def test_random_292(self):
        input = """
Class getStudent {
     main() {
        io.getInt(n);
        Foreach (i In 0 .. n) {
            io.fflush(stdin);
            io.getBoolean(option);
            new_student = (School.getNameClass(range.random() % School.num_Class)).getStudent(name,id,option);
            Class.updateStudent(new_student);
        }
    }
}"""
        expect = "Error on line 9 col 12: Class"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_random_293(self):
        input = """
                Class a {
                Var r, s: Int = 1, 0;
                
                main(){
                    Val a, b: Float = 1.5E10, -10.;
                }
               
        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_random_294(self):
        input = """
Class linked_list {
    Val $node : start;
    linked_list(node: s) {
        Self.start = s;
    }
    $getNode(index: Int; node : n) {
        If (index == 0) 
            { Return n; }
        Else
           { Return Self.getNode(index - 1, n.getNext()); }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_random_295(self):
        input = """
Class mainFuncion {
    insert () {
        If (index == 0) 
           { n.setNext(root.getNext());}
        Else 
           { Self.insert(index - 1, root.getNext(), n)[Math.ceil(10, 5)[iphone.get()]] = 1; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_random_296(self):
        input = """
Class mainFuncion {
     insert () {
        If (index == 0) {
            root.setNext(n);
            If (index == 0)
            n.setNext(root.getNext());
        Else 
            { insert(index - 1, root.getNext(), n); }
        }
        Else
            { array.insert(index - 1, root.getNext(), n);} 
    }
}"""
        expect = "Error on line 7 col 12: n"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_arraylit_297(self):
        input = """
Class tesster {
    getCaculatorInt() {
        arr = Array(1, a - b, a * bb);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_arraylit_298(self):
        input = """
Class tesster {
    getCaculatorInt() {
        arr1sd = Array(a + b, a - b, a * b, a % b, a / b);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_arraylit_299(self):
        input = """
Class tesster {
    $getCaculatorInt($a,b : Int) {
        a132 = a + b;
        a2 = a- b;
        arr = Array(a1,a2,a3,a4,a5);
    }
}"""
        expect = "Error on line 3 col 21: $a"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test300(self):
        input = """
        Class a {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
        }"""
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.test(input,expect,300))
