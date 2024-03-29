/*
 * Raymond@HZHL2 ~/code/python/scribble-tools
 * $ java -cp lib/antlr-3.1.3.jar org.antlr.Tool -o bin src/scribble/Scribble.g
*/

// Use language actions to directly create lists etc.? but ties the grammar source to that language?

// Garbage at the end of input file seems to just get ignored, no error raised. but also for e.g. two package declarations -- check if this is still the case?


grammar Scribble;

options
{
	language = Python;
	output = AST;
	ASTLabelType = CommonTree;
	backtrack = true;  // backtracking disabled by default? Is it bad to rely on this option?
	//memoize = true;
}

tokens
{
	/*
	 * Parser input constants (lexer output; keywords, Section 2.4)
	 */
	MODULEKW = 'module';
	IMPORTKW = 'import';
	TYPEKW = 'type';
	PROTOCOLKW = 'protocol';
	GLOBALKW = 'global';
	LOCALKW = 'local';
	ROLEKW = 'role';
	SIGKW = 'sig';
	INSTANTIATESKW = 'instantiates';
	ASKW = 'as';

	FROMKW = 'from';
	TOKW = 'to';
	CHOICEKW = 'choice';
	ATKW = 'at';
	ORKW = 'or';
	RECKW = 'rec';
	CONTINUEKW = 'continue';
	PARKW = 'par';
	ANDKW = 'and';
	INTERRUPTIBLEKW = 'interruptible';
	WITHKW = 'with';
	BYKW = 'by';  /* from for interrupts is more expected, but from is
	                 not good for multiple roles (generally, the comma
	                 in interrupt message list and role list looks like
	                 "and" rather than "or") */
	THROWSKW = 'throws';
	CATCHESKW = 'catches';
	DOKW = 'do';
	//SPAWNKW = 'spawn';


	/*
	 * Parser output node types (corresponding to the various syntactic
	 * categories) i.e. the labels used to distinguish resulting AST nodes.
	 * The value of these token variables doesn't matter, only the token
	 * (i.e. variable) names themselves are used (for AST node root text
	 * field)
	 */
	//MODULE = 'module';
	MODULE = 'modul';
	//PACKAGEDECL = 'package-decl';
	MODULEDECL = 'module-decl';
	//IMPORTDECL = 'import-decl';
	//FROMIMPORTDECL = 'from-import-decl';
	IMPORTMODULE = 'import-module';
	IMPORTMEMBER = 'import-member';
	PAYLOADTYPEDECL = 'payload-type-decl';
	PARAMETERDECLLIST = 'parameter-decl-list';
	PARAMETERDECL = 'parameter-decl';
	MESSAGESIGNATURE = 'message-signature';
	ROLEDECLLIST = 'role-decl-list';
	ROLEDECL = 'role-decl';
	ARGUMENTLIST = 'argument-list';
	ARGUMENT = 'argument';
	PAYLOAD = 'payload';
	PAYLOADELEMENT = 'payloadelement';
	ROLEINSTANTIATIONLIST = 'role-instantiation-list';
	ROLEINSTANTIATION = 'role-instantiation';

	GLOBALPROTOCOLDECL = 'global-protocol-decl';
	GLOBALPROTOCOLDEF = 'global-protocol-def';
	GLOBALPROTOCOLINSTANCE = 'global-protocol-instance';
	//GLOBALPROTOCOLBODY = 'global-protocol-body';
	GLOBALPROTOCOLBLOCK = 'global-protocol-block';
	GLOBALINTERACTIONSEQUENCE = 'global-interaction-sequence';
	GLOBALMESSAGETRANSFER = 'global-message-transfer';
	GLOBALCHOICE = 'global-choice';
	GLOBALRECURSION = 'global-recursion';
	GLOBALCONTINUE = 'global-continue';
	GLOBALPARALLEL = 'global-parallel';
	GLOBALINTERRUPTIBLE = 'global-interruptible';
	GLOBALINTERRUPT = 'global-interrupt';
	GLOBALDO = 'global-do';
	//GLOBALSPAWN = 'global-spawn';

	LOCALPROTOCOLDECL = 'local-protocol-decl';
	LOCALPROTOCOLDEF = 'local-protocol-def';
	LOCALPROTOCOLINSTANCE = 'local-protocol-instance';
	LOCALPROTOCOLBLOCK = 'local-protocol-block';
	LOCALINTERACTIONSEQUENCE = 'local-interaction-sequence';
	LOCALMESSAGETRANSFER = 'local-message-transfer';
	LOCALCHOICE = 'local-choice';
	LOCALRECURSION = 'local-recursion';
	LOCALCONTINUE = 'local-continue';
	LOCALPARALLEL = 'local-parallel';
	LOCALINTERRUPTIBLE = 'local-interruptible';
	LOCALINTERRUPT = 'local-interrupt';
	LOCALDO = 'local-do';
	LOCALTHROW = 'local-throw';
	LOCALCATCH = 'local-catch';
	LOCALSEND = 'local-send';
	LOCALRECEIVE = 'local-receive';


	/*
	 * Some utility constants; AST token values are the variable names (not
	 * the variable values).
	 * (N.B. Some grammar rules use dummy placeholder values, but others do not)
	 */
	EMPTY_MESSAGE_OP = '__empty_message_op';
	EMPTY_ANNOTATION = '__empty_annotation';
	EMPTY_PARAMETER_DECL_LIST = '__empty_parameter_decl_list';
	EMPTY_ARGUMENT_LIST = '__empty_argument_list';
	EMPTY_MODULE_NAME = '__empty_module_name';
	EMPTY_SCOPE_NAME = '__empty_scope_name';
	EMPTY_LOCAL_THROW = '__empty_local_throw';
	EMPTY_LOCAL_CATCHES = '__empty_local_catch';

	KIND_MESSAGE_SIGNATURE = 'KIND_MESSAGE_SIGNATURE';
	KIND_PAYLOAD_TYPE = 'KIND_PAYLOAD_TYPE';
}


