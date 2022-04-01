# Generated from d:\HCMUT_PPL\Programming Code\Week 1 - Lexer\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("\u0093\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2")
        buf.write("\7\2\34\n\2\f\2\16\2\37\13\2\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\'\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\60\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3B\n\3\3\4\5\4E\n\4\3\4\3\4\3\4\6\4J\n\4\r\4")
        buf.write("\16\4K\5\4N\n\4\3\4\3\4\5\4R\n\4\3\4\3\4\7\4V\n\4\f\4")
        buf.write("\16\4Y\13\4\3\5\3\5\3\5\6\5^\n\5\r\5\16\5_\5\5b\n\5\3")
        buf.write("\6\3\6\3\6\3\6\7\6h\n\6\f\6\16\6k\13\6\3\6\3\6\3\7\3\7")
        buf.write("\7\7q\n\7\f\7\16\7t\13\7\3\7\3\7\6\7x\n\7\r\7\16\7y\7")
        buf.write("\7|\n\7\f\7\16\7\177\13\7\3\7\3\7\5\7\u0083\n\7\3\b\6")
        buf.write("\b\u0086\n\b\r\b\16\b\u0087\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\2\13\6\r\7\17\b\21")
        buf.write("\t\23\n\25\13\27\f\3\2\b\3\2c|\4\2\62;c|\3\2\63;\3\2\62")
        buf.write(";\3\2))\5\2\13\f\17\17\"\"\2\u00a8\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3")
        buf.write("\31\3\2\2\2\5&\3\2\2\2\7D\3\2\2\2\ta\3\2\2\2\13c\3\2\2")
        buf.write("\2\r\u0082\3\2\2\2\17\u0085\3\2\2\2\21\u008b\3\2\2\2\23")
        buf.write("\u008d\3\2\2\2\25\u008f\3\2\2\2\27\u0091\3\2\2\2\31\35")
        buf.write("\t\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2\34\37\3\2\2\2\35")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\4\3\2\2\2\37\35\3\2\2\2 ")
        buf.write("\'\7\62\2\2!\"\t\4\2\2\"\'\t\5\2\2#$\t\4\2\2$%\t\5\2\2")
        buf.write("%\'\t\5\2\2& \3\2\2\2&!\3\2\2\2&#\3\2\2\2\'(\3\2\2\2(")
        buf.write("/\7\60\2\2)\60\7\62\2\2*+\t\4\2\2+\60\t\5\2\2,-\t\4\2")
        buf.write("\2-.\t\5\2\2.\60\t\5\2\2/)\3\2\2\2/*\3\2\2\2/,\3\2\2\2")
        buf.write("\60\61\3\2\2\2\618\7\60\2\2\629\7\62\2\2\63\64\t\4\2\2")
        buf.write("\649\t\5\2\2\65\66\t\4\2\2\66\67\t\5\2\2\679\t\5\2\28")
        buf.write("\62\3\2\2\28\63\3\2\2\28\65\3\2\2\29:\3\2\2\2:A\7\60\2")
        buf.write("\2;B\7\62\2\2<=\t\4\2\2=B\t\5\2\2>?\t\4\2\2?@\t\5\2\2")
        buf.write("@B\t\5\2\2A;\3\2\2\2A<\3\2\2\2A>\3\2\2\2B\6\3\2\2\2CE")
        buf.write("\7/\2\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2\2FM\5\t\5\2GI\7\60")
        buf.write("\2\2HJ\t\5\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2")
        buf.write("LN\3\2\2\2MG\3\2\2\2MN\3\2\2\2NO\3\2\2\2OQ\7g\2\2PR\7")
        buf.write("/\2\2QP\3\2\2\2QR\3\2\2\2RS\3\2\2\2SW\t\4\2\2TV\t\5\2")
        buf.write("\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\b\3\2\2\2")
        buf.write("YW\3\2\2\2Zb\t\5\2\2[]\t\4\2\2\\^\t\5\2\2]\\\3\2\2\2^")
        buf.write("_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2aZ\3\2\2\2a[\3")
        buf.write("\2\2\2b\n\3\2\2\2ci\t\6\2\2dh\n\6\2\2ef\t\6\2\2fh\t\6")
        buf.write("\2\2gd\3\2\2\2ge\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2")
        buf.write("jl\3\2\2\2ki\3\2\2\2lm\t\6\2\2m\f\3\2\2\2nr\t\4\2\2oq")
        buf.write("\t\5\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s}\3\2")
        buf.write("\2\2tr\3\2\2\2uw\7a\2\2vx\t\5\2\2wv\3\2\2\2xy\3\2\2\2")
        buf.write("yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{u\3\2\2\2|\177\3\2\2\2")
        buf.write("}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080")
        buf.write("\u0083\b\7\2\2\u0081\u0083\7\62\2\2\u0082n\3\2\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\16\3\2\2\2\u0084\u0086\t\7\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\b")
        buf.write("\b\3\2\u008a\20\3\2\2\2\u008b\u008c\13\2\2\2\u008c\22")
        buf.write("\3\2\2\2\u008d\u008e\13\2\2\2\u008e\24\3\2\2\2\u008f\u0090")
        buf.write("\13\2\2\2\u0090\26\3\2\2\2\u0091\u0092\13\2\2\2\u0092")
        buf.write("\30\3\2\2\2\26\2\35&/8ADKMQW_agiry}\u0082\u0087\4\3\7")
        buf.write("\2\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    IPV4 = 2
    REAL = 3
    STRING = 4
    INT_PHP = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "IPV4", "REAL", "STRING", "INT_PHP", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "IPV4", "REAL", "DECIMAL", "STRING", "INT_PHP", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.INT_PHP_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_PHP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     


