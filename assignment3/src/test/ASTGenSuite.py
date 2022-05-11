import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
            Class B{
                $test(a, b, c : Int){
                }
            }
            
            Class Program{
                main(){
                    B::$test(1.1,2,3);
                    Return;
                }
            }
         """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,300))
   