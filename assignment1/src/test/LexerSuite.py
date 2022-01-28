import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

##======================================= Indentifier ==========================================##      
    def test_valid_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "qwerty Qwerty02 _QweRty03",
            "qwerty,Qwerty02,_QweRty03,<EOF>",
            101
        ))
        
    def test_valid_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "id ID _id iD _Id i123",
            "id,ID,_id,iD,_Id,i123,<EOF>",
            102
        ))
        
    def test_valid_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "number_id Id_Number Number1_id _id_number _1id_Number",
            "number_id,Id_Number,Number1_id,_id_number,_1id_Number,<EOF>",
            103
        ))   
        
    def test_valid_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "_ i I ___i _i_ _1i__ Q__ ______1 i______1",
            "_,i,I,___i,_i_,_1i__,Q__,______1,i______1,<EOF>",
            104
        ))   
        
    def test_invalid_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "123id id-123 id&123 id% 123_",
            "123,id,id,-,123,id,Error Token &",
            105
        ))   
        
    def test_invalid_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(
            "id$ i$1 _$ 123$ id1_$$ 00$00",
            "id,Error Token $",
            106
        ))  
        
    def test_valid_dollar_identifier(self):
        """test dollar identifiers"""
        self.assertTrue(TestLexer.test(
            "$1 $a $A $_ $_a1a $1a1 $a1a $a_A",
            "$1,$a,$A,$_,$_a1a,$1a1,$a1a,$a_A,<EOF>",
            107
        ))   
        
    def test_valid_dollar_identifier2(self):
        """test dollar identifiers"""
        self.assertTrue(TestLexer.test(
            "$abc $123abc $___123 $_a_B_C $_1_a__bc $1a2b_3c $AbC__1_23",
            "$abc,$123abc,$___123,$_a_B_C,$_1_a__bc,$1a2b_3c,$AbC__1_23,<EOF>",
            108
        ))   
        
    def test_invalid_dollar_identifier(self):
        """test invalid dollar identifiers"""
        self.assertTrue(TestLexer.test(
            "$$ $_$ $--$ $:$",
            "Error Token $",
            109
        ))     
    
    def test_invalid_dollar_identifier2(self):
        """test invalid dollar identifiers"""
        self.assertTrue(TestLexer.test(
            "$id$1 $1__$ $id-1 $$__id",
            "$id,$1,$1__,Error Token $",
            110
        ))     
##======================================= Intlit ==========================================##     
    def test_valid_intlit(self):
        """test valid integer literal"""
        self.assertTrue(TestLexer.test(
            "1234 0123 0x1A 0b11111111 1_234_567",
            "1234,0123,0x1A,0b11111111,1234567,<EOF>",
            111
        ))     
        
    def test_valid_intlit2(self):
        """test valid integer literal"""
        self.assertTrue(TestLexer.test(
            "0 00 0b0 0B0 0x0 0X0",
            "0,00,0b0,0B0,0x0,0X0,<EOF>",
            112
        ))   
    
    def test_valid_intlit3(self):
        """test valid integer literal"""
        self.assertTrue(TestLexer.test(
            "0 1 0x01 0b01 001 1_000_000",
            "0,1,0x0,1,0b0,1,00,1,1000000,<EOF>",
            113
        ))   
    
    def test_valid_intlit4(self):
        """test valid integer literal"""
        self.assertTrue(TestLexer.test(
            """
            0001321 00000031231 000312312 00312 0 123 132 012 1 2 3 8912 
            000000000000000001 09132 321 
            000000000000001
            """,
            "00,01321,00,00,00,31231,00,0312312,00,312,0,123,132,012,1,2,3,8912,00,00,00,00,00,00,00,00,01,0,9132,321,00,00,00,00,00,00,00,1,<EOF>",
            114
        ))
    def test_invalid_intlit2(self):
        """test invalid integer literal"""
        self.assertTrue(TestLexer.test(
            "00123 0b01010 0x0123 0b1100 0X0_AABB_CCDD 0B00_001_101 010101 000000 0b0010",
            "00,123,0b0,1010,0x0,123,0b1100,0X0,_AABB_CCDD,0B0,0,_001_101,010101,00,00,00,0b0,010,<EOF>",
            115
        ))    
    
    def test_invalid_intlit(self):
        """test invalid integer literal"""
        self.assertTrue(TestLexer.test(
            "0Xffffff 0xffffff 0Xaa_ff_00 0xGHJK 0x123_abc 0b123 0_00000000 0B_010101 0X_AAAAAA 0ABCD",
            "0,Xffffff,0,xffffff,0,Xaa_ff_00,0,xGHJK,0x123,_abc,0b1,23,0,_00000000,0,B_010101,0,X_AAAAAA,0,ABCD,<EOF>",
            116
        ))     