/****************************************************************************
 * Chapter 2 Lexical Structure (Lexer rules)
 ***************************************************************************/

/*
 * Section 2.1 White space (Section 2.1)
 */
WHITESPACE:
	('\t' | ' ' | '\r' | '\n'| '\u000C')+
	{
		$channel = HIDDEN;
	}
;

/**
 * Section 2.2 Comments
 */
COMMENT:
	'/*' .* '*/'
	{
		$channel=HIDDEN;
	}
;

LINE_COMMENT:
	'//' ~('\n'|'\r')* '\r'? '\n'
	{
		$channel=HIDDEN;
	}
;

/**
 * Section 2.3 Identifiers
 */
IDENTIFIER:
	(LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*
;

fragment SYMBOL:
	'{' | '}' | '(' | ')' | '[' | ']' | ':' | '/' | '\\' | '.' | '\#'
|
	'&' | '?' | '!'	| UNDERSCORE
;

// Comes after SYMBOL due to an ANTLR syntax highlighting issue
// involving quotes
EXTIDENTIFIER:
	'\"' (LETTER | UNDERSCORE) (LETTER | DIGIT | SYMBOL)* '\"'
;

fragment LETTER:
	'a'..'z' | 'A'..'Z'
;

fragment DIGIT:
	'0'..'9'
;

fragment UNDERSCORE:
	'_'
;


/****************************************************************************
 * Chapter 3 Syntax (Parser rules)
 ***************************************************************************/

/*
 * Section 3.1 Primitive Names
 */
rolename: IDENTIFIER;
payloadtypename: IDENTIFIER;
protocolname: IDENTIFIER;
parametername: IDENTIFIER;
annotationname: IDENTIFIER;
recursionlabelname: IDENTIFIER;
scopename: IDENTIFIER;


/**
 * Section 3.2.1 Package, Module and Module Member Names
 */
/*packagename:
	IDENTIFIER ('.' IDENTIFIER)*
	->
	(IDENTIFIER)+
;*/

modulename:
	//packagename '.' IDENTIFIER  // Not working
	IDENTIFIER ('.' IDENTIFIER)* '.' IDENTIFIER
	->
	(IDENTIFIER)+
|
	IDENTIFIER
	->
	(IDENTIFIER)+
;

membername:
	simplemembername
|
	fullmembername
;

simplemembername:
	payloadtypename
|
	protocolname  /* Generates an ANTLR warning since both are IDENTIFIER
	                 if no backtrack (makes ANTLR think this alternative
	                 is reachable, but actually it isn't) */
;

fullmembername:
	modulename '.' simplemembername  /* Needs backtrack=true
	                                    since the simplemembername can/will
																			be eagerly consumed by modulename */
	->
	modulename simplemembername
;


/**
 * Section 3.2.2 Top-level Module Structure
 */
module:
	moduledecl (importdecl)* (payloadtypedecl)* (protocoldecl)*
	->
	/* "Root value" seems to be stored as a string (the token name, not
	   value), other parts stored as subtrees */
	^(MODULE moduledecl (importdecl)* (payloadtypedecl)* (protocoldecl)*)
	/* Looks for a token called "MODULE", but uses the token name, not the
	   value of the token... */
;


/**
 * Section 3.2.3 Module Declarations
 */
moduledecl:
	MODULEKW modulename ';'
	->
	^(MODULEDECL modulename)
;


/**
 * Section 3.3 Import Declarations
 */
importdecl:
	importmodule
|
	importmember
;

importmodule:
	IMPORTKW modulename ';'
	->
	^(IMPORTMODULE modulename)  /* Dummy empty values not used consistently
	                               across categories */
|
	IMPORTKW modulename ASKW IDENTIFIER ';'
	->
	^(IMPORTMODULE ASKW IDENTIFIER modulename)  // Ordered to make AST node
	                                            // getters easier
;

importmember:
	FROMKW modulename IMPORTKW simplemembername ';'
	->
	^(IMPORTMEMBER simplemembername modulename)  // Ordered to make AST node
	                                             // getters easier
|
	FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';'
	->
	^(IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename)
	// IDENTIFIER used (instead of simplemembername) to swap element order
;


/**
 * Section 3.4 Payload Type Declarations
 */
payloadtypedecl:
	TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';'
	->
	^(PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename)
  /* Seems to go off "element order" in the output references,
	   no way to label/index the elements */
;


/**
 * Section 3.5 Message Signatures
 */
messageoperator:
	(LETTER | DIGIT | UNDERSCORE)+
;

messagesignature:
	'(' payload ')'
	->
	^(MESSAGESIGNATURE EMPTY_MESSAGE_OP payload)
|
	//messageoperator '(' payload ')'  // Doesn't work (conflict with IDENTIFIER?)
	IDENTIFIER '(' payload ')'
	->
	//^(MESSAGESIGNATURE messageoperator payload)
	^(MESSAGESIGNATURE IDENTIFIER payload)
;

payload:
	->
	^(PAYLOAD)
|
	payloadelement (',' payloadelement)*
	->
	^(PAYLOAD (payloadelement)+)
;

payloadelement:
	payloadtypename
	->
	^(PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename)
|
	parametername  /* An IDENTIFIER, like payloadtypename, so generates warnings
	                  (unless backtrack=true) */
	->
	^(PAYLOADELEMENT EMPTY_ANNOTATION parametername)
|
	annotationname ':' payloadtypename
	->
	^(PAYLOADELEMENT annotationname payloadtypename)
|
	annotationname ':' parametername
	->
	^(PAYLOADELEMENT annotationname parametername)
;


/**
 * Section 3.6 Protocol Declarations
 */
protocoldecl:
	globalprotocoldecl
|
	localprotocoldecl
;


/**
 * Section 3.7 Global Protocol Declarations
 */
globalprotocoldecl:
	 globalprotocolheader globalprotocoldefinition
	->
	^(GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition)
|
	globalprotocolheader globalprotocolinstance
	->
	^(GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance)
;

globalprotocolheader:  // Currently, header is not an explicit category
	GLOBALKW PROTOCOLKW protocolname roledecllist
	->
	protocolname EMPTY_PARAMETER_DECL_LIST roledecllist
|
	GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist
	->
	protocolname parameterdecllist roledecllist
;

roledecllist:
	'(' roledecl (',' roledecl)* ')'
	->
	^(ROLEDECLLIST (roledecl)+)
;

roledecl:
	ROLEKW rolename
	->
	^(ROLEDECL rolename)
|
	ROLEKW rolename ASKW rolename
	->
	^(ROLEDECL rolename rolename)
;

parameterdecllist:
	'<' parameterdecl (',' parameterdecl)* '>'
	->
	^(PARAMETERDECLLIST (parameterdecl)+)
;

parameterdecl:
	 TYPEKW parametername
	->
	^(PARAMETERDECL KIND_PAYLOAD_TYPE parametername)
|
	 TYPEKW parametername ASKW parametername
	->
	^(PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername)
|
	 SIGKW parametername
	->
	^(PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername)
|
	 SIGKW parametername ASKW parametername
	->
	^(PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername)
;


/**
 * Section 3.7.1 Global Protocol Definitions
 */
globalprotocoldefinition:
	globalprotocolblock
	->
	^(GLOBALPROTOCOLDEF globalprotocolblock)
;


/**
 * Section 3.7.2 Global Protocol Instantiation
 */
globalprotocolinstance:
	INSTANTIATESKW membername roleinstantiationlist ';'
	->
	^(GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername)
	// membername at end to make indexing easier (could make proper name nodes)
|
	INSTANTIATESKW membername argumentlist roleinstantiationlist ';'
	->
	^(GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername)
;

roleinstantiationlist:
	'(' roleinstantiation (',' roleinstantiation)* ')'
	->
	^(ROLEINSTANTIATIONLIST (roleinstantiation)+)
;

roleinstantiation:
	rolename
	->
	^(ROLEINSTANTIATION rolename)
|
	rolename ASKW rolename
	->
	^(ROLEINSTANTIATION rolename rolename)
;

argumentlist:
	'<' argument (',' argument)* '>'
	->
	^(ARGUMENTLIST (argument)+)
;

argument:
	messagesignature
	->
	^(ARGUMENT messagesignature)
|
	messagesignature ASKW parametername
	->
	^(ARGUMENT messagesignature parametername)
|
	payloadtypename
	->
	^(ARGUMENT payloadtypename)
|
	payloadtypename ASKW parametername
	->
	^(ARGUMENT payloadtypename parametername)
|
	parametername  // generates warnings unless backtrack=true
	->
	^(ARGUMENT parametername)
|
	parametername ASKW parametername
	->
	^(ARGUMENT parametername ASKW parametername)
;


/**
 * Section 3.7.3 Global Interaction Sequences and Blocks
 */
globalprotocolblock:
	'{' globalinteractionsequence '}'
	->
	^(GLOBALPROTOCOLBLOCK globalinteractionsequence)
;

globalinteractionsequence:
	(globalinteraction)*
	->
	^(GLOBALINTERACTIONSEQUENCE (globalinteraction)*)
;

globalinteraction:
	globalmessagetransfer
|
	globalchoice
|
	globalrecursion
|
	globalcontinue
|
	globalparallel
|
	globalinterruptible
|
	globaldo
/*|
	globalspawn*/
;


/**
 * Section 3.7.4 Global Message Transfer
 */
globalmessagetransfer:
	message FROMKW rolename TOKW rolename (',' rolename )* ';'
	->
	^(GLOBALMESSAGETRANSFER message rolename (rolename)+)
;

message:
	messagesignature
|
	parametername
;


/**
 * Section 3.7.5 Global Choice
 */
globalchoice:
	CHOICEKW ATKW rolename globalprotocolblock (ORKW globalprotocolblock)*
	->
	^(GLOBALCHOICE rolename globalprotocolblock+)
;


/**
 * Section 3.7.6 Global Recursion
 */
globalrecursion:
	RECKW recursionlabelname globalprotocolblock
	->
	^(GLOBALRECURSION recursionlabelname globalprotocolblock)
;

globalcontinue:
	CONTINUEKW recursionlabelname ';'
	->
	^(GLOBALCONTINUE recursionlabelname)
;


/**
 * Section 3.7.7 Global Parallel
 */
globalparallel:
	PARKW globalprotocolblock (ANDKW globalprotocolblock)*
	->
	^(GLOBALPARALLEL globalprotocolblock+)
;


/**
 * Section 3.7.8 Global Interruptible
 */
globalinterruptible:
	INTERRUPTIBLEKW globalprotocolblock WITHKW '{' (globalinterrupt)* '}'
	->
	^(GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock (globalinterrupt)*)
|
	INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' (globalinterrupt)* '}'
	->
	^(GLOBALINTERRUPTIBLE scopename globalprotocolblock (globalinterrupt)*)
