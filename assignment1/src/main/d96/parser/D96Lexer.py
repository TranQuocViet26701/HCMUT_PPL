# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0267\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u00b3\n\3\3\3\3\3\3\4\3\4\5\4\u00b9\n\4")
        buf.write("\3\4\3\4\7\4\u00bd\n\4\f\4\16\4\u00c0\13\4\3\4\3\4\5\4")
        buf.write("\u00c4\n\4\3\4\3\4\7\4\u00c8\n\4\f\4\16\4\u00cb\13\4\5")
        buf.write("\4\u00cd\n\4\3\4\3\4\5\4\u00d1\n\4\3\4\6\4\u00d4\n\4\r")
        buf.write("\4\16\4\u00d5\3\4\3\4\7\4\u00da\n\4\f\4\16\4\u00dd\13")
        buf.write("\4\3\4\3\4\5\4\u00e1\n\4\3\4\6\4\u00e4\n\4\r\4\16\4\u00e5")
        buf.write("\5\4\u00e8\n\4\3\4\3\4\3\5\3\5\5\5\u00ee\n\5\3\6\3\6\7")
        buf.write("\6\u00f2\n\6\f\6\16\6\u00f5\13\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\7=\u01d3\n=\f=\16=\u01d6\13=\3>\3>\6")
        buf.write(">\u01da\n>\r>\16>\u01db\3?\3?\3@\3@\7@\u01e2\n@\f@\16")
        buf.write("@\u01e5\13@\3@\3@\6@\u01e9\n@\r@\16@\u01ea\7@\u01ed\n")
        buf.write("@\f@\16@\u01f0\13@\3A\3A\3A\3A\7A\u01f6\nA\fA\16A\u01f9")
        buf.write("\13A\3A\3A\6A\u01fd\nA\rA\16A\u01fe\7A\u0201\nA\fA\16")
        buf.write("A\u0204\13A\3B\3B\3B\7B\u0209\nB\fB\16B\u020c\13B\3B\3")
        buf.write("B\6B\u0210\nB\rB\16B\u0211\7B\u0214\nB\fB\16B\u0217\13")
        buf.write("B\3C\3C\3C\3C\7C\u021d\nC\fC\16C\u0220\13C\3C\3C\6C\u0224")
        buf.write("\nC\rC\16C\u0225\7C\u0228\nC\fC\16C\u022b\13C\3D\3D\3")
        buf.write("D\3D\5D\u0231\nD\3E\3E\3E\3F\3F\3F\3G\6G\u023a\nG\rG\16")
        buf.write("G\u023b\3G\3G\3H\6H\u0241\nH\rH\16H\u0242\3H\3H\3I\3I")
        buf.write("\7I\u0249\nI\fI\16I\u024c\13I\3I\3I\3I\3I\7I\u0252\nI")
        buf.write("\fI\16I\u0255\13I\3I\3I\5I\u0259\nI\3J\3J\7J\u025d\nJ")
        buf.write("\fJ\16J\u0260\13J\3J\3J\3J\3K\3K\3K\3\u009d\2L\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d@\u008fA\u0091B\u0093C\u0095D\3\2\23\4\2DDdd\4")
        buf.write("\2ZZzz\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\3\2\63;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3\2\62\63")
        buf.write("\6\2\n\f\16\17$$^^\t\2))^^ddhhppttvv\5\2\13\f\16\17\"")
        buf.write("\"\4\2\f\f\17\17\2\u028a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\3\u0097\3\2\2\2\5\u00b2\3\2\2\2\7\u00e7\3\2\2\2\t\u00ed")
        buf.write("\3\2\2\2\13\u00ef\3\2\2\2\r\u00f9\3\2\2\2\17\u00ff\3\2")
        buf.write("\2\2\21\u0108\3\2\2\2\23\u010b\3\2\2\2\25\u0112\3\2\2")
        buf.write("\2\27\u0117\3\2\2\2\31\u011f\3\2\2\2\33\u0124\3\2\2\2")
        buf.write("\35\u012a\3\2\2\2\37\u0130\3\2\2\2!\u0133\3\2\2\2#\u0137")
        buf.write("\3\2\2\2%\u013d\3\2\2\2\'\u0145\3\2\2\2)\u014c\3\2\2\2")
        buf.write("+\u0153\3\2\2\2-\u0158\3\2\2\2/\u015d\3\2\2\2\61\u0163")
        buf.write("\3\2\2\2\63\u0167\3\2\2\2\65\u016b\3\2\2\2\67\u0177\3")
        buf.write("\2\2\29\u0182\3\2\2\2;\u0186\3\2\2\2=\u0189\3\2\2\2?\u018b")
        buf.write("\3\2\2\2A\u018d\3\2\2\2C\u018f\3\2\2\2E\u0191\3\2\2\2")
        buf.write("G\u0193\3\2\2\2I\u0195\3\2\2\2K\u0198\3\2\2\2M\u019b\3")
        buf.write("\2\2\2O\u019e\3\2\2\2Q\u01a0\3\2\2\2S\u01a3\3\2\2\2U\u01a5")
        buf.write("\3\2\2\2W\u01a8\3\2\2\2Y\u01aa\3\2\2\2[\u01ad\3\2\2\2")
        buf.write("]\u01b1\3\2\2\2_\u01b4\3\2\2\2a\u01b7\3\2\2\2c\u01b9\3")
        buf.write("\2\2\2e\u01bb\3\2\2\2g\u01bd\3\2\2\2i\u01bf\3\2\2\2k\u01c1")
        buf.write("\3\2\2\2m\u01c3\3\2\2\2o\u01c5\3\2\2\2q\u01c7\3\2\2\2")
        buf.write("s\u01c9\3\2\2\2u\u01cc\3\2\2\2w\u01ce\3\2\2\2y\u01d0\3")
        buf.write("\2\2\2{\u01d7\3\2\2\2}\u01dd\3\2\2\2\177\u01df\3\2\2\2")
        buf.write("\u0081\u01f1\3\2\2\2\u0083\u0205\3\2\2\2\u0085\u0218\3")
        buf.write("\2\2\2\u0087\u0230\3\2\2\2\u0089\u0232\3\2\2\2\u008b\u0235")
        buf.write("\3\2\2\2\u008d\u0239\3\2\2\2\u008f\u0240\3\2\2\2\u0091")
        buf.write("\u0258\3\2\2\2\u0093\u025a\3\2\2\2\u0095\u0264\3\2\2\2")
        buf.write("\u0097\u0098\7%\2\2\u0098\u0099\7%\2\2\u0099\u009d\3\2")
        buf.write("\2\2\u009a\u009c\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7%\2\2")
        buf.write("\u00a1\u00a2\7%\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b")
        buf.write("\2\2\2\u00a4\4\3\2\2\2\u00a5\u00b3\7\62\2\2\u00a6\u00a7")
        buf.write("\7\62\2\2\u00a7\u00b3\7\62\2\2\u00a8\u00a9\7\62\2\2\u00a9")
        buf.write("\u00aa\t\2\2\2\u00aa\u00b3\7\62\2\2\u00ab\u00ac\7\62\2")
        buf.write("\2\u00ac\u00ad\t\3\2\2\u00ad\u00b3\7\62\2\2\u00ae\u00b3")
        buf.write("\5\u0085C\2\u00af\u00b3\5\177@\2\u00b0\u00b3\5\u0081A")
        buf.write("\2\u00b1\u00b3\5\u0083B\2\u00b2\u00a5\3\2\2\2\u00b2\u00a6")
        buf.write("\3\2\2\2\u00b2\u00a8\3\2\2\2\u00b2\u00ab\3\2\2\2\u00b2")
        buf.write("\u00ae\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b")
        buf.write("\3\3\2\u00b5\6\3\2\2\2\u00b6\u00b9\7\62\2\2\u00b7\u00b9")
        buf.write("\5\177@\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00be\7\60\2\2\u00bb\u00bd\5}?\2")
        buf.write("\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3")
        buf.write("\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00e8\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c1\u00c4\7\62\2\2\u00c2\u00c4\5\177@\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00cc\3\2\2\2")
        buf.write("\u00c5\u00c9\7\60\2\2\u00c6\u00c8\5}?\2\u00c7\u00c6\3")
        buf.write("\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\u00c5\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00d0\t\4\2\2\u00cf\u00d1\t\5\2\2\u00d0\u00cf\3")
        buf.write("\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d4")
        buf.write("\5}?\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00e8\3\2\2\2\u00d7")
        buf.write("\u00db\7\60\2\2\u00d8\u00da\5}?\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3")
        buf.write("\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0")
        buf.write("\t\4\2\2\u00df\u00e1\t\5\2\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5}?\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00b8\3")
        buf.write("\2\2\2\u00e7\u00c3\3\2\2\2\u00e7\u00d7\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00ea\b\4\4\2\u00ea\b\3\2\2\2\u00eb\u00ee")
        buf.write("\5\31\r\2\u00ec\u00ee\5\33\16\2\u00ed\u00eb\3\2\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\n\3\2\2\2\u00ef\u00f3\7$\2\2\u00f0")
        buf.write("\u00f2\5\u0087D\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5\3\2")
        buf.write("\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\7$\2\2\u00f7")
        buf.write("\u00f8\b\6\5\2\u00f8\f\3\2\2\2\u00f9\u00fa\7D\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7c\2\2\u00fd")
        buf.write("\u00fe\7m\2\2\u00fe\16\3\2\2\2\u00ff\u0100\7E\2\2\u0100")
        buf.write("\u0101\7q\2\2\u0101\u0102\7p\2\2\u0102\u0103\7v\2\2\u0103")
        buf.write("\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106\7w\2\2\u0106")
        buf.write("\u0107\7g\2\2\u0107\20\3\2\2\2\u0108\u0109\7K\2\2\u0109")
        buf.write("\u010a\7h\2\2\u010a\22\3\2\2\2\u010b\u010c\7G\2\2\u010c")
        buf.write("\u010d\7n\2\2\u010d\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f")
        buf.write("\u0110\7k\2\2\u0110\u0111\7h\2\2\u0111\24\3\2\2\2\u0112")
        buf.write("\u0113\7G\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115")
        buf.write("\u0116\7g\2\2\u0116\26\3\2\2\2\u0117\u0118\7H\2\2\u0118")
        buf.write("\u0119\7q\2\2\u0119\u011a\7t\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\u011c\7c\2\2\u011c\u011d\7e\2\2\u011d\u011e\7j\2\2\u011e")
        buf.write("\30\3\2\2\2\u011f\u0120\7V\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7w\2\2\u0122\u0123\7g\2\2\u0123\32\3\2\2\2\u0124")
        buf.write("\u0125\7H\2\2\u0125\u0126\7c\2\2\u0126\u0127\7n\2\2\u0127")
        buf.write("\u0128\7u\2\2\u0128\u0129\7g\2\2\u0129\34\3\2\2\2\u012a")
        buf.write("\u012b\7C\2\2\u012b\u012c\7t\2\2\u012c\u012d\7t\2\2\u012d")
        buf.write("\u012e\7c\2\2\u012e\u012f\7{\2\2\u012f\36\3\2\2\2\u0130")
        buf.write("\u0131\7K\2\2\u0131\u0132\7p\2\2\u0132 \3\2\2\2\u0133")
        buf.write("\u0134\7K\2\2\u0134\u0135\7p\2\2\u0135\u0136\7v\2\2\u0136")
        buf.write("\"\3\2\2\2\u0137\u0138\7H\2\2\u0138\u0139\7n\2\2\u0139")
        buf.write("\u013a\7q\2\2\u013a\u013b\7c\2\2\u013b\u013c\7v\2\2\u013c")
        buf.write("$\3\2\2\2\u013d\u013e\7D\2\2\u013e\u013f\7q\2\2\u013f")
        buf.write("\u0140\7q\2\2\u0140\u0141\7n\2\2\u0141\u0142\7g\2\2\u0142")
        buf.write("\u0143\7c\2\2\u0143\u0144\7p\2\2\u0144&\3\2\2\2\u0145")
        buf.write("\u0146\7U\2\2\u0146\u0147\7v\2\2\u0147\u0148\7t\2\2\u0148")
        buf.write("\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b\7i\2\2\u014b")
        buf.write("(\3\2\2\2\u014c\u014d\7T\2\2\u014d\u014e\7g\2\2\u014e")
        buf.write("\u014f\7v\2\2\u014f\u0150\7w\2\2\u0150\u0151\7t\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152*\3\2\2\2\u0153\u0154\7U\2\2\u0154")
        buf.write("\u0155\7g\2\2\u0155\u0156\7n\2\2\u0156\u0157\7h\2\2\u0157")
        buf.write(",\3\2\2\2\u0158\u0159\7P\2\2\u0159\u015a\7w\2\2\u015a")
        buf.write("\u015b\7n\2\2\u015b\u015c\7n\2\2\u015c.\3\2\2\2\u015d")
        buf.write("\u015e\7E\2\2\u015e\u015f\7n\2\2\u015f\u0160\7c\2\2\u0160")
        buf.write("\u0161\7u\2\2\u0161\u0162\7u\2\2\u0162\60\3\2\2\2\u0163")
        buf.write("\u0164\7X\2\2\u0164\u0165\7c\2\2\u0165\u0166\7n\2\2\u0166")
        buf.write("\62\3\2\2\2\u0167\u0168\7X\2\2\u0168\u0169\7c\2\2\u0169")
        buf.write("\u016a\7t\2\2\u016a\64\3\2\2\2\u016b\u016c\7E\2\2\u016c")
        buf.write("\u016d\7q\2\2\u016d\u016e\7p\2\2\u016e\u016f\7u\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172\7w\2\2\u0172")
        buf.write("\u0173\7e\2\2\u0173\u0174\7v\2\2\u0174\u0175\7q\2\2\u0175")
        buf.write("\u0176\7t\2\2\u0176\66\3\2\2\2\u0177\u0178\7F\2\2\u0178")
        buf.write("\u0179\7g\2\2\u0179\u017a\7u\2\2\u017a\u017b\7v\2\2\u017b")
        buf.write("\u017c\7t\2\2\u017c\u017d\7w\2\2\u017d\u017e\7e\2\2\u017e")
        buf.write("\u017f\7v\2\2\u017f\u0180\7q\2\2\u0180\u0181\7t\2\2\u0181")
        buf.write("8\3\2\2\2\u0182\u0183\7P\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("\u0185\7y\2\2\u0185:\3\2\2\2\u0186\u0187\7D\2\2\u0187")
        buf.write("\u0188\7{\2\2\u0188<\3\2\2\2\u0189\u018a\7-\2\2\u018a")
        buf.write(">\3\2\2\2\u018b\u018c\7/\2\2\u018c@\3\2\2\2\u018d\u018e")
        buf.write("\7,\2\2\u018eB\3\2\2\2\u018f\u0190\7\61\2\2\u0190D\3\2")
        buf.write("\2\2\u0191\u0192\7\'\2\2\u0192F\3\2\2\2\u0193\u0194\7")
        buf.write("#\2\2\u0194H\3\2\2\2\u0195\u0196\7(\2\2\u0196\u0197\7")
        buf.write("(\2\2\u0197J\3\2\2\2\u0198\u0199\7~\2\2\u0199\u019a\7")
        buf.write("~\2\2\u019aL\3\2\2\2\u019b\u019c\7?\2\2\u019c\u019d\7")
        buf.write("?\2\2\u019dN\3\2\2\2\u019e\u019f\7?\2\2\u019fP\3\2\2\2")
        buf.write("\u01a0\u01a1\7#\2\2\u01a1\u01a2\7?\2\2\u01a2R\3\2\2\2")
        buf.write("\u01a3\u01a4\7@\2\2\u01a4T\3\2\2\2\u01a5\u01a6\7@\2\2")
        buf.write("\u01a6\u01a7\7?\2\2\u01a7V\3\2\2\2\u01a8\u01a9\7>\2\2")
        buf.write("\u01a9X\3\2\2\2\u01aa\u01ab\7>\2\2\u01ab\u01ac\7?\2\2")
        buf.write("\u01acZ\3\2\2\2\u01ad\u01ae\7?\2\2\u01ae\u01af\7?\2\2")
        buf.write("\u01af\u01b0\7\60\2\2\u01b0\\\3\2\2\2\u01b1\u01b2\7-\2")
        buf.write("\2\u01b2\u01b3\7\60\2\2\u01b3^\3\2\2\2\u01b4\u01b5\7<")
        buf.write("\2\2\u01b5\u01b6\7<\2\2\u01b6`\3\2\2\2\u01b7\u01b8\59")
        buf.write("\35\2\u01b8b\3\2\2\2\u01b9\u01ba\7*\2\2\u01bad\3\2\2\2")
        buf.write("\u01bb\u01bc\7+\2\2\u01bcf\3\2\2\2\u01bd\u01be\7}\2\2")
        buf.write("\u01beh\3\2\2\2\u01bf\u01c0\7\177\2\2\u01c0j\3\2\2\2\u01c1")
        buf.write("\u01c2\7]\2\2\u01c2l\3\2\2\2\u01c3\u01c4\7_\2\2\u01c4")
        buf.write("n\3\2\2\2\u01c5\u01c6\7=\2\2\u01c6p\3\2\2\2\u01c7\u01c8")
        buf.write("\7<\2\2\u01c8r\3\2\2\2\u01c9\u01ca\7\60\2\2\u01ca\u01cb")
        buf.write("\7\60\2\2\u01cbt\3\2\2\2\u01cc\u01cd\7\60\2\2\u01cdv\3")
        buf.write("\2\2\2\u01ce\u01cf\7.\2\2\u01cfx\3\2\2\2\u01d0\u01d4\t")
        buf.write("\6\2\2\u01d1\u01d3\t\7\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("z\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d9\7&\2\2\u01d8")
        buf.write("\u01da\t\7\2\2\u01d9\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc|\3\2\2")
        buf.write("\2\u01dd\u01de\t\b\2\2\u01de~\3\2\2\2\u01df\u01e3\t\t")
        buf.write("\2\2\u01e0\u01e2\5}?\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01ee\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\7a\2\2")
        buf.write("\u01e7\u01e9\5}?\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2")
        buf.write("\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed")
        buf.write("\3\2\2\2\u01ec\u01e6\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u0080\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f1\u01f2\7\62\2\2\u01f2\u01f3")
        buf.write("\t\3\2\2\u01f3\u01f7\t\n\2\2\u01f4\u01f6\t\13\2\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u0202\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01fa\u01fc\7a\2\2\u01fb\u01fd\t\13\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u01fa\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u0082\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0206")
        buf.write("\7\62\2\2\u0206\u020a\t\f\2\2\u0207\u0209\t\r\2\2\u0208")
        buf.write("\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u0215\3\2\2\2\u020c\u020a\3")
        buf.write("\2\2\2\u020d\u020f\7a\2\2\u020e\u0210\t\r\2\2\u020f\u020e")
        buf.write("\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u020f\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u0214\3\2\2\2\u0213\u020d\3\2\2\2")
        buf.write("\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216\u0084\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219")
        buf.write("\7\62\2\2\u0219\u021a\t\2\2\2\u021a\u021e\7\63\2\2\u021b")
        buf.write("\u021d\t\16\2\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2")
        buf.write("\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0229")
        buf.write("\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0223\7a\2\2\u0222")
        buf.write("\u0224\t\16\2\2\u0223\u0222\3\2\2\2\u0224\u0225\3\2\2")
        buf.write("\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228")
        buf.write("\3\2\2\2\u0227\u0221\3\2\2\2\u0228\u022b\3\2\2\2\u0229")
        buf.write("\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u0086\3\2\2\2")
        buf.write("\u022b\u0229\3\2\2\2\u022c\u0231\5\u0089E\2\u022d\u0231")
        buf.write("\n\17\2\2\u022e\u022f\7)\2\2\u022f\u0231\7$\2\2\u0230")
        buf.write("\u022c\3\2\2\2\u0230\u022d\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0231\u0088\3\2\2\2\u0232\u0233\7^\2\2\u0233\u0234\t")
        buf.write("\20\2\2\u0234\u008a\3\2\2\2\u0235\u0236\7^\2\2\u0236\u0237")
        buf.write("\n\20\2\2\u0237\u008c\3\2\2\2\u0238\u023a\t\21\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u0239\3\2\2\2")
        buf.write("\u023b\u023c\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\b")
        buf.write("G\2\2\u023e\u008e\3\2\2\2\u023f\u0241\7\f\2\2\u0240\u023f")
        buf.write("\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\bH\2\2")
        buf.write("\u0245\u0090\3\2\2\2\u0246\u024a\7$\2\2\u0247\u0249\5")
        buf.write("\u0087D\2\u0248\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a")
        buf.write("\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024d\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024d\u024e\7\2\2\3\u024e\u0259\b")
        buf.write("I\6\2\u024f\u0253\7$\2\2\u0250\u0252\5\u0087D\2\u0251")
        buf.write("\u0250\3\2\2\2\u0252\u0255\3\2\2\2\u0253\u0251\3\2\2\2")
        buf.write("\u0253\u0254\3\2\2\2\u0254\u0256\3\2\2\2\u0255\u0253\3")
        buf.write("\2\2\2\u0256\u0257\t\22\2\2\u0257\u0259\bI\7\2\u0258\u0246")
        buf.write("\3\2\2\2\u0258\u024f\3\2\2\2\u0259\u0092\3\2\2\2\u025a")
        buf.write("\u025e\7$\2\2\u025b\u025d\5\u0087D\2\u025c\u025b\3\2\2")
        buf.write("\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f")
        buf.write("\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2\u0261")
        buf.write("\u0262\5\u008bF\2\u0262\u0263\bJ\b\2\u0263\u0094\3\2\2")
        buf.write("\2\u0264\u0265\13\2\2\2\u0265\u0266\bK\t\2\u0266\u0096")
        buf.write("\3\2\2\2\'\2\u009d\u00b2\u00b8\u00be\u00c3\u00c9\u00cc")
        buf.write("\u00d0\u00d5\u00db\u00e0\u00e5\u00e7\u00ed\u00f3\u01d4")
        buf.write("\u01db\u01e3\u01ea\u01ee\u01f7\u01fe\u0202\u020a\u0211")
        buf.write("\u0215\u021e\u0225\u0229\u0230\u023b\u0242\u024a\u0253")
        buf.write("\u0258\u025e\n\b\2\2\3\3\2\3\4\3\3\6\4\3I\5\3I\6\3J\7")
        buf.write("\3K\b")
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
    NEW_OP = 48
    LB = 49
    RB = 50
    LP = 51
    RP = 52
    LSB = 53
    RSB = 54
    SEMI = 55
    COLON = 56
    TWODOT = 57
    DOT = 58
    CM = 59
    ID = 60
    DOLLAR_ID = 61
    WS = 62
    NEWLINE = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

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
            "LT", "LTE", "COMPARE_STRING", "CONCATE", "TWOCOLON", "NEW_OP", 
            "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COLON", "TWODOT", 
            "DOT", "CM", "ID", "DOLLAR_ID", "WS", "NEWLINE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "SELF", "NULL", "CLASS", "VAL", "VAR", 
                  "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "GT", "GTE", "LT", "LTE", "COMPARE_STRING", 
                  "CONCATE", "TWOCOLON", "NEW_OP", "LB", "RB", "LP", "RP", 
                  "LSB", "RSB", "SEMI", "COLON", "TWODOT", "DOT", "CM", 
                  "ID", "DOLLAR_ID", "DIGIT", "NONEZERO_DECIMAL", "NONEZERO_HEXADECIMAL", 
                  "NONEZERO_OCTAL", "NONEZERO_BINARY", "STR_CHAR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "WS", "NEWLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INTLIT_action 
            actions[2] = self.FLOATLIT_action 
            actions[4] = self.STRINGLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
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
     


