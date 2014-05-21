# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 src/scribble/Scribble.g 2014-03-31 18:11:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EMPTY_LOCAL_CATCHES=82
LOCALPROTOCOLDECL=58
LETTER=88
EXTIDENTIFIER=93
LOCALINTERRUPT=69
CATCHESKW=27
LOCALRECEIVE=74
MODULEDECL=30
KIND_MESSAGE_SIGNATURE=83
LOCALCONTINUE=66
EMPTY_MESSAGE_OP=75
EOF=-1
T__94=94
PARAMETERDECL=35
PARAMETERDECLLIST=34
ROLEINSTANTIATION=44
LOCALCHOICE=64
LOCALCATCH=72
GLOBALPARALLEL=54
CONTINUEKW=20
GLOBALPROTOCOLDEF=46
PAYLOADTYPEDECL=33
COMMENT=86
IMPORTMODULE=31
GLOBALCHOICE=51
T__99=99
T__98=98
T__97=97
T__96=96
T__95=95
ROLEINSTANTIATIONLIST=43
EMPTY_ARGUMENT_LIST=78
SYMBOL=92
LINE_COMMENT=87
LOCALSEND=73
WHITESPACE=85
UNDERSCORE=89
SIGKW=11
IMPORTKW=5
EMPTY_LOCAL_THROW=81
EMPTY_ANNOTATION=76
GLOBALMESSAGETRANSFER=50
MODULEKW=4
GLOBALINTERRUPT=56
LOCALKW=9
GLOBALPROTOCOLINSTANCE=47
ATKW=17
IMPORTMEMBER=32
MESSAGESIGNATURE=36
KIND_PAYLOAD_TYPE=84
CHOICEKW=16
GLOBALPROTOCOLDECL=45
DOKW=28
ARGUMENTLIST=39
LOCALPROTOCOLBLOCK=61
ROLEKW=10
EMPTY_SCOPE_NAME=80
LOCALDO=70
EMPTY_PARAMETER_DECL_LIST=77
TOKW=15
INSTANTIATESKW=12
WITHKW=24
ASKW=13
GLOBALDO=57
IDENTIFIER=91
T__103=103
THROWSKW=26
ARGUMENT=40
GLOBALRECURSION=52
ANDKW=22
DIGIT=90
LOCALINTERRUPTIBLE=68
EMPTY_MODULE_NAME=79
FROMKW=14
GLOBALPROTOCOLBLOCK=48
INTERRUPTIBLEKW=23
GLOBALINTERRUPTIBLE=55
PARKW=21
T__102=102
TYPEKW=6
RECKW=19
T__101=101
PAYLOAD=41
T__100=100
LOCALINTERACTIONSEQUENCE=62
GLOBALINTERACTIONSEQUENCE=49
LOCALMESSAGETRANSFER=63
MODULE=29
BYKW=25
ORKW=18
LOCALRECURSION=65
PROTOCOLKW=7
LOCALPROTOCOLINSTANCE=60
ROLEDECLLIST=37
LOCALPARALLEL=67
GLOBALCONTINUE=53
LOCALPROTOCOLDEF=59
ROLEDECL=38
GLOBALKW=8
PAYLOADELEMENT=42
LOCALTHROW=71

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "MODULEKW", "IMPORTKW", "TYPEKW", "PROTOCOLKW", "GLOBALKW", "LOCALKW", 
    "ROLEKW", "SIGKW", "INSTANTIATESKW", "ASKW", "FROMKW", "TOKW", "CHOICEKW", 
    "ATKW", "ORKW", "RECKW", "CONTINUEKW", "PARKW", "ANDKW", "INTERRUPTIBLEKW", 
    "WITHKW", "BYKW", "THROWSKW", "CATCHESKW", "DOKW", "MODULE", "MODULEDECL", 
    "IMPORTMODULE", "IMPORTMEMBER", "PAYLOADTYPEDECL", "PARAMETERDECLLIST", 
    "PARAMETERDECL", "MESSAGESIGNATURE", "ROLEDECLLIST", "ROLEDECL", "ARGUMENTLIST", 
    "ARGUMENT", "PAYLOAD", "PAYLOADELEMENT", "ROLEINSTANTIATIONLIST", "ROLEINSTANTIATION", 
    "GLOBALPROTOCOLDECL", "GLOBALPROTOCOLDEF", "GLOBALPROTOCOLINSTANCE", 
    "GLOBALPROTOCOLBLOCK", "GLOBALINTERACTIONSEQUENCE", "GLOBALMESSAGETRANSFER", 
    "GLOBALCHOICE", "GLOBALRECURSION", "GLOBALCONTINUE", "GLOBALPARALLEL", 
    "GLOBALINTERRUPTIBLE", "GLOBALINTERRUPT", "GLOBALDO", "LOCALPROTOCOLDECL", 
    "LOCALPROTOCOLDEF", "LOCALPROTOCOLINSTANCE", "LOCALPROTOCOLBLOCK", "LOCALINTERACTIONSEQUENCE", 
    "LOCALMESSAGETRANSFER", "LOCALCHOICE", "LOCALRECURSION", "LOCALCONTINUE", 
    "LOCALPARALLEL", "LOCALINTERRUPTIBLE", "LOCALINTERRUPT", "LOCALDO", 
    "LOCALTHROW", "LOCALCATCH", "LOCALSEND", "LOCALRECEIVE", "EMPTY_MESSAGE_OP", 
    "EMPTY_ANNOTATION", "EMPTY_PARAMETER_DECL_LIST", "EMPTY_ARGUMENT_LIST", 
    "EMPTY_MODULE_NAME", "EMPTY_SCOPE_NAME", "EMPTY_LOCAL_THROW", "EMPTY_LOCAL_CATCHES", 
    "KIND_MESSAGE_SIGNATURE", "KIND_PAYLOAD_TYPE", "WHITESPACE", "COMMENT", 
    "LINE_COMMENT", "LETTER", "UNDERSCORE", "DIGIT", "IDENTIFIER", "SYMBOL", 
    "EXTIDENTIFIER", "'.'", "';'", "'<'", "'>'", "'('", "')'", "','", "':'", 
    "'{'", "'}'"
]




