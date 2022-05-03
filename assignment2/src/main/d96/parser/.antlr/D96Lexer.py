# Generated from d:\HCMUT_PPL\assignment2\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0263\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00b1\n\3\3\3\3\3\3\4\3\4\5\4\u00b7\n\4\3\4\3")
        buf.write("\4\7\4\u00bb\n\4\f\4\16\4\u00be\13\4\3\4\3\4\5\4\u00c2")
        buf.write("\n\4\3\4\3\4\7\4\u00c6\n\4\f\4\16\4\u00c9\13\4\5\4\u00cb")
        buf.write("\n\4\3\4\3\4\5\4\u00cf\n\4\3\4\6\4\u00d2\n\4\r\4\16\4")
        buf.write("\u00d3\3\4\3\4\7\4\u00d8\n\4\f\4\16\4\u00db\13\4\3\4\3")
        buf.write("\4\5\4\u00df\n\4\3\4\6\4\u00e2\n\4\r\4\16\4\u00e3\5\4")
        buf.write("\u00e6\n\4\3\4\3\4\3\5\3\5\5\5\u00ec\n\5\3\6\3\6\7\6\u00f0")
        buf.write("\n\6\f\6\16\6\u00f3\13\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3;\3;\3<\3<\7<\u01cf")
        buf.write("\n<\f<\16<\u01d2\13<\3=\3=\6=\u01d6\n=\r=\16=\u01d7\3")
        buf.write(">\3>\3?\3?\7?\u01de\n?\f?\16?\u01e1\13?\3?\3?\6?\u01e5")
        buf.write("\n?\r?\16?\u01e6\7?\u01e9\n?\f?\16?\u01ec\13?\3@\3@\3")
        buf.write("@\3@\7@\u01f2\n@\f@\16@\u01f5\13@\3@\3@\6@\u01f9\n@\r")
        buf.write("@\16@\u01fa\7@\u01fd\n@\f@\16@\u0200\13@\3A\3A\3A\7A\u0205")
        buf.write("\nA\fA\16A\u0208\13A\3A\3A\6A\u020c\nA\rA\16A\u020d\7")
        buf.write("A\u0210\nA\fA\16A\u0213\13A\3B\3B\3B\3B\7B\u0219\nB\f")
        buf.write("B\16B\u021c\13B\3B\3B\6B\u0220\nB\rB\16B\u0221\7B\u0224")
        buf.write("\nB\fB\16B\u0227\13B\3C\3C\3C\3C\5C\u022d\nC\3D\3D\3D")
        buf.write("\3E\3E\3E\3F\6F\u0236\nF\rF\16F\u0237\3F\3F\3G\6G\u023d")
        buf.write("\nG\rG\16G\u023e\3G\3G\3H\3H\7H\u0245\nH\fH\16H\u0248")
        buf.write("\13H\3H\3H\3H\3H\7H\u024e\nH\fH\16H\u0251\13H\3H\3H\5")
        buf.write("H\u0255\nH\3I\3I\7I\u0259\nI\fI\16I\u025c\13I\3I\3I\3")
        buf.write("I\3J\3J\3J\3\u009b\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2\u0081\2\u0083\2")
        buf.write("\u0085\2\u0087\2\u0089\2\u008b?\u008d@\u008fA\u0091B\u0093")
        buf.write("C\3\2\23\4\2DDdd\4\2ZZzz\4\2GGgg\4\2--//\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\3\2\63;\4\2\63;CH\4\2\62;CH\3\2")
        buf.write("\639\3\2\629\3\2\62\63\6\2\n\f\16\17$$^^\t\2))^^ddhhp")
        buf.write("pttvv\5\2\13\f\16\17\"\"\5\2\n\f\16\17^^\2\u0286\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u00b0\3\2\2\2\7\u00e5")
        buf.write("\3\2\2\2\t\u00eb\3\2\2\2\13\u00ed\3\2\2\2\r\u00f7\3\2")
        buf.write("\2\2\17\u00fd\3\2\2\2\21\u0106\3\2\2\2\23\u0109\3\2\2")
        buf.write("\2\25\u0110\3\2\2\2\27\u0115\3\2\2\2\31\u011d\3\2\2\2")
        buf.write("\33\u0122\3\2\2\2\35\u0128\3\2\2\2\37\u012e\3\2\2\2!\u0131")
        buf.write("\3\2\2\2#\u0135\3\2\2\2%\u013b\3\2\2\2\'\u0143\3\2\2\2")
        buf.write(")\u014a\3\2\2\2+\u0151\3\2\2\2-\u0156\3\2\2\2/\u015b\3")
        buf.write("\2\2\2\61\u0161\3\2\2\2\63\u0165\3\2\2\2\65\u0169\3\2")
        buf.write("\2\2\67\u0175\3\2\2\29\u0180\3\2\2\2;\u0184\3\2\2\2=\u0187")
        buf.write("\3\2\2\2?\u0189\3\2\2\2A\u018b\3\2\2\2C\u018d\3\2\2\2")
        buf.write("E\u018f\3\2\2\2G\u0191\3\2\2\2I\u0193\3\2\2\2K\u0196\3")
        buf.write("\2\2\2M\u0199\3\2\2\2O\u019c\3\2\2\2Q\u019e\3\2\2\2S\u01a1")
        buf.write("\3\2\2\2U\u01a3\3\2\2\2W\u01a6\3\2\2\2Y\u01a8\3\2\2\2")
        buf.write("[\u01ab\3\2\2\2]\u01af\3\2\2\2_\u01b2\3\2\2\2a\u01b5\3")
        buf.write("\2\2\2c\u01b7\3\2\2\2e\u01b9\3\2\2\2g\u01bb\3\2\2\2i\u01bd")
        buf.write("\3\2\2\2k\u01bf\3\2\2\2m\u01c1\3\2\2\2o\u01c3\3\2\2\2")
        buf.write("q\u01c5\3\2\2\2s\u01c8\3\2\2\2u\u01ca\3\2\2\2w\u01cc\3")
        buf.write("\2\2\2y\u01d3\3\2\2\2{\u01d9\3\2\2\2}\u01db\3\2\2\2\177")
        buf.write("\u01ed\3\2\2\2\u0081\u0201\3\2\2\2\u0083\u0214\3\2\2\2")
        buf.write("\u0085\u022c\3\2\2\2\u0087\u022e\3\2\2\2\u0089\u0231\3")
        buf.write("\2\2\2\u008b\u0235\3\2\2\2\u008d\u023c\3\2\2\2\u008f\u0254")
        buf.write("\3\2\2\2\u0091\u0256\3\2\2\2\u0093\u0260\3\2\2\2\u0095")
        buf.write("\u0096\7%\2\2\u0096\u0097\7%\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009a\13\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7%\2\2\u009f")
        buf.write("\u00a0\7%\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b\2\2\2")
        buf.write("\u00a2\4\3\2\2\2\u00a3\u00b1\7\62\2\2\u00a4\u00a5\7\62")
        buf.write("\2\2\u00a5\u00b1\7\62\2\2\u00a6\u00a7\7\62\2\2\u00a7\u00a8")
        buf.write("\t\2\2\2\u00a8\u00b1\7\62\2\2\u00a9\u00aa\7\62\2\2\u00aa")
        buf.write("\u00ab\t\3\2\2\u00ab\u00b1\7\62\2\2\u00ac\u00b1\5\u0083")
        buf.write("B\2\u00ad\u00b1\5}?\2\u00ae\u00b1\5\177@\2\u00af\u00b1")
        buf.write("\5\u0081A\2\u00b0\u00a3\3\2\2\2\u00b0\u00a4\3\2\2\2\u00b0")
        buf.write("\u00a6\3\2\2\2\u00b0\u00a9\3\2\2\2\u00b0\u00ac\3\2\2\2")
        buf.write("\u00b0\u00ad\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\b\3\3\2\u00b3\6")
        buf.write("\3\2\2\2\u00b4\u00b7\7\62\2\2\u00b5\u00b7\5}?\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00bc\7\60\2\2\u00b9\u00bb\5{>\2\u00ba\u00b9\3")
        buf.write("\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bd\u00e6\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf")
        buf.write("\u00c2\7\62\2\2\u00c0\u00c2\5}?\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\u00ca\3\2\2\2\u00c3\u00c7\7")
        buf.write("\60\2\2\u00c4\u00c6\5{>\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00c3\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\t")
        buf.write("\4\2\2\u00cd\u00cf\t\5\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00d2\5{>\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00e6\3\2\2\2\u00d5\u00d9\7\60\2")
        buf.write("\2\u00d6\u00d8\5{>\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3")
        buf.write("\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\t\4\2\2\u00dd")
        buf.write("\u00df\t\5\2\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e1\3\2\2\2\u00e0\u00e2\5{>\2\u00e1\u00e0\3\2")
        buf.write("\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00b6\3\2\2\2\u00e5")
        buf.write("\u00c1\3\2\2\2\u00e5\u00d5\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\b\4\4\2\u00e8\b\3\2\2\2\u00e9\u00ec\5\31")
        buf.write("\r\2\u00ea\u00ec\5\33\16\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\n\3\2\2\2\u00ed\u00f1\7$\2\2\u00ee\u00f0")
        buf.write("\5\u0085C\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7$\2\2\u00f5\u00f6\b")
        buf.write("\6\5\2\u00f6\f\3\2\2\2\u00f7\u00f8\7D\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7m\2\2\u00fc\16\3\2\2\2\u00fd\u00fe\7E\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\20\3\2\2\2\u0106\u0107\7K\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\22\3\2\2\2\u0109\u010a\7G\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7h\2\2\u010f\24\3\2\2\2\u0110\u0111")
        buf.write("\7G\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\26\3\2\2\2\u0115\u0116\7H\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7t\2\2\u0118\u0119\7g\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7e\2\2\u011b\u011c\7j\2\2\u011c\30")
        buf.write("\3\2\2\2\u011d\u011e\7V\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7g\2\2\u0121\32\3\2\2\2\u0122\u0123")
        buf.write("\7H\2\2\u0123\u0124\7c\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7u\2\2\u0126\u0127\7g\2\2\u0127\34\3\2\2\2\u0128\u0129")
        buf.write("\7C\2\2\u0129\u012a\7t\2\2\u012a\u012b\7t\2\2\u012b\u012c")
        buf.write("\7c\2\2\u012c\u012d\7{\2\2\u012d\36\3\2\2\2\u012e\u012f")
        buf.write("\7K\2\2\u012f\u0130\7p\2\2\u0130 \3\2\2\2\u0131\u0132")
        buf.write("\7K\2\2\u0132\u0133\7p\2\2\u0133\u0134\7v\2\2\u0134\"")
        buf.write("\3\2\2\2\u0135\u0136\7H\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\u0139\7c\2\2\u0139\u013a\7v\2\2\u013a$\3")
        buf.write("\2\2\2\u013b\u013c\7D\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7n\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7c\2\2\u0141\u0142\7p\2\2\u0142&\3\2\2\2\u0143\u0144")
        buf.write("\7U\2\2\u0144\u0145\7v\2\2\u0145\u0146\7t\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7p\2\2\u0148\u0149\7i\2\2\u0149(\3")
        buf.write("\2\2\2\u014a\u014b\7T\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7w\2\2\u014e\u014f\7t\2\2\u014f\u0150")
        buf.write("\7p\2\2\u0150*\3\2\2\2\u0151\u0152\7U\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7n\2\2\u0154\u0155\7h\2\2\u0155,\3")
        buf.write("\2\2\2\u0156\u0157\7P\2\2\u0157\u0158\7w\2\2\u0158\u0159")
        buf.write("\7n\2\2\u0159\u015a\7n\2\2\u015a.\3\2\2\2\u015b\u015c")
        buf.write("\7E\2\2\u015c\u015d\7n\2\2\u015d\u015e\7c\2\2\u015e\u015f")
        buf.write("\7u\2\2\u015f\u0160\7u\2\2\u0160\60\3\2\2\2\u0161\u0162")
        buf.write("\7X\2\2\u0162\u0163\7c\2\2\u0163\u0164\7n\2\2\u0164\62")
        buf.write("\3\2\2\2\u0165\u0166\7X\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\64\3\2\2\2\u0169\u016a\7E\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7p\2\2\u016c\u016d\7u\2\2\u016d\u016e")
        buf.write("\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170\7w\2\2\u0170\u0171")
        buf.write("\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\66\3\2\2\2\u0175\u0176\7F\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177\u0178\7u\2\2\u0178\u0179\7v\2\2\u0179\u017a")
        buf.write("\7t\2\2\u017a\u017b\7w\2\2\u017b\u017c\7e\2\2\u017c\u017d")
        buf.write("\7v\2\2\u017d\u017e\7q\2\2\u017e\u017f\7t\2\2\u017f8\3")
        buf.write("\2\2\2\u0180\u0181\7P\2\2\u0181\u0182\7g\2\2\u0182\u0183")
        buf.write("\7y\2\2\u0183:\3\2\2\2\u0184\u0185\7D\2\2\u0185\u0186")
        buf.write("\7{\2\2\u0186<\3\2\2\2\u0187\u0188\7-\2\2\u0188>\3\2\2")
        buf.write("\2\u0189\u018a\7/\2\2\u018a@\3\2\2\2\u018b\u018c\7,\2")
        buf.write("\2\u018cB\3\2\2\2\u018d\u018e\7\61\2\2\u018eD\3\2\2\2")
        buf.write("\u018f\u0190\7\'\2\2\u0190F\3\2\2\2\u0191\u0192\7#\2\2")
        buf.write("\u0192H\3\2\2\2\u0193\u0194\7(\2\2\u0194\u0195\7(\2\2")
        buf.write("\u0195J\3\2\2\2\u0196\u0197\7~\2\2\u0197\u0198\7~\2\2")
        buf.write("\u0198L\3\2\2\2\u0199\u019a\7?\2\2\u019a\u019b\7?\2\2")
        buf.write("\u019bN\3\2\2\2\u019c\u019d\7?\2\2\u019dP\3\2\2\2\u019e")
        buf.write("\u019f\7#\2\2\u019f\u01a0\7?\2\2\u01a0R\3\2\2\2\u01a1")
        buf.write("\u01a2\7@\2\2\u01a2T\3\2\2\2\u01a3\u01a4\7@\2\2\u01a4")
        buf.write("\u01a5\7?\2\2\u01a5V\3\2\2\2\u01a6\u01a7\7>\2\2\u01a7")
        buf.write("X\3\2\2\2\u01a8\u01a9\7>\2\2\u01a9\u01aa\7?\2\2\u01aa")
        buf.write("Z\3\2\2\2\u01ab\u01ac\7?\2\2\u01ac\u01ad\7?\2\2\u01ad")
        buf.write("\u01ae\7\60\2\2\u01ae\\\3\2\2\2\u01af\u01b0\7-\2\2\u01b0")
        buf.write("\u01b1\7\60\2\2\u01b1^\3\2\2\2\u01b2\u01b3\7<\2\2\u01b3")
        buf.write("\u01b4\7<\2\2\u01b4`\3\2\2\2\u01b5\u01b6\7*\2\2\u01b6")
        buf.write("b\3\2\2\2\u01b7\u01b8\7+\2\2\u01b8d\3\2\2\2\u01b9\u01ba")
        buf.write("\7}\2\2\u01baf\3\2\2\2\u01bb\u01bc\7\177\2\2\u01bch\3")
        buf.write("\2\2\2\u01bd\u01be\7]\2\2\u01bej\3\2\2\2\u01bf\u01c0\7")
        buf.write("_\2\2\u01c0l\3\2\2\2\u01c1\u01c2\7=\2\2\u01c2n\3\2\2\2")
        buf.write("\u01c3\u01c4\7<\2\2\u01c4p\3\2\2\2\u01c5\u01c6\7\60\2")
        buf.write("\2\u01c6\u01c7\7\60\2\2\u01c7r\3\2\2\2\u01c8\u01c9\7\60")
        buf.write("\2\2\u01c9t\3\2\2\2\u01ca\u01cb\7.\2\2\u01cbv\3\2\2\2")
        buf.write("\u01cc\u01d0\t\6\2\2\u01cd\u01cf\t\7\2\2\u01ce\u01cd\3")
        buf.write("\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1x\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5")
        buf.write("\7&\2\2\u01d4\u01d6\t\7\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8z\3\2\2\2\u01d9\u01da\t\b\2\2\u01da|\3\2\2\2\u01db")
        buf.write("\u01df\t\t\2\2\u01dc\u01de\5{>\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01ea\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4\7")
        buf.write("a\2\2\u01e3\u01e5\5{>\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e9\3\2\2\2\u01e8\u01e2\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb~\3\2\2")
        buf.write("\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7\62\2\2\u01ee\u01ef")
        buf.write("\t\3\2\2\u01ef\u01f3\t\n\2\2\u01f0\u01f2\t\13\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f3\u01f4\3\2\2\2\u01f4\u01fe\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f6\u01f8\7a\2\2\u01f7\u01f9\t\13\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01f6\3\2\2\2")
        buf.write("\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3")
        buf.write("\2\2\2\u01ff\u0080\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202")
        buf.write("\7\62\2\2\u0202\u0206\t\f\2\2\u0203\u0205\t\r\2\2\u0204")
        buf.write("\u0203\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0211\3\2\2\2\u0208\u0206\3")
        buf.write("\2\2\2\u0209\u020b\7a\2\2\u020a\u020c\t\r\2\2\u020b\u020a")
        buf.write("\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u0209\3\2\2\2")
        buf.write("\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3")
        buf.write("\2\2\2\u0212\u0082\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0215")
        buf.write("\7\62\2\2\u0215\u0216\t\2\2\2\u0216\u021a\7\63\2\2\u0217")
        buf.write("\u0219\t\16\2\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2")
        buf.write("\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u0225")
        buf.write("\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u021f\7a\2\2\u021e")
        buf.write("\u0220\t\16\2\2\u021f\u021e\3\2\2\2\u0220\u0221\3\2\2")
        buf.write("\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0224")
        buf.write("\3\2\2\2\u0223\u021d\3\2\2\2\u0224\u0227\3\2\2\2\u0225")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0084\3\2\2\2")
        buf.write("\u0227\u0225\3\2\2\2\u0228\u022d\5\u0087D\2\u0229\u022d")
        buf.write("\n\17\2\2\u022a\u022b\7)\2\2\u022b\u022d\7$\2\2\u022c")
        buf.write("\u0228\3\2\2\2\u022c\u0229\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022d\u0086\3\2\2\2\u022e\u022f\7^\2\2\u022f\u0230\t")
        buf.write("\20\2\2\u0230\u0088\3\2\2\2\u0231\u0232\7^\2\2\u0232\u0233")
        buf.write("\n\20\2\2\u0233\u008a\3\2\2\2\u0234\u0236\t\21\2\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\b")
        buf.write("F\2\2\u023a\u008c\3\2\2\2\u023b\u023d\7\f\2\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\bG\2\2")
        buf.write("\u0241\u008e\3\2\2\2\u0242\u0246\7$\2\2\u0243\u0245\5")
        buf.write("\u0085C\2\u0244\u0243\3\2\2\2\u0245\u0248\3\2\2\2\u0246")
        buf.write("\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0249\3\2\2\2")
        buf.write("\u0248\u0246\3\2\2\2\u0249\u024a\7\2\2\3\u024a\u0255\b")
        buf.write("H\6\2\u024b\u024f\7$\2\2\u024c\u024e\5\u0085C\2\u024d")
        buf.write("\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2")
        buf.write("\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3")
        buf.write("\2\2\2\u0252\u0253\t\22\2\2\u0253\u0255\bH\7\2\u0254\u0242")
        buf.write("\3\2\2\2\u0254\u024b\3\2\2\2\u0255\u0090\3\2\2\2\u0256")
        buf.write("\u025a\7$\2\2\u0257\u0259\5\u0085C\2\u0258\u0257\3\2\2")
        buf.write("\2\u0259\u025c\3\2\2\2\u025a\u0258\3\2\2\2\u025a\u025b")
        buf.write("\3\2\2\2\u025b\u025d\3\2\2\2\u025c\u025a\3\2\2\2\u025d")
        buf.write("\u025e\5\u0089E\2\u025e\u025f\bI\b\2\u025f\u0092\3\2\2")
        buf.write("\2\u0260\u0261\13\2\2\2\u0261\u0262\bJ\t\2\u0262\u0094")
        buf.write("\3\2\2\2\'\2\u009b\u00b0\u00b6\u00bc\u00c1\u00c7\u00ca")
        buf.write("\u00ce\u00d3\u00d9\u00de\u00e3\u00e5\u00eb\u00f1\u01d0")
        buf.write("\u01d7\u01df\u01e6\u01ea\u01f3\u01fa\u01fe\u0206\u020d")
        buf.write("\u0211\u021a\u0221\u0225\u022c\u0237\u023e\u0246\u024f")
        buf.write("\u0254\u025a\n\b\2\2\3\3\2\3\4\3\3\6\4\3H\5\3H\6\3I\7")
        buf.write("\3J\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLLIT = 4
    STRINGLIT = 5
    BREAK = 6
    CONTINUE = 7
    IF = 8
    ELSEIF = 9
    ELSE = 10
    FOREACH = 11
    TRUE = 12
    FALSE = 13
    ARRAY = 14
    IN = 15
    INT = 16
    FLOAT = 17
    BOOLEAN = 18
    STRING = 19
    RETURN = 20
    SELF = 21
    NULL = 22
    CLASS = 23
    VAL = 24
    VAR = 25
    CONSTRUCTOR = 26
    DESTRUCTOR = 27
    NEW = 28
    BY = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    ASSIGN = 39
    NOT_EQUAL = 40
    GT = 41
    GTE = 42
    LT = 43
    LTE = 44
    COMPARE_STRING = 45
    CONCATE = 46
    TWOCOLON = 47
    LB = 48
    RB = 49
    LP = 50
    RP = 51
    LSB = 52
    RSB = 53
    SEMI = 54
    COLON = 55
    TWODOT = 56
    DOT = 57
    CM = 58
    ID = 59
    DOLLAR_ID = 60
    WS = 61
    NEWLINE = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Self'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", 
            "'+.'", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "':'", "'..'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "SELF", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "GT", "GTE", 
            "LT", "LTE", "COMPARE_STRING", "CONCATE", "TWOCOLON", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COLON", "TWODOT", "DOT", 
            "CM", "ID", "DOLLAR_ID", "WS", "NEWLINE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "SELF", "NULL", "CLASS", "VAL", "VAR", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "GT", "GTE", "LT", "LTE", "COMPARE_STRING", 
                  "CONCATE", "TWOCOLON", "LB", "RB", "LP", "RP", "LSB", 
                  "RSB", "SEMI", "COLON", "TWODOT", "DOT", "CM", "ID", "DOLLAR_ID", 
                  "DIGIT", "NONEZERO_DECIMAL", "NONEZERO_HEXADECIMAL", "NONEZERO_OCTAL", 
                  "NONEZERO_BINARY", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "WS", "NEWLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    global countName
    countName = 0
    global countValue 
    countValue = 0


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INTLIT_action 
            actions[2] = self.FLOATLIT_action 
            actions[4] = self.STRINGLIT_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UncloseString(self.text[1:])
     

        if actionIndex == 4:
             raise UncloseString(self.text[1:-1]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise IllegalEscape(self.text[1:] )
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
             raise ErrorToken(self.text) 
     