;

globalinterrupt:
	message (',' message)* BYKW rolename ';'
	->
	^(GLOBALINTERRUPT rolename (message)+)
;


/**
 * Section 3.7.9 Global Do
 */
globaldo:
	DOKW membername roleinstantiationlist ';'
	->
	^(GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername)
	// membername at end to make indexing easier (like instantiation)
|
	DOKW membername argumentlist roleinstantiationlist ';'
	->
	^(GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername)
|
	DOKW scopename ':' membername roleinstantiationlist ';'
	->
	^(GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername)
|
	DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
	->
	^(GLOBALDO scopename argumentlist roleinstantiationlist membername)
;


/**
 * TODO: Global Spawn
 */
/*globalspawn:
	SPAWNKW membername '(' roleinstantiationlist ')' ';'
	->
	^(GLOBALSPAWN membername EMPTY_ARGUMENT_LIST roleinstantiationlist)
|
	SPAWNKW membername '<' argumentlist '>' '(' roleinstantiationlist ')' ';'
	->
	^(GLOBALSPAWN membername argumentlist roleinstantiationlist)
;*/


/*
 * Section 3.8 Local Protocol Declarations
 */
localprotocoldecl:
	localprotocolheader localprotocoldefinition
	->
	^(LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition)
|
	localprotocolheader localprotocolinstance
	->
	^(LOCALPROTOCOLDECL localprotocolheader localprotocolinstance)