class ScribbleParser(Parser):
    grammarFileName = "src/scribble/Scribble.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ScribbleParser, self).__init__(input, state, *args, **kwargs)

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )

        self.dfa41 = self.DFA41(
            self, 41,
            eot = self.DFA41_eot,
            eof = self.DFA41_eof,
            min = self.DFA41_min,
            max = self.DFA41_max,
            accept = self.DFA41_accept,
            special = self.DFA41_special,
            transition = self.DFA41_transition
            )

        self.dfa43 = self.DFA43(
            self, 43,
            eot = self.DFA43_eot,
            eof = self.DFA43_eof,
            min = self.DFA43_min,
            max = self.DFA43_max,
            accept = self.DFA43_accept,
            special = self.DFA43_special,
            transition = self.DFA43_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class rolename_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.rolename_return, self).__init__()

            self.tree = None




    # $ANTLR start "rolename"
    # src/scribble/Scribble.g:204:1: rolename : IDENTIFIER ;
    def rolename(self, ):

        retval = self.rolename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER1 = None

        IDENTIFIER1_tree = None

        try:
            try:
                # src/scribble/Scribble.g:211:9: ( IDENTIFIER )
                # src/scribble/Scribble.g:211:11: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER1=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_rolename1006)
                if self._state.backtracking == 0:

                    IDENTIFIER1_tree = self._adaptor.createWithPayload(IDENTIFIER1)
                    self._adaptor.addChild(root_0, IDENTIFIER1_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rolename"

    class payloadtypename_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.payloadtypename_return, self).__init__()

            self.tree = None




    # $ANTLR start "payloadtypename"
    # src/scribble/Scribble.g:212:1: payloadtypename : IDENTIFIER ;
    def payloadtypename(self, ):

        retval = self.payloadtypename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER2 = None

        IDENTIFIER2_tree = None

        try:
            try:
                # src/scribble/Scribble.g:212:16: ( IDENTIFIER )
                # src/scribble/Scribble.g:212:18: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER2=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_payloadtypename1012)
                if self._state.backtracking == 0:

                    IDENTIFIER2_tree = self._adaptor.createWithPayload(IDENTIFIER2)
                    self._adaptor.addChild(root_0, IDENTIFIER2_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "payloadtypename"

    class protocolname_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.protocolname_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolname"
    # src/scribble/Scribble.g:213:1: protocolname : IDENTIFIER ;
    def protocolname(self, ):

        retval = self.protocolname_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER3 = None

        IDENTIFIER3_tree = None

        try:
            try:
                # src/scribble/Scribble.g:213:13: ( IDENTIFIER )
                # src/scribble/Scribble.g:213:15: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER3=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_protocolname1018)
                if self._state.backtracking == 0:

                    IDENTIFIER3_tree = self._adaptor.createWithPayload(IDENTIFIER3)
                    self._adaptor.addChild(root_0, IDENTIFIER3_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocolname"

    class parametername_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.parametername_return, self).__init__()

            self.tree = None




    # $ANTLR start "parametername"
    # src/scribble/Scribble.g:214:1: parametername : IDENTIFIER ;
    def parametername(self, ):

        retval = self.parametername_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER4 = None

        IDENTIFIER4_tree = None

        try:
            try:
                # src/scribble/Scribble.g:214:14: ( IDENTIFIER )
                # src/scribble/Scribble.g:214:16: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER4=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parametername1024)
                if self._state.backtracking == 0:

                    IDENTIFIER4_tree = self._adaptor.createWithPayload(IDENTIFIER4)
                    self._adaptor.addChild(root_0, IDENTIFIER4_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parametername"

    class annotationname_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.annotationname_return, self).__init__()

            self.tree = None




    # $ANTLR start "annotationname"
    # src/scribble/Scribble.g:215:1: annotationname : IDENTIFIER ;
    def annotationname(self, ):

        retval = self.annotationname_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER5 = None

        IDENTIFIER5_tree = None

        try:
            try:
                # src/scribble/Scribble.g:215:15: ( IDENTIFIER )
                # src/scribble/Scribble.g:215:17: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER5=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_annotationname1030)
                if self._state.backtracking == 0:

                    IDENTIFIER5_tree = self._adaptor.createWithPayload(IDENTIFIER5)
                    self._adaptor.addChild(root_0, IDENTIFIER5_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "annotationname"

    class recursionlabelname_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.recursionlabelname_return, self).__init__()

            self.tree = None




    # $ANTLR start "recursionlabelname"
    # src/scribble/Scribble.g:216:1: recursionlabelname : IDENTIFIER ;
    def recursionlabelname(self, ):

        retval = self.recursionlabelname_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER6 = None

        IDENTIFIER6_tree = None

        try:
            try:
                # src/scribble/Scribble.g:216:19: ( IDENTIFIER )
                # src/scribble/Scribble.g:216:21: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER6=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_recursionlabelname1036)
                if self._state.backtracking == 0:

                    IDENTIFIER6_tree = self._adaptor.createWithPayload(IDENTIFIER6)
                    self._adaptor.addChild(root_0, IDENTIFIER6_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "recursionlabelname"

    class scopename_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.scopename_return, self).__init__()

            self.tree = None




    # $ANTLR start "scopename"
    # src/scribble/Scribble.g:217:1: scopename : IDENTIFIER ;
    def scopename(self, ):

        retval = self.scopename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER7 = None

        IDENTIFIER7_tree = None

        try:
            try:
                # src/scribble/Scribble.g:217:10: ( IDENTIFIER )
                # src/scribble/Scribble.g:217:12: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER7=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_scopename1042)
                if self._state.backtracking == 0:

                    IDENTIFIER7_tree = self._adaptor.createWithPayload(IDENTIFIER7)
                    self._adaptor.addChild(root_0, IDENTIFIER7_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "scopename"

    class modulename_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.modulename_return, self).__init__()

            self.tree = None




    # $ANTLR start "modulename"
    # src/scribble/Scribble.g:220:1: modulename : ( IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER -> ( IDENTIFIER )+ | IDENTIFIER -> ( IDENTIFIER )+ );
    def modulename(self, ):

        retval = self.modulename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER8 = None
        char_literal9 = None
        IDENTIFIER10 = None
        char_literal11 = None
        IDENTIFIER12 = None
        IDENTIFIER13 = None

        IDENTIFIER8_tree = None
        char_literal9_tree = None
        IDENTIFIER10_tree = None
        char_literal11_tree = None
        IDENTIFIER12_tree = None
        IDENTIFIER13_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")

        try:
            try:
                # src/scribble/Scribble.g:229:11: ( IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER -> ( IDENTIFIER )+ | IDENTIFIER -> ( IDENTIFIER )+ )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == IDENTIFIER) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 94) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == IDENTIFIER) :
                            LA2_4 = self.input.LA(4)

                            if (LA2_4 == 96 or LA2_4 == 98) :
                                alt2 = 2
                            elif (LA2_4 == IMPORTKW or LA2_4 == ASKW or (94 <= LA2_4 <= 95)) :
                                alt2 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 2, 4, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 2, 2, self.input)

                            raise nvae

                    elif (LA2_1 == IMPORTKW or LA2_1 == ASKW or LA2_1 == 95) :
                        alt2 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 2, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # src/scribble/Scribble.g:231:2: IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER
                    pass 
                    IDENTIFIER8=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1058) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER8)
                    # src/scribble/Scribble.g:231:13: ( '.' IDENTIFIER )*
                    while True: #loop1
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == 94) :
                            LA1_1 = self.input.LA(2)

                            if (LA1_1 == IDENTIFIER) :
                                LA1_2 = self.input.LA(3)

                                if (LA1_2 == 94) :
                                    LA1_3 = self.input.LA(4)

                                    if (LA1_3 == IDENTIFIER) :
                                        LA1_5 = self.input.LA(5)

                                        if (LA1_5 == IMPORTKW or LA1_5 == ASKW or (94 <= LA1_5 <= 95)) :
                                            alt1 = 1










                        if alt1 == 1:
                            # src/scribble/Scribble.g:231:14: '.' IDENTIFIER
                            pass 
                            char_literal9=self.match(self.input, 94, self.FOLLOW_94_in_modulename1061) 
                            if self._state.backtracking == 0:
                                stream_94.add(char_literal9)
                            IDENTIFIER10=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1063) 
                            if self._state.backtracking == 0:
                                stream_IDENTIFIER.add(IDENTIFIER10)


                        else:
                            break #loop1
                    char_literal11=self.match(self.input, 94, self.FOLLOW_94_in_modulename1067) 
                    if self._state.backtracking == 0:
                        stream_94.add(char_literal11)
                    IDENTIFIER12=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1069) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER12)

                    # AST Rewrite
                    # elements: IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 232:2: -> ( IDENTIFIER )+
                        # src/scribble/Scribble.g:233:2: ( IDENTIFIER )+
                        if not (stream_IDENTIFIER.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_IDENTIFIER.hasNext():
                            self._adaptor.addChild(root_0, stream_IDENTIFIER.nextNode())


                        stream_IDENTIFIER.reset()



                        retval.tree = root_0


                elif alt2 == 2:
                    # src/scribble/Scribble.g:235:2: IDENTIFIER
                    pass 
                    IDENTIFIER13=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1083) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER13)

                    # AST Rewrite
                    # elements: IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 236:2: -> ( IDENTIFIER )+
                        # src/scribble/Scribble.g:237:2: ( IDENTIFIER )+
                        if not (stream_IDENTIFIER.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_IDENTIFIER.hasNext():
                            self._adaptor.addChild(root_0, stream_IDENTIFIER.nextNode())


                        stream_IDENTIFIER.reset()



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "modulename"

    class membername_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.membername_return, self).__init__()

            self.tree = None




    # $ANTLR start "membername"
    # src/scribble/Scribble.g:240:1: membername : ( simplemembername | fullmembername );
    def membername(self, ):

        retval = self.membername_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simplemembername14 = None

        fullmembername15 = None



        try:
            try:
                # src/scribble/Scribble.g:240:11: ( simplemembername | fullmembername )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 96 or LA3_1 == 98) :
                        alt3 = 1
                    elif (LA3_1 == 94) :
                        alt3 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # src/scribble/Scribble.g:241:2: simplemembername
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simplemembername_in_membername1101)
                    simplemembername14 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simplemembername14.tree)


                elif alt3 == 2:
                    # src/scribble/Scribble.g:243:2: fullmembername
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fullmembername_in_membername1106)
                    fullmembername15 = self.fullmembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fullmembername15.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "membername"

    class simplemembername_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.simplemembername_return, self).__init__()

            self.tree = None




    # $ANTLR start "simplemembername"
    # src/scribble/Scribble.g:246:1: simplemembername : ( payloadtypename | protocolname );
    def simplemembername(self, ):

        retval = self.simplemembername_return()
        retval.start = self.input.LT(1)

        root_0 = None

        payloadtypename16 = None

        protocolname17 = None



        try:
            try:
                # src/scribble/Scribble.g:246:17: ( payloadtypename | protocolname )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    LA4_1 = self.input.LA(2)

                    if (self.synpred4_Scribble()) :
                        alt4 = 1
                    elif (True) :
                        alt4 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # src/scribble/Scribble.g:247:2: payloadtypename
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_payloadtypename_in_simplemembername1115)
                    payloadtypename16 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, payloadtypename16.tree)


                elif alt4 == 2:
                    # src/scribble/Scribble.g:249:2: protocolname
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_protocolname_in_simplemembername1120)
                    protocolname17 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, protocolname17.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simplemembername"

    class fullmembername_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.fullmembername_return, self).__init__()

            self.tree = None




    # $ANTLR start "fullmembername"
    # src/scribble/Scribble.g:254:1: fullmembername : modulename '.' simplemembername -> modulename simplemembername ;
    def fullmembername(self, ):

        retval = self.fullmembername_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal19 = None
        modulename18 = None

        simplemembername20 = None


        char_literal19_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        stream_simplemembername = RewriteRuleSubtreeStream(self._adaptor, "rule simplemembername")
        try:
            try:
                # src/scribble/Scribble.g:254:15: ( modulename '.' simplemembername -> modulename simplemembername )
                # src/scribble/Scribble.g:255:2: modulename '.' simplemembername
                pass 
                self._state.following.append(self.FOLLOW_modulename_in_fullmembername1132)
                modulename18 = self.modulename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_modulename.add(modulename18.tree)
                char_literal19=self.match(self.input, 94, self.FOLLOW_94_in_fullmembername1134) 
                if self._state.backtracking == 0:
                    stream_94.add(char_literal19)
                self._state.following.append(self.FOLLOW_simplemembername_in_fullmembername1136)
                simplemembername20 = self.simplemembername()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_simplemembername.add(simplemembername20.tree)

                # AST Rewrite
                # elements: simplemembername, modulename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 258:2: -> modulename simplemembername
                    self._adaptor.addChild(root_0, stream_modulename.nextTree())
                    self._adaptor.addChild(root_0, stream_simplemembername.nextTree())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fullmembername"

    class module_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.module_return, self).__init__()

            self.tree = None




    # $ANTLR start "module"
    # src/scribble/Scribble.g:263:1: module : moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* ) ;
    def module(self, ):

        retval = self.module_return()
        retval.start = self.input.LT(1)

        root_0 = None

        moduledecl21 = None

        importdecl22 = None

        payloadtypedecl23 = None

        protocoldecl24 = None


        stream_importdecl = RewriteRuleSubtreeStream(self._adaptor, "rule importdecl")
        stream_protocoldecl = RewriteRuleSubtreeStream(self._adaptor, "rule protocoldecl")
        stream_payloadtypedecl = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypedecl")
        stream_moduledecl = RewriteRuleSubtreeStream(self._adaptor, "rule moduledecl")
        try:
            try:
                # src/scribble/Scribble.g:266:7: ( moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* ) )
                # src/scribble/Scribble.g:267:2: moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )*
                pass 
                self._state.following.append(self.FOLLOW_moduledecl_in_module1159)
                moduledecl21 = self.moduledecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_moduledecl.add(moduledecl21.tree)
                # src/scribble/Scribble.g:267:13: ( importdecl )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == IMPORTKW or LA5_0 == FROMKW) :
                        alt5 = 1


                    if alt5 == 1:
                        # src/scribble/Scribble.g:267:14: importdecl
                        pass 
                        self._state.following.append(self.FOLLOW_importdecl_in_module1162)
                        importdecl22 = self.importdecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_importdecl.add(importdecl22.tree)


                    else:
                        break #loop5
                # src/scribble/Scribble.g:267:27: ( payloadtypedecl )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TYPEKW) :
                        alt6 = 1


                    if alt6 == 1:
                        # src/scribble/Scribble.g:267:28: payloadtypedecl
                        pass 
                        self._state.following.append(self.FOLLOW_payloadtypedecl_in_module1167)
                        payloadtypedecl23 = self.payloadtypedecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_payloadtypedecl.add(payloadtypedecl23.tree)


                    else:
                        break #loop6
                # src/scribble/Scribble.g:267:46: ( protocoldecl )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((GLOBALKW <= LA7_0 <= LOCALKW)) :
                        alt7 = 1


                    if alt7 == 1:
                        # src/scribble/Scribble.g:267:47: protocoldecl
                        pass 
                        self._state.following.append(self.FOLLOW_protocoldecl_in_module1172)
                        protocoldecl24 = self.protocoldecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_protocoldecl.add(protocoldecl24.tree)


                    else:
                        break #loop7

                # AST Rewrite
                # elements: payloadtypedecl, protocoldecl, moduledecl, importdecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 268:2: -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* )
                    # src/scribble/Scribble.g:271:2: ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MODULE, "MODULE"), root_1)

                    self._adaptor.addChild(root_1, stream_moduledecl.nextTree())
                    # src/scribble/Scribble.g:271:22: ( importdecl )*
                    while stream_importdecl.hasNext():
                        self._adaptor.addChild(root_1, stream_importdecl.nextTree())


                    stream_importdecl.reset();
                    # src/scribble/Scribble.g:271:36: ( payloadtypedecl )*
                    while stream_payloadtypedecl.hasNext():
                        self._adaptor.addChild(root_1, stream_payloadtypedecl.nextTree())


                    stream_payloadtypedecl.reset();
                    # src/scribble/Scribble.g:271:55: ( protocoldecl )*
                    while stream_protocoldecl.hasNext():
                        self._adaptor.addChild(root_1, stream_protocoldecl.nextTree())


                    stream_protocoldecl.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "module"

    class moduledecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.moduledecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "moduledecl"
    # src/scribble/Scribble.g:277:1: moduledecl : MODULEKW modulename ';' -> ^( MODULEDECL modulename ) ;
    def moduledecl(self, ):

        retval = self.moduledecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MODULEKW25 = None
        char_literal27 = None
        modulename26 = None


        MODULEKW25_tree = None
        char_literal27_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_MODULEKW = RewriteRuleTokenStream(self._adaptor, "token MODULEKW")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        try:
            try:
                # src/scribble/Scribble.g:280:11: ( MODULEKW modulename ';' -> ^( MODULEDECL modulename ) )
                # src/scribble/Scribble.g:281:2: MODULEKW modulename ';'
                pass 
                MODULEKW25=self.match(self.input, MODULEKW, self.FOLLOW_MODULEKW_in_moduledecl1217) 
                if self._state.backtracking == 0:
                    stream_MODULEKW.add(MODULEKW25)
                self._state.following.append(self.FOLLOW_modulename_in_moduledecl1219)
                modulename26 = self.modulename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_modulename.add(modulename26.tree)
                char_literal27=self.match(self.input, 95, self.FOLLOW_95_in_moduledecl1221) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal27)

                # AST Rewrite
                # elements: modulename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 282:2: -> ^( MODULEDECL modulename )
                    # src/scribble/Scribble.g:283:2: ^( MODULEDECL modulename )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MODULEDECL, "MODULEDECL"), root_1)

                    self._adaptor.addChild(root_1, stream_modulename.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "moduledecl"

    class importdecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.importdecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importdecl"
    # src/scribble/Scribble.g:287:1: importdecl : ( importmodule | importmember );
    def importdecl(self, ):

        retval = self.importdecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        importmodule28 = None

        importmember29 = None



        try:
            try:
                # src/scribble/Scribble.g:290:11: ( importmodule | importmember )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == IMPORTKW) :
                    alt8 = 1
                elif (LA8_0 == FROMKW) :
                    alt8 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # src/scribble/Scribble.g:291:2: importmodule
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_importmodule_in_importdecl1243)
                    importmodule28 = self.importmodule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, importmodule28.tree)


                elif alt8 == 2:
                    # src/scribble/Scribble.g:293:2: importmember
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_importmember_in_importdecl1248)
                    importmember29 = self.importmember()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, importmember29.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importdecl"

    class importmodule_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.importmodule_return, self).__init__()

            self.tree = None




    # $ANTLR start "importmodule"
    # src/scribble/Scribble.g:296:1: importmodule : ( IMPORTKW modulename ';' -> ^( IMPORTMODULE modulename ) | IMPORTKW modulename ASKW IDENTIFIER ';' -> ^( IMPORTMODULE ASKW IDENTIFIER modulename ) );
    def importmodule(self, ):

        retval = self.importmodule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTKW30 = None
        char_literal32 = None
        IMPORTKW33 = None
        ASKW35 = None
        IDENTIFIER36 = None
        char_literal37 = None
        modulename31 = None

        modulename34 = None


        IMPORTKW30_tree = None
        char_literal32_tree = None
        IMPORTKW33_tree = None
        ASKW35_tree = None
        IDENTIFIER36_tree = None
        char_literal37_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_IMPORTKW = RewriteRuleTokenStream(self._adaptor, "token IMPORTKW")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        try:
            try:
                # src/scribble/Scribble.g:296:13: ( IMPORTKW modulename ';' -> ^( IMPORTMODULE modulename ) | IMPORTKW modulename ASKW IDENTIFIER ';' -> ^( IMPORTMODULE ASKW IDENTIFIER modulename ) )
                alt9 = 2
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # src/scribble/Scribble.g:297:2: IMPORTKW modulename ';'
                    pass 
                    IMPORTKW30=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmodule1257) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW30)
                    self._state.following.append(self.FOLLOW_modulename_in_importmodule1259)
                    modulename31 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename31.tree)
                    char_literal32=self.match(self.input, 95, self.FOLLOW_95_in_importmodule1261) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal32)

                    # AST Rewrite
                    # elements: modulename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 298:2: -> ^( IMPORTMODULE modulename )
                        # src/scribble/Scribble.g:299:2: ^( IMPORTMODULE modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPORTMODULE, "IMPORTMODULE"), root_1)

                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt9 == 2:
                    # src/scribble/Scribble.g:302:2: IMPORTKW modulename ASKW IDENTIFIER ';'
                    pass 
                    IMPORTKW33=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmodule1279) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW33)
                    self._state.following.append(self.FOLLOW_modulename_in_importmodule1281)
                    modulename34 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename34.tree)
                    ASKW35=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_importmodule1283) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW35)
                    IDENTIFIER36=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_importmodule1285) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER36)
                    char_literal37=self.match(self.input, 95, self.FOLLOW_95_in_importmodule1287) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal37)

                    # AST Rewrite
                    # elements: modulename, ASKW, IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 303:2: -> ^( IMPORTMODULE ASKW IDENTIFIER modulename )
                        # src/scribble/Scribble.g:304:2: ^( IMPORTMODULE ASKW IDENTIFIER modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPORTMODULE, "IMPORTMODULE"), root_1)

                        self._adaptor.addChild(root_1, stream_ASKW.nextNode())
                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importmodule"

    class importmember_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.importmember_return, self).__init__()

            self.tree = None




    # $ANTLR start "importmember"
    # src/scribble/Scribble.g:308:1: importmember : ( FROMKW modulename IMPORTKW simplemembername ';' -> ^( IMPORTMEMBER simplemembername modulename ) | FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';' -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename ) );
    def importmember(self, ):

        retval = self.importmember_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROMKW38 = None
        IMPORTKW40 = None
        char_literal42 = None
        FROMKW43 = None
        IMPORTKW45 = None
        ASKW47 = None
        IDENTIFIER48 = None
        char_literal49 = None
        modulename39 = None

        simplemembername41 = None

        modulename44 = None

        simplemembername46 = None


        FROMKW38_tree = None
        IMPORTKW40_tree = None
        char_literal42_tree = None
        FROMKW43_tree = None
        IMPORTKW45_tree = None
        ASKW47_tree = None
        IDENTIFIER48_tree = None
        char_literal49_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_IMPORTKW = RewriteRuleTokenStream(self._adaptor, "token IMPORTKW")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        stream_simplemembername = RewriteRuleSubtreeStream(self._adaptor, "rule simplemembername")
        try:
            try:
                # src/scribble/Scribble.g:308:13: ( FROMKW modulename IMPORTKW simplemembername ';' -> ^( IMPORTMEMBER simplemembername modulename ) | FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';' -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename ) )
                alt10 = 2
                alt10 = self.dfa10.predict(self.input)
                if alt10 == 1:
                    # src/scribble/Scribble.g:309:2: FROMKW modulename IMPORTKW simplemembername ';'
                    pass 
                    FROMKW38=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importmember1358) 
                    if self._state.backtracking == 0:
                        stream_FROMKW.add(FROMKW38)
                    self._state.following.append(self.FOLLOW_modulename_in_importmember1360)
                    modulename39 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename39.tree)
                    IMPORTKW40=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmember1362) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW40)
                    self._state.following.append(self.FOLLOW_simplemembername_in_importmember1364)
                    simplemembername41 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_simplemembername.add(simplemembername41.tree)
                    char_literal42=self.match(self.input, 95, self.FOLLOW_95_in_importmember1366) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal42)

                    # AST Rewrite
                    # elements: simplemembername, modulename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 310:2: -> ^( IMPORTMEMBER simplemembername modulename )
                        # src/scribble/Scribble.g:311:2: ^( IMPORTMEMBER simplemembername modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPORTMEMBER, "IMPORTMEMBER"), root_1)

                        self._adaptor.addChild(root_1, stream_simplemembername.nextTree())
                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt10 == 2:
                    # src/scribble/Scribble.g:314:2: FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';'
                    pass 
                    FROMKW43=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importmember1432) 
                    if self._state.backtracking == 0:
                        stream_FROMKW.add(FROMKW43)
                    self._state.following.append(self.FOLLOW_modulename_in_importmember1434)
                    modulename44 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename44.tree)
                    IMPORTKW45=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmember1436) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW45)
                    self._state.following.append(self.FOLLOW_simplemembername_in_importmember1438)
                    simplemembername46 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_simplemembername.add(simplemembername46.tree)
                    ASKW47=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_importmember1440) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW47)
                    IDENTIFIER48=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_importmember1442) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER48)
                    char_literal49=self.match(self.input, 95, self.FOLLOW_95_in_importmember1444) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal49)

                    # AST Rewrite
                    # elements: ASKW, modulename, IDENTIFIER, simplemembername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 315:2: -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename )
                        # src/scribble/Scribble.g:316:2: ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPORTMEMBER, "IMPORTMEMBER"), root_1)

                        self._adaptor.addChild(root_1, stream_ASKW.nextNode())
                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_simplemembername.nextTree())
                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importmember"

    class payloadtypedecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.payloadtypedecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "payloadtypedecl"
    # src/scribble/Scribble.g:321:1: payloadtypedecl : TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';' -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename ) ;
    def payloadtypedecl(self, ):

        retval = self.payloadtypedecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TYPEKW50 = None
        char_literal51 = None
        IDENTIFIER52 = None
        char_literal53 = None
        EXTIDENTIFIER54 = None
        FROMKW55 = None
        EXTIDENTIFIER56 = None
        ASKW57 = None
        char_literal59 = None
        payloadtypename58 = None


        TYPEKW50_tree = None
        char_literal51_tree = None
        IDENTIFIER52_tree = None
        char_literal53_tree = None
        EXTIDENTIFIER54_tree = None
        FROMKW55_tree = None
        EXTIDENTIFIER56_tree = None
        ASKW57_tree = None
        char_literal59_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_TYPEKW = RewriteRuleTokenStream(self._adaptor, "token TYPEKW")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_EXTIDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token EXTIDENTIFIER")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        try:
            try:
                # src/scribble/Scribble.g:324:16: ( TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';' -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename ) )
                # src/scribble/Scribble.g:325:2: TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';'
                pass 
                TYPEKW50=self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_payloadtypedecl1474) 
                if self._state.backtracking == 0:
                    stream_TYPEKW.add(TYPEKW50)
                char_literal51=self.match(self.input, 96, self.FOLLOW_96_in_payloadtypedecl1476) 
                if self._state.backtracking == 0:
                    stream_96.add(char_literal51)
                IDENTIFIER52=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_payloadtypedecl1478) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER52)
                char_literal53=self.match(self.input, 97, self.FOLLOW_97_in_payloadtypedecl1480) 
                if self._state.backtracking == 0:
                    stream_97.add(char_literal53)
                EXTIDENTIFIER54=self.match(self.input, EXTIDENTIFIER, self.FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1482) 
                if self._state.backtracking == 0:
                    stream_EXTIDENTIFIER.add(EXTIDENTIFIER54)
                FROMKW55=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_payloadtypedecl1484) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW55)
                EXTIDENTIFIER56=self.match(self.input, EXTIDENTIFIER, self.FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1486) 
                if self._state.backtracking == 0:
                    stream_EXTIDENTIFIER.add(EXTIDENTIFIER56)
                ASKW57=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_payloadtypedecl1488) 
                if self._state.backtracking == 0:
                    stream_ASKW.add(ASKW57)
                self._state.following.append(self.FOLLOW_payloadtypename_in_payloadtypedecl1490)
                payloadtypename58 = self.payloadtypename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_payloadtypename.add(payloadtypename58.tree)
                char_literal59=self.match(self.input, 95, self.FOLLOW_95_in_payloadtypedecl1492) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal59)

                # AST Rewrite
                # elements: EXTIDENTIFIER, IDENTIFIER, EXTIDENTIFIER, payloadtypename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 326:2: -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename )
                    # src/scribble/Scribble.g:327:2: ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOADTYPEDECL, "PAYLOADTYPEDECL"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                    self._adaptor.addChild(root_1, stream_EXTIDENTIFIER.nextNode())
                    self._adaptor.addChild(root_1, stream_EXTIDENTIFIER.nextNode())
                    self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "payloadtypedecl"

    class messageoperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.messageoperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "messageoperator"
    # src/scribble/Scribble.g:333:1: messageoperator : ( LETTER | DIGIT | UNDERSCORE )+ ;
    def messageoperator(self, ):

        retval = self.messageoperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set60 = None

        set60_tree = None

        try:
            try:
                # src/scribble/Scribble.g:336:16: ( ( LETTER | DIGIT | UNDERSCORE )+ )
                # src/scribble/Scribble.g:337:2: ( LETTER | DIGIT | UNDERSCORE )+
                pass 
                root_0 = self._adaptor.nil()

                # src/scribble/Scribble.g:337:2: ( LETTER | DIGIT | UNDERSCORE )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((LETTER <= LA11_0 <= DIGIT)) :
                        alt11 = 1


                    if alt11 == 1:
                        # src/scribble/Scribble.g:
                        pass 
                        set60 = self.input.LT(1)
                        if (LETTER <= self.input.LA(1) <= DIGIT):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set60))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        if cnt11 >= 1:
                            break #loop11

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "messageoperator"

    class messagesignature_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.messagesignature_return, self).__init__()

            self.tree = None




    # $ANTLR start "messagesignature"
    # src/scribble/Scribble.g:340:1: messagesignature : ( '(' payload ')' -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload ) | IDENTIFIER '(' payload ')' -> ^( MESSAGESIGNATURE IDENTIFIER payload ) );
    def messagesignature(self, ):

        retval = self.messagesignature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal61 = None
        char_literal63 = None
        IDENTIFIER64 = None
        char_literal65 = None
        char_literal67 = None
        payload62 = None

        payload66 = None


        char_literal61_tree = None
        char_literal63_tree = None
        IDENTIFIER64_tree = None
        char_literal65_tree = None
        char_literal67_tree = None
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_payload = RewriteRuleSubtreeStream(self._adaptor, "rule payload")
        try:
            try:
                # src/scribble/Scribble.g:340:17: ( '(' payload ')' -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload ) | IDENTIFIER '(' payload ')' -> ^( MESSAGESIGNATURE IDENTIFIER payload ) )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 98) :
                    alt12 = 1
                elif (LA12_0 == IDENTIFIER) :
                    alt12 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # src/scribble/Scribble.g:341:2: '(' payload ')'
                    pass 
                    char_literal61=self.match(self.input, 98, self.FOLLOW_98_in_messagesignature1544) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal61)
                    self._state.following.append(self.FOLLOW_payload_in_messagesignature1546)
                    payload62 = self.payload()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payload.add(payload62.tree)
                    char_literal63=self.match(self.input, 99, self.FOLLOW_99_in_messagesignature1548) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal63)

                    # AST Rewrite
                    # elements: payload
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 342:2: -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload )
                        # src/scribble/Scribble.g:343:2: ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MESSAGESIGNATURE, "MESSAGESIGNATURE"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_MESSAGE_OP, "EMPTY_MESSAGE_OP"))
                        self._adaptor.addChild(root_1, stream_payload.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt12 == 2:
                    # src/scribble/Scribble.g:346:2: IDENTIFIER '(' payload ')'
                    pass 
                    IDENTIFIER64=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_messagesignature1567) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER64)
                    char_literal65=self.match(self.input, 98, self.FOLLOW_98_in_messagesignature1569) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal65)
                    self._state.following.append(self.FOLLOW_payload_in_messagesignature1571)
                    payload66 = self.payload()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payload.add(payload66.tree)
                    char_literal67=self.match(self.input, 99, self.FOLLOW_99_in_messagesignature1573) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal67)

                    # AST Rewrite
                    # elements: IDENTIFIER, payload
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 347:2: -> ^( MESSAGESIGNATURE IDENTIFIER payload )
                        # src/scribble/Scribble.g:349:2: ^( MESSAGESIGNATURE IDENTIFIER payload )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MESSAGESIGNATURE, "MESSAGESIGNATURE"), root_1)

                        self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                        self._adaptor.addChild(root_1, stream_payload.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "messagesignature"

    class payload_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.payload_return, self).__init__()

            self.tree = None




    # $ANTLR start "payload"
    # src/scribble/Scribble.g:352:1: payload : ( -> ^( PAYLOAD ) | payloadelement ( ',' payloadelement )* -> ^( PAYLOAD ( payloadelement )+ ) );
    def payload(self, ):

        retval = self.payload_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal69 = None
        payloadelement68 = None

        payloadelement70 = None


        char_literal69_tree = None
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_payloadelement = RewriteRuleSubtreeStream(self._adaptor, "rule payloadelement")
        try:
            try:
                # src/scribble/Scribble.g:352:8: ( -> ^( PAYLOAD ) | payloadelement ( ',' payloadelement )* -> ^( PAYLOAD ( payloadelement )+ ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 99) :
                    alt14 = 1
                elif (LA14_0 == IDENTIFIER) :
                    alt14 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # src/scribble/Scribble.g:353:2: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 353:2: -> ^( PAYLOAD )
                        # src/scribble/Scribble.g:354:2: ^( PAYLOAD )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOAD, "PAYLOAD"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt14 == 2:
                    # src/scribble/Scribble.g:356:2: payloadelement ( ',' payloadelement )*
                    pass 
                    self._state.following.append(self.FOLLOW_payloadelement_in_payload1606)
                    payloadelement68 = self.payloadelement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadelement.add(payloadelement68.tree)
                    # src/scribble/Scribble.g:356:17: ( ',' payloadelement )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == 100) :
                            alt13 = 1


                        if alt13 == 1:
                            # src/scribble/Scribble.g:356:18: ',' payloadelement
                            pass 
                            char_literal69=self.match(self.input, 100, self.FOLLOW_100_in_payload1609) 
                            if self._state.backtracking == 0:
                                stream_100.add(char_literal69)
                            self._state.following.append(self.FOLLOW_payloadelement_in_payload1611)
                            payloadelement70 = self.payloadelement()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_payloadelement.add(payloadelement70.tree)


                        else:
                            break #loop13

                    # AST Rewrite
                    # elements: payloadelement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 357:2: -> ^( PAYLOAD ( payloadelement )+ )
                        # src/scribble/Scribble.g:358:2: ^( PAYLOAD ( payloadelement )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOAD, "PAYLOAD"), root_1)

                        # src/scribble/Scribble.g:358:12: ( payloadelement )+
                        if not (stream_payloadelement.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_payloadelement.hasNext():
                            self._adaptor.addChild(root_1, stream_payloadelement.nextTree())


                        stream_payloadelement.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "payload"

    class payloadelement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.payloadelement_return, self).__init__()

            self.tree = None




    # $ANTLR start "payloadelement"
    # src/scribble/Scribble.g:361:1: payloadelement : ( payloadtypename -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename ) | parametername -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername ) | annotationname ':' payloadtypename -> ^( PAYLOADELEMENT annotationname payloadtypename ) | annotationname ':' parametername -> ^( PAYLOADELEMENT annotationname parametername ) );
    def payloadelement(self, ):

        retval = self.payloadelement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal74 = None
        char_literal77 = None
        payloadtypename71 = None

        parametername72 = None

        annotationname73 = None

        payloadtypename75 = None

        annotationname76 = None

        parametername78 = None


        char_literal74_tree = None
        char_literal77_tree = None
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_annotationname = RewriteRuleSubtreeStream(self._adaptor, "rule annotationname")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        try:
            try:
                # src/scribble/Scribble.g:361:15: ( payloadtypename -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename ) | parametername -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername ) | annotationname ':' payloadtypename -> ^( PAYLOADELEMENT annotationname payloadtypename ) | annotationname ':' parametername -> ^( PAYLOADELEMENT annotationname parametername ) )
                alt15 = 4
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IDENTIFIER) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == 101) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == IDENTIFIER) :
                            LA15_5 = self.input.LA(4)

                            if (self.synpred19_Scribble()) :
                                alt15 = 3
                            elif (True) :
                                alt15 = 4
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 15, 5, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae

                    elif (self.synpred17_Scribble()) :
                        alt15 = 1
                    elif (self.synpred18_Scribble()) :
                        alt15 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # src/scribble/Scribble.g:362:2: payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_payloadelement1635)
                    payloadtypename71 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename71.tree)

                    # AST Rewrite
                    # elements: payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 363:2: -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename )
                        # src/scribble/Scribble.g:364:2: ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ANNOTATION, "EMPTY_ANNOTATION"))
                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 2:
                    # src/scribble/Scribble.g:366:2: parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_payloadelement1652)
                    parametername72 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername72.tree)

                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 368:2: -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername )
                        # src/scribble/Scribble.g:369:2: ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ANNOTATION, "EMPTY_ANNOTATION"))
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 3:
                    # src/scribble/Scribble.g:371:2: annotationname ':' payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_annotationname_in_payloadelement1672)
                    annotationname73 = self.annotationname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationname.add(annotationname73.tree)
                    char_literal74=self.match(self.input, 101, self.FOLLOW_101_in_payloadelement1674) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal74)
                    self._state.following.append(self.FOLLOW_payloadtypename_in_payloadelement1676)
                    payloadtypename75 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename75.tree)

                    # AST Rewrite
                    # elements: annotationname, payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 372:2: -> ^( PAYLOADELEMENT annotationname payloadtypename )
                        # src/scribble/Scribble.g:373:2: ^( PAYLOADELEMENT annotationname payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_annotationname.nextTree())
                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 4:
                    # src/scribble/Scribble.g:375:2: annotationname ':' parametername
                    pass 
                    self._state.following.append(self.FOLLOW_annotationname_in_payloadelement1693)
                    annotationname76 = self.annotationname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationname.add(annotationname76.tree)
                    char_literal77=self.match(self.input, 101, self.FOLLOW_101_in_payloadelement1695) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal77)
                    self._state.following.append(self.FOLLOW_parametername_in_payloadelement1697)
                    parametername78 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername78.tree)

                    # AST Rewrite
                    # elements: annotationname, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 376:2: -> ^( PAYLOADELEMENT annotationname parametername )
                        # src/scribble/Scribble.g:377:2: ^( PAYLOADELEMENT annotationname parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_annotationname.nextTree())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "payloadelement"

    class protocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.protocoldecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocoldecl"
    # src/scribble/Scribble.g:381:1: protocoldecl : ( globalprotocoldecl | localprotocoldecl );
    def protocoldecl(self, ):

        retval = self.protocoldecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        globalprotocoldecl79 = None

        localprotocoldecl80 = None



        try:
            try:
                # src/scribble/Scribble.g:384:13: ( globalprotocoldecl | localprotocoldecl )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == GLOBALKW) :
                    alt16 = 1
                elif (LA16_0 == LOCALKW) :
                    alt16 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # src/scribble/Scribble.g:385:2: globalprotocoldecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalprotocoldecl_in_protocoldecl1721)
                    globalprotocoldecl79 = self.globalprotocoldecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalprotocoldecl79.tree)


                elif alt16 == 2:
                    # src/scribble/Scribble.g:387:2: localprotocoldecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localprotocoldecl_in_protocoldecl1726)
                    localprotocoldecl80 = self.localprotocoldecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localprotocoldecl80.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocoldecl"

    class globalprotocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalprotocoldecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalprotocoldecl"
    # src/scribble/Scribble.g:391:1: globalprotocoldecl : ( globalprotocolheader globalprotocoldefinition -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition ) | globalprotocolheader globalprotocolinstance -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance ) );
    def globalprotocoldecl(self, ):

        retval = self.globalprotocoldecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        globalprotocolheader81 = None

        globalprotocoldefinition82 = None

        globalprotocolheader83 = None

        globalprotocolinstance84 = None


        stream_globalprotocolheader = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolheader")
        stream_globalprotocolinstance = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolinstance")
        stream_globalprotocoldefinition = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocoldefinition")
        try:
            try:
                # src/scribble/Scribble.g:394:19: ( globalprotocolheader globalprotocoldefinition -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition ) | globalprotocolheader globalprotocolinstance -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance ) )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # src/scribble/Scribble.g:395:3: globalprotocolheader globalprotocoldefinition
                    pass 
                    self._state.following.append(self.FOLLOW_globalprotocolheader_in_globalprotocoldecl1739)
                    globalprotocolheader81 = self.globalprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolheader.add(globalprotocolheader81.tree)
                    self._state.following.append(self.FOLLOW_globalprotocoldefinition_in_globalprotocoldecl1741)
                    globalprotocoldefinition82 = self.globalprotocoldefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocoldefinition.add(globalprotocoldefinition82.tree)

                    # AST Rewrite
                    # elements: globalprotocoldefinition, globalprotocolheader
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 396:2: -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition )
                        # src/scribble/Scribble.g:397:2: ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLDECL, "GLOBALPROTOCOLDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_globalprotocolheader.nextTree())
                        self._adaptor.addChild(root_1, stream_globalprotocoldefinition.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt17 == 2:
                    # src/scribble/Scribble.g:399:2: globalprotocolheader globalprotocolinstance
                    pass 
                    self._state.following.append(self.FOLLOW_globalprotocolheader_in_globalprotocoldecl1758)
                    globalprotocolheader83 = self.globalprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolheader.add(globalprotocolheader83.tree)
                    self._state.following.append(self.FOLLOW_globalprotocolinstance_in_globalprotocoldecl1760)
                    globalprotocolinstance84 = self.globalprotocolinstance()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolinstance.add(globalprotocolinstance84.tree)

                    # AST Rewrite
                    # elements: globalprotocolinstance, globalprotocolheader
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 400:2: -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance )
                        # src/scribble/Scribble.g:401:2: ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLDECL, "GLOBALPROTOCOLDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_globalprotocolheader.nextTree())
                        self._adaptor.addChild(root_1, stream_globalprotocolinstance.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalprotocoldecl"

    class globalprotocolheader_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalprotocolheader_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalprotocolheader"
    # src/scribble/Scribble.g:404:1: globalprotocolheader : ( GLOBALKW PROTOCOLKW protocolname roledecllist -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist | GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist -> protocolname parameterdecllist roledecllist );
    def globalprotocolheader(self, ):

        retval = self.globalprotocolheader_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GLOBALKW85 = None
        PROTOCOLKW86 = None
        GLOBALKW89 = None
        PROTOCOLKW90 = None
        protocolname87 = None

        roledecllist88 = None

        protocolname91 = None

        parameterdecllist92 = None

        roledecllist93 = None


        GLOBALKW85_tree = None
        PROTOCOLKW86_tree = None
        GLOBALKW89_tree = None
        PROTOCOLKW90_tree = None
        stream_GLOBALKW = RewriteRuleTokenStream(self._adaptor, "token GLOBALKW")
        stream_PROTOCOLKW = RewriteRuleTokenStream(self._adaptor, "token PROTOCOLKW")
        stream_protocolname = RewriteRuleSubtreeStream(self._adaptor, "rule protocolname")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_parameterdecllist = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecllist")
        try:
            try:
                # src/scribble/Scribble.g:404:21: ( GLOBALKW PROTOCOLKW protocolname roledecllist -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist | GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist -> protocolname parameterdecllist roledecllist )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == GLOBALKW) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == PROTOCOLKW) :
                        LA18_2 = self.input.LA(3)

                        if (LA18_2 == IDENTIFIER) :
                            LA18_3 = self.input.LA(4)

                            if (LA18_3 == 98) :
                                alt18 = 1
                            elif (LA18_3 == 96) :
                                alt18 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 18, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 18, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 18, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # src/scribble/Scribble.g:405:2: GLOBALKW PROTOCOLKW protocolname roledecllist
                    pass 
                    GLOBALKW85=self.match(self.input, GLOBALKW, self.FOLLOW_GLOBALKW_in_globalprotocolheader1783) 
                    if self._state.backtracking == 0:
                        stream_GLOBALKW.add(GLOBALKW85)
                    PROTOCOLKW86=self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_globalprotocolheader1785) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW86)
                    self._state.following.append(self.FOLLOW_protocolname_in_globalprotocolheader1787)
                    protocolname87 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname87.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_globalprotocolheader1789)
                    roledecllist88 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist88.tree)

                    # AST Rewrite
                    # elements: roledecllist, protocolname
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 406:2: -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_PARAMETER_DECL_LIST, "EMPTY_PARAMETER_DECL_LIST"))
                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())



                        retval.tree = root_0


                elif alt18 == 2:
                    # src/scribble/Scribble.g:409:2: GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist
                    pass 
                    GLOBALKW89=self.match(self.input, GLOBALKW, self.FOLLOW_GLOBALKW_in_globalprotocolheader1804) 
                    if self._state.backtracking == 0:
                        stream_GLOBALKW.add(GLOBALKW89)
                    PROTOCOLKW90=self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_globalprotocolheader1806) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW90)
                    self._state.following.append(self.FOLLOW_protocolname_in_globalprotocolheader1808)
                    protocolname91 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname91.tree)
                    self._state.following.append(self.FOLLOW_parameterdecllist_in_globalprotocolheader1810)
                    parameterdecllist92 = self.parameterdecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameterdecllist.add(parameterdecllist92.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_globalprotocolheader1812)
                    roledecllist93 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist93.tree)

                    # AST Rewrite
                    # elements: protocolname, roledecllist, parameterdecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 410:2: -> protocolname parameterdecllist roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())
                        self._adaptor.addChild(root_0, stream_parameterdecllist.nextTree())
                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalprotocolheader"

    class roledecllist_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.roledecllist_return, self).__init__()

            self.tree = None




    # $ANTLR start "roledecllist"
    # src/scribble/Scribble.g:414:1: roledecllist : '(' roledecl ( ',' roledecl )* ')' -> ^( ROLEDECLLIST ( roledecl )+ ) ;
    def roledecllist(self, ):

        retval = self.roledecllist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal94 = None
        char_literal96 = None
        char_literal98 = None
        roledecl95 = None

        roledecl97 = None


        char_literal94_tree = None
        char_literal96_tree = None
        char_literal98_tree = None
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_roledecl = RewriteRuleSubtreeStream(self._adaptor, "rule roledecl")
        try:
            try:
                # src/scribble/Scribble.g:414:13: ( '(' roledecl ( ',' roledecl )* ')' -> ^( ROLEDECLLIST ( roledecl )+ ) )
                # src/scribble/Scribble.g:415:2: '(' roledecl ( ',' roledecl )* ')'
                pass 
                char_literal94=self.match(self.input, 98, self.FOLLOW_98_in_roledecllist1831) 
                if self._state.backtracking == 0:
                    stream_98.add(char_literal94)
                self._state.following.append(self.FOLLOW_roledecl_in_roledecllist1833)
                roledecl95 = self.roledecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roledecl.add(roledecl95.tree)
                # src/scribble/Scribble.g:415:15: ( ',' roledecl )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 100) :
                        alt19 = 1


                    if alt19 == 1:
                        # src/scribble/Scribble.g:415:16: ',' roledecl
                        pass 
                        char_literal96=self.match(self.input, 100, self.FOLLOW_100_in_roledecllist1836) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal96)
                        self._state.following.append(self.FOLLOW_roledecl_in_roledecllist1838)
                        roledecl97 = self.roledecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roledecl.add(roledecl97.tree)


                    else:
                        break #loop19
                char_literal98=self.match(self.input, 99, self.FOLLOW_99_in_roledecllist1842) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal98)

                # AST Rewrite
                # elements: roledecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 416:2: -> ^( ROLEDECLLIST ( roledecl )+ )
                    # src/scribble/Scribble.g:417:2: ^( ROLEDECLLIST ( roledecl )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEDECLLIST, "ROLEDECLLIST"), root_1)

                    # src/scribble/Scribble.g:417:17: ( roledecl )+
                    if not (stream_roledecl.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roledecl.hasNext():
                        self._adaptor.addChild(root_1, stream_roledecl.nextTree())


                    stream_roledecl.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roledecllist"

    class roledecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.roledecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "roledecl"
    # src/scribble/Scribble.g:420:1: roledecl : ( ROLEKW rolename -> ^( ROLEDECL rolename ) | ROLEKW rolename ASKW rolename -> ^( ROLEDECL rolename rolename ) );
    def roledecl(self, ):

        retval = self.roledecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ROLEKW99 = None
        ROLEKW101 = None
        ASKW103 = None
        rolename100 = None

        rolename102 = None

        rolename104 = None


        ROLEKW99_tree = None
        ROLEKW101_tree = None
        ASKW103_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_ROLEKW = RewriteRuleTokenStream(self._adaptor, "token ROLEKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:420:9: ( ROLEKW rolename -> ^( ROLEDECL rolename ) | ROLEKW rolename ASKW rolename -> ^( ROLEDECL rolename rolename ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ROLEKW) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == IDENTIFIER) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 == ASKW) :
                            alt20 = 2
                        elif (LA20_2 == EOF or (99 <= LA20_2 <= 100)) :
                            alt20 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 20, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # src/scribble/Scribble.g:421:2: ROLEKW rolename
                    pass 
                    ROLEKW99=self.match(self.input, ROLEKW, self.FOLLOW_ROLEKW_in_roledecl1864) 
                    if self._state.backtracking == 0:
                        stream_ROLEKW.add(ROLEKW99)
                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1866)
                    rolename100 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename100.tree)

                    # AST Rewrite
                    # elements: rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 422:2: -> ^( ROLEDECL rolename )
                        # src/scribble/Scribble.g:423:2: ^( ROLEDECL rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEDECL, "ROLEDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt20 == 2:
                    # src/scribble/Scribble.g:425:2: ROLEKW rolename ASKW rolename
                    pass 
                    ROLEKW101=self.match(self.input, ROLEKW, self.FOLLOW_ROLEKW_in_roledecl1881) 
                    if self._state.backtracking == 0:
                        stream_ROLEKW.add(ROLEKW101)
                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1883)
                    rolename102 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename102.tree)
                    ASKW103=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_roledecl1885) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW103)
                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1887)
                    rolename104 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename104.tree)

                    # AST Rewrite
                    # elements: rolename, rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 426:2: -> ^( ROLEDECL rolename rolename )
                        # src/scribble/Scribble.g:427:2: ^( ROLEDECL rolename rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEDECL, "ROLEDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roledecl"

    class parameterdecllist_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.parameterdecllist_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterdecllist"
    # src/scribble/Scribble.g:430:1: parameterdecllist : '<' parameterdecl ( ',' parameterdecl )* '>' -> ^( PARAMETERDECLLIST ( parameterdecl )+ ) ;
    def parameterdecllist(self, ):

        retval = self.parameterdecllist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal105 = None
        char_literal107 = None
        char_literal109 = None
        parameterdecl106 = None

        parameterdecl108 = None


        char_literal105_tree = None
        char_literal107_tree = None
        char_literal109_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_parameterdecl = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecl")
        try:
            try:
                # src/scribble/Scribble.g:430:18: ( '<' parameterdecl ( ',' parameterdecl )* '>' -> ^( PARAMETERDECLLIST ( parameterdecl )+ ) )
                # src/scribble/Scribble.g:431:2: '<' parameterdecl ( ',' parameterdecl )* '>'
                pass 
                char_literal105=self.match(self.input, 96, self.FOLLOW_96_in_parameterdecllist1908) 
                if self._state.backtracking == 0:
                    stream_96.add(char_literal105)
                self._state.following.append(self.FOLLOW_parameterdecl_in_parameterdecllist1910)
                parameterdecl106 = self.parameterdecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_parameterdecl.add(parameterdecl106.tree)
                # src/scribble/Scribble.g:431:20: ( ',' parameterdecl )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 100) :
                        alt21 = 1


                    if alt21 == 1:
                        # src/scribble/Scribble.g:431:21: ',' parameterdecl
                        pass 
                        char_literal107=self.match(self.input, 100, self.FOLLOW_100_in_parameterdecllist1913) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal107)
                        self._state.following.append(self.FOLLOW_parameterdecl_in_parameterdecllist1915)
                        parameterdecl108 = self.parameterdecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameterdecl.add(parameterdecl108.tree)


                    else:
                        break #loop21
                char_literal109=self.match(self.input, 97, self.FOLLOW_97_in_parameterdecllist1919) 
                if self._state.backtracking == 0:
                    stream_97.add(char_literal109)

                # AST Rewrite
                # elements: parameterdecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 432:2: -> ^( PARAMETERDECLLIST ( parameterdecl )+ )
                    # src/scribble/Scribble.g:433:2: ^( PARAMETERDECLLIST ( parameterdecl )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERDECLLIST, "PARAMETERDECLLIST"), root_1)

                    # src/scribble/Scribble.g:433:22: ( parameterdecl )+
                    if not (stream_parameterdecl.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_parameterdecl.hasNext():
                        self._adaptor.addChild(root_1, stream_parameterdecl.nextTree())


                    stream_parameterdecl.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameterdecllist"

    class parameterdecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.parameterdecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterdecl"
    # src/scribble/Scribble.g:436:1: parameterdecl : ( TYPEKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername ) | TYPEKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername ) | SIGKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername ) | SIGKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername ) );
    def parameterdecl(self, ):

        retval = self.parameterdecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TYPEKW110 = None
        TYPEKW112 = None
        ASKW114 = None
        SIGKW116 = None
        SIGKW118 = None
        ASKW120 = None
        parametername111 = None

        parametername113 = None

        parametername115 = None

        parametername117 = None

        parametername119 = None

        parametername121 = None


        TYPEKW110_tree = None
        TYPEKW112_tree = None
        ASKW114_tree = None
        SIGKW116_tree = None
        SIGKW118_tree = None
        ASKW120_tree = None
        stream_TYPEKW = RewriteRuleTokenStream(self._adaptor, "token TYPEKW")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_SIGKW = RewriteRuleTokenStream(self._adaptor, "token SIGKW")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        try:
            try:
                # src/scribble/Scribble.g:436:14: ( TYPEKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername ) | TYPEKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername ) | SIGKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername ) | SIGKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername ) )
                alt22 = 4
                LA22_0 = self.input.LA(1)

                if (LA22_0 == TYPEKW) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == IDENTIFIER) :
                        LA22_3 = self.input.LA(3)

                        if (LA22_3 == ASKW) :
                            alt22 = 2
                        elif (LA22_3 == EOF or LA22_3 == 97 or LA22_3 == 100) :
                            alt22 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 22, 3, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae

                elif (LA22_0 == SIGKW) :
                    LA22_2 = self.input.LA(2)

                    if (LA22_2 == IDENTIFIER) :
                        LA22_4 = self.input.LA(3)

                        if (LA22_4 == EOF or LA22_4 == 97 or LA22_4 == 100) :
                            alt22 = 3
                        elif (LA22_4 == ASKW) :
                            alt22 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 22, 4, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 22, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # src/scribble/Scribble.g:437:3: TYPEKW parametername
                    pass 
                    TYPEKW110=self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_parameterdecl1942) 
                    if self._state.backtracking == 0:
                        stream_TYPEKW.add(TYPEKW110)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1944)
                    parametername111 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername111.tree)

                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 438:2: -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername )
                        # src/scribble/Scribble.g:439:2: ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(KIND_PAYLOAD_TYPE, "KIND_PAYLOAD_TYPE"))
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 2:
                    # src/scribble/Scribble.g:441:3: TYPEKW parametername ASKW parametername
                    pass 
                    TYPEKW112=self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_parameterdecl1962) 
                    if self._state.backtracking == 0:
                        stream_TYPEKW.add(TYPEKW112)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1964)
                    parametername113 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername113.tree)
                    ASKW114=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_parameterdecl1966) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW114)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1968)
                    parametername115 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername115.tree)

                    # AST Rewrite
                    # elements: parametername, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 442:2: -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername )
                        # src/scribble/Scribble.g:443:2: ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(KIND_PAYLOAD_TYPE, "KIND_PAYLOAD_TYPE"))
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 3:
                    # src/scribble/Scribble.g:445:3: SIGKW parametername
                    pass 
                    SIGKW116=self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterdecl1988) 
                    if self._state.backtracking == 0:
                        stream_SIGKW.add(SIGKW116)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1990)
                    parametername117 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername117.tree)

                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 446:2: -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername )
                        # src/scribble/Scribble.g:447:2: ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(KIND_MESSAGE_SIGNATURE, "KIND_MESSAGE_SIGNATURE"))
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 4:
                    # src/scribble/Scribble.g:449:3: SIGKW parametername ASKW parametername
                    pass 
                    SIGKW118=self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterdecl2008) 
                    if self._state.backtracking == 0:
                        stream_SIGKW.add(SIGKW118)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl2010)
                    parametername119 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername119.tree)
                    ASKW120=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_parameterdecl2012) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW120)
                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl2014)
                    parametername121 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername121.tree)

                    # AST Rewrite
                    # elements: parametername, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 450:2: -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername )
                        # src/scribble/Scribble.g:451:2: ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(KIND_MESSAGE_SIGNATURE, "KIND_MESSAGE_SIGNATURE"))
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameterdecl"

    class globalprotocoldefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalprotocoldefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalprotocoldefinition"
    # src/scribble/Scribble.g:455:1: globalprotocoldefinition : globalprotocolblock -> ^( GLOBALPROTOCOLDEF globalprotocolblock ) ;
    def globalprotocoldefinition(self, ):

        retval = self.globalprotocoldefinition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        globalprotocolblock122 = None


        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:458:25: ( globalprotocolblock -> ^( GLOBALPROTOCOLDEF globalprotocolblock ) )
                # src/scribble/Scribble.g:459:2: globalprotocolblock
                pass 
                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalprotocoldefinition2040)
                globalprotocolblock122 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock122.tree)

                # AST Rewrite
                # elements: globalprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 460:2: -> ^( GLOBALPROTOCOLDEF globalprotocolblock )
                    # src/scribble/Scribble.g:461:2: ^( GLOBALPROTOCOLDEF globalprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLDEF, "GLOBALPROTOCOLDEF"), root_1)

                    self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalprotocoldefinition"

    class globalprotocolinstance_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalprotocolinstance_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalprotocolinstance"
    # src/scribble/Scribble.g:465:1: globalprotocolinstance : ( INSTANTIATESKW membername roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | INSTANTIATESKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername ) );
    def globalprotocolinstance(self, ):

        retval = self.globalprotocolinstance_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INSTANTIATESKW123 = None
        char_literal126 = None
        INSTANTIATESKW127 = None
        char_literal131 = None
        membername124 = None

        roleinstantiationlist125 = None

        membername128 = None

        argumentlist129 = None

        roleinstantiationlist130 = None


        INSTANTIATESKW123_tree = None
        char_literal126_tree = None
        INSTANTIATESKW127_tree = None
        char_literal131_tree = None
        stream_INSTANTIATESKW = RewriteRuleTokenStream(self._adaptor, "token INSTANTIATESKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        try:
            try:
                # src/scribble/Scribble.g:468:23: ( INSTANTIATESKW membername roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | INSTANTIATESKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername ) )
                alt23 = 2
                alt23 = self.dfa23.predict(self.input)
                if alt23 == 1:
                    # src/scribble/Scribble.g:469:2: INSTANTIATESKW membername roleinstantiationlist ';'
                    pass 
                    INSTANTIATESKW123=self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2062) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW123)
                    self._state.following.append(self.FOLLOW_membername_in_globalprotocolinstance2064)
                    membername124 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername124.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globalprotocolinstance2066)
                    roleinstantiationlist125 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist125.tree)
                    char_literal126=self.match(self.input, 95, self.FOLLOW_95_in_globalprotocolinstance2068) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal126)

                    # AST Rewrite
                    # elements: membername, roleinstantiationlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 470:2: -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # src/scribble/Scribble.g:471:2: ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLINSTANCE, "GLOBALPROTOCOLINSTANCE"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # src/scribble/Scribble.g:474:2: INSTANTIATESKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    INSTANTIATESKW127=self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2089) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW127)
                    self._state.following.append(self.FOLLOW_membername_in_globalprotocolinstance2091)
                    membername128 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername128.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_globalprotocolinstance2093)
                    argumentlist129 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist129.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globalprotocolinstance2095)
                    roleinstantiationlist130 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist130.tree)
                    char_literal131=self.match(self.input, 95, self.FOLLOW_95_in_globalprotocolinstance2097) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal131)

                    # AST Rewrite
                    # elements: membername, roleinstantiationlist, argumentlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 475:2: -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername )
                        # src/scribble/Scribble.g:476:2: ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLINSTANCE, "GLOBALPROTOCOLINSTANCE"), root_1)

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalprotocolinstance"

    class roleinstantiationlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.roleinstantiationlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleinstantiationlist"
    # src/scribble/Scribble.g:479:1: roleinstantiationlist : '(' roleinstantiation ( ',' roleinstantiation )* ')' -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ ) ;
    def roleinstantiationlist(self, ):

        retval = self.roleinstantiationlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal132 = None
        char_literal134 = None
        char_literal136 = None
        roleinstantiation133 = None

        roleinstantiation135 = None


        char_literal132_tree = None
        char_literal134_tree = None
        char_literal136_tree = None
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_roleinstantiation = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiation")
        try:
            try:
                # src/scribble/Scribble.g:479:22: ( '(' roleinstantiation ( ',' roleinstantiation )* ')' -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ ) )
                # src/scribble/Scribble.g:480:2: '(' roleinstantiation ( ',' roleinstantiation )* ')'
                pass 
                char_literal132=self.match(self.input, 98, self.FOLLOW_98_in_roleinstantiationlist2120) 
                if self._state.backtracking == 0:
                    stream_98.add(char_literal132)
                self._state.following.append(self.FOLLOW_roleinstantiation_in_roleinstantiationlist2122)
                roleinstantiation133 = self.roleinstantiation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleinstantiation.add(roleinstantiation133.tree)
                # src/scribble/Scribble.g:480:24: ( ',' roleinstantiation )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 100) :
                        alt24 = 1


                    if alt24 == 1:
                        # src/scribble/Scribble.g:480:25: ',' roleinstantiation
                        pass 
                        char_literal134=self.match(self.input, 100, self.FOLLOW_100_in_roleinstantiationlist2125) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal134)
                        self._state.following.append(self.FOLLOW_roleinstantiation_in_roleinstantiationlist2127)
                        roleinstantiation135 = self.roleinstantiation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roleinstantiation.add(roleinstantiation135.tree)


                    else:
                        break #loop24
                char_literal136=self.match(self.input, 99, self.FOLLOW_99_in_roleinstantiationlist2131) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal136)

                # AST Rewrite
                # elements: roleinstantiation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 481:2: -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ )
                    # src/scribble/Scribble.g:482:2: ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEINSTANTIATIONLIST, "ROLEINSTANTIATIONLIST"), root_1)

                    # src/scribble/Scribble.g:482:26: ( roleinstantiation )+
                    if not (stream_roleinstantiation.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleinstantiation.hasNext():
                        self._adaptor.addChild(root_1, stream_roleinstantiation.nextTree())


                    stream_roleinstantiation.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleinstantiationlist"

    class roleinstantiation_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.roleinstantiation_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleinstantiation"
    # src/scribble/Scribble.g:485:1: roleinstantiation : ( rolename -> ^( ROLEINSTANTIATION rolename ) | rolename ASKW rolename -> ^( ROLEINSTANTIATION rolename rolename ) );
    def roleinstantiation(self, ):

        retval = self.roleinstantiation_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASKW139 = None
        rolename137 = None

        rolename138 = None

        rolename140 = None


        ASKW139_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:485:18: ( rolename -> ^( ROLEINSTANTIATION rolename ) | rolename ASKW rolename -> ^( ROLEINSTANTIATION rolename rolename ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == IDENTIFIER) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == ASKW) :
                        alt25 = 2
                    elif (LA25_1 == EOF or (99 <= LA25_1 <= 100)) :
                        alt25 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # src/scribble/Scribble.g:486:2: rolename
                    pass 
                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2153)
                    rolename137 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename137.tree)

                    # AST Rewrite
                    # elements: rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 487:2: -> ^( ROLEINSTANTIATION rolename )
                        # src/scribble/Scribble.g:488:2: ^( ROLEINSTANTIATION rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEINSTANTIATION, "ROLEINSTANTIATION"), root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt25 == 2:
                    # src/scribble/Scribble.g:490:2: rolename ASKW rolename
                    pass 
                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2168)
                    rolename138 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename138.tree)
                    ASKW139=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_roleinstantiation2170) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW139)
                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2172)
                    rolename140 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename140.tree)

                    # AST Rewrite
                    # elements: rolename, rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 491:2: -> ^( ROLEINSTANTIATION rolename rolename )
                        # src/scribble/Scribble.g:492:2: ^( ROLEINSTANTIATION rolename rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLEINSTANTIATION, "ROLEINSTANTIATION"), root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleinstantiation"

    class argumentlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.argumentlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "argumentlist"
    # src/scribble/Scribble.g:495:1: argumentlist : '<' argument ( ',' argument )* '>' -> ^( ARGUMENTLIST ( argument )+ ) ;
    def argumentlist(self, ):

        retval = self.argumentlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal141 = None
        char_literal143 = None
        char_literal145 = None
        argument142 = None

        argument144 = None


        char_literal141_tree = None
        char_literal143_tree = None
        char_literal145_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_argument = RewriteRuleSubtreeStream(self._adaptor, "rule argument")
        try:
            try:
                # src/scribble/Scribble.g:495:13: ( '<' argument ( ',' argument )* '>' -> ^( ARGUMENTLIST ( argument )+ ) )
                # src/scribble/Scribble.g:496:2: '<' argument ( ',' argument )* '>'
                pass 
                char_literal141=self.match(self.input, 96, self.FOLLOW_96_in_argumentlist2193) 
                if self._state.backtracking == 0:
                    stream_96.add(char_literal141)
                self._state.following.append(self.FOLLOW_argument_in_argumentlist2195)
                argument142 = self.argument()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_argument.add(argument142.tree)
                # src/scribble/Scribble.g:496:15: ( ',' argument )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == 100) :
                        alt26 = 1


                    if alt26 == 1:
                        # src/scribble/Scribble.g:496:16: ',' argument
                        pass 
                        char_literal143=self.match(self.input, 100, self.FOLLOW_100_in_argumentlist2198) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal143)
                        self._state.following.append(self.FOLLOW_argument_in_argumentlist2200)
                        argument144 = self.argument()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_argument.add(argument144.tree)


                    else:
                        break #loop26
                char_literal145=self.match(self.input, 97, self.FOLLOW_97_in_argumentlist2204) 
                if self._state.backtracking == 0:
                    stream_97.add(char_literal145)

                # AST Rewrite
                # elements: argument
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 497:2: -> ^( ARGUMENTLIST ( argument )+ )
                    # src/scribble/Scribble.g:498:2: ^( ARGUMENTLIST ( argument )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENTLIST, "ARGUMENTLIST"), root_1)

                    # src/scribble/Scribble.g:498:17: ( argument )+
                    if not (stream_argument.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_argument.hasNext():
                        self._adaptor.addChild(root_1, stream_argument.nextTree())


                    stream_argument.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "argumentlist"

    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.argument_return, self).__init__()

            self.tree = None




    # $ANTLR start "argument"
    # src/scribble/Scribble.g:501:1: argument : ( messagesignature -> ^( ARGUMENT messagesignature ) | messagesignature ASKW parametername -> ^( ARGUMENT messagesignature parametername ) | payloadtypename -> ^( ARGUMENT payloadtypename ) | payloadtypename ASKW parametername -> ^( ARGUMENT payloadtypename parametername ) | parametername -> ^( ARGUMENT parametername ) | parametername ASKW parametername -> ^( ARGUMENT parametername ASKW parametername ) );
    def argument(self, ):

        retval = self.argument_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASKW148 = None
        ASKW152 = None
        ASKW156 = None
        messagesignature146 = None

        messagesignature147 = None

        parametername149 = None

        payloadtypename150 = None

        payloadtypename151 = None

        parametername153 = None

        parametername154 = None

        parametername155 = None

        parametername157 = None


        ASKW148_tree = None
        ASKW152_tree = None
        ASKW156_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_messagesignature = RewriteRuleSubtreeStream(self._adaptor, "rule messagesignature")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        try:
            try:
                # src/scribble/Scribble.g:501:9: ( messagesignature -> ^( ARGUMENT messagesignature ) | messagesignature ASKW parametername -> ^( ARGUMENT messagesignature parametername ) | payloadtypename -> ^( ARGUMENT payloadtypename ) | payloadtypename ASKW parametername -> ^( ARGUMENT payloadtypename parametername ) | parametername -> ^( ARGUMENT parametername ) | parametername ASKW parametername -> ^( ARGUMENT parametername ASKW parametername ) )
                alt27 = 6
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # src/scribble/Scribble.g:502:2: messagesignature
                    pass 
                    self._state.following.append(self.FOLLOW_messagesignature_in_argument2226)
                    messagesignature146 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_messagesignature.add(messagesignature146.tree)

                    # AST Rewrite
                    # elements: messagesignature
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 503:2: -> ^( ARGUMENT messagesignature )
                        # src/scribble/Scribble.g:504:2: ^( ARGUMENT messagesignature )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_messagesignature.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 2:
                    # src/scribble/Scribble.g:506:2: messagesignature ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_messagesignature_in_argument2241)
                    messagesignature147 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_messagesignature.add(messagesignature147.tree)
                    ASKW148=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2243) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW148)
                    self._state.following.append(self.FOLLOW_parametername_in_argument2245)
                    parametername149 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername149.tree)

                    # AST Rewrite
                    # elements: messagesignature, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 507:2: -> ^( ARGUMENT messagesignature parametername )
                        # src/scribble/Scribble.g:508:2: ^( ARGUMENT messagesignature parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_messagesignature.nextTree())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 3:
                    # src/scribble/Scribble.g:510:2: payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_argument2262)
                    payloadtypename150 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename150.tree)

                    # AST Rewrite
                    # elements: payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 511:2: -> ^( ARGUMENT payloadtypename )
                        # src/scribble/Scribble.g:512:2: ^( ARGUMENT payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 4:
                    # src/scribble/Scribble.g:514:2: payloadtypename ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_argument2277)
                    payloadtypename151 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename151.tree)
                    ASKW152=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2279) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW152)
                    self._state.following.append(self.FOLLOW_parametername_in_argument2281)
                    parametername153 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername153.tree)

                    # AST Rewrite
                    # elements: parametername, payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 515:2: -> ^( ARGUMENT payloadtypename parametername )
                        # src/scribble/Scribble.g:516:2: ^( ARGUMENT payloadtypename parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 5:
                    # src/scribble/Scribble.g:518:2: parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_argument2298)
                    parametername154 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername154.tree)

                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 519:2: -> ^( ARGUMENT parametername )
                        # src/scribble/Scribble.g:520:2: ^( ARGUMENT parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 6:
                    # src/scribble/Scribble.g:522:2: parametername ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_argument2315)
                    parametername155 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername155.tree)
                    ASKW156=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2317) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW156)
                    self._state.following.append(self.FOLLOW_parametername_in_argument2319)
                    parametername157 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername157.tree)

                    # AST Rewrite
                    # elements: parametername, parametername, ASKW
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 523:2: -> ^( ARGUMENT parametername ASKW parametername )
                        # src/scribble/Scribble.g:524:2: ^( ARGUMENT parametername ASKW parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGUMENT, "ARGUMENT"), root_1)

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())
                        self._adaptor.addChild(root_1, stream_ASKW.nextNode())
                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "argument"

    class globalprotocolblock_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalprotocolblock_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalprotocolblock"
    # src/scribble/Scribble.g:528:1: globalprotocolblock : '{' globalinteractionsequence '}' -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence ) ;
    def globalprotocolblock(self, ):

        retval = self.globalprotocolblock_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal158 = None
        char_literal160 = None
        globalinteractionsequence159 = None


        char_literal158_tree = None
        char_literal160_tree = None
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_globalinteractionsequence = RewriteRuleSubtreeStream(self._adaptor, "rule globalinteractionsequence")
        try:
            try:
                # src/scribble/Scribble.g:531:20: ( '{' globalinteractionsequence '}' -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence ) )
                # src/scribble/Scribble.g:532:2: '{' globalinteractionsequence '}'
                pass 
                char_literal158=self.match(self.input, 102, self.FOLLOW_102_in_globalprotocolblock2345) 
                if self._state.backtracking == 0:
                    stream_102.add(char_literal158)
                self._state.following.append(self.FOLLOW_globalinteractionsequence_in_globalprotocolblock2347)
                globalinteractionsequence159 = self.globalinteractionsequence()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalinteractionsequence.add(globalinteractionsequence159.tree)
                char_literal160=self.match(self.input, 103, self.FOLLOW_103_in_globalprotocolblock2349) 
                if self._state.backtracking == 0:
                    stream_103.add(char_literal160)

                # AST Rewrite
                # elements: globalinteractionsequence
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 533:2: -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence )
                    # src/scribble/Scribble.g:534:2: ^( GLOBALPROTOCOLBLOCK globalinteractionsequence )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPROTOCOLBLOCK, "GLOBALPROTOCOLBLOCK"), root_1)

                    self._adaptor.addChild(root_1, stream_globalinteractionsequence.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalprotocolblock"

    class globalinteractionsequence_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalinteractionsequence_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalinteractionsequence"
    # src/scribble/Scribble.g:537:1: globalinteractionsequence : ( globalinteraction )* -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* ) ;
    def globalinteractionsequence(self, ):

        retval = self.globalinteractionsequence_return()
        retval.start = self.input.LT(1)

        root_0 = None

        globalinteraction161 = None


        stream_globalinteraction = RewriteRuleSubtreeStream(self._adaptor, "rule globalinteraction")
        try:
            try:
                # src/scribble/Scribble.g:537:26: ( ( globalinteraction )* -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* ) )
                # src/scribble/Scribble.g:538:2: ( globalinteraction )*
                pass 
                # src/scribble/Scribble.g:538:2: ( globalinteraction )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == CHOICEKW or (RECKW <= LA28_0 <= PARKW) or LA28_0 == INTERRUPTIBLEKW or LA28_0 == DOKW or LA28_0 == IDENTIFIER or LA28_0 == 98) :
                        alt28 = 1


                    if alt28 == 1:
                        # src/scribble/Scribble.g:538:3: globalinteraction
                        pass 
                        self._state.following.append(self.FOLLOW_globalinteraction_in_globalinteractionsequence2369)
                        globalinteraction161 = self.globalinteraction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalinteraction.add(globalinteraction161.tree)


                    else:
                        break #loop28

                # AST Rewrite
                # elements: globalinteraction
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 539:2: -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* )
                    # src/scribble/Scribble.g:540:2: ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALINTERACTIONSEQUENCE, "GLOBALINTERACTIONSEQUENCE"), root_1)

                    # src/scribble/Scribble.g:540:30: ( globalinteraction )*
                    while stream_globalinteraction.hasNext():
                        self._adaptor.addChild(root_1, stream_globalinteraction.nextTree())


                    stream_globalinteraction.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalinteractionsequence"

    class globalinteraction_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalinteraction_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalinteraction"
    # src/scribble/Scribble.g:543:1: globalinteraction : ( globalmessagetransfer | globalchoice | globalrecursion | globalcontinue | globalparallel | globalinterruptible | globaldo );
    def globalinteraction(self, ):

        retval = self.globalinteraction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        globalmessagetransfer162 = None

        globalchoice163 = None

        globalrecursion164 = None

        globalcontinue165 = None

        globalparallel166 = None

        globalinterruptible167 = None

        globaldo168 = None



        try:
            try:
                # src/scribble/Scribble.g:543:18: ( globalmessagetransfer | globalchoice | globalrecursion | globalcontinue | globalparallel | globalinterruptible | globaldo )
                alt29 = 7
                LA29 = self.input.LA(1)
                if LA29 == IDENTIFIER or LA29 == 98:
                    alt29 = 1
                elif LA29 == CHOICEKW:
                    alt29 = 2
                elif LA29 == RECKW:
                    alt29 = 3
                elif LA29 == CONTINUEKW:
                    alt29 = 4
                elif LA29 == PARKW:
                    alt29 = 5
                elif LA29 == INTERRUPTIBLEKW:
                    alt29 = 6
                elif LA29 == DOKW:
                    alt29 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # src/scribble/Scribble.g:544:2: globalmessagetransfer
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalmessagetransfer_in_globalinteraction2393)
                    globalmessagetransfer162 = self.globalmessagetransfer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalmessagetransfer162.tree)


                elif alt29 == 2:
                    # src/scribble/Scribble.g:546:2: globalchoice
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalchoice_in_globalinteraction2398)
                    globalchoice163 = self.globalchoice()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalchoice163.tree)


                elif alt29 == 3:
                    # src/scribble/Scribble.g:548:2: globalrecursion
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalrecursion_in_globalinteraction2403)
                    globalrecursion164 = self.globalrecursion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalrecursion164.tree)


                elif alt29 == 4:
                    # src/scribble/Scribble.g:550:2: globalcontinue
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalcontinue_in_globalinteraction2408)
                    globalcontinue165 = self.globalcontinue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalcontinue165.tree)


                elif alt29 == 5:
                    # src/scribble/Scribble.g:552:2: globalparallel
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalparallel_in_globalinteraction2413)
                    globalparallel166 = self.globalparallel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalparallel166.tree)


                elif alt29 == 6:
                    # src/scribble/Scribble.g:554:2: globalinterruptible
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalinterruptible_in_globalinteraction2418)
                    globalinterruptible167 = self.globalinterruptible()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalinterruptible167.tree)


                elif alt29 == 7:
                    # src/scribble/Scribble.g:556:2: globaldo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globaldo_in_globalinteraction2423)
                    globaldo168 = self.globaldo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globaldo168.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalinteraction"

    class globalmessagetransfer_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalmessagetransfer_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalmessagetransfer"
    # src/scribble/Scribble.g:562:1: globalmessagetransfer : message FROMKW rolename TOKW rolename ( ',' rolename )* ';' -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ ) ;
    def globalmessagetransfer(self, ):

        retval = self.globalmessagetransfer_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROMKW170 = None
        TOKW172 = None
        char_literal174 = None
        char_literal176 = None
        message169 = None

        rolename171 = None

        rolename173 = None

        rolename175 = None


        FROMKW170_tree = None
        TOKW172_tree = None
        char_literal174_tree = None
        char_literal176_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:565:22: ( message FROMKW rolename TOKW rolename ( ',' rolename )* ';' -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ ) )
                # src/scribble/Scribble.g:566:2: message FROMKW rolename TOKW rolename ( ',' rolename )* ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_globalmessagetransfer2437)
                message169 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message169.tree)
                FROMKW170=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_globalmessagetransfer2439) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW170)
                self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2441)
                rolename171 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename171.tree)
                TOKW172=self.match(self.input, TOKW, self.FOLLOW_TOKW_in_globalmessagetransfer2443) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW172)
                self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2445)
                rolename173 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename173.tree)
                # src/scribble/Scribble.g:566:40: ( ',' rolename )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 100) :
                        alt30 = 1


                    if alt30 == 1:
                        # src/scribble/Scribble.g:566:41: ',' rolename
                        pass 
                        char_literal174=self.match(self.input, 100, self.FOLLOW_100_in_globalmessagetransfer2448) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal174)
                        self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2450)
                        rolename175 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename175.tree)


                    else:
                        break #loop30
                char_literal176=self.match(self.input, 95, self.FOLLOW_95_in_globalmessagetransfer2455) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal176)

                # AST Rewrite
                # elements: rolename, rolename, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 567:2: -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ )
                    # src/scribble/Scribble.g:568:2: ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALMESSAGETRANSFER, "GLOBALMESSAGETRANSFER"), root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())
                    self._adaptor.addChild(root_1, stream_rolename.nextTree())
                    # src/scribble/Scribble.g:568:43: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalmessagetransfer"

    class message_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.message_return, self).__init__()

            self.tree = None




    # $ANTLR start "message"
    # src/scribble/Scribble.g:571:1: message : ( messagesignature | parametername );
    def message(self, ):

        retval = self.message_return()
        retval.start = self.input.LT(1)

        root_0 = None

        messagesignature177 = None

        parametername178 = None



        try:
            try:
                # src/scribble/Scribble.g:571:8: ( messagesignature | parametername )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == 98) :
                    alt31 = 1
                elif (LA31_0 == IDENTIFIER) :
                    LA31_2 = self.input.LA(2)

                    if (LA31_2 == 98) :
                        alt31 = 1
                    elif (LA31_2 == EOF or (FROMKW <= LA31_2 <= TOKW) or LA31_2 == BYKW or LA31_2 == 100) :
                        alt31 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 31, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # src/scribble/Scribble.g:572:2: messagesignature
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_messagesignature_in_message2481)
                    messagesignature177 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, messagesignature177.tree)


                elif alt31 == 2:
                    # src/scribble/Scribble.g:574:2: parametername
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_parametername_in_message2486)
                    parametername178 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parametername178.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message"

    class globalchoice_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalchoice_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalchoice"
    # src/scribble/Scribble.g:578:1: globalchoice : CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )* -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ ) ;
    def globalchoice(self, ):

        retval = self.globalchoice_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHOICEKW179 = None
        ATKW180 = None
        ORKW183 = None
        rolename181 = None

        globalprotocolblock182 = None

        globalprotocolblock184 = None


        CHOICEKW179_tree = None
        ATKW180_tree = None
        ORKW183_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_ORKW = RewriteRuleTokenStream(self._adaptor, "token ORKW")
        stream_CHOICEKW = RewriteRuleTokenStream(self._adaptor, "token CHOICEKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:581:13: ( CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )* -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ ) )
                # src/scribble/Scribble.g:582:2: CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )*
                pass 
                CHOICEKW179=self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_globalchoice2498) 
                if self._state.backtracking == 0:
                    stream_CHOICEKW.add(CHOICEKW179)
                ATKW180=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_globalchoice2500) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(ATKW180)
                self._state.following.append(self.FOLLOW_rolename_in_globalchoice2502)
                rolename181 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename181.tree)
                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalchoice2504)
                globalprotocolblock182 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock182.tree)
                # src/scribble/Scribble.g:582:45: ( ORKW globalprotocolblock )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ORKW) :
                        alt32 = 1


                    if alt32 == 1:
                        # src/scribble/Scribble.g:582:46: ORKW globalprotocolblock
                        pass 
                        ORKW183=self.match(self.input, ORKW, self.FOLLOW_ORKW_in_globalchoice2507) 
                        if self._state.backtracking == 0:
                            stream_ORKW.add(ORKW183)
                        self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalchoice2509)
                        globalprotocolblock184 = self.globalprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalprotocolblock.add(globalprotocolblock184.tree)


                    else:
                        break #loop32

                # AST Rewrite
                # elements: globalprotocolblock, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 583:2: -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ )
                    # src/scribble/Scribble.g:584:2: ^( GLOBALCHOICE rolename ( globalprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALCHOICE, "GLOBALCHOICE"), root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())
                    # src/scribble/Scribble.g:584:26: ( globalprotocolblock )+
                    if not (stream_globalprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_globalprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())


                    stream_globalprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalchoice"

    class globalrecursion_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalrecursion_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalrecursion"
    # src/scribble/Scribble.g:588:1: globalrecursion : RECKW recursionlabelname globalprotocolblock -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock ) ;
    def globalrecursion(self, ):

        retval = self.globalrecursion_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RECKW185 = None
        recursionlabelname186 = None

        globalprotocolblock187 = None


        RECKW185_tree = None
        stream_RECKW = RewriteRuleTokenStream(self._adaptor, "token RECKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # src/scribble/Scribble.g:591:16: ( RECKW recursionlabelname globalprotocolblock -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock ) )
                # src/scribble/Scribble.g:592:2: RECKW recursionlabelname globalprotocolblock
                pass 
                RECKW185=self.match(self.input, RECKW, self.FOLLOW_RECKW_in_globalrecursion2536) 
                if self._state.backtracking == 0:
                    stream_RECKW.add(RECKW185)
                self._state.following.append(self.FOLLOW_recursionlabelname_in_globalrecursion2538)
                recursionlabelname186 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname186.tree)
                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalrecursion2540)
                globalprotocolblock187 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock187.tree)

                # AST Rewrite
                # elements: recursionlabelname, globalprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 593:2: -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock )
                    # src/scribble/Scribble.g:594:2: ^( GLOBALRECURSION recursionlabelname globalprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALRECURSION, "GLOBALRECURSION"), root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())
                    self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalrecursion"

    class globalcontinue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalcontinue_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalcontinue"
    # src/scribble/Scribble.g:597:1: globalcontinue : CONTINUEKW recursionlabelname ';' -> ^( GLOBALCONTINUE recursionlabelname ) ;
    def globalcontinue(self, ):

        retval = self.globalcontinue_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONTINUEKW188 = None
        char_literal190 = None
        recursionlabelname189 = None


        CONTINUEKW188_tree = None
        char_literal190_tree = None
        stream_CONTINUEKW = RewriteRuleTokenStream(self._adaptor, "token CONTINUEKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # src/scribble/Scribble.g:597:15: ( CONTINUEKW recursionlabelname ';' -> ^( GLOBALCONTINUE recursionlabelname ) )
                # src/scribble/Scribble.g:598:2: CONTINUEKW recursionlabelname ';'
                pass 
                CONTINUEKW188=self.match(self.input, CONTINUEKW, self.FOLLOW_CONTINUEKW_in_globalcontinue2561) 
                if self._state.backtracking == 0:
                    stream_CONTINUEKW.add(CONTINUEKW188)
                self._state.following.append(self.FOLLOW_recursionlabelname_in_globalcontinue2563)
                recursionlabelname189 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname189.tree)
                char_literal190=self.match(self.input, 95, self.FOLLOW_95_in_globalcontinue2565) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal190)

                # AST Rewrite
                # elements: recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 599:2: -> ^( GLOBALCONTINUE recursionlabelname )
                    # src/scribble/Scribble.g:600:2: ^( GLOBALCONTINUE recursionlabelname )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALCONTINUE, "GLOBALCONTINUE"), root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalcontinue"

    class globalparallel_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalparallel_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalparallel"
    # src/scribble/Scribble.g:604:1: globalparallel : PARKW globalprotocolblock ( ANDKW globalprotocolblock )* -> ^( GLOBALPARALLEL ( globalprotocolblock )+ ) ;
    def globalparallel(self, ):

        retval = self.globalparallel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARKW191 = None
        ANDKW193 = None
        globalprotocolblock192 = None

        globalprotocolblock194 = None


        PARKW191_tree = None
        ANDKW193_tree = None
        stream_PARKW = RewriteRuleTokenStream(self._adaptor, "token PARKW")
        stream_ANDKW = RewriteRuleTokenStream(self._adaptor, "token ANDKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:607:15: ( PARKW globalprotocolblock ( ANDKW globalprotocolblock )* -> ^( GLOBALPARALLEL ( globalprotocolblock )+ ) )
                # src/scribble/Scribble.g:608:2: PARKW globalprotocolblock ( ANDKW globalprotocolblock )*
                pass 
                PARKW191=self.match(self.input, PARKW, self.FOLLOW_PARKW_in_globalparallel2587) 
                if self._state.backtracking == 0:
                    stream_PARKW.add(PARKW191)
                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalparallel2589)
                globalprotocolblock192 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock192.tree)
                # src/scribble/Scribble.g:608:28: ( ANDKW globalprotocolblock )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == ANDKW) :
                        alt33 = 1


                    if alt33 == 1:
                        # src/scribble/Scribble.g:608:29: ANDKW globalprotocolblock
                        pass 
                        ANDKW193=self.match(self.input, ANDKW, self.FOLLOW_ANDKW_in_globalparallel2592) 
                        if self._state.backtracking == 0:
                            stream_ANDKW.add(ANDKW193)
                        self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalparallel2594)
                        globalprotocolblock194 = self.globalprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalprotocolblock.add(globalprotocolblock194.tree)


                    else:
                        break #loop33

                # AST Rewrite
                # elements: globalprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 609:2: -> ^( GLOBALPARALLEL ( globalprotocolblock )+ )
                    # src/scribble/Scribble.g:610:2: ^( GLOBALPARALLEL ( globalprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALPARALLEL, "GLOBALPARALLEL"), root_1)

                    # src/scribble/Scribble.g:610:19: ( globalprotocolblock )+
                    if not (stream_globalprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_globalprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())


                    stream_globalprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalparallel"

    class globalinterruptible_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalinterruptible_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalinterruptible"
    # src/scribble/Scribble.g:614:1: globalinterruptible : ( INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* ) | INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* ) );
    def globalinterruptible(self, ):

        retval = self.globalinterruptible_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INTERRUPTIBLEKW195 = None
        WITHKW197 = None
        char_literal198 = None
        char_literal200 = None
        INTERRUPTIBLEKW201 = None
        WITHKW204 = None
        char_literal205 = None
        char_literal207 = None
        globalprotocolblock196 = None

        globalinterrupt199 = None

        scopename202 = None

        globalprotocolblock203 = None

        globalinterrupt206 = None


        INTERRUPTIBLEKW195_tree = None
        WITHKW197_tree = None
        char_literal198_tree = None
        char_literal200_tree = None
        INTERRUPTIBLEKW201_tree = None
        WITHKW204_tree = None
        char_literal205_tree = None
        char_literal207_tree = None
        stream_WITHKW = RewriteRuleTokenStream(self._adaptor, "token WITHKW")
        stream_INTERRUPTIBLEKW = RewriteRuleTokenStream(self._adaptor, "token INTERRUPTIBLEKW")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_globalinterrupt = RewriteRuleSubtreeStream(self._adaptor, "rule globalinterrupt")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:617:20: ( INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* ) | INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == INTERRUPTIBLEKW) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == 102) :
                        alt36 = 1
                    elif (LA36_1 == IDENTIFIER) :
                        alt36 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # src/scribble/Scribble.g:618:2: INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}'
                    pass 
                    INTERRUPTIBLEKW195=self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2619) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW195)
                    self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalinterruptible2621)
                    globalprotocolblock196 = self.globalprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolblock.add(globalprotocolblock196.tree)
                    WITHKW197=self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_globalinterruptible2623) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW197)
                    char_literal198=self.match(self.input, 102, self.FOLLOW_102_in_globalinterruptible2625) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal198)
                    # src/scribble/Scribble.g:618:49: ( globalinterrupt )*
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == IDENTIFIER or LA34_0 == 98) :
                            alt34 = 1


                        if alt34 == 1:
                            # src/scribble/Scribble.g:618:50: globalinterrupt
                            pass 
                            self._state.following.append(self.FOLLOW_globalinterrupt_in_globalinterruptible2628)
                            globalinterrupt199 = self.globalinterrupt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_globalinterrupt.add(globalinterrupt199.tree)


                        else:
                            break #loop34
                    char_literal200=self.match(self.input, 103, self.FOLLOW_103_in_globalinterruptible2632) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal200)

                    # AST Rewrite
                    # elements: globalprotocolblock, globalinterrupt
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 619:2: -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* )
                        # src/scribble/Scribble.g:620:2: ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALINTERRUPTIBLE, "GLOBALINTERRUPTIBLE"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME"))
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())
                        # src/scribble/Scribble.g:620:61: ( globalinterrupt )*
                        while stream_globalinterrupt.hasNext():
                            self._adaptor.addChild(root_1, stream_globalinterrupt.nextTree())


                        stream_globalinterrupt.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt36 == 2:
                    # src/scribble/Scribble.g:622:2: INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}'
                    pass 
                    INTERRUPTIBLEKW201=self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2654) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW201)
                    self._state.following.append(self.FOLLOW_scopename_in_globalinterruptible2656)
                    scopename202 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename202.tree)
                    self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalinterruptible2658)
                    globalprotocolblock203 = self.globalprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolblock.add(globalprotocolblock203.tree)
                    WITHKW204=self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_globalinterruptible2660) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW204)
                    char_literal205=self.match(self.input, 102, self.FOLLOW_102_in_globalinterruptible2662) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal205)
                    # src/scribble/Scribble.g:622:59: ( globalinterrupt )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == IDENTIFIER or LA35_0 == 98) :
                            alt35 = 1


                        if alt35 == 1:
                            # src/scribble/Scribble.g:622:60: globalinterrupt
                            pass 
                            self._state.following.append(self.FOLLOW_globalinterrupt_in_globalinterruptible2665)
                            globalinterrupt206 = self.globalinterrupt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_globalinterrupt.add(globalinterrupt206.tree)


                        else:
                            break #loop35
                    char_literal207=self.match(self.input, 103, self.FOLLOW_103_in_globalinterruptible2669) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal207)

                    # AST Rewrite
                    # elements: scopename, globalinterrupt, globalprotocolblock
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 623:2: -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* )
                        # src/scribble/Scribble.g:624:2: ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALINTERRUPTIBLE, "GLOBALINTERRUPTIBLE"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())
                        # src/scribble/Scribble.g:624:54: ( globalinterrupt )*
                        while stream_globalinterrupt.hasNext():
                            self._adaptor.addChild(root_1, stream_globalinterrupt.nextTree())


                        stream_globalinterrupt.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalinterruptible"

    class globalinterrupt_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globalinterrupt_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalinterrupt"
    # src/scribble/Scribble.g:627:1: globalinterrupt : message ( ',' message )* BYKW rolename ';' -> ^( GLOBALINTERRUPT rolename ( message )+ ) ;
    def globalinterrupt(self, ):

        retval = self.globalinterrupt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal209 = None
        BYKW211 = None
        char_literal213 = None
        message208 = None

        message210 = None

        rolename212 = None


        char_literal209_tree = None
        BYKW211_tree = None
        char_literal213_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_BYKW = RewriteRuleTokenStream(self._adaptor, "token BYKW")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:627:16: ( message ( ',' message )* BYKW rolename ';' -> ^( GLOBALINTERRUPT rolename ( message )+ ) )
                # src/scribble/Scribble.g:628:2: message ( ',' message )* BYKW rolename ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_globalinterrupt2695)
                message208 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message208.tree)
                # src/scribble/Scribble.g:628:10: ( ',' message )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == 100) :
                        alt37 = 1


                    if alt37 == 1:
                        # src/scribble/Scribble.g:628:11: ',' message
                        pass 
                        char_literal209=self.match(self.input, 100, self.FOLLOW_100_in_globalinterrupt2698) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal209)
                        self._state.following.append(self.FOLLOW_message_in_globalinterrupt2700)
                        message210 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message210.tree)


                    else:
                        break #loop37
                BYKW211=self.match(self.input, BYKW, self.FOLLOW_BYKW_in_globalinterrupt2704) 
                if self._state.backtracking == 0:
                    stream_BYKW.add(BYKW211)
                self._state.following.append(self.FOLLOW_rolename_in_globalinterrupt2706)
                rolename212 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename212.tree)
                char_literal213=self.match(self.input, 95, self.FOLLOW_95_in_globalinterrupt2708) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal213)

                # AST Rewrite
                # elements: message, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 629:2: -> ^( GLOBALINTERRUPT rolename ( message )+ )
                    # src/scribble/Scribble.g:630:2: ^( GLOBALINTERRUPT rolename ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALINTERRUPT, "GLOBALINTERRUPT"), root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())
                    # src/scribble/Scribble.g:630:29: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalinterrupt"

    class globaldo_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.globaldo_return, self).__init__()

            self.tree = None




    # $ANTLR start "globaldo"
    # src/scribble/Scribble.g:634:1: globaldo : ( DOKW membername roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername ) );
    def globaldo(self, ):

        retval = self.globaldo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOKW214 = None
        char_literal217 = None
        DOKW218 = None
        char_literal222 = None
        DOKW223 = None
        char_literal225 = None
        char_literal228 = None
        DOKW229 = None
        char_literal231 = None
        char_literal235 = None
        membername215 = None

        roleinstantiationlist216 = None

        membername219 = None

        argumentlist220 = None

        roleinstantiationlist221 = None

        scopename224 = None

        membername226 = None

        roleinstantiationlist227 = None

        scopename230 = None

        membername232 = None

        argumentlist233 = None

        roleinstantiationlist234 = None


        DOKW214_tree = None
        char_literal217_tree = None
        DOKW218_tree = None
        char_literal222_tree = None
        DOKW223_tree = None
        char_literal225_tree = None
        char_literal228_tree = None
        DOKW229_tree = None
        char_literal231_tree = None
        char_literal235_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_DOKW = RewriteRuleTokenStream(self._adaptor, "token DOKW")
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        try:
            try:
                # src/scribble/Scribble.g:637:9: ( DOKW membername roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername ) )
                alt38 = 4
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # src/scribble/Scribble.g:638:2: DOKW membername roleinstantiationlist ';'
                    pass 
                    DOKW214=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2735) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW214)
                    self._state.following.append(self.FOLLOW_membername_in_globaldo2737)
                    membername215 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername215.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2739)
                    roleinstantiationlist216 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist216.tree)
                    char_literal217=self.match(self.input, 95, self.FOLLOW_95_in_globaldo2741) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal217)

                    # AST Rewrite
                    # elements: roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 639:2: -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # src/scribble/Scribble.g:640:2: ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALDO, "GLOBALDO"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME"))
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt38 == 2:
                    # src/scribble/Scribble.g:643:2: DOKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW218=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2764) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW218)
                    self._state.following.append(self.FOLLOW_membername_in_globaldo2766)
                    membername219 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername219.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_globaldo2768)
                    argumentlist220 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist220.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2770)
                    roleinstantiationlist221 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist221.tree)
                    char_literal222=self.match(self.input, 95, self.FOLLOW_95_in_globaldo2772) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal222)

                    # AST Rewrite
                    # elements: membername, argumentlist, roleinstantiationlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 644:2: -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        # src/scribble/Scribble.g:645:2: ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALDO, "GLOBALDO"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME"))
                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt38 == 3:
                    # src/scribble/Scribble.g:647:2: DOKW scopename ':' membername roleinstantiationlist ';'
                    pass 
                    DOKW223=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2793) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW223)
                    self._state.following.append(self.FOLLOW_scopename_in_globaldo2795)
                    scopename224 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename224.tree)
                    char_literal225=self.match(self.input, 101, self.FOLLOW_101_in_globaldo2797) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal225)
                    self._state.following.append(self.FOLLOW_membername_in_globaldo2799)
                    membername226 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername226.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2801)
                    roleinstantiationlist227 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist227.tree)
                    char_literal228=self.match(self.input, 95, self.FOLLOW_95_in_globaldo2803) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal228)

                    # AST Rewrite
                    # elements: scopename, roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 648:2: -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # src/scribble/Scribble.g:649:2: ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALDO, "GLOBALDO"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt38 == 4:
                    # src/scribble/Scribble.g:651:2: DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW229=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2824) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW229)
                    self._state.following.append(self.FOLLOW_scopename_in_globaldo2826)
                    scopename230 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename230.tree)
                    char_literal231=self.match(self.input, 101, self.FOLLOW_101_in_globaldo2828) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal231)
                    self._state.following.append(self.FOLLOW_membername_in_globaldo2830)
                    membername232 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername232.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_globaldo2832)
                    argumentlist233 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist233.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2834)
                    roleinstantiationlist234 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist234.tree)
                    char_literal235=self.match(self.input, 95, self.FOLLOW_95_in_globaldo2836) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal235)

                    # AST Rewrite
                    # elements: membername, argumentlist, roleinstantiationlist, scopename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 652:2: -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername )
                        # src/scribble/Scribble.g:653:2: ^( GLOBALDO scopename argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBALDO, "GLOBALDO"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globaldo"

    class localprotocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localprotocoldecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "localprotocoldecl"
    # src/scribble/Scribble.g:657:1: localprotocoldecl : ( localprotocolheader localprotocoldefinition -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition ) | localprotocolheader localprotocolinstance -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance ) );
    def localprotocoldecl(self, ):

        retval = self.localprotocoldecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        localprotocolheader236 = None

        localprotocoldefinition237 = None

        localprotocolheader238 = None

        localprotocolinstance239 = None


        stream_localprotocolinstance = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolinstance")
        stream_localprotocolheader = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolheader")
        stream_localprotocoldefinition = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocoldefinition")
        try:
            try:
                # src/scribble/Scribble.g:674:18: ( localprotocolheader localprotocoldefinition -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition ) | localprotocolheader localprotocolinstance -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance ) )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # src/scribble/Scribble.g:675:2: localprotocolheader localprotocoldefinition
                    pass 
                    self._state.following.append(self.FOLLOW_localprotocolheader_in_localprotocoldecl2870)
                    localprotocolheader236 = self.localprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolheader.add(localprotocolheader236.tree)
                    self._state.following.append(self.FOLLOW_localprotocoldefinition_in_localprotocoldecl2872)
                    localprotocoldefinition237 = self.localprotocoldefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocoldefinition.add(localprotocoldefinition237.tree)

                    # AST Rewrite
                    # elements: localprotocolheader, localprotocoldefinition
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 676:2: -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition )
                        # src/scribble/Scribble.g:677:2: ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLDECL, "LOCALPROTOCOLDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_localprotocolheader.nextTree())
                        self._adaptor.addChild(root_1, stream_localprotocoldefinition.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt39 == 2:
                    # src/scribble/Scribble.g:679:2: localprotocolheader localprotocolinstance
                    pass 
                    self._state.following.append(self.FOLLOW_localprotocolheader_in_localprotocoldecl2889)
                    localprotocolheader238 = self.localprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolheader.add(localprotocolheader238.tree)
                    self._state.following.append(self.FOLLOW_localprotocolinstance_in_localprotocoldecl2891)
                    localprotocolinstance239 = self.localprotocolinstance()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolinstance.add(localprotocolinstance239.tree)

                    # AST Rewrite
                    # elements: localprotocolheader, localprotocolinstance
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 680:2: -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance )
                        # src/scribble/Scribble.g:681:2: ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLDECL, "LOCALPROTOCOLDECL"), root_1)

                        self._adaptor.addChild(root_1, stream_localprotocolheader.nextTree())
                        self._adaptor.addChild(root_1, stream_localprotocolinstance.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localprotocoldecl"

    class localprotocolheader_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localprotocolheader_return, self).__init__()

            self.tree = None




    # $ANTLR start "localprotocolheader"
    # src/scribble/Scribble.g:684:1: localprotocolheader : ( LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist | LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist -> protocolname rolename parameterdecllist roledecllist );
    def localprotocolheader(self, ):

        retval = self.localprotocolheader_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOCALKW240 = None
        PROTOCOLKW241 = None
        ATKW243 = None
        LOCALKW246 = None
        PROTOCOLKW247 = None
        ATKW249 = None
        protocolname242 = None

        rolename244 = None

        roledecllist245 = None

        protocolname248 = None

        rolename250 = None

        parameterdecllist251 = None

        roledecllist252 = None


        LOCALKW240_tree = None
        PROTOCOLKW241_tree = None
        ATKW243_tree = None
        LOCALKW246_tree = None
        PROTOCOLKW247_tree = None
        ATKW249_tree = None
        stream_LOCALKW = RewriteRuleTokenStream(self._adaptor, "token LOCALKW")
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_PROTOCOLKW = RewriteRuleTokenStream(self._adaptor, "token PROTOCOLKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_protocolname = RewriteRuleSubtreeStream(self._adaptor, "rule protocolname")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_parameterdecllist = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecllist")
        try:
            try:
                # src/scribble/Scribble.g:684:20: ( LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist | LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist -> protocolname rolename parameterdecllist roledecllist )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == LOCALKW) :
                    LA40_1 = self.input.LA(2)

                    if (LA40_1 == PROTOCOLKW) :
                        LA40_2 = self.input.LA(3)

                        if (LA40_2 == IDENTIFIER) :
                            LA40_3 = self.input.LA(4)

                            if (LA40_3 == ATKW) :
                                LA40_4 = self.input.LA(5)

                                if (LA40_4 == IDENTIFIER) :
                                    LA40_5 = self.input.LA(6)

                                    if (LA40_5 == 96) :
                                        alt40 = 2
                                    elif (LA40_5 == 98) :
                                        alt40 = 1
                                    else:
                                        if self._state.backtracking > 0:
                                            raise BacktrackingFailed

                                        nvae = NoViableAltException("", 40, 5, self.input)

                                        raise nvae

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    nvae = NoViableAltException("", 40, 4, self.input)

                                    raise nvae

                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 40, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 40, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 40, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # src/scribble/Scribble.g:685:2: LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist
                    pass 
                    LOCALKW240=self.match(self.input, LOCALKW, self.FOLLOW_LOCALKW_in_localprotocolheader2912) 
                    if self._state.backtracking == 0:
                        stream_LOCALKW.add(LOCALKW240)
                    PROTOCOLKW241=self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_localprotocolheader2914) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW241)
                    self._state.following.append(self.FOLLOW_protocolname_in_localprotocolheader2916)
                    protocolname242 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname242.tree)
                    ATKW243=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localprotocolheader2918) 
                    if self._state.backtracking == 0:
                        stream_ATKW.add(ATKW243)
                    self._state.following.append(self.FOLLOW_rolename_in_localprotocolheader2920)
                    rolename244 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename244.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolheader2922)
                    roledecllist245 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist245.tree)

                    # AST Rewrite
                    # elements: roledecllist, rolename, protocolname
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 686:2: -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())
                        self._adaptor.addChild(root_0, stream_rolename.nextTree())
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_PARAMETER_DECL_LIST, "EMPTY_PARAMETER_DECL_LIST"))
                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())



                        retval.tree = root_0


                elif alt40 == 2:
                    # src/scribble/Scribble.g:689:2: LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist
                    pass 
                    LOCALKW246=self.match(self.input, LOCALKW, self.FOLLOW_LOCALKW_in_localprotocolheader2939) 
                    if self._state.backtracking == 0:
                        stream_LOCALKW.add(LOCALKW246)
                    PROTOCOLKW247=self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_localprotocolheader2941) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW247)
                    self._state.following.append(self.FOLLOW_protocolname_in_localprotocolheader2943)
                    protocolname248 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname248.tree)
                    ATKW249=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localprotocolheader2945) 
                    if self._state.backtracking == 0:
                        stream_ATKW.add(ATKW249)
                    self._state.following.append(self.FOLLOW_rolename_in_localprotocolheader2947)
                    rolename250 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename250.tree)
                    self._state.following.append(self.FOLLOW_parameterdecllist_in_localprotocolheader2949)
                    parameterdecllist251 = self.parameterdecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameterdecllist.add(parameterdecllist251.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolheader2951)
                    roledecllist252 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist252.tree)

                    # AST Rewrite
                    # elements: parameterdecllist, rolename, roledecllist, protocolname
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 690:2: -> protocolname rolename parameterdecllist roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())
                        self._adaptor.addChild(root_0, stream_rolename.nextTree())
                        self._adaptor.addChild(root_0, stream_parameterdecllist.nextTree())
                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localprotocolheader"

    class localprotocoldefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localprotocoldefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "localprotocoldefinition"
    # src/scribble/Scribble.g:695:1: localprotocoldefinition : localprotocolblock -> ^( LOCALPROTOCOLDEF localprotocolblock ) ;
    def localprotocoldefinition(self, ):

        retval = self.localprotocoldefinition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        localprotocolblock253 = None


        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:698:24: ( localprotocolblock -> ^( LOCALPROTOCOLDEF localprotocolblock ) )
                # src/scribble/Scribble.g:699:2: localprotocolblock
                pass 
                self._state.following.append(self.FOLLOW_localprotocolblock_in_localprotocoldefinition2975)
                localprotocolblock253 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock253.tree)

                # AST Rewrite
                # elements: localprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 700:2: -> ^( LOCALPROTOCOLDEF localprotocolblock )
                    # src/scribble/Scribble.g:701:2: ^( LOCALPROTOCOLDEF localprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLDEF, "LOCALPROTOCOLDEF"), root_1)

                    self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localprotocoldefinition"

    class localprotocolinstance_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localprotocolinstance_return, self).__init__()

            self.tree = None




    # $ANTLR start "localprotocolinstance"
    # src/scribble/Scribble.g:705:1: localprotocolinstance : ( INSTANTIATESKW membername roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername ) | INSTANTIATESKW membername argumentlist roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername ) );
    def localprotocolinstance(self, ):

        retval = self.localprotocolinstance_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INSTANTIATESKW254 = None
        char_literal257 = None
        INSTANTIATESKW258 = None
        char_literal262 = None
        membername255 = None

        roledecllist256 = None

        membername259 = None

        argumentlist260 = None

        roledecllist261 = None


        INSTANTIATESKW254_tree = None
        char_literal257_tree = None
        INSTANTIATESKW258_tree = None
        char_literal262_tree = None
        stream_INSTANTIATESKW = RewriteRuleTokenStream(self._adaptor, "token INSTANTIATESKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        try:
            try:
                # src/scribble/Scribble.g:708:22: ( INSTANTIATESKW membername roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername ) | INSTANTIATESKW membername argumentlist roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername ) )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # src/scribble/Scribble.g:709:2: INSTANTIATESKW membername roledecllist ';'
                    pass 
                    INSTANTIATESKW254=self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_localprotocolinstance2997) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW254)
                    self._state.following.append(self.FOLLOW_membername_in_localprotocolinstance2999)
                    membername255 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername255.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolinstance3001)
                    roledecllist256 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist256.tree)
                    char_literal257=self.match(self.input, 95, self.FOLLOW_95_in_localprotocolinstance3003) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal257)

                    # AST Rewrite
                    # elements: membername, roledecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 710:2: -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername )
                        # src/scribble/Scribble.g:711:2: ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLINSTANCE, "LOCALPROTOCOLINSTANCE"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roledecllist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt41 == 2:
                    # src/scribble/Scribble.g:713:2: INSTANTIATESKW membername argumentlist roledecllist ';'
                    pass 
                    INSTANTIATESKW258=self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_localprotocolinstance3022) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW258)
                    self._state.following.append(self.FOLLOW_membername_in_localprotocolinstance3024)
                    membername259 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername259.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_localprotocolinstance3026)
                    argumentlist260 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist260.tree)
                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolinstance3028)
                    roledecllist261 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist261.tree)
                    char_literal262=self.match(self.input, 95, self.FOLLOW_95_in_localprotocolinstance3030) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal262)

                    # AST Rewrite
                    # elements: roledecllist, membername, argumentlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 714:2: -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername )
                        # src/scribble/Scribble.g:715:2: ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLINSTANCE, "LOCALPROTOCOLINSTANCE"), root_1)

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roledecllist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localprotocolinstance"

    class localprotocolblock_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localprotocolblock_return, self).__init__()

            self.tree = None




    # $ANTLR start "localprotocolblock"
    # src/scribble/Scribble.g:719:1: localprotocolblock : '{' localinteractionsequence '}' -> ^( LOCALPROTOCOLBLOCK localinteractionsequence ) ;
    def localprotocolblock(self, ):

        retval = self.localprotocolblock_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal263 = None
        char_literal265 = None
        localinteractionsequence264 = None


        char_literal263_tree = None
        char_literal265_tree = None
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_localinteractionsequence = RewriteRuleSubtreeStream(self._adaptor, "rule localinteractionsequence")
        try:
            try:
                # src/scribble/Scribble.g:722:19: ( '{' localinteractionsequence '}' -> ^( LOCALPROTOCOLBLOCK localinteractionsequence ) )
                # src/scribble/Scribble.g:723:2: '{' localinteractionsequence '}'
                pass 
                char_literal263=self.match(self.input, 102, self.FOLLOW_102_in_localprotocolblock3056) 
                if self._state.backtracking == 0:
                    stream_102.add(char_literal263)
                self._state.following.append(self.FOLLOW_localinteractionsequence_in_localprotocolblock3058)
                localinteractionsequence264 = self.localinteractionsequence()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localinteractionsequence.add(localinteractionsequence264.tree)
                char_literal265=self.match(self.input, 103, self.FOLLOW_103_in_localprotocolblock3060) 
                if self._state.backtracking == 0:
                    stream_103.add(char_literal265)

                # AST Rewrite
                # elements: localinteractionsequence
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 724:2: -> ^( LOCALPROTOCOLBLOCK localinteractionsequence )
                    # src/scribble/Scribble.g:725:2: ^( LOCALPROTOCOLBLOCK localinteractionsequence )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPROTOCOLBLOCK, "LOCALPROTOCOLBLOCK"), root_1)

                    self._adaptor.addChild(root_1, stream_localinteractionsequence.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localprotocolblock"

    class localinteractionsequence_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localinteractionsequence_return, self).__init__()

            self.tree = None




    # $ANTLR start "localinteractionsequence"
    # src/scribble/Scribble.g:728:1: localinteractionsequence : ( localinteraction )* -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* ) ;
    def localinteractionsequence(self, ):

        retval = self.localinteractionsequence_return()
        retval.start = self.input.LT(1)

        root_0 = None

        localinteraction266 = None


        stream_localinteraction = RewriteRuleSubtreeStream(self._adaptor, "rule localinteraction")
        try:
            try:
                # src/scribble/Scribble.g:728:25: ( ( localinteraction )* -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* ) )
                # src/scribble/Scribble.g:729:2: ( localinteraction )*
                pass 
                # src/scribble/Scribble.g:729:2: ( localinteraction )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == CHOICEKW or (RECKW <= LA42_0 <= PARKW) or LA42_0 == INTERRUPTIBLEKW or LA42_0 == DOKW or LA42_0 == IDENTIFIER or LA42_0 == 98) :
                        alt42 = 1


                    if alt42 == 1:
                        # src/scribble/Scribble.g:729:3: localinteraction
                        pass 
                        self._state.following.append(self.FOLLOW_localinteraction_in_localinteractionsequence3080)
                        localinteraction266 = self.localinteraction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localinteraction.add(localinteraction266.tree)


                    else:
                        break #loop42

                # AST Rewrite
                # elements: localinteraction
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 730:2: -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* )
                    # src/scribble/Scribble.g:731:2: ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALINTERACTIONSEQUENCE, "LOCALINTERACTIONSEQUENCE"), root_1)

                    # src/scribble/Scribble.g:731:29: ( localinteraction )*
                    while stream_localinteraction.hasNext():
                        self._adaptor.addChild(root_1, stream_localinteraction.nextTree())


                    stream_localinteraction.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localinteractionsequence"

    class localinteraction_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localinteraction_return, self).__init__()

            self.tree = None




    # $ANTLR start "localinteraction"
    # src/scribble/Scribble.g:734:1: localinteraction : ( localsend | localreceive | localchoice | localparallel | localrecursion | localcontinue | localinterruptible | localdo );
    def localinteraction(self, ):

        retval = self.localinteraction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        localsend267 = None

        localreceive268 = None

        localchoice269 = None

        localparallel270 = None

        localrecursion271 = None

        localcontinue272 = None

        localinterruptible273 = None

        localdo274 = None



        try:
            try:
                # src/scribble/Scribble.g:734:17: ( localsend | localreceive | localchoice | localparallel | localrecursion | localcontinue | localinterruptible | localdo )
                alt43 = 8
                alt43 = self.dfa43.predict(self.input)
                if alt43 == 1:
                    # src/scribble/Scribble.g:735:2: localsend
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localsend_in_localinteraction3104)
                    localsend267 = self.localsend()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localsend267.tree)


                elif alt43 == 2:
                    # src/scribble/Scribble.g:737:2: localreceive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localreceive_in_localinteraction3109)
                    localreceive268 = self.localreceive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localreceive268.tree)


                elif alt43 == 3:
                    # src/scribble/Scribble.g:739:2: localchoice
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localchoice_in_localinteraction3114)
                    localchoice269 = self.localchoice()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localchoice269.tree)


                elif alt43 == 4:
                    # src/scribble/Scribble.g:741:2: localparallel
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localparallel_in_localinteraction3119)
                    localparallel270 = self.localparallel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localparallel270.tree)


                elif alt43 == 5:
                    # src/scribble/Scribble.g:743:2: localrecursion
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localrecursion_in_localinteraction3124)
                    localrecursion271 = self.localrecursion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localrecursion271.tree)


                elif alt43 == 6:
                    # src/scribble/Scribble.g:745:2: localcontinue
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localcontinue_in_localinteraction3129)
                    localcontinue272 = self.localcontinue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localcontinue272.tree)


                elif alt43 == 7:
                    # src/scribble/Scribble.g:747:2: localinterruptible
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localinterruptible_in_localinteraction3134)
                    localinterruptible273 = self.localinterruptible()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localinterruptible273.tree)


                elif alt43 == 8:
                    # src/scribble/Scribble.g:749:2: localdo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_localdo_in_localinteraction3139)
                    localdo274 = self.localdo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localdo274.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localinteraction"

    class localsend_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localsend_return, self).__init__()

            self.tree = None




    # $ANTLR start "localsend"
    # src/scribble/Scribble.g:755:1: localsend : message TOKW rolename ( ',' rolename )* ';' -> ^( LOCALSEND message ( rolename )+ ) ;
    def localsend(self, ):

        retval = self.localsend_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKW276 = None
        char_literal278 = None
        char_literal280 = None
        message275 = None

        rolename277 = None

        rolename279 = None


        TOKW276_tree = None
        char_literal278_tree = None
        char_literal280_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:758:10: ( message TOKW rolename ( ',' rolename )* ';' -> ^( LOCALSEND message ( rolename )+ ) )
                # src/scribble/Scribble.g:759:2: message TOKW rolename ( ',' rolename )* ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_localsend3153)
                message275 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message275.tree)
                TOKW276=self.match(self.input, TOKW, self.FOLLOW_TOKW_in_localsend3155) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW276)
                self._state.following.append(self.FOLLOW_rolename_in_localsend3157)
                rolename277 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename277.tree)
                # src/scribble/Scribble.g:759:24: ( ',' rolename )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == 100) :
                        alt44 = 1


                    if alt44 == 1:
                        # src/scribble/Scribble.g:759:25: ',' rolename
                        pass 
                        char_literal278=self.match(self.input, 100, self.FOLLOW_100_in_localsend3160) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal278)
                        self._state.following.append(self.FOLLOW_rolename_in_localsend3162)
                        rolename279 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename279.tree)


                    else:
                        break #loop44
                char_literal280=self.match(self.input, 95, self.FOLLOW_95_in_localsend3166) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal280)

                # AST Rewrite
                # elements: rolename, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 760:2: -> ^( LOCALSEND message ( rolename )+ )
                    # src/scribble/Scribble.g:761:2: ^( LOCALSEND message ( rolename )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALSEND, "LOCALSEND"), root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())
                    # src/scribble/Scribble.g:761:22: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localsend"

    class localreceive_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localreceive_return, self).__init__()

            self.tree = None




    # $ANTLR start "localreceive"
    # src/scribble/Scribble.g:764:1: localreceive : message FROMKW IDENTIFIER ';' -> ^( LOCALRECEIVE message IDENTIFIER ) ;
    def localreceive(self, ):

        retval = self.localreceive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROMKW282 = None
        IDENTIFIER283 = None
        char_literal284 = None
        message281 = None


        FROMKW282_tree = None
        IDENTIFIER283_tree = None
        char_literal284_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # src/scribble/Scribble.g:764:13: ( message FROMKW IDENTIFIER ';' -> ^( LOCALRECEIVE message IDENTIFIER ) )
                # src/scribble/Scribble.g:765:2: message FROMKW IDENTIFIER ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_localreceive3190)
                message281 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message281.tree)
                FROMKW282=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_localreceive3192) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW282)
                IDENTIFIER283=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_localreceive3194) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER283)
                char_literal284=self.match(self.input, 95, self.FOLLOW_95_in_localreceive3196) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal284)

                # AST Rewrite
                # elements: message, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 766:2: -> ^( LOCALRECEIVE message IDENTIFIER )
                    # src/scribble/Scribble.g:767:2: ^( LOCALRECEIVE message IDENTIFIER )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALRECEIVE, "LOCALRECEIVE"), root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())
                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localreceive"

    class localchoice_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localchoice_return, self).__init__()

            self.tree = None




    # $ANTLR start "localchoice"
    # src/scribble/Scribble.g:771:1: localchoice : CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )* -> ^( LOCALCHOICE rolename ( localprotocolblock )+ ) ;
    def localchoice(self, ):

        retval = self.localchoice_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHOICEKW285 = None
        ATKW286 = None
        ORKW289 = None
        rolename287 = None

        localprotocolblock288 = None

        localprotocolblock290 = None


        CHOICEKW285_tree = None
        ATKW286_tree = None
        ORKW289_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_ORKW = RewriteRuleTokenStream(self._adaptor, "token ORKW")
        stream_CHOICEKW = RewriteRuleTokenStream(self._adaptor, "token CHOICEKW")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:774:12: ( CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )* -> ^( LOCALCHOICE rolename ( localprotocolblock )+ ) )
                # src/scribble/Scribble.g:775:2: CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )*
                pass 
                CHOICEKW285=self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_localchoice3220) 
                if self._state.backtracking == 0:
                    stream_CHOICEKW.add(CHOICEKW285)
                ATKW286=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localchoice3222) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(ATKW286)
                self._state.following.append(self.FOLLOW_rolename_in_localchoice3224)
                rolename287 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename287.tree)
                self._state.following.append(self.FOLLOW_localprotocolblock_in_localchoice3226)
                localprotocolblock288 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock288.tree)
                # src/scribble/Scribble.g:775:44: ( ORKW localprotocolblock )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ORKW) :
                        alt45 = 1


                    if alt45 == 1:
                        # src/scribble/Scribble.g:775:45: ORKW localprotocolblock
                        pass 
                        ORKW289=self.match(self.input, ORKW, self.FOLLOW_ORKW_in_localchoice3229) 
                        if self._state.backtracking == 0:
                            stream_ORKW.add(ORKW289)
                        self._state.following.append(self.FOLLOW_localprotocolblock_in_localchoice3231)
                        localprotocolblock290 = self.localprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localprotocolblock.add(localprotocolblock290.tree)


                    else:
                        break #loop45

                # AST Rewrite
                # elements: localprotocolblock, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 776:2: -> ^( LOCALCHOICE rolename ( localprotocolblock )+ )
                    # src/scribble/Scribble.g:777:2: ^( LOCALCHOICE rolename ( localprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALCHOICE, "LOCALCHOICE"), root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())
                    # src/scribble/Scribble.g:777:25: ( localprotocolblock )+
                    if not (stream_localprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_localprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())


                    stream_localprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localchoice"

    class localrecursion_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localrecursion_return, self).__init__()

            self.tree = None




    # $ANTLR start "localrecursion"
    # src/scribble/Scribble.g:781:1: localrecursion : RECKW recursionlabelname localprotocolblock -> ^( LOCALRECURSION recursionlabelname localprotocolblock ) ;
    def localrecursion(self, ):

        retval = self.localrecursion_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RECKW291 = None
        recursionlabelname292 = None

        localprotocolblock293 = None


        RECKW291_tree = None
        stream_RECKW = RewriteRuleTokenStream(self._adaptor, "token RECKW")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # src/scribble/Scribble.g:784:15: ( RECKW recursionlabelname localprotocolblock -> ^( LOCALRECURSION recursionlabelname localprotocolblock ) )
                # src/scribble/Scribble.g:785:2: RECKW recursionlabelname localprotocolblock
                pass 
                RECKW291=self.match(self.input, RECKW, self.FOLLOW_RECKW_in_localrecursion3258) 
                if self._state.backtracking == 0:
                    stream_RECKW.add(RECKW291)
                self._state.following.append(self.FOLLOW_recursionlabelname_in_localrecursion3260)
                recursionlabelname292 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname292.tree)
                self._state.following.append(self.FOLLOW_localprotocolblock_in_localrecursion3262)
                localprotocolblock293 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock293.tree)

                # AST Rewrite
                # elements: localprotocolblock, recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 786:2: -> ^( LOCALRECURSION recursionlabelname localprotocolblock )
                    # src/scribble/Scribble.g:787:2: ^( LOCALRECURSION recursionlabelname localprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALRECURSION, "LOCALRECURSION"), root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())
                    self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localrecursion"

    class localcontinue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localcontinue_return, self).__init__()

            self.tree = None




    # $ANTLR start "localcontinue"
    # src/scribble/Scribble.g:790:1: localcontinue : CONTINUEKW recursionlabelname ';' -> ^( LOCALCONTINUE recursionlabelname ) ;
    def localcontinue(self, ):

        retval = self.localcontinue_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONTINUEKW294 = None
        char_literal296 = None
        recursionlabelname295 = None


        CONTINUEKW294_tree = None
        char_literal296_tree = None
        stream_CONTINUEKW = RewriteRuleTokenStream(self._adaptor, "token CONTINUEKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # src/scribble/Scribble.g:790:14: ( CONTINUEKW recursionlabelname ';' -> ^( LOCALCONTINUE recursionlabelname ) )
                # src/scribble/Scribble.g:791:2: CONTINUEKW recursionlabelname ';'
                pass 
                CONTINUEKW294=self.match(self.input, CONTINUEKW, self.FOLLOW_CONTINUEKW_in_localcontinue3283) 
                if self._state.backtracking == 0:
                    stream_CONTINUEKW.add(CONTINUEKW294)
                self._state.following.append(self.FOLLOW_recursionlabelname_in_localcontinue3285)
                recursionlabelname295 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname295.tree)
                char_literal296=self.match(self.input, 95, self.FOLLOW_95_in_localcontinue3287) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal296)

                # AST Rewrite
                # elements: recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 792:2: -> ^( LOCALCONTINUE recursionlabelname )
                    # src/scribble/Scribble.g:793:2: ^( LOCALCONTINUE recursionlabelname )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALCONTINUE, "LOCALCONTINUE"), root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localcontinue"

    class localparallel_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localparallel_return, self).__init__()

            self.tree = None




    # $ANTLR start "localparallel"
    # src/scribble/Scribble.g:797:1: localparallel : PARKW localprotocolblock ( ANDKW localprotocolblock )* -> ^( LOCALPARALLEL ( localprotocolblock )+ ) ;
    def localparallel(self, ):

        retval = self.localparallel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARKW297 = None
        ANDKW299 = None
        localprotocolblock298 = None

        localprotocolblock300 = None


        PARKW297_tree = None
        ANDKW299_tree = None
        stream_PARKW = RewriteRuleTokenStream(self._adaptor, "token PARKW")
        stream_ANDKW = RewriteRuleTokenStream(self._adaptor, "token ANDKW")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        try:
            try:
                # src/scribble/Scribble.g:800:14: ( PARKW localprotocolblock ( ANDKW localprotocolblock )* -> ^( LOCALPARALLEL ( localprotocolblock )+ ) )
                # src/scribble/Scribble.g:801:2: PARKW localprotocolblock ( ANDKW localprotocolblock )*
                pass 
                PARKW297=self.match(self.input, PARKW, self.FOLLOW_PARKW_in_localparallel3309) 
                if self._state.backtracking == 0:
                    stream_PARKW.add(PARKW297)
                self._state.following.append(self.FOLLOW_localprotocolblock_in_localparallel3311)
                localprotocolblock298 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock298.tree)
                # src/scribble/Scribble.g:801:27: ( ANDKW localprotocolblock )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == ANDKW) :
                        alt46 = 1


                    if alt46 == 1:
                        # src/scribble/Scribble.g:801:28: ANDKW localprotocolblock
                        pass 
                        ANDKW299=self.match(self.input, ANDKW, self.FOLLOW_ANDKW_in_localparallel3314) 
                        if self._state.backtracking == 0:
                            stream_ANDKW.add(ANDKW299)
                        self._state.following.append(self.FOLLOW_localprotocolblock_in_localparallel3316)
                        localprotocolblock300 = self.localprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localprotocolblock.add(localprotocolblock300.tree)


                    else:
                        break #loop46

                # AST Rewrite
                # elements: localprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 802:2: -> ^( LOCALPARALLEL ( localprotocolblock )+ )
                    # src/scribble/Scribble.g:803:2: ^( LOCALPARALLEL ( localprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALPARALLEL, "LOCALPARALLEL"), root_1)

                    # src/scribble/Scribble.g:803:18: ( localprotocolblock )+
                    if not (stream_localprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_localprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())


                    stream_localprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localparallel"

    class localinterruptible_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localinterruptible_return, self).__init__()

            self.tree = None




    # $ANTLR start "localinterruptible"
    # src/scribble/Scribble.g:807:1: localinterruptible : ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* ) | INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* ) );
    def localinterruptible(self, ):

        retval = self.localinterruptible_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INTERRUPTIBLEKW301 = None
        WITHKW304 = None
        char_literal305 = None
        char_literal307 = None
        INTERRUPTIBLEKW308 = None
        WITHKW311 = None
        char_literal312 = None
        char_literal315 = None
        scopename302 = None

        localprotocolblock303 = None

        localcatch306 = None

        scopename309 = None

        localprotocolblock310 = None

        localthrow313 = None

        localcatch314 = None


        INTERRUPTIBLEKW301_tree = None
        WITHKW304_tree = None
        char_literal305_tree = None
        char_literal307_tree = None
        INTERRUPTIBLEKW308_tree = None
        WITHKW311_tree = None
        char_literal312_tree = None
        char_literal315_tree = None
        stream_WITHKW = RewriteRuleTokenStream(self._adaptor, "token WITHKW")
        stream_INTERRUPTIBLEKW = RewriteRuleTokenStream(self._adaptor, "token INTERRUPTIBLEKW")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_localthrow = RewriteRuleSubtreeStream(self._adaptor, "rule localthrow")
        stream_localcatch = RewriteRuleSubtreeStream(self._adaptor, "rule localcatch")
        try:
            try:
                # src/scribble/Scribble.g:810:19: ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* ) | INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* ) )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == INTERRUPTIBLEKW) :
                    LA49_1 = self.input.LA(2)

                    if (self.synpred71_Scribble()) :
                        alt49 = 1
                    elif (True) :
                        alt49 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 49, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # src/scribble/Scribble.g:815:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}'
                    pass 
                    INTERRUPTIBLEKW301=self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3344) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW301)
                    self._state.following.append(self.FOLLOW_scopename_in_localinterruptible3346)
                    scopename302 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename302.tree)
                    self._state.following.append(self.FOLLOW_localprotocolblock_in_localinterruptible3348)
                    localprotocolblock303 = self.localprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolblock.add(localprotocolblock303.tree)
                    WITHKW304=self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_localinterruptible3350) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW304)
                    char_literal305=self.match(self.input, 102, self.FOLLOW_102_in_localinterruptible3352) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal305)
                    # src/scribble/Scribble.g:815:58: ( localcatch )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == CATCHESKW) :
                            alt47 = 1


                        if alt47 == 1:
                            # src/scribble/Scribble.g:815:59: localcatch
                            pass 
                            self._state.following.append(self.FOLLOW_localcatch_in_localinterruptible3355)
                            localcatch306 = self.localcatch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_localcatch.add(localcatch306.tree)


                        else:
                            break #loop47
                    char_literal307=self.match(self.input, 103, self.FOLLOW_103_in_localinterruptible3359) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal307)

                    # AST Rewrite
                    # elements: scopename, localprotocolblock, localcatch
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 816:2: -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* )
                        # src/scribble/Scribble.g:817:2: ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALINTERRUPTIBLE, "LOCALINTERRUPTIBLE"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_LOCAL_THROW, "EMPTY_LOCAL_THROW"))
                        # src/scribble/Scribble.g:817:70: ( localcatch )*
                        while stream_localcatch.hasNext():
                            self._adaptor.addChild(root_1, stream_localcatch.nextTree())


                        stream_localcatch.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt49 == 2:
                    # src/scribble/Scribble.g:819:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}'
                    pass 
                    INTERRUPTIBLEKW308=self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3383) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW308)
                    self._state.following.append(self.FOLLOW_scopename_in_localinterruptible3385)
                    scopename309 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename309.tree)
                    self._state.following.append(self.FOLLOW_localprotocolblock_in_localinterruptible3387)
                    localprotocolblock310 = self.localprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolblock.add(localprotocolblock310.tree)
                    WITHKW311=self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_localinterruptible3389) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW311)
                    char_literal312=self.match(self.input, 102, self.FOLLOW_102_in_localinterruptible3391) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal312)
                    self._state.following.append(self.FOLLOW_localthrow_in_localinterruptible3393)
                    localthrow313 = self.localthrow()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localthrow.add(localthrow313.tree)
                    # src/scribble/Scribble.g:819:69: ( localcatch )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == CATCHESKW) :
                            alt48 = 1


                        if alt48 == 1:
                            # src/scribble/Scribble.g:819:70: localcatch
                            pass 
                            self._state.following.append(self.FOLLOW_localcatch_in_localinterruptible3396)
                            localcatch314 = self.localcatch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_localcatch.add(localcatch314.tree)


                        else:
                            break #loop48
                    char_literal315=self.match(self.input, 103, self.FOLLOW_103_in_localinterruptible3400) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal315)

                    # AST Rewrite
                    # elements: localthrow, localprotocolblock, scopename, localcatch
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 820:2: -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* )
                        # src/scribble/Scribble.g:821:2: ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALINTERRUPTIBLE, "LOCALINTERRUPTIBLE"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())
                        self._adaptor.addChild(root_1, stream_localthrow.nextTree())
                        # src/scribble/Scribble.g:821:63: ( localcatch )*
                        while stream_localcatch.hasNext():
                            self._adaptor.addChild(root_1, stream_localcatch.nextTree())


                        stream_localcatch.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localinterruptible"

    class localthrow_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localthrow_return, self).__init__()

            self.tree = None




    # $ANTLR start "localthrow"
    # src/scribble/Scribble.g:830:1: localthrow : THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';' -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ ) ;
    def localthrow(self, ):

        retval = self.localthrow_return()
        retval.start = self.input.LT(1)

        root_0 = None

        THROWSKW316 = None
        char_literal318 = None
        TOKW320 = None
        char_literal322 = None
        char_literal324 = None
        message317 = None

        message319 = None

        rolename321 = None

        rolename323 = None


        THROWSKW316_tree = None
        char_literal318_tree = None
        TOKW320_tree = None
        char_literal322_tree = None
        char_literal324_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_THROWSKW = RewriteRuleTokenStream(self._adaptor, "token THROWSKW")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:830:11: ( THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';' -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ ) )
                # src/scribble/Scribble.g:831:2: THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';'
                pass 
                THROWSKW316=self.match(self.input, THROWSKW, self.FOLLOW_THROWSKW_in_localthrow3431) 
                if self._state.backtracking == 0:
                    stream_THROWSKW.add(THROWSKW316)
                self._state.following.append(self.FOLLOW_message_in_localthrow3433)
                message317 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message317.tree)
                # src/scribble/Scribble.g:831:19: ( ',' message )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == 100) :
                        alt50 = 1


                    if alt50 == 1:
                        # src/scribble/Scribble.g:831:20: ',' message
                        pass 
                        char_literal318=self.match(self.input, 100, self.FOLLOW_100_in_localthrow3436) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal318)
                        self._state.following.append(self.FOLLOW_message_in_localthrow3438)
                        message319 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message319.tree)


                    else:
                        break #loop50
                TOKW320=self.match(self.input, TOKW, self.FOLLOW_TOKW_in_localthrow3442) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW320)
                self._state.following.append(self.FOLLOW_rolename_in_localthrow3444)
                rolename321 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename321.tree)
                # src/scribble/Scribble.g:831:48: ( ',' rolename )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == 100) :
                        alt51 = 1


                    if alt51 == 1:
                        # src/scribble/Scribble.g:831:49: ',' rolename
                        pass 
                        char_literal322=self.match(self.input, 100, self.FOLLOW_100_in_localthrow3447) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal322)
                        self._state.following.append(self.FOLLOW_rolename_in_localthrow3449)
                        rolename323 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename323.tree)


                    else:
                        break #loop51
                char_literal324=self.match(self.input, 95, self.FOLLOW_95_in_localthrow3453) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal324)

                # AST Rewrite
                # elements: rolename, TOKW, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 832:2: -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ )
                    # src/scribble/Scribble.g:833:2: ^( LOCALTHROW ( rolename )+ TOKW ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALTHROW, "LOCALTHROW"), root_1)

                    # src/scribble/Scribble.g:833:15: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()
                    self._adaptor.addChild(root_1, stream_TOKW.nextNode())
                    # src/scribble/Scribble.g:833:32: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localthrow"

    class localcatch_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localcatch_return, self).__init__()

            self.tree = None




    # $ANTLR start "localcatch"
    # src/scribble/Scribble.g:836:1: localcatch : CATCHESKW message ( ',' message )* FROMKW rolename ';' -> ^( LOCALCATCH rolename ( message )+ ) ;
    def localcatch(self, ):

        retval = self.localcatch_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CATCHESKW325 = None
        char_literal327 = None
        FROMKW329 = None
        char_literal331 = None
        message326 = None

        message328 = None

        rolename330 = None


        CATCHESKW325_tree = None
        char_literal327_tree = None
        FROMKW329_tree = None
        char_literal331_tree = None
        stream_CATCHESKW = RewriteRuleTokenStream(self._adaptor, "token CATCHESKW")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # src/scribble/Scribble.g:836:11: ( CATCHESKW message ( ',' message )* FROMKW rolename ';' -> ^( LOCALCATCH rolename ( message )+ ) )
                # src/scribble/Scribble.g:837:2: CATCHESKW message ( ',' message )* FROMKW rolename ';'
                pass 
                CATCHESKW325=self.match(self.input, CATCHESKW, self.FOLLOW_CATCHESKW_in_localcatch3482) 
                if self._state.backtracking == 0:
                    stream_CATCHESKW.add(CATCHESKW325)
                self._state.following.append(self.FOLLOW_message_in_localcatch3484)
                message326 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message326.tree)
                # src/scribble/Scribble.g:837:20: ( ',' message )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == 100) :
                        alt52 = 1


                    if alt52 == 1:
                        # src/scribble/Scribble.g:837:21: ',' message
                        pass 
                        char_literal327=self.match(self.input, 100, self.FOLLOW_100_in_localcatch3487) 
                        if self._state.backtracking == 0:
                            stream_100.add(char_literal327)
                        self._state.following.append(self.FOLLOW_message_in_localcatch3489)
                        message328 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message328.tree)


                    else:
                        break #loop52
                FROMKW329=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_localcatch3493) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW329)
                self._state.following.append(self.FOLLOW_rolename_in_localcatch3495)
                rolename330 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename330.tree)
                char_literal331=self.match(self.input, 95, self.FOLLOW_95_in_localcatch3497) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal331)

                # AST Rewrite
                # elements: rolename, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 838:2: -> ^( LOCALCATCH rolename ( message )+ )
                    # src/scribble/Scribble.g:839:2: ^( LOCALCATCH rolename ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALCATCH, "LOCALCATCH"), root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())
                    # src/scribble/Scribble.g:839:24: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localcatch"

    class localdo_return(ParserRuleReturnScope):
        def __init__(self):
            super(ScribbleParser.localdo_return, self).__init__()

            self.tree = None




    # $ANTLR start "localdo"
    # src/scribble/Scribble.g:843:1: localdo : ( DOKW membername roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername ) );
    def localdo(self, ):

        retval = self.localdo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOKW332 = None
        char_literal335 = None
        DOKW336 = None
        char_literal340 = None
        DOKW341 = None
        char_literal343 = None
        char_literal346 = None
        DOKW347 = None
        char_literal349 = None
        char_literal353 = None
        membername333 = None

        roleinstantiationlist334 = None

        membername337 = None

        argumentlist338 = None

        roleinstantiationlist339 = None

        scopename342 = None

        membername344 = None

        roleinstantiationlist345 = None

        scopename348 = None

        membername350 = None

        argumentlist351 = None

        roleinstantiationlist352 = None


        DOKW332_tree = None
        char_literal335_tree = None
        DOKW336_tree = None
        char_literal340_tree = None
        DOKW341_tree = None
        char_literal343_tree = None
        char_literal346_tree = None
        DOKW347_tree = None
        char_literal349_tree = None
        char_literal353_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_DOKW = RewriteRuleTokenStream(self._adaptor, "token DOKW")
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        try:
            try:
                # src/scribble/Scribble.g:846:8: ( DOKW membername roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername ) )
                alt53 = 4
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # src/scribble/Scribble.g:847:2: DOKW membername roleinstantiationlist ';'
                    pass 
                    DOKW332=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3524) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW332)
                    self._state.following.append(self.FOLLOW_membername_in_localdo3526)
                    membername333 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername333.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3528)
                    roleinstantiationlist334 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist334.tree)
                    char_literal335=self.match(self.input, 95, self.FOLLOW_95_in_localdo3530) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal335)

                    # AST Rewrite
                    # elements: roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 848:2: -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # src/scribble/Scribble.g:849:2: ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALDO, "LOCALDO"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME"))
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 2:
                    # src/scribble/Scribble.g:852:2: DOKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW336=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3553) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW336)
                    self._state.following.append(self.FOLLOW_membername_in_localdo3555)
                    membername337 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername337.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_localdo3557)
                    argumentlist338 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist338.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3559)
                    roleinstantiationlist339 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist339.tree)
                    char_literal340=self.match(self.input, 95, self.FOLLOW_95_in_localdo3561) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal340)

                    # AST Rewrite
                    # elements: roleinstantiationlist, argumentlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 853:2: -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        # src/scribble/Scribble.g:854:2: ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALDO, "LOCALDO"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME"))
                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 3:
                    # src/scribble/Scribble.g:856:2: DOKW scopename ':' membername roleinstantiationlist ';'
                    pass 
                    DOKW341=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3582) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW341)
                    self._state.following.append(self.FOLLOW_scopename_in_localdo3584)
                    scopename342 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename342.tree)
                    char_literal343=self.match(self.input, 101, self.FOLLOW_101_in_localdo3586) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal343)
                    self._state.following.append(self.FOLLOW_membername_in_localdo3588)
                    membername344 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername344.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3590)
                    roleinstantiationlist345 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist345.tree)
                    char_literal346=self.match(self.input, 95, self.FOLLOW_95_in_localdo3592) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal346)

                    # AST Rewrite
                    # elements: membername, roleinstantiationlist, scopename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 857:2: -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # src/scribble/Scribble.g:858:2: ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALDO, "LOCALDO"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST"))
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 4:
                    # src/scribble/Scribble.g:860:2: DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW347=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3613) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW347)
                    self._state.following.append(self.FOLLOW_scopename_in_localdo3615)
                    scopename348 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename348.tree)
                    char_literal349=self.match(self.input, 101, self.FOLLOW_101_in_localdo3617) 
                    if self._state.backtracking == 0:
                        stream_101.add(char_literal349)
                    self._state.following.append(self.FOLLOW_membername_in_localdo3619)
                    membername350 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername350.tree)
                    self._state.following.append(self.FOLLOW_argumentlist_in_localdo3621)
                    argumentlist351 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist351.tree)
                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3623)
                    roleinstantiationlist352 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist352.tree)
                    char_literal353=self.match(self.input, 95, self.FOLLOW_95_in_localdo3625) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal353)

                    # AST Rewrite
                    # elements: scopename, argumentlist, membername, roleinstantiationlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 861:2: -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername )
                        # src/scribble/Scribble.g:862:2: ^( LOCALDO scopename argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LOCALDO, "LOCALDO"), root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())
                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())
                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())
                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "localdo"

    # $ANTLR start "synpred4_Scribble"
    def synpred4_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:247:2: ( payloadtypename )
        # src/scribble/Scribble.g:247:2: payloadtypename
        pass 
        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred4_Scribble1115)
        self.payloadtypename()

        self._state.following.pop()


    # $ANTLR end "synpred4_Scribble"



    # $ANTLR start "synpred17_Scribble"
    def synpred17_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:362:2: ( payloadtypename )
        # src/scribble/Scribble.g:362:2: payloadtypename
        pass 
        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred17_Scribble1635)
        self.payloadtypename()

        self._state.following.pop()


    # $ANTLR end "synpred17_Scribble"



    # $ANTLR start "synpred18_Scribble"
    def synpred18_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:366:2: ( parametername )
        # src/scribble/Scribble.g:366:2: parametername
        pass 
        self._state.following.append(self.FOLLOW_parametername_in_synpred18_Scribble1652)
        self.parametername()

        self._state.following.pop()


    # $ANTLR end "synpred18_Scribble"



    # $ANTLR start "synpred19_Scribble"
    def synpred19_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:371:2: ( annotationname ':' payloadtypename )
        # src/scribble/Scribble.g:371:2: annotationname ':' payloadtypename
        pass 
        self._state.following.append(self.FOLLOW_annotationname_in_synpred19_Scribble1672)
        self.annotationname()

        self._state.following.pop()
        self.match(self.input, 101, self.FOLLOW_101_in_synpred19_Scribble1674)
        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred19_Scribble1676)
        self.payloadtypename()

        self._state.following.pop()


    # $ANTLR end "synpred19_Scribble"



    # $ANTLR start "synpred35_Scribble"
    def synpred35_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:510:2: ( payloadtypename )
        # src/scribble/Scribble.g:510:2: payloadtypename
        pass 
        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred35_Scribble2262)
        self.payloadtypename()

        self._state.following.pop()


    # $ANTLR end "synpred35_Scribble"



    # $ANTLR start "synpred36_Scribble"
    def synpred36_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:514:2: ( payloadtypename ASKW parametername )
        # src/scribble/Scribble.g:514:2: payloadtypename ASKW parametername
        pass 
        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred36_Scribble2277)
        self.payloadtypename()

        self._state.following.pop()
        self.match(self.input, ASKW, self.FOLLOW_ASKW_in_synpred36_Scribble2279)
        self._state.following.append(self.FOLLOW_parametername_in_synpred36_Scribble2281)
        self.parametername()

        self._state.following.pop()


    # $ANTLR end "synpred36_Scribble"



    # $ANTLR start "synpred37_Scribble"
    def synpred37_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:518:2: ( parametername )
        # src/scribble/Scribble.g:518:2: parametername
        pass 
        self._state.following.append(self.FOLLOW_parametername_in_synpred37_Scribble2298)
        self.parametername()

        self._state.following.pop()


    # $ANTLR end "synpred37_Scribble"



    # $ANTLR start "synpred71_Scribble"
    def synpred71_Scribble_fragment(self, ):
        # src/scribble/Scribble.g:815:2: ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' )
        # src/scribble/Scribble.g:815:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}'
        pass 
        self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_synpred71_Scribble3344)
        self._state.following.append(self.FOLLOW_scopename_in_synpred71_Scribble3346)
        self.scopename()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_localprotocolblock_in_synpred71_Scribble3348)
        self.localprotocolblock()

        self._state.following.pop()
        self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_synpred71_Scribble3350)
        self.match(self.input, 102, self.FOLLOW_102_in_synpred71_Scribble3352)
        # src/scribble/Scribble.g:815:58: ( localcatch )*
        while True: #loop56
            alt56 = 2
            LA56_0 = self.input.LA(1)

            if (LA56_0 == CATCHESKW) :
                alt56 = 1


            if alt56 == 1:
                # src/scribble/Scribble.g:815:59: localcatch
                pass 
                self._state.following.append(self.FOLLOW_localcatch_in_synpred71_Scribble3355)
                self.localcatch()

                self._state.following.pop()


            else:
                break #loop56
        self.match(self.input, 103, self.FOLLOW_103_in_synpred71_Scribble3359)


    # $ANTLR end "synpred71_Scribble"




    # Delegated rules

    def synpred19_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred19_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred37_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred37_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred36_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred36_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred18_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred18_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred35_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred35_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred71_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred71_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\5\1\133\1\15\1\uffff\1\133\1\uffff\1\15"
        )

    DFA9_max = DFA.unpack(
        u"\1\5\1\133\1\137\1\uffff\1\133\1\uffff\1\137"
        )

    DFA9_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1\1\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3\120\uffff\1\4\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\120\uffff\1\4\1\5")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\16\1\133\1\5\2\133\1\5\1\15\2\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\16\1\133\1\136\2\133\1\136\1\137\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\7\uffff\1\1\1\2"
        )

    DFA10_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\130\uffff\1\3"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\4\130\uffff\1\3"),
        DFA.unpack(u"\1\10\121\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\57\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\57\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\10\1\7\1\133\1\140\1\12\1\6\3\133\3\15\1\133\1\12\1\14\1\6\1"
        u"\142\2\133\1\143\1\133\2\uffff\2\133\1\12\2\141\3\15\4\133\1\15"
        u"\1\143\2\141\1\12\1\14\2\133\1\143\1\15\1\133\1\143"
        )

    DFA17_max = DFA.unpack(
        u"\1\10\1\7\1\133\1\142\1\12\1\13\3\133\3\144\1\133\1\12\1\146\1"
        u"\13\1\142\2\133\1\144\1\133\2\uffff\2\133\1\12\5\144\4\133\4\144"
        u"\1\12\1\146\2\133\2\144\1\133\1\144"
        )

    DFA17_accept = DFA.unpack(
        u"\25\uffff\1\2\1\1\30\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\57\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\5\1\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\7\4\uffff\1\10"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\14\125\uffff\1\16\1\15"),
        DFA.unpack(u"\1\21\123\uffff\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\22\123\uffff\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\25\131\uffff\1\26"),
        DFA.unpack(u"\1\27\4\uffff\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\16\1\15"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\40\125\uffff\1\16\1\15"),
        DFA.unpack(u"\1\41\123\uffff\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\42\123\uffff\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\51\125\uffff\1\50\1\47"),
        DFA.unpack(u"\1\16\1\15"),
        DFA.unpack(u"\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\20\2\uffff\1\17"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\25\131\uffff\1\26"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\50\1\47"),
        DFA.unpack(u"\1\55\125\uffff\1\50\1\47"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\50\1\47")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA23_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA23_min = DFA.unpack(
        u"\1\14\1\133\1\136\1\uffff\1\133\1\uffff\1\136"
        )

    DFA23_max = DFA.unpack(
        u"\1\14\1\133\1\142\1\uffff\1\133\1\uffff\1\142"
        )

    DFA23_accept = DFA.unpack(
        u"\3\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA23_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA23_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\1\uffff\1\5\1\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\uffff\1\5\1\uffff\1\3")
    ]

    # class definition for DFA #23

    class DFA23(DFA):
        pass


    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\3\uffff\1\12\11\uffff\1\12\16\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\2\133\2\15\1\143\2\133\4\uffff\2\133\1\15\1\143\1\0\2\143\2\133"
        u"\2\uffff\1\133\3\143\1\133\1\143"
        )

    DFA27_max = DFA.unpack(
        u"\1\142\1\143\1\142\1\144\1\145\1\143\1\133\4\uffff\2\133\1\144"
        u"\1\145\1\0\1\144\1\145\2\133\2\uffff\1\133\1\144\1\145\1\144\1"
        u"\133\1\144"
        )

    DFA27_accept = DFA.unpack(
        u"\7\uffff\1\3\1\5\1\2\1\1\11\uffff\1\4\1\6\6\uffff"
        )

    DFA27_special = DFA.unpack(
        u"\2\uffff\1\1\14\uffff\1\0\14\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u"\1\4\7\uffff\1\3"),
        DFA.unpack(u"\1\6\124\uffff\1\5"),
        DFA.unpack(u"\1\11\123\uffff\1\12\2\uffff\1\12"),
        DFA.unpack(u"\1\3\1\14\1\13"),
        DFA.unpack(u"\1\16\7\uffff\1\15"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\11\123\uffff\1\12\2\uffff\1\12"),
        DFA.unpack(u"\1\15\1\23\1\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\3\1\14"),
        DFA.unpack(u"\1\3\1\14\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\15\1\23"),
        DFA.unpack(u"\1\15\1\23\1\32"),
        DFA.unpack(u"\1\3\1\14"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\15\1\23")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA27_15 = input.LA(1)

                 
                index27_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred36_Scribble()):
                    s = 20

                elif (True):
                    s = 21

                 
                input.seek(index27_15)
                if s >= 0:
                    return s
            elif s == 1: 
                LA27_2 = input.LA(1)

                 
                index27_2 = input.index()
                input.rewind()
                s = -1
                if (LA27_2 == 98):
                    s = 5

                elif (LA27_2 == ASKW):
                    s = 6

                elif (self.synpred35_Scribble()):
                    s = 7

                elif (self.synpred37_Scribble()):
                    s = 8

                 
                input.seek(index27_2)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 27, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\34\1\133\1\136\1\133\1\uffff\1\133\1\uffff\2\136\1\133\2\uffff"
        u"\1\136"
        )

    DFA38_max = DFA.unpack(
        u"\1\34\1\133\1\145\1\133\1\uffff\1\133\1\uffff\2\142\1\133\2\uffff"
        u"\1\142"
        )

    DFA38_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1\3\uffff\1\4\1\3\1\uffff"
        )

    DFA38_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3\1\uffff\1\4\1\uffff\1\6\2\uffff\1\5"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\1\4\1\uffff\1\6"),
        DFA.unpack(u"\1\11\1\uffff\1\12\1\uffff\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\1\uffff\1\12\1\uffff\1\13")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\61\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\61\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\11\1\7\1\133\1\21\1\133\1\140\1\12\1\6\3\133\3\15\1\133\1\12"
        u"\1\14\1\133\1\6\1\142\1\133\1\143\1\133\2\uffff\1\141\2\133\1\12"
        u"\1\141\3\15\4\133\1\15\1\143\2\141\1\133\1\12\1\14\1\143\1\133"
        u"\1\15\1\133\1\143"
        )

    DFA39_max = DFA.unpack(
        u"\1\11\1\7\1\133\1\21\1\133\1\142\1\12\1\13\3\133\3\144\1\133\1"
        u"\12\1\146\1\133\1\13\1\142\1\133\1\144\1\133\2\uffff\1\144\2\133"
        u"\1\12\4\144\4\133\4\144\1\133\1\12\1\146\1\144\1\133\1\144\1\133"
        u"\1\144"
        )

    DFA39_accept = DFA.unpack(
        u"\27\uffff\1\2\1\1\30\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\61\uffff"
        )

            
    DFA39_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\1\uffff\1\6"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\11\4\uffff\1\12"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\16\125\uffff\1\20\1\17"),
        DFA.unpack(u"\1\21\123\uffff\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\24\123\uffff\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27\131\uffff\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32\4\uffff\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\20\1\17"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\42\125\uffff\1\20\1\17"),
        DFA.unpack(u"\1\43\123\uffff\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\44\123\uffff\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51\125\uffff\1\53\1\52"),
        DFA.unpack(u"\1\20\1\17"),
        DFA.unpack(u"\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\23\2\uffff\1\22"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\27\131\uffff\1\30"),
        DFA.unpack(u"\1\53\1\52"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57\125\uffff\1\53\1\52"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\53\1\52")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA41_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA41_min = DFA.unpack(
        u"\1\14\1\133\1\136\1\uffff\1\133\1\uffff\1\136"
        )

    DFA41_max = DFA.unpack(
        u"\1\14\1\133\1\142\1\uffff\1\133\1\uffff\1\142"
        )

    DFA41_accept = DFA.unpack(
        u"\3\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA41_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA41_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\1\uffff\1\5\1\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\uffff\1\5\1\uffff\1\3")
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass


    # lookup tables for DFA #43

    DFA43_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA43_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA43_min = DFA.unpack(
        u"\1\20\1\133\1\16\6\uffff\1\16\1\143\1\133\2\uffff\2\133\1\16\3"
        u"\143\3\133\3\143\1\133\1\143"
        )

    DFA43_max = DFA.unpack(
        u"\1\142\1\143\1\142\6\uffff\1\17\1\145\1\143\2\uffff\2\133\1\17"
        u"\2\145\1\144\3\133\1\145\2\144\1\133\1\144"
        )

    DFA43_accept = DFA.unpack(
        u"\3\uffff\1\3\1\4\1\5\1\6\1\7\1\10\3\uffff\1\1\1\2\16\uffff"
        )

    DFA43_special = DFA.unpack(
        u"\34\uffff"
        )

            
    DFA43_transition = [
        DFA.unpack(u"\1\3\2\uffff\1\5\1\6\1\4\1\uffff\1\7\4\uffff\1\10\76"
        u"\uffff\1\2\6\uffff\1\1"),
        DFA.unpack(u"\1\12\7\uffff\1\11"),
        DFA.unpack(u"\1\15\1\14\122\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15\1\14"),
        DFA.unpack(u"\1\11\1\16\1\17"),
        DFA.unpack(u"\1\21\7\uffff\1\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\15\1\14"),
        DFA.unpack(u"\1\20\1\24\1\25"),
        DFA.unpack(u"\1\11\1\16\1\26"),
        DFA.unpack(u"\1\11\1\16"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\20\1\24\1\32"),
        DFA.unpack(u"\1\20\1\24"),
        DFA.unpack(u"\1\11\1\16"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\20\1\24")
    ]

    # class definition for DFA #43

    class DFA43(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\1\34\1\133\1\136\1\uffff\1\133\1\uffff\1\133\2\136\1\133\2\uffff"
        u"\1\136"
        )

    DFA53_max = DFA.unpack(
        u"\1\34\1\133\1\145\1\uffff\1\133\1\uffff\1\133\2\142\1\133\2\uffff"
        u"\1\142"
        )

    DFA53_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1\4\uffff\1\4\1\3\1\uffff"
        )

    DFA53_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA53_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\1\uffff\1\3\1\uffff\1\5\2\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\4\1\uffff\1\3\1\uffff\1\5"),
        DFA.unpack(u"\1\11\1\uffff\1\12\1\uffff\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\1\uffff\1\12\1\uffff\1\13")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


 

    FOLLOW_IDENTIFIER_in_rolename1006 = frozenset([1])
    FOLLOW_IDENTIFIER_in_payloadtypename1012 = frozenset([1])
    FOLLOW_IDENTIFIER_in_protocolname1018 = frozenset([1])
    FOLLOW_IDENTIFIER_in_parametername1024 = frozenset([1])
    FOLLOW_IDENTIFIER_in_annotationname1030 = frozenset([1])
    FOLLOW_IDENTIFIER_in_recursionlabelname1036 = frozenset([1])
    FOLLOW_IDENTIFIER_in_scopename1042 = frozenset([1])
    FOLLOW_IDENTIFIER_in_modulename1058 = frozenset([94])
    FOLLOW_94_in_modulename1061 = frozenset([91])
    FOLLOW_IDENTIFIER_in_modulename1063 = frozenset([94])
    FOLLOW_94_in_modulename1067 = frozenset([91])
    FOLLOW_IDENTIFIER_in_modulename1069 = frozenset([1])
    FOLLOW_IDENTIFIER_in_modulename1083 = frozenset([1])
    FOLLOW_simplemembername_in_membername1101 = frozenset([1])
    FOLLOW_fullmembername_in_membername1106 = frozenset([1])
    FOLLOW_payloadtypename_in_simplemembername1115 = frozenset([1])
    FOLLOW_protocolname_in_simplemembername1120 = frozenset([1])
    FOLLOW_modulename_in_fullmembername1132 = frozenset([94])
    FOLLOW_94_in_fullmembername1134 = frozenset([91])
    FOLLOW_simplemembername_in_fullmembername1136 = frozenset([1])
    FOLLOW_moduledecl_in_module1159 = frozenset([1, 5, 6, 8, 9, 14])
    FOLLOW_importdecl_in_module1162 = frozenset([1, 5, 6, 8, 9, 14])
    FOLLOW_payloadtypedecl_in_module1167 = frozenset([1, 6, 8, 9])
    FOLLOW_protocoldecl_in_module1172 = frozenset([1, 8, 9])
    FOLLOW_MODULEKW_in_moduledecl1217 = frozenset([91])
    FOLLOW_modulename_in_moduledecl1219 = frozenset([95])
    FOLLOW_95_in_moduledecl1221 = frozenset([1])
    FOLLOW_importmodule_in_importdecl1243 = frozenset([1])
    FOLLOW_importmember_in_importdecl1248 = frozenset([1])
    FOLLOW_IMPORTKW_in_importmodule1257 = frozenset([91])
    FOLLOW_modulename_in_importmodule1259 = frozenset([95])
    FOLLOW_95_in_importmodule1261 = frozenset([1])
    FOLLOW_IMPORTKW_in_importmodule1279 = frozenset([91])
    FOLLOW_modulename_in_importmodule1281 = frozenset([13])
    FOLLOW_ASKW_in_importmodule1283 = frozenset([91])
    FOLLOW_IDENTIFIER_in_importmodule1285 = frozenset([95])
    FOLLOW_95_in_importmodule1287 = frozenset([1])
    FOLLOW_FROMKW_in_importmember1358 = frozenset([91])
    FOLLOW_modulename_in_importmember1360 = frozenset([5])
    FOLLOW_IMPORTKW_in_importmember1362 = frozenset([91])
    FOLLOW_simplemembername_in_importmember1364 = frozenset([95])
    FOLLOW_95_in_importmember1366 = frozenset([1])
    FOLLOW_FROMKW_in_importmember1432 = frozenset([91])
    FOLLOW_modulename_in_importmember1434 = frozenset([5])
    FOLLOW_IMPORTKW_in_importmember1436 = frozenset([91])
    FOLLOW_simplemembername_in_importmember1438 = frozenset([13])
    FOLLOW_ASKW_in_importmember1440 = frozenset([91])
    FOLLOW_IDENTIFIER_in_importmember1442 = frozenset([95])
    FOLLOW_95_in_importmember1444 = frozenset([1])
    FOLLOW_TYPEKW_in_payloadtypedecl1474 = frozenset([96])
    FOLLOW_96_in_payloadtypedecl1476 = frozenset([91])
    FOLLOW_IDENTIFIER_in_payloadtypedecl1478 = frozenset([97])
    FOLLOW_97_in_payloadtypedecl1480 = frozenset([93])
    FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1482 = frozenset([14])
    FOLLOW_FROMKW_in_payloadtypedecl1484 = frozenset([93])
    FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1486 = frozenset([13])
    FOLLOW_ASKW_in_payloadtypedecl1488 = frozenset([91])
    FOLLOW_payloadtypename_in_payloadtypedecl1490 = frozenset([95])
    FOLLOW_95_in_payloadtypedecl1492 = frozenset([1])
    FOLLOW_set_in_messageoperator1524 = frozenset([1, 88, 89, 90])
    FOLLOW_98_in_messagesignature1544 = frozenset([91, 99])
    FOLLOW_payload_in_messagesignature1546 = frozenset([99])
    FOLLOW_99_in_messagesignature1548 = frozenset([1])
    FOLLOW_IDENTIFIER_in_messagesignature1567 = frozenset([98])
    FOLLOW_98_in_messagesignature1569 = frozenset([91, 99])
    FOLLOW_payload_in_messagesignature1571 = frozenset([99])
    FOLLOW_99_in_messagesignature1573 = frozenset([1])
    FOLLOW_payloadelement_in_payload1606 = frozenset([1, 100])
    FOLLOW_100_in_payload1609 = frozenset([91, 100])
    FOLLOW_payloadelement_in_payload1611 = frozenset([1, 100])
    FOLLOW_payloadtypename_in_payloadelement1635 = frozenset([1])
    FOLLOW_parametername_in_payloadelement1652 = frozenset([1])
    FOLLOW_annotationname_in_payloadelement1672 = frozenset([101])
    FOLLOW_101_in_payloadelement1674 = frozenset([91])
    FOLLOW_payloadtypename_in_payloadelement1676 = frozenset([1])
    FOLLOW_annotationname_in_payloadelement1693 = frozenset([101])
    FOLLOW_101_in_payloadelement1695 = frozenset([91])
    FOLLOW_parametername_in_payloadelement1697 = frozenset([1])
    FOLLOW_globalprotocoldecl_in_protocoldecl1721 = frozenset([1])
    FOLLOW_localprotocoldecl_in_protocoldecl1726 = frozenset([1])
    FOLLOW_globalprotocolheader_in_globalprotocoldecl1739 = frozenset([102])
    FOLLOW_globalprotocoldefinition_in_globalprotocoldecl1741 = frozenset([1])
    FOLLOW_globalprotocolheader_in_globalprotocoldecl1758 = frozenset([12])
    FOLLOW_globalprotocolinstance_in_globalprotocoldecl1760 = frozenset([1])
    FOLLOW_GLOBALKW_in_globalprotocolheader1783 = frozenset([7])
    FOLLOW_PROTOCOLKW_in_globalprotocolheader1785 = frozenset([91])
    FOLLOW_protocolname_in_globalprotocolheader1787 = frozenset([98])
    FOLLOW_roledecllist_in_globalprotocolheader1789 = frozenset([1])
    FOLLOW_GLOBALKW_in_globalprotocolheader1804 = frozenset([7])
    FOLLOW_PROTOCOLKW_in_globalprotocolheader1806 = frozenset([91])
    FOLLOW_protocolname_in_globalprotocolheader1808 = frozenset([96])
    FOLLOW_parameterdecllist_in_globalprotocolheader1810 = frozenset([98])
    FOLLOW_roledecllist_in_globalprotocolheader1812 = frozenset([1])
    FOLLOW_98_in_roledecllist1831 = frozenset([10])
    FOLLOW_roledecl_in_roledecllist1833 = frozenset([99, 100])
    FOLLOW_100_in_roledecllist1836 = frozenset([10])
    FOLLOW_roledecl_in_roledecllist1838 = frozenset([99, 100])
    FOLLOW_99_in_roledecllist1842 = frozenset([1])
    FOLLOW_ROLEKW_in_roledecl1864 = frozenset([91])
    FOLLOW_rolename_in_roledecl1866 = frozenset([1])
    FOLLOW_ROLEKW_in_roledecl1881 = frozenset([91])
    FOLLOW_rolename_in_roledecl1883 = frozenset([13])
    FOLLOW_ASKW_in_roledecl1885 = frozenset([91])
    FOLLOW_rolename_in_roledecl1887 = frozenset([1])
    FOLLOW_96_in_parameterdecllist1908 = frozenset([6, 11])
    FOLLOW_parameterdecl_in_parameterdecllist1910 = frozenset([97, 100])
    FOLLOW_100_in_parameterdecllist1913 = frozenset([6, 11])
    FOLLOW_parameterdecl_in_parameterdecllist1915 = frozenset([97, 100])
    FOLLOW_97_in_parameterdecllist1919 = frozenset([1])
    FOLLOW_TYPEKW_in_parameterdecl1942 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl1944 = frozenset([1])
    FOLLOW_TYPEKW_in_parameterdecl1962 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl1964 = frozenset([13])
    FOLLOW_ASKW_in_parameterdecl1966 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl1968 = frozenset([1])
    FOLLOW_SIGKW_in_parameterdecl1988 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl1990 = frozenset([1])
    FOLLOW_SIGKW_in_parameterdecl2008 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl2010 = frozenset([13])
    FOLLOW_ASKW_in_parameterdecl2012 = frozenset([91])
    FOLLOW_parametername_in_parameterdecl2014 = frozenset([1])
    FOLLOW_globalprotocolblock_in_globalprotocoldefinition2040 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2062 = frozenset([91])
    FOLLOW_membername_in_globalprotocolinstance2064 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globalprotocolinstance2066 = frozenset([95])
    FOLLOW_95_in_globalprotocolinstance2068 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2089 = frozenset([91])
    FOLLOW_membername_in_globalprotocolinstance2091 = frozenset([96])
    FOLLOW_argumentlist_in_globalprotocolinstance2093 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globalprotocolinstance2095 = frozenset([95])
    FOLLOW_95_in_globalprotocolinstance2097 = frozenset([1])
    FOLLOW_98_in_roleinstantiationlist2120 = frozenset([91])
    FOLLOW_roleinstantiation_in_roleinstantiationlist2122 = frozenset([99, 100])
    FOLLOW_100_in_roleinstantiationlist2125 = frozenset([91])
    FOLLOW_roleinstantiation_in_roleinstantiationlist2127 = frozenset([99, 100])
    FOLLOW_99_in_roleinstantiationlist2131 = frozenset([1])
    FOLLOW_rolename_in_roleinstantiation2153 = frozenset([1])
    FOLLOW_rolename_in_roleinstantiation2168 = frozenset([13])
    FOLLOW_ASKW_in_roleinstantiation2170 = frozenset([91])
    FOLLOW_rolename_in_roleinstantiation2172 = frozenset([1])
    FOLLOW_96_in_argumentlist2193 = frozenset([91, 98])
    FOLLOW_argument_in_argumentlist2195 = frozenset([97, 100])
    FOLLOW_100_in_argumentlist2198 = frozenset([91, 98])
    FOLLOW_argument_in_argumentlist2200 = frozenset([97, 100])
    FOLLOW_97_in_argumentlist2204 = frozenset([1])
    FOLLOW_messagesignature_in_argument2226 = frozenset([1])
    FOLLOW_messagesignature_in_argument2241 = frozenset([13])
    FOLLOW_ASKW_in_argument2243 = frozenset([91])
    FOLLOW_parametername_in_argument2245 = frozenset([1])
    FOLLOW_payloadtypename_in_argument2262 = frozenset([1])
    FOLLOW_payloadtypename_in_argument2277 = frozenset([13])
    FOLLOW_ASKW_in_argument2279 = frozenset([91])
    FOLLOW_parametername_in_argument2281 = frozenset([1])
    FOLLOW_parametername_in_argument2298 = frozenset([1])
    FOLLOW_parametername_in_argument2315 = frozenset([13])
    FOLLOW_ASKW_in_argument2317 = frozenset([91])
    FOLLOW_parametername_in_argument2319 = frozenset([1])
    FOLLOW_102_in_globalprotocolblock2345 = frozenset([16, 19, 20, 21, 23, 28, 91, 98, 103])
    FOLLOW_globalinteractionsequence_in_globalprotocolblock2347 = frozenset([103])
    FOLLOW_103_in_globalprotocolblock2349 = frozenset([1])
    FOLLOW_globalinteraction_in_globalinteractionsequence2369 = frozenset([1, 16, 19, 20, 21, 23, 28, 91, 98])
    FOLLOW_globalmessagetransfer_in_globalinteraction2393 = frozenset([1])
    FOLLOW_globalchoice_in_globalinteraction2398 = frozenset([1])
    FOLLOW_globalrecursion_in_globalinteraction2403 = frozenset([1])
    FOLLOW_globalcontinue_in_globalinteraction2408 = frozenset([1])
    FOLLOW_globalparallel_in_globalinteraction2413 = frozenset([1])
    FOLLOW_globalinterruptible_in_globalinteraction2418 = frozenset([1])
    FOLLOW_globaldo_in_globalinteraction2423 = frozenset([1])
    FOLLOW_message_in_globalmessagetransfer2437 = frozenset([14])
    FOLLOW_FROMKW_in_globalmessagetransfer2439 = frozenset([91])
    FOLLOW_rolename_in_globalmessagetransfer2441 = frozenset([15])
    FOLLOW_TOKW_in_globalmessagetransfer2443 = frozenset([91])
    FOLLOW_rolename_in_globalmessagetransfer2445 = frozenset([95, 100])
    FOLLOW_100_in_globalmessagetransfer2448 = frozenset([91])
    FOLLOW_rolename_in_globalmessagetransfer2450 = frozenset([95, 100])
    FOLLOW_95_in_globalmessagetransfer2455 = frozenset([1])
    FOLLOW_messagesignature_in_message2481 = frozenset([1])
    FOLLOW_parametername_in_message2486 = frozenset([1])
    FOLLOW_CHOICEKW_in_globalchoice2498 = frozenset([17])
    FOLLOW_ATKW_in_globalchoice2500 = frozenset([91])
    FOLLOW_rolename_in_globalchoice2502 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalchoice2504 = frozenset([1, 18])
    FOLLOW_ORKW_in_globalchoice2507 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalchoice2509 = frozenset([1, 18])
    FOLLOW_RECKW_in_globalrecursion2536 = frozenset([91])
    FOLLOW_recursionlabelname_in_globalrecursion2538 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalrecursion2540 = frozenset([1])
    FOLLOW_CONTINUEKW_in_globalcontinue2561 = frozenset([91])
    FOLLOW_recursionlabelname_in_globalcontinue2563 = frozenset([95])
    FOLLOW_95_in_globalcontinue2565 = frozenset([1])
    FOLLOW_PARKW_in_globalparallel2587 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalparallel2589 = frozenset([1, 22])
    FOLLOW_ANDKW_in_globalparallel2592 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalparallel2594 = frozenset([1, 22])
    FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2619 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalinterruptible2621 = frozenset([24])
    FOLLOW_WITHKW_in_globalinterruptible2623 = frozenset([102])
    FOLLOW_102_in_globalinterruptible2625 = frozenset([91, 98, 103])
    FOLLOW_globalinterrupt_in_globalinterruptible2628 = frozenset([91, 98, 103])
    FOLLOW_103_in_globalinterruptible2632 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2654 = frozenset([91])
    FOLLOW_scopename_in_globalinterruptible2656 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalinterruptible2658 = frozenset([24])
    FOLLOW_WITHKW_in_globalinterruptible2660 = frozenset([102])
    FOLLOW_102_in_globalinterruptible2662 = frozenset([91, 98, 103])
    FOLLOW_globalinterrupt_in_globalinterruptible2665 = frozenset([91, 98, 103])
    FOLLOW_103_in_globalinterruptible2669 = frozenset([1])
    FOLLOW_message_in_globalinterrupt2695 = frozenset([25, 100])
    FOLLOW_100_in_globalinterrupt2698 = frozenset([91, 98])
    FOLLOW_message_in_globalinterrupt2700 = frozenset([25, 100])
    FOLLOW_BYKW_in_globalinterrupt2704 = frozenset([91])
    FOLLOW_rolename_in_globalinterrupt2706 = frozenset([95])
    FOLLOW_95_in_globalinterrupt2708 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2735 = frozenset([91])
    FOLLOW_membername_in_globaldo2737 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globaldo2739 = frozenset([95])
    FOLLOW_95_in_globaldo2741 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2764 = frozenset([91])
    FOLLOW_membername_in_globaldo2766 = frozenset([96])
    FOLLOW_argumentlist_in_globaldo2768 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globaldo2770 = frozenset([95])
    FOLLOW_95_in_globaldo2772 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2793 = frozenset([91])
    FOLLOW_scopename_in_globaldo2795 = frozenset([101])
    FOLLOW_101_in_globaldo2797 = frozenset([91])
    FOLLOW_membername_in_globaldo2799 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globaldo2801 = frozenset([95])
    FOLLOW_95_in_globaldo2803 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2824 = frozenset([91])
    FOLLOW_scopename_in_globaldo2826 = frozenset([101])
    FOLLOW_101_in_globaldo2828 = frozenset([91])
    FOLLOW_membername_in_globaldo2830 = frozenset([96])
    FOLLOW_argumentlist_in_globaldo2832 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_globaldo2834 = frozenset([95])
    FOLLOW_95_in_globaldo2836 = frozenset([1])
    FOLLOW_localprotocolheader_in_localprotocoldecl2870 = frozenset([102])
    FOLLOW_localprotocoldefinition_in_localprotocoldecl2872 = frozenset([1])
    FOLLOW_localprotocolheader_in_localprotocoldecl2889 = frozenset([12])
    FOLLOW_localprotocolinstance_in_localprotocoldecl2891 = frozenset([1])
    FOLLOW_LOCALKW_in_localprotocolheader2912 = frozenset([7])
    FOLLOW_PROTOCOLKW_in_localprotocolheader2914 = frozenset([91])
    FOLLOW_protocolname_in_localprotocolheader2916 = frozenset([17])
    FOLLOW_ATKW_in_localprotocolheader2918 = frozenset([91])
    FOLLOW_rolename_in_localprotocolheader2920 = frozenset([98])
    FOLLOW_roledecllist_in_localprotocolheader2922 = frozenset([1])
    FOLLOW_LOCALKW_in_localprotocolheader2939 = frozenset([7])
    FOLLOW_PROTOCOLKW_in_localprotocolheader2941 = frozenset([91])
    FOLLOW_protocolname_in_localprotocolheader2943 = frozenset([17])
    FOLLOW_ATKW_in_localprotocolheader2945 = frozenset([91])
    FOLLOW_rolename_in_localprotocolheader2947 = frozenset([96])
    FOLLOW_parameterdecllist_in_localprotocolheader2949 = frozenset([98])
    FOLLOW_roledecllist_in_localprotocolheader2951 = frozenset([1])
    FOLLOW_localprotocolblock_in_localprotocoldefinition2975 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_localprotocolinstance2997 = frozenset([91])
    FOLLOW_membername_in_localprotocolinstance2999 = frozenset([98])
    FOLLOW_roledecllist_in_localprotocolinstance3001 = frozenset([95])
    FOLLOW_95_in_localprotocolinstance3003 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_localprotocolinstance3022 = frozenset([91])
    FOLLOW_membername_in_localprotocolinstance3024 = frozenset([96])
    FOLLOW_argumentlist_in_localprotocolinstance3026 = frozenset([98])
    FOLLOW_roledecllist_in_localprotocolinstance3028 = frozenset([95])
    FOLLOW_95_in_localprotocolinstance3030 = frozenset([1])
    FOLLOW_102_in_localprotocolblock3056 = frozenset([16, 19, 20, 21, 23, 28, 91, 98, 103])
    FOLLOW_localinteractionsequence_in_localprotocolblock3058 = frozenset([103])
    FOLLOW_103_in_localprotocolblock3060 = frozenset([1])
    FOLLOW_localinteraction_in_localinteractionsequence3080 = frozenset([1, 16, 19, 20, 21, 23, 28, 91, 98])
    FOLLOW_localsend_in_localinteraction3104 = frozenset([1])
    FOLLOW_localreceive_in_localinteraction3109 = frozenset([1])
    FOLLOW_localchoice_in_localinteraction3114 = frozenset([1])
    FOLLOW_localparallel_in_localinteraction3119 = frozenset([1])
    FOLLOW_localrecursion_in_localinteraction3124 = frozenset([1])
    FOLLOW_localcontinue_in_localinteraction3129 = frozenset([1])
    FOLLOW_localinterruptible_in_localinteraction3134 = frozenset([1])
    FOLLOW_localdo_in_localinteraction3139 = frozenset([1])
    FOLLOW_message_in_localsend3153 = frozenset([15])
    FOLLOW_TOKW_in_localsend3155 = frozenset([91])
    FOLLOW_rolename_in_localsend3157 = frozenset([95, 100])
    FOLLOW_100_in_localsend3160 = frozenset([91])
    FOLLOW_rolename_in_localsend3162 = frozenset([95, 100])
    FOLLOW_95_in_localsend3166 = frozenset([1])
    FOLLOW_message_in_localreceive3190 = frozenset([14])
    FOLLOW_FROMKW_in_localreceive3192 = frozenset([91])
    FOLLOW_IDENTIFIER_in_localreceive3194 = frozenset([95])
    FOLLOW_95_in_localreceive3196 = frozenset([1])
    FOLLOW_CHOICEKW_in_localchoice3220 = frozenset([17])
    FOLLOW_ATKW_in_localchoice3222 = frozenset([91])
    FOLLOW_rolename_in_localchoice3224 = frozenset([102])
    FOLLOW_localprotocolblock_in_localchoice3226 = frozenset([1, 18])
    FOLLOW_ORKW_in_localchoice3229 = frozenset([102])
    FOLLOW_localprotocolblock_in_localchoice3231 = frozenset([1, 18])
    FOLLOW_RECKW_in_localrecursion3258 = frozenset([91])
    FOLLOW_recursionlabelname_in_localrecursion3260 = frozenset([102])
    FOLLOW_localprotocolblock_in_localrecursion3262 = frozenset([1])
    FOLLOW_CONTINUEKW_in_localcontinue3283 = frozenset([91])
    FOLLOW_recursionlabelname_in_localcontinue3285 = frozenset([95])
    FOLLOW_95_in_localcontinue3287 = frozenset([1])
    FOLLOW_PARKW_in_localparallel3309 = frozenset([102])
    FOLLOW_localprotocolblock_in_localparallel3311 = frozenset([1, 22])
    FOLLOW_ANDKW_in_localparallel3314 = frozenset([102])
    FOLLOW_localprotocolblock_in_localparallel3316 = frozenset([1, 22])
    FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3344 = frozenset([91])
    FOLLOW_scopename_in_localinterruptible3346 = frozenset([102])
    FOLLOW_localprotocolblock_in_localinterruptible3348 = frozenset([24])
    FOLLOW_WITHKW_in_localinterruptible3350 = frozenset([102])
    FOLLOW_102_in_localinterruptible3352 = frozenset([27, 103])
    FOLLOW_localcatch_in_localinterruptible3355 = frozenset([27, 103])
    FOLLOW_103_in_localinterruptible3359 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3383 = frozenset([91])
    FOLLOW_scopename_in_localinterruptible3385 = frozenset([102])
    FOLLOW_localprotocolblock_in_localinterruptible3387 = frozenset([24])
    FOLLOW_WITHKW_in_localinterruptible3389 = frozenset([102])
    FOLLOW_102_in_localinterruptible3391 = frozenset([26])
    FOLLOW_localthrow_in_localinterruptible3393 = frozenset([27, 103])
    FOLLOW_localcatch_in_localinterruptible3396 = frozenset([27, 103])
    FOLLOW_103_in_localinterruptible3400 = frozenset([1])
    FOLLOW_THROWSKW_in_localthrow3431 = frozenset([91, 98])
    FOLLOW_message_in_localthrow3433 = frozenset([15, 100])
    FOLLOW_100_in_localthrow3436 = frozenset([91, 98])
    FOLLOW_message_in_localthrow3438 = frozenset([15, 100])
    FOLLOW_TOKW_in_localthrow3442 = frozenset([91])
    FOLLOW_rolename_in_localthrow3444 = frozenset([95, 100])
    FOLLOW_100_in_localthrow3447 = frozenset([91])
    FOLLOW_rolename_in_localthrow3449 = frozenset([95, 100])
    FOLLOW_95_in_localthrow3453 = frozenset([1])
    FOLLOW_CATCHESKW_in_localcatch3482 = frozenset([91, 98])
    FOLLOW_message_in_localcatch3484 = frozenset([14, 100])
    FOLLOW_100_in_localcatch3487 = frozenset([91, 98])
    FOLLOW_message_in_localcatch3489 = frozenset([14, 100])
    FOLLOW_FROMKW_in_localcatch3493 = frozenset([91])
    FOLLOW_rolename_in_localcatch3495 = frozenset([95])
    FOLLOW_95_in_localcatch3497 = frozenset([1])
    FOLLOW_DOKW_in_localdo3524 = frozenset([91])
    FOLLOW_membername_in_localdo3526 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_localdo3528 = frozenset([95])
    FOLLOW_95_in_localdo3530 = frozenset([1])
    FOLLOW_DOKW_in_localdo3553 = frozenset([91])
    FOLLOW_membername_in_localdo3555 = frozenset([96])
    FOLLOW_argumentlist_in_localdo3557 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_localdo3559 = frozenset([95])
    FOLLOW_95_in_localdo3561 = frozenset([1])
    FOLLOW_DOKW_in_localdo3582 = frozenset([91])
    FOLLOW_scopename_in_localdo3584 = frozenset([101])
    FOLLOW_101_in_localdo3586 = frozenset([91])
    FOLLOW_membername_in_localdo3588 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_localdo3590 = frozenset([95])
    FOLLOW_95_in_localdo3592 = frozenset([1])
    FOLLOW_DOKW_in_localdo3613 = frozenset([91])
    FOLLOW_scopename_in_localdo3615 = frozenset([101])
    FOLLOW_101_in_localdo3617 = frozenset([91])
    FOLLOW_membername_in_localdo3619 = frozenset([96])
    FOLLOW_argumentlist_in_localdo3621 = frozenset([98])
    FOLLOW_roleinstantiationlist_in_localdo3623 = frozenset([95])
    FOLLOW_95_in_localdo3625 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred4_Scribble1115 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred17_Scribble1635 = frozenset([1])
    FOLLOW_parametername_in_synpred18_Scribble1652 = frozenset([1])
    FOLLOW_annotationname_in_synpred19_Scribble1672 = frozenset([101])
    FOLLOW_101_in_synpred19_Scribble1674 = frozenset([91])
    FOLLOW_payloadtypename_in_synpred19_Scribble1676 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred35_Scribble2262 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred36_Scribble2277 = frozenset([13])
    FOLLOW_ASKW_in_synpred36_Scribble2279 = frozenset([91])
    FOLLOW_parametername_in_synpred36_Scribble2281 = frozenset([1])
    FOLLOW_parametername_in_synpred37_Scribble2298 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_synpred71_Scribble3344 = frozenset([91])
    FOLLOW_scopename_in_synpred71_Scribble3346 = frozenset([102])
    FOLLOW_localprotocolblock_in_synpred71_Scribble3348 = frozenset([24])
    FOLLOW_WITHKW_in_synpred71_Scribble3350 = frozenset([102])
    FOLLOW_102_in_synpred71_Scribble3352 = frozenset([27, 103])
    FOLLOW_localcatch_in_synpred71_Scribble3355 = frozenset([27, 103])
    FOLLOW_103_in_synpred71_Scribble3359 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ScribbleLexer", ScribbleParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