##======================================= Boollit ==========================================##         
    def test_valid_boollit(self):
        """test valid boolean literal"""
        self.assertTrue(TestLexer.test(
            "True False",
            "True,False,<EOF>",
            117
        ))     
    
    def test_invalid_boollit(self):
        """test invalid boolean literal"""
        self.assertTrue(TestLexer.test(
            "true false TRUE FALSE TruE FalsE TRUe FALSe truE falsE",
            "true,false,TRUE,FALSE,TruE,FalsE,TRUe,FALSe,truE,falsE,<EOF>",
            118
        ))     
##======================================= Floatlit ==========================================##
    def test_valid_floatlit(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "1.234 1.2e3 7E-10 1_234.567",
            "1.234,1.2e3,7E-10,1234.567,<EOF>",
            119
        ))     
    
    def test_valid_floatlit2(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "9.0 12e8 1. 0.33E-3 128e+42",
            "9.0,12e8,1.,0.33E-3,128e+42,<EOF>",
            120
        ))     
    
    def test_valid_floatlit3(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "123_456. 0.123_456 123_456.12_34_56 1.5e123_456 1_0.1_2e-1_000",
            "123456.,0.123,_456,123456.12,_34_56,1.5e123,_456,10.1,_2e,-,1000,<EOF>",
            121
        ))     
    
    def test_invalid_floatlit(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.test(
            "00001.1101010101000 000000001e-542400 000313121.e00031321132",
            "00,00,1.1101010101000,00,00,00,00,1e-542400,00,0313121,.e00031321132,<EOF>",
            122
        ))     
    
    def test_invalid_floatlit2(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.test(
            "1e 123e e123 e-132 -e123 123e1 .e10",
            "1,e,123,e,e123,e,-,132,-,e123,123e1,.e10,<EOF>",
            123
        ))     