;

localprotocolheader:
	LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist
	->
	protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist
|
	LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist
	->
	protocolname rolename parameterdecllist roledecllist
;


/**
 * Section 3.8.1 Local Protocol Definitions
 */
localprotocoldefinition:
	localprotocolblock
	->
	^(LOCALPROTOCOLDEF localprotocolblock)
;


/**
 * Section 3.8.2 Local Protocol Instantiation
 */
localprotocolinstance:
	INSTANTIATESKW membername roledecllist ';'
	->
	^(LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername)
|
	INSTANTIATESKW membername argumentlist roledecllist ';'
	->
	^(LOCALPROTOCOLINSTANCE argumentlist roledecllist membername)
;


/**
 * Section 3.8.3 Local Interaction Blocks and Sequences
 */
localprotocolblock:
	'{' localinteractionsequence '}'
	->
	^(LOCALPROTOCOLBLOCK localinteractionsequence)
;

localinteractionsequence:
	(localinteraction)*
	->
	^(LOCALINTERACTIONSEQUENCE (localinteraction)*)
;

localinteraction:
	localsend
|
	localreceive
|
	localchoice
|
	localparallel
|
	localrecursion
|
	localcontinue
|
	localinterruptible
|
	localdo
/*|
	localspawn*/
