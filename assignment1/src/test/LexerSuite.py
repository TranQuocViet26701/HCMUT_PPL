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
            120
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
            122
        ))
    def test_invalid_intlit2(self):
        """test invalid integer literal"""
        self.assertTrue(TestLexer.test(
            "00123 0b01010 0x0123 0b1100 0X0_AABB_CCDD 0B00_001_101 010101 000000 0b0010",
            "00,123,0b0,1010,0x0,123,0b1100,0X0,_AABB_CCDD,0B0,0,_001_101,010101,00,00,00,0b0,010,<EOF>",
            153
        ))    
    
    def test_invalid_intlit(self):
        """test invalid integer literal"""
        self.assertTrue(TestLexer.test(
            "0Xffffff 0xffffff 0Xaa_ff_00 0xGHJK 0x123_abc 0b123 0_00000000 0B_010101 0X_AAAAAA 0ABCD",
            "0,Xffffff,0,xffffff,0,Xaa_ff_00,0,xGHJK,0x123,_abc,0b1,23,0,_00000000,0,B_010101,0,X_AAAAAA,0,ABCD,<EOF>",
            121
        ))     
##======================================= Boollit ==========================================##         
    def test_valid_boollit(self):
        """test valid boolean literal"""
        self.assertTrue(TestLexer.test(
            "True False",
            "True,False,<EOF>",
            113
        ))     
    
    def test_invalid_boollit(self):
        """test invalid boolean literal"""
        self.assertTrue(TestLexer.test(
            "true false TRUE FALSE TruE FalsE TRUe FALSe truE falsE",
            "true,false,TRUE,FALSE,TruE,FalsE,TRUe,FALSe,truE,falsE,<EOF>",
            114
        ))     
##======================================= Floatlit ==========================================##
    def test_valid_floatlit(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "1.234 1.2e3 7E-10 1_234.567",
            "1.234,1.2e3,7E-10,1234.567,<EOF>",
            115
        ))     
    
    def test_valid_floatlit2(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "9.0 12e8 1. 0.33E-3 128e+42",
            "9.0,12e8,1.,0.33E-3,128e+42,<EOF>",
            116
        ))     
    
    def test_valid_floatlit3(self):
        """test valid float literal"""
        self.assertTrue(TestLexer.test(
            "123_456. 0.123_456 123_456.12_34_56 1.5e123_456 1_0.1_2e-1_000",
            "123456.,0.123,_456,123456.12,_34_56,1.5e123,_456,10.1,_2e,-,1000,<EOF>",
            117
        ))     
    
    def test_invalid_floatlit(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.test(
            "00001.1101010101000 000000001e-542400 000313121.e00031321132",
            "00,00,1.1101010101000,00,00,00,00,1e-542400,00,0313121,.e00031321132,<EOF>",
            118
        ))     
    
    def test_invalid_floatlit2(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.test(
            "1e 123e e123 e-132 -e123 123e1 .e10",
            "1,e,123,e,e123,e,-,132,-,e123,123e1,.e10,<EOF>",
            119
        ))     
##======================================= Stringlit ==========================================##
    def test_valid_stringlit(self):
        """test valid string lit"""
        self.assertTrue(TestLexer.test(
            """
            "He asked me: '"Where is John?'""
            "This is a string containing tab \t"
            """,
            """"He asked me: '"Where is John?'"","This is a string containing tab 	",<EOF>""",
            123
        ))     

    def test_illegal_escape_string(self):
        """test illegal escape string"""
        self.assertTrue(TestLexer.test(
            """
            "abc\\h def"
            """,
            """Illegal Escape In String: abc\h""",
            124
        ))     

    def test_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            """
            " hello lexer
            """,
            """Unclosed String:  hello lexer""",
            125
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
            126
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
            127
        ))
    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
            " abc \n xyz "
            " abc \\n xyz "
            """,
            """Unclosed String:  abc """,
            128
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
            " hello lexer \t \b \n \""     asdf
            """,
            """Unclosed String:  hello lexer 	  """,
            129
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
            r""""backspace  \b","formfeed   \f","return     \r","newline    \n","tab        \t","single quote       \'","backslash  \\ ",<EOF>""",
            130
        ))

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r""" Illegal"\a" """,
            r"""Illegal,Illegal Escape In String: \a""",
            131
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            " hey hey \c \d "
            """,
            """Illegal Escape In String:  hey hey \c""",
            132
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            " hey hey \s\d\\f "
            """,
            """Illegal Escape In String:  hey hey \s""",
            133
        ))

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
            "qwerty - xyz"
            "qwerty \ xyz"
            """,
            """"qwerty - xyz",Illegal Escape In String: qwerty \ """,
            134
        ))

    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
            "qwerty - xyz"
            "qwerty \yyz"
            """,
            """"qwerty - xyz",Illegal Escape In String: qwerty \y""",
            135
        ))

    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "abc\qwerty"
            """,
            """Illegal Escape In String: abc\q""",
            136
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "\a"
            """,
            """"",<EOF>""",
            137
        ))

    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "9juFvp3leS.dasd1f21.da1.pg56WPtopzJdR6D8GUyK^*&*13\o"
            """,
            """Illegal Escape In String: 9juFvp3leS.dasd1f21.da1.pg56WPtopzJdR6D8GUyK^*&*13\o""",
            138
        ))

    def test_illegal9(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
            "%&*%(%&(\#!\4))"
            """,
            """Illegal Escape In String: %&*%(%&(\#""", 
            139
        ))

    def test_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
            " abc \n  123 "
            """,
            """Unclosed String:  abc """,
            140
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
            141
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
            142
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
            143
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
            144
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
            145
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
            146
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
            147
        ))

    def test_mix_comment4(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is a block comment so # has no meaning here ##
            """,
            "<EOF>",
            148
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
            149
        ))

    def test_invalid_comment2(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            ##!/usr/bin/env python3##
            /## -*- coding: UTF-8 -*-
            ##""",
            "/,<EOF>",
            150
        ))

    def test_invalid_comment3(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            <!-- begin& wsf_resource_nodes -->
            <!-- end: wsf_resource_nodes -->
            """,
            "<,!,-,-,begin,Error Token &",
            151
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
            152
        ))       