##======================================= Stringlit ==========================================##
    def test_valid_stringlit(self):
        """test valid string lit"""
        self.assertTrue(TestLexer.test(
            """
            "He asked me: '"Where is John?'""
            "This is a string containing tab \t"
            """,
            """He asked me: '"Where is John?'",Unclosed String: This is a string containing tab """,
            124
        ))     

    def test_illegal_escape_string(self):
        """test illegal escape string"""
        self.assertTrue(TestLexer.test(
            """
            "abc\\h def"
            """,
            """Illegal Escape In String: abc\h""",
            125
        ))     

    def test_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            """
            " hello lexer
            """,
            """Unclosed String:  hello lexer""",
            126
        )) 
        
    def test_unclose_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
            "Newline
            multiple lines
            "
            """,
            """Unclosed String: Newline""",
            127
        ))
        
    def test_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
            s = "string          '
            "a = 4
            g = 9
            """,
            """s,=,Unclosed String: string          '""",
            128
        ))
    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
            " abc \n xyz "
            " abc \\n xyz "
            """,
            """Unclosed String:  abc """,
            129
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
            " hello lexer \t \b \n \""     asdf
            """,
            """Unclosed String:  hello lexer """,
            130
        ))

    def test_escape3(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
            "backspace  \b"
            "formfeed   \f"
            "return     \r"
            "newline    \n"
            "tab        \t"
            "single quote       \'"
            "backslash  \\ "
            """,
            r"""backspace  \b,formfeed   \f,return     \r,newline    \n,tab        \t,single quote       \',backslash  \\ ,<EOF>""",
            131
        ))

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r""" Illegal"\a" """,
            r"""Illegal,Illegal Escape In String: \a""",
            132
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            " hey hey \c \d "
            """,
            """Illegal Escape In String:  hey hey \c""",
            133
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            " hey hey \s\d\\f "
            """,
            """Illegal Escape In String:  hey hey \s""",
            134
        ))

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
            "qwerty - xyz"
            "qwerty \ xyz"
            """,
            """qwerty - xyz,Illegal Escape In String: qwerty \ """,
            135
        ))

    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
            "qwerty - xyz"
            "qwerty \yyz"
            """,
            """qwerty - xyz,Illegal Escape In String: qwerty \y""",
            136
        ))

    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "abc\qwerty"
            """,
            """Illegal Escape In String: abc\q""",
            137
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "\a"
            """,
            """,<EOF>""",
            138
        ))

    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "9juFvp3leS.dasd1f21.da1.pg56WPtopzJdR6D8GUyK^*&*13\o"
            """,
            """Illegal Escape In String: 9juFvp3leS.dasd1f21.da1.pg56WPtopzJdR6D8GUyK^*&*13\o""",
            139
        ))

    def test_illegal9(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            "%&*%(%&(\#!\4))"
            """,
            """Illegal Escape In String: %&*%(%&(\#""", 
            140
        ))

    def test_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
            " abc \n  123 "
            """,
            """Unclosed String:  abc """,
            141
        ))
##======================================= Comment ==========================================##
    def test_comment(self):
        """Test Comment"""
        self.assertTrue(TestLexer.test(
            """
            ## comment ##
            ## comment ##
            """, 
            "<EOF>", 
            142
        ))

    def test_multiline_comment(self):
        """ Test Multi-line Comment """
        self.assertTrue(TestLexer.test(
            """
            ##  Comment with multiple lines
                Hello comments
                This is block comment
            ##
            """,
            "<EOF>",
            143
        ))

    def test_multiline_comment2(self):
        """ Test Multi-line Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is another way to do it, also in C.
            -- It is easier to do in editors that do not automatically indent the second
            -- through last lines of the comment one space from the first.
            -- It is also used in Holub's book, in rule 31.
            ##
            """,
            "<EOF>",
            144
        ))

    def test_multiline_comment3(self):
        """ Test Multi-line Comment """
        self.assertTrue(TestLexer.test(
            """
            ##--------------------------#
            -                           -
            - This is the comment body. -
            - Variation Two.            -
            -                           -
            #--------------------------##
            """,
            "<EOF>",
            145
        ))

    def test_mix_comment(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is a block comment ##
            ## This is a line comment##
            ## Comment with multiple lines
                Hello comments
            ##
            ##
                Comment multiple lines
            ##
            ## nest comments
                ## inline comment ##
            ## inline comment ##
            ##
            """,
            "inline,comment,inline,comment,<EOF>",
            146
        ))

    def test_mix_comment2(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is a
            ## multi-line
            comment.
            ##
            """,
            "multi,-,line,comment,.,Error Token #",
            147
        ))

    def test_mix_comment3(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ##/* /* # // /b/r/n */ */
            /*/* This is a block comment so # has no meaning here*/ */
            # This is comment ##
            """,
            "<EOF>",
            148
        ))

    def test_mix_comment4(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is a block comment so # has no meaning here ##
            """,
            "<EOF>",
            149
        ))

    def test_invalid_comment(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            ## inline comment \b \t
            ## is multiple lines
            ## inline comment ##
            """,
            "is,multiple,lines,<EOF>",
            150
        ))

    def test_invalid_comment2(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            ##!/usr/bin/env python3##
            /## -*- coding: UTF-8 -*-
            ##""",
            "/,<EOF>",
            151
        ))

    def test_invalid_comment3(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            <!-- begin& wsf_resource_nodes -->
            <!-- end: wsf_resource_nodes -->
            """,
            "<,!,-,-,begin,Error Token &",
            152
        ))

    def test_invalid_comment4(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            ##* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            ##* All characters after an exclamation mark are considered as comments *
            #!* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *#
            """,
            "*,All,characters,after,an,exclamation,mark,are,considered,as,comments,*,Error Token #",
            153
        ))       
    def test_escape4(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
    " hello hello lexer \t \b \n \""     asdf
    """,

            """Unclosed String:  hello hello lexer """,
            154
        ))
##======================================= Random ==========================================##
    def test_random(self):
        """ Test random"""
        self.assertTrue(TestLexer.test(
            """ Array("new","word"), """,
            """Array,(,new,,,word,),,,<EOF>""",
            155
        ))
# check WS and NEWLINE -> SKIP
    def test_ws_1(self):
        self.assertTrue(TestLexer.test(
            "abc\\bb\t\fabc",
            "abc,Error Token \\",
            156
        ))
    def test_ws_2(self):
        self.assertTrue(TestLexer.test(
            "a\n\nb\tc\fd\r\r\t\f\tac+123?",
            "a,b,c,d,ac,+,123,Error Token ?",
            157
        ))
    def test_stmt_1(self):
        self.assertTrue(TestLexer.test(
            "break continue;",
            "break,continue,;,<EOF>",
            158
        ))
    def test_stmt_2(self):
        self.assertTrue(TestLexer.test(
            "continue;",
            "continue,;,<EOF>",
            159
        ))
    def test_stmt_3(self):
        self.assertTrue(TestLexer.test(
            "If (a != b) \n Continuea=a+1;\n Elseif b=0;",
            "If,(,a,!=,b,),Continuea,=,a,+,1,;,Elseif,b,=,0,;,<EOF>",
            160
        ))
    def test_stmt_4(self):
        self.assertTrue(TestLexer.test(
            "Return newn then animal(a,b + c);",
            "Return,newn,then,animal,(,a,,,b,+,c,),;,<EOF>",
            161
        ))
    def test_stmt_5(self):
        self.assertTrue(TestLexer.test(
            "callFn then unction(a + b*c % (d+2));",
            "callFn,then,unction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",
            162
        ))
    def test_stmt_6(self):
        self.assertTrue(TestLexer.test(
            "a[7+9]=12;\nForeach (i In 1 .. 10 By 2) {\na[i]=a[i]+1;\ncalFunction(i);}",
            "a,[,7,+,9,],=,12,;,Foreach,(,i,In,1,..,10,By,2,),{,a,[,i,],=,a,[,i,],+,1,;,calFunction,(,i,),;,},<EOF>", 
            163
        ))
    def test_stmt_7(self):
        self.assertTrue(TestLexer.test(
            "a=1;\nb[1+c]=(True && !f || _z)!=false;",
            "a,=,1,;,b,[,1,+,c,],=,(,True,&&,!,f,||,_z,),!=,false,;,<EOF>",
            164
        ))
    def test_stmt_8(self):
        self.assertTrue(TestLexer.test(
            """animal.cat.talk(s + "abc");""",
            """animal,.,cat,.,talk,(,s,+,abc,),;,<EOF>""",
            165
        ))
    def test_stmt_9(self):
        self.assertTrue(TestLexer.test(
            "Return abc.getArea(1 True + 2) - (new obj()).arr[1];",
            "Return,abc,.,getArea,(,1,True,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",
            166
        ))
    def test_stmt_10(self):
        self.assertTrue(TestLexer.test(
            "Foreach (i In 1 .. 10 By 2) {\ncallFunction(); if a == arr[1] then Break; else callF();}",
            "Foreach,(,i,In,1,..,10,By,2,),{,callFunction,(,),;,if,a,==,arr,[,1,],then,Break,;,else,callF,(,),;,},<EOF>",
            167
        ))
    # test method declaration
    def test_met_de_1(self):
        self.assertTrue(TestLexer.test(
            "true(){}",
            "true,(,),{,},<EOF>",
            168
        ))
    def test_met_de_2(self):
        self.assertTrue(TestLexer.test(
            "cacul(int true falsea,b) {Return a +b;}",
            "cacul,(,int,true,falsea,,,b,),{,Return,a,+,b,;,},<EOF>",
            169
        ))
    def test_met_de_3(self):
        self.assertTrue(TestLexer.test(
            "classCheck(a,b : Int; c : Float) { If (a < b) {Return c;} Elseif {Return a + b;}}",
            "classCheck,(,a,,,b,:,Int,;,c,:,Float,),{,If,(,a,<,b,),{,Return,c,;,},Elseif,{,Return,a,+,b,;,},},<EOF>",
            170
        ))
    def test_met_de_4(self):
        self.assertTrue(TestLexer.test(
            "float ?function_test() {}",
            "float,Error Token ?",
            171
        ))
    def test_met_de_5(self):
        self.assertTrue(TestLexer.test(
            """void function_test(int a) {/*comment at here*/ getString("input\n");}""",
            """void,function_test,(,int,a,),{,/,*,comment,at,here,*,/,getString,(,Unclosed String: input""",
            172
        ))
    def test_met_de_6(self):
        self.assertTrue(TestLexer.test(
            "int add(int a,b) {return a+b;}\nfloat add(float a,b) {return a+b;}",
            "int,add,(,int,a,,,b,),{,return,a,+,b,;,},float,add,(,float,a,,,b,),{,return,a,+,b,;,},<EOF>", 
            173
        ))
    def test_met_de_7(self):
        self.assertTrue(TestLexer.test(
            "dog return(int h,t) {#make new dog with h and t\nif(h > t) then return new dog(h,t); else return nil;}#end function",
            "dog,return,(,int,h,,,t,),{,Error Token #", 
            174
        ))
    def test_met_de_8(self):
        self.assertTrue(TestLexer.test(
            "string return(string input; int l) {classSTR.getData(input);\nif (l > 0) then return getS()^input; else return input;}",
            "string,return,(,string,input,;,int,l,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),then,return,getS,(,),Error Token ^", 
            175
        ))
    def test_met_de_9(self):
        self.assertTrue(TestLexer.test(
            "int return(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}",
            "int,return,(,),{,int,data,=,Error Token ?",
            176
        ))
    def test_met_de_10(self):
        self.assertTrue(TestLexer.test(
            """ string get_Special_String(){return "abc\\g!!";}""",
            """string,get_Special_String,(,),{,return,Illegal Escape In String: abc\g""",
            177
        ))
    # test class
    def test_class_1(self):
        self.assertTrue(TestLexer.test(
            "Class A{df }",
            "Class,A,{,df,},<EOF>",
            178
        ))
    def test_class_2(self):
        self.assertTrue(TestLexer.test(
            "Class A Class : B {}",
            "Class,A,Class,:,B,{,},<EOF>",
            179
        ))
    def test_class_3(self):
        self.assertTrue(TestLexer.test(
            "Class A{Var a : Int = 5;##this is cmt##}",
            "Class,A,{,Var,a,:,Int,=,5,;,},<EOF>",
            180
        ))
    def test_class_4(self):
        self.assertTrue(TestLexer.test(
            """Class str{ static string[3] a_str= {"abc","a\rb","xyz "}}""",
            """Class,str,{,static,string,[,3,],a_str,=,{,abc,,,Unclosed String: a""", 
            181
        ))
    def test_class_5(self):
        self.assertTrue(TestLexer.test(
            "Class A {A(int a,b; float c) { callFunction(a + b - c);}}",
            "Class,A,{,A,(,int,a,,,b,;,float,c,),{,callFunction,(,a,+,b,-,c,),;,},},<EOF>", 
            182
        ))
    def test_class_6(self):
        self.assertTrue(TestLexer.test(
            """Class A {void Float foo() {Out.print("abc")}}\nClass B : A {int[5] arr;}""",
            """Class,A,{,void,Float,foo,(,),{,Out,.,print,(,abc,),},},Class,B,:,A,{,int,[,5,],arr,;,},<EOF>""",
            183
        ))
    def test_class_7(self):
        self.assertTrue(TestLexer.test(
            "Class A {B makeNew@B()C { return new B();}}",
            "Class,A,{,B,makeNew,Error Token @",
            184
        ))
    def test_C_8(self):
        self.assertTrue(TestLexer.test(
            "Class A{} Class B {} Class C : A{##cmt}",
            "Class,A,{,},Class,B,{,},Class,C,:,A,{,Error Token #",
            185))
    def test_class_9(self):
        self.assertTrue(TestLexer.test(
            "class A{for i downto := 1 downto 1.0E+123 do x := x + 2;#abc}",
            "class,A,{,for,i,downto,:,=,1,downto,1.0E+123,do,x,:,=,x,+,2,;,Error Token #", 
            186
        ))
    def test_class_10(self):
        self.assertTrue(TestLexer.test(
            """class downto obj_zz {if a == b them "string\\"\\"\\"" else "string\\s"}""",
            r"""class,downto,obj_zz,{,if,a,==,b,them,Illegal Escape In String: string\"""",
            187
        ))
    def test_random_1(self):
        self.assertTrue(TestLexer.test(
            "ascn downto +nad xmmc skc / 223 2.341 + sad - asc ___asint Initlit C++",
            "ascn,downto,+,nad,xmmc,skc,/,223,2.341,+,sad,-,asc,___asint,Initlit,C,+,+,<EOF>", 
            188
        ))
    def test_random_2(self):
        self.assertTrue(TestLexer.test(
            "check downto ant downto void ++ 2030/12 if a == b: z++; ",
            "check,downto,ant,downto,void,+,+,2030,/,12,if,a,==,b,:,z,+,+,;,<EOF>", 
            189
        ))
    def test_random_3(self):
        self.assertTrue(TestLexer.test(
            "#downto <stdio.h>\nint main(){}",
            "Error Token #",
            190
        ))
    def test_random_5(self):
        self.assertTrue(TestLexer.test(
            "1x  1z\n3y  main3t(x + z + y + 1) % 3(x + z + t + 1) % 3(x + y + t + 3) % 3(y + t + z + 3) % 3",
            "1,x,1,z,3,y,main3t,(,x,+,z,+,y,+,1,),%,3,(,x,+,z,+,t,+,1,),%,3,(,x,+,y,+,t,+,3,),%,3,(,y,+,t,+,z,+,3,),%,3,<EOF>",
            191
        ))
    def test_random_6(self):
        self.assertTrue(TestLexer.test(
            "class,A,{,void,foo,(,),{,print,(,abc,),},},class,B,extends,A,{,int,[,5,],arr,;,}",
            "class,,,A,,,{,,,void,,,foo,,,(,,,),,,{,,,print,,,(,,,abc,,,),,,},,,},,,class,,,B,,,extends,,,A,,,{,,,int,,,[,,,5,,,],,,arr,,,;,,,},<EOF>", 
            192
        ))
    def test_random_7(self):
        self.assertTrue(TestLexer.test(
            """#include <iostream>
using namespace std;
int main() {
    for (int x = 1; x < 10; x++)
        for (int y = 1; y < 10; y++)
            
                }
}
            """, 
            "Error Token #", 
            193
        ))
    def test_random_8(self):
        self.assertTrue(TestLexer.test(
            """if (N >= 10000)	num_of_thread = 1000;
	                                      else  if = 1;
            """,
            "if,(,N,>=,10000,),num_of_thread,=,1000,;,else,if,=,1,;,<EOF>", 
            194
        ))
    def test_random_9(self):
        input = """printf("PI = %f\n", 4.0 * incircle / N);
	printf("TIME = %d sec\n", (if int)(time(NULL) - start));
	if(&lock);
	pthread_exit(NULL);"""
        output = """printf,(,Unclosed String: PI = %f"""
        self.assertTrue(TestLexer.test(input,output,195))
    def test_random_10(self):
        input = """for(void void i = 0; i <= num_of_thread; i++) {
		if (i != num_of_thread)
			void(&threads[i], NULL, runner, (void *) loop_per_thread);
		else
			pthread_create(&threads[i], NULL, runner, (void *) (N % num_of_thread));
	}"""
        output = """for,(,void,void,i,=,0,;,i,<=,num_of_thread,;,i,+,+,),{,if,(,i,!=,num_of_thread,),void,(,Error Token &"""
        self.assertTrue(TestLexer.test(input, output, 196))
    def test_random_11(self):
        input ="""
        void add(int s, int t) {
        Interval newBus;
        else if (insertBus(newBus)) {
            insertData(1, s);
            insertData(0, t);newBus.start = s;
        newBus.end = t;
        }
    }"""
        output = "void,add,(,int,s,,,int,t,),{,Interval,newBus,;,else,if,(,insertBus,(,newBus,),),{,insertData,(,1,,,s,),;,insertData,(,0,,,t,),;,newBus,.,start,=,s,;,newBus,.,end,=,t,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,output,197))
    def test_random_12(self):
        input = """    void remove(int s, int t) {
        Interval deleteBus;
        deleteBus.start = s;
        deleteBus.end = t;
        else if (insertBus(deleteBus)) {
            insertData(1, s);
newBus.start = s;
        newBus.end = t;            findMax();
        }
    }
    int minPark() {
        return max;
    }"""
        output = "void,remove,(,int,s,,,int,t,),{,Interval,deleteBus,;,deleteBus,.,start,=,s,;,deleteBus,.,end,=,t,;,else,if,(,insertBus,(,deleteBus,),),{,insertData,(,1,,,s,),;,newBus,.,start,=,s,;,newBus,.,end,=,t,;,findMax,(,),;,},},int,minPark,(,),{,return,max,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 198))
    def test_random_13(self):
        input = """/*cmt cmt cmt##### /*/*findMax abcd #123123\n\\z\t \\" 123 abc##### \\" \n"""
        output = """/,*,cmt,cmt,cmt,Error Token #"""
        self.assertTrue(TestLexer.test(input, output, 199))
    def test_random_14(self):
        input = """Interval(findMax start = 0, int end = 0) {
            this->start = start;
            this->end = end;
        }
        bool operator<(Interval &a) {
            if (this->start < a.start)    return 1;
            if (this->start > a.start)    return 0;
findMax()            return 0;
        }
        
        }"""
        output = "Interval,(,findMax,start,=,0,,,int,end,=,0,),{,this,-,>,start,=,start,;,this,-,>,end,=,end,;,},bool,operator,<,(,Interval,Error Token &"
        self.assertTrue(TestLexer.test(input, output, 200))