;


/**
 * Section 3.8.4 Local Send and Receive
 */
localsend:
	message TOKW rolename (',' rolename)* ';'
	->
	^(LOCALSEND message (rolename)+)
;

localreceive:
	message FROMKW IDENTIFIER ';'
	->
	^(LOCALRECEIVE message IDENTIFIER)
;


/**
 * Section 3.8.5 Local Choice
 */
localchoice:
	CHOICEKW ATKW rolename localprotocolblock (ORKW localprotocolblock)*
	->
	^(LOCALCHOICE rolename localprotocolblock+)
;


/**
 * Section 3.8.6 Local Recursion
 */
localrecursion:
	RECKW recursionlabelname localprotocolblock
	->
	^(LOCALRECURSION recursionlabelname localprotocolblock)
;

localcontinue:
	CONTINUEKW recursionlabelname ';'
	->
	^(LOCALCONTINUE recursionlabelname)
;


/**
 * Section 3.8.7 Local Parallel
 */
localparallel:
	PARKW localprotocolblock (ANDKW localprotocolblock)*
	->
	^(LOCALPARALLEL localprotocolblock+)
;


/**
 * Section 3.8.8 Local Interruptible
 */
localinterruptible:
	/*INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrowandorcatch '}'
	->
	^(LOCALINTERRUPTIBLE scopename localprotocolblock localthrowandorcatch)
|*/
	INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' (localcatch)* '}'
	->
	^(LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW (localcatch)*)
|
	INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow (localcatch)* '}'
	->
	^(LOCALINTERRUPTIBLE scopename localprotocolblock localthrow (localcatch)*)
;

/*localthrowandorcatch:
	localthrow (localcatch)*
|
	(localcatch)+
;*/

localthrow:
	THROWSKW message (',' message)* TOKW rolename (',' rolename)* ';'
	->
	^(LOCALTHROW (rolename)+ TOKW (message)+)
;

localcatch:
	CATCHESKW message (',' message)* FROMKW rolename ';'
	->
	^(LOCALCATCH rolename (message)+)
;


/**
 * Section 3.8.9 Local Do
 */
localdo:
	DOKW membername roleinstantiationlist ';'
	->
	^(LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername)
	// membername at end to make indexing easier (like Global)
|
	DOKW membername argumentlist roleinstantiationlist ';'
	->
	^(LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername)
|
	DOKW scopename ':' membername roleinstantiationlist ';'
	->
	^(LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername)
|
	DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
	->
	^(LOCALDO scopename argumentlist roleinstantiationlist membername)
;

