// Generated from /home/lesire/Work/HierarchicalPlanning/pddl-python/PDDL.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PDDLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LP=1, RP=2, OF=3, EQUALS=4, DEFINE=5, DOMAIN=6, PROBLEM=7, DDOMAIN=8, 
		REQUIREMENTS=9, TYPES=10, CONSTANTS=11, PREDICATES=12, OBJECTS=13, INIT=14, 
		GOAL=15, ACTION=16, PARAMETERS=17, PRECONDITION=18, EFFECT=19, OBSERVE=20, 
		TASK=21, METHOD=22, ORDERED=23, SUBTASKS=24, ORDERING=25, CONSTRAINTS=26, 
		HTN=27, BEFORE=28, NOT=29, AND=30, FORALL=31, WHEN=32, EITHER=33, UNKNOWN=34, 
		OR=35, ONEOF=36, REQUIRE_KEY=37, NAME=38, VARIABLE=39, NUMBER=40, LINE_COMMENT=41, 
		WHITESPACE=42;
	public static final int
		RULE_pddl = 0, RULE_domain = 1, RULE_requireDef = 2, RULE_typesDef = 3, 
		RULE_typedList = 4, RULE_constantsDef = 5, RULE_typedObjList = 6, RULE_predicatesDef = 7, 
		RULE_predicateDef = 8, RULE_typedVarList = 9, RULE_structureDef = 10, 
		RULE_actionDef = 11, RULE_goalDef = 12, RULE_effectDef = 13, RULE_cEffect = 14, 
		RULE_condEffect = 15, RULE_observeDef = 16, RULE_literal = 17, RULE_atomicFormula = 18, 
		RULE_term = 19, RULE_taskDef = 20, RULE_methodDef = 21, RULE_taskNetworkDef = 22, 
		RULE_subtasksDef = 23, RULE_subtaskDef = 24, RULE_orderingDefs = 25, RULE_orderingDef = 26, 
		RULE_constraintDefs = 27, RULE_constraintDef = 28, RULE_problem = 29, 
		RULE_objectDeclaration = 30, RULE_init = 31, RULE_initEl = 32, RULE_goal = 33, 
		RULE_htnDef = 34, RULE_nameDef = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"pddl", "domain", "requireDef", "typesDef", "typedList", "constantsDef", 
			"typedObjList", "predicatesDef", "predicateDef", "typedVarList", "structureDef", 
			"actionDef", "goalDef", "effectDef", "cEffect", "condEffect", "observeDef", 
			"literal", "atomicFormula", "term", "taskDef", "methodDef", "taskNetworkDef", 
			"subtasksDef", "subtaskDef", "orderingDefs", "orderingDef", "constraintDefs", 
			"constraintDef", "problem", "objectDeclaration", "init", "initEl", "goal", 
			"htnDef", "nameDef"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'-'", "'='", "'define'", "'domain'", "'problem'", 
			"':domain'", "':requirements'", "':types'", "':constants'", "':predicates'", 
			"':objects'", "':init'", "':goal'", "':action'", "':parameters'", "':precondition'", 
			"':effect'", "':observe'", "':task'", "':method'", null, null, null, 
			"':constraints'", "':htn'", "'<'", "'not'", "'and'", "'forall'", "'when'", 
			"'either'", "'unknown'", "'or'", "'oneof'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LP", "RP", "OF", "EQUALS", "DEFINE", "DOMAIN", "PROBLEM", "DDOMAIN", 
			"REQUIREMENTS", "TYPES", "CONSTANTS", "PREDICATES", "OBJECTS", "INIT", 
			"GOAL", "ACTION", "PARAMETERS", "PRECONDITION", "EFFECT", "OBSERVE", 
			"TASK", "METHOD", "ORDERED", "SUBTASKS", "ORDERING", "CONSTRAINTS", "HTN", 
			"BEFORE", "NOT", "AND", "FORALL", "WHEN", "EITHER", "UNKNOWN", "OR", 
			"ONEOF", "REQUIRE_KEY", "NAME", "VARIABLE", "NUMBER", "LINE_COMMENT", 
			"WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PDDL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PDDLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class PddlContext extends ParserRuleContext {
		public DomainContext domain() {
			return getRuleContext(DomainContext.class,0);
		}
		public ProblemContext problem() {
			return getRuleContext(ProblemContext.class,0);
		}
		public PddlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pddl; }
	}

	public final PddlContext pddl() throws RecognitionException {
		PddlContext _localctx = new PddlContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_pddl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(72);
				domain();
				}
				break;
			case 2:
				{
				setState(73);
				problem();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DomainContext extends ParserRuleContext {
		public Token name;
		public RequireDefContext requirements;
		public TypesDefContext types;
		public ConstantsDefContext constants;
		public PredicatesDefContext predicates;
		public StructureDefContext structureDef;
		public List<StructureDefContext> operators = new ArrayList<StructureDefContext>();
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode DEFINE() { return getToken(PDDLParser.DEFINE, 0); }
		public TerminalNode DOMAIN() { return getToken(PDDLParser.DOMAIN, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public List<RequireDefContext> requireDef() {
			return getRuleContexts(RequireDefContext.class);
		}
		public RequireDefContext requireDef(int i) {
			return getRuleContext(RequireDefContext.class,i);
		}
		public List<TypesDefContext> typesDef() {
			return getRuleContexts(TypesDefContext.class);
		}
		public TypesDefContext typesDef(int i) {
			return getRuleContext(TypesDefContext.class,i);
		}
		public List<ConstantsDefContext> constantsDef() {
			return getRuleContexts(ConstantsDefContext.class);
		}
		public ConstantsDefContext constantsDef(int i) {
			return getRuleContext(ConstantsDefContext.class,i);
		}
		public List<PredicatesDefContext> predicatesDef() {
			return getRuleContexts(PredicatesDefContext.class);
		}
		public PredicatesDefContext predicatesDef(int i) {
			return getRuleContext(PredicatesDefContext.class,i);
		}
		public List<StructureDefContext> structureDef() {
			return getRuleContexts(StructureDefContext.class);
		}
		public StructureDefContext structureDef(int i) {
			return getRuleContext(StructureDefContext.class,i);
		}
		public DomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_domain; }
	}

	public final DomainContext domain() throws RecognitionException {
		DomainContext _localctx = new DomainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_domain);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(LP);
			setState(77);
			match(DEFINE);
			setState(78);
			match(LP);
			setState(79);
			match(DOMAIN);
			setState(80);
			((DomainContext)_localctx).name = match(NAME);
			setState(81);
			match(RP);
			setState(88);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(86);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						setState(82);
						((DomainContext)_localctx).requirements = requireDef();
						}
						break;
					case 2:
						{
						setState(83);
						((DomainContext)_localctx).types = typesDef();
						}
						break;
					case 3:
						{
						setState(84);
						((DomainContext)_localctx).constants = constantsDef();
						}
						break;
					case 4:
						{
						setState(85);
						((DomainContext)_localctx).predicates = predicatesDef();
						}
						break;
					}
					} 
				}
				setState(90);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LP) {
				{
				{
				setState(91);
				((DomainContext)_localctx).structureDef = structureDef();
				((DomainContext)_localctx).operators.add(((DomainContext)_localctx).structureDef);
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RequireDefContext extends ParserRuleContext {
		public Token REQUIRE_KEY;
		public List<Token> keys = new ArrayList<Token>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode REQUIREMENTS() { return getToken(PDDLParser.REQUIREMENTS, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<TerminalNode> REQUIRE_KEY() { return getTokens(PDDLParser.REQUIRE_KEY); }
		public TerminalNode REQUIRE_KEY(int i) {
			return getToken(PDDLParser.REQUIRE_KEY, i);
		}
		public RequireDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireDef; }
	}

	public final RequireDefContext requireDef() throws RecognitionException {
		RequireDefContext _localctx = new RequireDefContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_requireDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(LP);
			setState(100);
			match(REQUIREMENTS);
			setState(102); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(101);
				((RequireDefContext)_localctx).REQUIRE_KEY = match(REQUIRE_KEY);
				((RequireDefContext)_localctx).keys.add(((RequireDefContext)_localctx).REQUIRE_KEY);
				}
				}
				setState(104); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==REQUIRE_KEY );
			setState(106);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypesDefContext extends ParserRuleContext {
		public TypedListContext types;
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode TYPES() { return getToken(PDDLParser.TYPES, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public TypedListContext typedList() {
			return getRuleContext(TypedListContext.class,0);
		}
		public TypesDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typesDef; }
	}

	public final TypesDefContext typesDef() throws RecognitionException {
		TypesDefContext _localctx = new TypesDefContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_typesDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(LP);
			setState(109);
			match(TYPES);
			setState(110);
			((TypesDefContext)_localctx).types = typedList();
			setState(111);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedListContext extends ParserRuleContext {
		public Token NAME;
		public List<Token> types = new ArrayList<Token>();
		public Token supertype;
		public TerminalNode OF() { return getToken(PDDLParser.OF, 0); }
		public TypedListContext typedList() {
			return getRuleContext(TypedListContext.class,0);
		}
		public List<TerminalNode> NAME() { return getTokens(PDDLParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(PDDLParser.NAME, i);
		}
		public TypedListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedList; }
	}

	public final TypedListContext typedList() throws RecognitionException {
		TypedListContext _localctx = new TypedListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typedList);
		int _la;
		try {
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(114); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(113);
					((TypedListContext)_localctx).NAME = match(NAME);
					((TypedListContext)_localctx).types.add(((TypedListContext)_localctx).NAME);
					}
					}
					setState(116); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==NAME );
				setState(118);
				match(OF);
				setState(119);
				((TypedListContext)_localctx).supertype = match(NAME);
				setState(120);
				typedList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NAME) {
					{
					{
					setState(121);
					((TypedListContext)_localctx).NAME = match(NAME);
					((TypedListContext)_localctx).types.add(((TypedListContext)_localctx).NAME);
					}
					}
					setState(126);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantsDefContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode CONSTANTS() { return getToken(PDDLParser.CONSTANTS, 0); }
		public TypedObjListContext typedObjList() {
			return getRuleContext(TypedObjListContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public ConstantsDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantsDef; }
	}

	public final ConstantsDefContext constantsDef() throws RecognitionException {
		ConstantsDefContext _localctx = new ConstantsDefContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constantsDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(LP);
			setState(130);
			match(CONSTANTS);
			setState(131);
			typedObjList();
			setState(132);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedObjListContext extends ParserRuleContext {
		public Token NAME;
		public List<Token> names = new ArrayList<Token>();
		public Token objtype;
		public TerminalNode OF() { return getToken(PDDLParser.OF, 0); }
		public TypedObjListContext typedObjList() {
			return getRuleContext(TypedObjListContext.class,0);
		}
		public List<TerminalNode> NAME() { return getTokens(PDDLParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(PDDLParser.NAME, i);
		}
		public TypedObjListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedObjList; }
	}

	public final TypedObjListContext typedObjList() throws RecognitionException {
		TypedObjListContext _localctx = new TypedObjListContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_typedObjList);
		int _la;
		try {
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(135); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(134);
					((TypedObjListContext)_localctx).NAME = match(NAME);
					((TypedObjListContext)_localctx).names.add(((TypedObjListContext)_localctx).NAME);
					}
					}
					setState(137); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==NAME );
				setState(139);
				match(OF);
				setState(140);
				((TypedObjListContext)_localctx).objtype = match(NAME);
				setState(141);
				typedObjList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NAME) {
					{
					{
					setState(142);
					((TypedObjListContext)_localctx).NAME = match(NAME);
					((TypedObjListContext)_localctx).names.add(((TypedObjListContext)_localctx).NAME);
					}
					}
					setState(147);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredicatesDefContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode PREDICATES() { return getToken(PDDLParser.PREDICATES, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<PredicateDefContext> predicateDef() {
			return getRuleContexts(PredicateDefContext.class);
		}
		public PredicateDefContext predicateDef(int i) {
			return getRuleContext(PredicateDefContext.class,i);
		}
		public PredicatesDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicatesDef; }
	}

	public final PredicatesDefContext predicatesDef() throws RecognitionException {
		PredicatesDefContext _localctx = new PredicatesDefContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_predicatesDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(LP);
			setState(151);
			match(PREDICATES);
			setState(153); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(152);
				predicateDef();
				}
				}
				setState(155); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(157);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredicateDefContext extends ParserRuleContext {
		public NameDefContext predicate;
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public NameDefContext nameDef() {
			return getRuleContext(NameDefContext.class,0);
		}
		public PredicateDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicateDef; }
	}

	public final PredicateDefContext predicateDef() throws RecognitionException {
		PredicateDefContext _localctx = new PredicateDefContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_predicateDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(LP);
			setState(160);
			((PredicateDefContext)_localctx).predicate = nameDef();
			setState(161);
			typedVarList();
			setState(162);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedVarListContext extends ParserRuleContext {
		public Token VARIABLE;
		public List<Token> names = new ArrayList<Token>();
		public Token vartype;
		public TerminalNode OF() { return getToken(PDDLParser.OF, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public List<TerminalNode> VARIABLE() { return getTokens(PDDLParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(PDDLParser.VARIABLE, i);
		}
		public TypedVarListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedVarList; }
	}

	public final TypedVarListContext typedVarList() throws RecognitionException {
		TypedVarListContext _localctx = new TypedVarListContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_typedVarList);
		int _la;
		try {
			setState(178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(165); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(164);
					((TypedVarListContext)_localctx).VARIABLE = match(VARIABLE);
					((TypedVarListContext)_localctx).names.add(((TypedVarListContext)_localctx).VARIABLE);
					}
					}
					setState(167); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==VARIABLE );
				setState(169);
				match(OF);
				setState(170);
				((TypedVarListContext)_localctx).vartype = match(NAME);
				setState(171);
				typedVarList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==VARIABLE) {
					{
					{
					setState(172);
					((TypedVarListContext)_localctx).VARIABLE = match(VARIABLE);
					((TypedVarListContext)_localctx).names.add(((TypedVarListContext)_localctx).VARIABLE);
					}
					}
					setState(177);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructureDefContext extends ParserRuleContext {
		public ActionDefContext actionDef() {
			return getRuleContext(ActionDefContext.class,0);
		}
		public TaskDefContext taskDef() {
			return getRuleContext(TaskDefContext.class,0);
		}
		public MethodDefContext methodDef() {
			return getRuleContext(MethodDefContext.class,0);
		}
		public StructureDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structureDef; }
	}

	public final StructureDefContext structureDef() throws RecognitionException {
		StructureDefContext _localctx = new StructureDefContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_structureDef);
		try {
			setState(183);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(180);
				actionDef();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				taskDef();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(182);
				methodDef();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ActionDefContext extends ParserRuleContext {
		public Token name;
		public TypedVarListContext parameters;
		public GoalDefContext precondition;
		public EffectDefContext effect;
		public ObserveDefContext observe;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode ACTION() { return getToken(PDDLParser.ACTION, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public TerminalNode PARAMETERS() { return getToken(PDDLParser.PARAMETERS, 0); }
		public TerminalNode PRECONDITION() { return getToken(PDDLParser.PRECONDITION, 0); }
		public TerminalNode EFFECT() { return getToken(PDDLParser.EFFECT, 0); }
		public TerminalNode OBSERVE() { return getToken(PDDLParser.OBSERVE, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public GoalDefContext goalDef() {
			return getRuleContext(GoalDefContext.class,0);
		}
		public EffectDefContext effectDef() {
			return getRuleContext(EffectDefContext.class,0);
		}
		public ObserveDefContext observeDef() {
			return getRuleContext(ObserveDefContext.class,0);
		}
		public ActionDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actionDef; }
	}

	public final ActionDefContext actionDef() throws RecognitionException {
		ActionDefContext _localctx = new ActionDefContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_actionDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(LP);
			setState(186);
			match(ACTION);
			setState(187);
			((ActionDefContext)_localctx).name = match(NAME);
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETERS) {
				{
				setState(188);
				match(PARAMETERS);
				setState(189);
				match(LP);
				setState(190);
				((ActionDefContext)_localctx).parameters = typedVarList();
				setState(191);
				match(RP);
				}
			}

			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRECONDITION) {
				{
				setState(195);
				match(PRECONDITION);
				setState(196);
				((ActionDefContext)_localctx).precondition = goalDef();
				}
			}

			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EFFECT) {
				{
				setState(199);
				match(EFFECT);
				setState(200);
				((ActionDefContext)_localctx).effect = effectDef();
				}
			}

			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OBSERVE) {
				{
				setState(203);
				match(OBSERVE);
				setState(204);
				((ActionDefContext)_localctx).observe = observeDef();
				}
			}

			setState(207);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GoalDefContext extends ParserRuleContext {
		public TypedVarListContext variables;
		public GoalDefContext gd;
		public GoalDefContext goalDef;
		public List<GoalDefContext> ands = new ArrayList<GoalDefContext>();
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode FORALL() { return getToken(PDDLParser.FORALL, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public List<GoalDefContext> goalDef() {
			return getRuleContexts(GoalDefContext.class);
		}
		public GoalDefContext goalDef(int i) {
			return getRuleContext(GoalDefContext.class,i);
		}
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public GoalDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_goalDef; }
	}

	public final GoalDefContext goalDef() throws RecognitionException {
		GoalDefContext _localctx = new GoalDefContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_goalDef);
		int _la;
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(LP);
				setState(210);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
				atomicFormula();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(212);
				literal();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(213);
				match(LP);
				setState(214);
				match(FORALL);
				setState(215);
				match(LP);
				setState(216);
				((GoalDefContext)_localctx).variables = typedVarList();
				setState(217);
				match(RP);
				setState(218);
				((GoalDefContext)_localctx).gd = goalDef();
				setState(219);
				match(RP);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(221);
				match(LP);
				setState(222);
				match(AND);
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(223);
					((GoalDefContext)_localctx).goalDef = goalDef();
					((GoalDefContext)_localctx).ands.add(((GoalDefContext)_localctx).goalDef);
					}
					}
					setState(228);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(229);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EffectDefContext extends ParserRuleContext {
		public CEffectContext cEffect;
		public List<CEffectContext> ands = new ArrayList<CEffectContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public List<CEffectContext> cEffect() {
			return getRuleContexts(CEffectContext.class);
		}
		public CEffectContext cEffect(int i) {
			return getRuleContext(CEffectContext.class,i);
		}
		public EffectDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effectDef; }
	}

	public final EffectDefContext effectDef() throws RecognitionException {
		EffectDefContext _localctx = new EffectDefContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_effectDef);
		int _la;
		try {
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(LP);
				setState(233);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
				match(LP);
				setState(235);
				match(AND);
				setState(239);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(236);
					((EffectDefContext)_localctx).cEffect = cEffect();
					((EffectDefContext)_localctx).ands.add(((EffectDefContext)_localctx).cEffect);
					}
					}
					setState(241);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(242);
				match(RP);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(243);
				cEffect();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CEffectContext extends ParserRuleContext {
		public Token VARIABLE;
		public List<Token> variables = new ArrayList<Token>();
		public GoalDefContext when;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode FORALL() { return getToken(PDDLParser.FORALL, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public EffectDefContext effectDef() {
			return getRuleContext(EffectDefContext.class,0);
		}
		public List<TerminalNode> VARIABLE() { return getTokens(PDDLParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(PDDLParser.VARIABLE, i);
		}
		public TerminalNode WHEN() { return getToken(PDDLParser.WHEN, 0); }
		public CondEffectContext condEffect() {
			return getRuleContext(CondEffectContext.class,0);
		}
		public GoalDefContext goalDef() {
			return getRuleContext(GoalDefContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public CEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cEffect; }
	}

	public final CEffectContext cEffect() throws RecognitionException {
		CEffectContext _localctx = new CEffectContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_cEffect);
		int _la;
		try {
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				match(LP);
				setState(247);
				match(FORALL);
				setState(248);
				match(LP);
				setState(252);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==VARIABLE) {
					{
					{
					setState(249);
					((CEffectContext)_localctx).VARIABLE = match(VARIABLE);
					((CEffectContext)_localctx).variables.add(((CEffectContext)_localctx).VARIABLE);
					}
					}
					setState(254);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(255);
				match(RP);
				setState(256);
				effectDef();
				setState(257);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(259);
				match(LP);
				setState(260);
				match(WHEN);
				setState(261);
				((CEffectContext)_localctx).when = goalDef();
				setState(262);
				condEffect();
				setState(263);
				match(RP);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(265);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondEffectContext extends ParserRuleContext {
		public LiteralContext literal;
		public List<LiteralContext> ands = new ArrayList<LiteralContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public CondEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condEffect; }
	}

	public final CondEffectContext condEffect() throws RecognitionException {
		CondEffectContext _localctx = new CondEffectContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_condEffect);
		int _la;
		try {
			setState(278);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(268);
				match(LP);
				setState(269);
				match(AND);
				setState(273);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(270);
					((CondEffectContext)_localctx).literal = literal();
					((CondEffectContext)_localctx).ands.add(((CondEffectContext)_localctx).literal);
					}
					}
					setState(275);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(276);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(277);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObserveDefContext extends ParserRuleContext {
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public ObserveDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_observeDef; }
	}

	public final ObserveDefContext observeDef() throws RecognitionException {
		ObserveDefContext _localctx = new ObserveDefContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_observeDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			atomicFormula();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode NOT() { return getToken(PDDLParser.NOT, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_literal);
		try {
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				atomicFormula();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				match(LP);
				setState(284);
				match(NOT);
				setState(285);
				atomicFormula();
				setState(286);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomicFormulaContext extends ParserRuleContext {
		public NameDefContext predicate;
		public TermContext term;
		public List<TermContext> arguments = new ArrayList<TermContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public NameDefContext nameDef() {
			return getRuleContext(NameDefContext.class,0);
		}
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public AtomicFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomicFormula; }
	}

	public final AtomicFormulaContext atomicFormula() throws RecognitionException {
		AtomicFormulaContext _localctx = new AtomicFormulaContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_atomicFormula);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(LP);
			setState(291);
			((AtomicFormulaContext)_localctx).predicate = nameDef();
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME || _la==VARIABLE) {
				{
				{
				setState(292);
				((AtomicFormulaContext)_localctx).term = term();
				((AtomicFormulaContext)_localctx).arguments.add(((AtomicFormulaContext)_localctx).term);
				}
				}
				setState(297);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(298);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public Token name;
		public Token variable;
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public TerminalNode VARIABLE() { return getToken(PDDLParser.VARIABLE, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_term);
		try {
			setState(302);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				((TermContext)_localctx).name = match(NAME);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(301);
				((TermContext)_localctx).variable = match(VARIABLE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TaskDefContext extends ParserRuleContext {
		public Token name;
		public TypedVarListContext parameters;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode TASK() { return getToken(PDDLParser.TASK, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public TerminalNode PARAMETERS() { return getToken(PDDLParser.PARAMETERS, 0); }
		public TerminalNode PRECONDITION() { return getToken(PDDLParser.PRECONDITION, 0); }
		public TerminalNode EFFECT() { return getToken(PDDLParser.EFFECT, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public TaskDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_taskDef; }
	}

	public final TaskDefContext taskDef() throws RecognitionException {
		TaskDefContext _localctx = new TaskDefContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_taskDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			match(LP);
			setState(305);
			match(TASK);
			setState(306);
			((TaskDefContext)_localctx).name = match(NAME);
			setState(312);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETERS) {
				{
				setState(307);
				match(PARAMETERS);
				setState(308);
				match(LP);
				setState(309);
				((TaskDefContext)_localctx).parameters = typedVarList();
				setState(310);
				match(RP);
				}
			}

			setState(317);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRECONDITION) {
				{
				setState(314);
				match(PRECONDITION);
				setState(315);
				match(LP);
				setState(316);
				match(RP);
				}
			}

			setState(322);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EFFECT) {
				{
				setState(319);
				match(EFFECT);
				setState(320);
				match(LP);
				setState(321);
				match(RP);
				}
			}

			setState(324);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodDefContext extends ParserRuleContext {
		public Token name;
		public TypedVarListContext parameters;
		public AtomicFormulaContext task;
		public GoalDefContext precondition;
		public TaskNetworkDefContext tn;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode METHOD() { return getToken(PDDLParser.METHOD, 0); }
		public TerminalNode TASK() { return getToken(PDDLParser.TASK, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public TerminalNode PARAMETERS() { return getToken(PDDLParser.PARAMETERS, 0); }
		public TerminalNode PRECONDITION() { return getToken(PDDLParser.PRECONDITION, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public GoalDefContext goalDef() {
			return getRuleContext(GoalDefContext.class,0);
		}
		public TaskNetworkDefContext taskNetworkDef() {
			return getRuleContext(TaskNetworkDefContext.class,0);
		}
		public MethodDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDef; }
	}

	public final MethodDefContext methodDef() throws RecognitionException {
		MethodDefContext _localctx = new MethodDefContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_methodDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(LP);
			setState(327);
			match(METHOD);
			setState(328);
			((MethodDefContext)_localctx).name = match(NAME);
			setState(334);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETERS) {
				{
				setState(329);
				match(PARAMETERS);
				setState(330);
				match(LP);
				setState(331);
				((MethodDefContext)_localctx).parameters = typedVarList();
				setState(332);
				match(RP);
				}
			}

			setState(336);
			match(TASK);
			setState(337);
			((MethodDefContext)_localctx).task = atomicFormula();
			setState(340);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRECONDITION) {
				{
				setState(338);
				match(PRECONDITION);
				setState(339);
				((MethodDefContext)_localctx).precondition = goalDef();
				}
			}

			setState(343);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ORDERED || _la==SUBTASKS) {
				{
				setState(342);
				((MethodDefContext)_localctx).tn = taskNetworkDef();
				}
			}

			setState(345);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TaskNetworkDefContext extends ParserRuleContext {
		public SubtasksDefContext subtasks;
		public ConstraintDefsContext constraints;
		public TerminalNode ORDERED() { return getToken(PDDLParser.ORDERED, 0); }
		public SubtasksDefContext subtasksDef() {
			return getRuleContext(SubtasksDefContext.class,0);
		}
		public TerminalNode CONSTRAINTS() { return getToken(PDDLParser.CONSTRAINTS, 0); }
		public ConstraintDefsContext constraintDefs() {
			return getRuleContext(ConstraintDefsContext.class,0);
		}
		public TerminalNode SUBTASKS() { return getToken(PDDLParser.SUBTASKS, 0); }
		public TerminalNode ORDERING() { return getToken(PDDLParser.ORDERING, 0); }
		public OrderingDefsContext orderingDefs() {
			return getRuleContext(OrderingDefsContext.class,0);
		}
		public TaskNetworkDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_taskNetworkDef; }
	}

	public final TaskNetworkDefContext taskNetworkDef() throws RecognitionException {
		TaskNetworkDefContext _localctx = new TaskNetworkDefContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_taskNetworkDef);
		int _la;
		try {
			setState(363);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ORDERED:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(ORDERED);
				setState(348);
				((TaskNetworkDefContext)_localctx).subtasks = subtasksDef();
				setState(351);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==CONSTRAINTS) {
					{
					setState(349);
					match(CONSTRAINTS);
					setState(350);
					((TaskNetworkDefContext)_localctx).constraints = constraintDefs();
					}
				}

				}
				break;
			case SUBTASKS:
				enterOuterAlt(_localctx, 2);
				{
				setState(353);
				match(SUBTASKS);
				setState(354);
				((TaskNetworkDefContext)_localctx).subtasks = subtasksDef();
				setState(357);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ORDERING) {
					{
					setState(355);
					match(ORDERING);
					setState(356);
					orderingDefs();
					}
				}

				setState(361);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==CONSTRAINTS) {
					{
					setState(359);
					match(CONSTRAINTS);
					setState(360);
					((TaskNetworkDefContext)_localctx).constraints = constraintDefs();
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubtasksDefContext extends ParserRuleContext {
		public SubtaskDefContext subtaskDef;
		public List<SubtaskDefContext> tasks = new ArrayList<SubtaskDefContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<SubtaskDefContext> subtaskDef() {
			return getRuleContexts(SubtaskDefContext.class);
		}
		public SubtaskDefContext subtaskDef(int i) {
			return getRuleContext(SubtaskDefContext.class,i);
		}
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public SubtasksDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtasksDef; }
	}

	public final SubtasksDefContext subtasksDef() throws RecognitionException {
		SubtasksDefContext _localctx = new SubtasksDefContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_subtasksDef);
		int _la;
		try {
			setState(377);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(365);
				match(LP);
				setState(366);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(367);
				((SubtasksDefContext)_localctx).subtaskDef = subtaskDef();
				((SubtasksDefContext)_localctx).tasks.add(((SubtasksDefContext)_localctx).subtaskDef);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(368);
				match(LP);
				setState(369);
				match(AND);
				setState(373);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(370);
					((SubtasksDefContext)_localctx).subtaskDef = subtaskDef();
					((SubtasksDefContext)_localctx).tasks.add(((SubtasksDefContext)_localctx).subtaskDef);
					}
					}
					setState(375);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(376);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubtaskDefContext extends ParserRuleContext {
		public Token taskId;
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public SubtaskDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtaskDef; }
	}

	public final SubtaskDefContext subtaskDef() throws RecognitionException {
		SubtaskDefContext _localctx = new SubtaskDefContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_subtaskDef);
		try {
			setState(385);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(379);
				match(LP);
				setState(380);
				((SubtaskDefContext)_localctx).taskId = match(NAME);
				setState(381);
				atomicFormula();
				setState(382);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(384);
				atomicFormula();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OrderingDefsContext extends ParserRuleContext {
		public OrderingDefContext orderingDef;
		public List<OrderingDefContext> order = new ArrayList<OrderingDefContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<OrderingDefContext> orderingDef() {
			return getRuleContexts(OrderingDefContext.class);
		}
		public OrderingDefContext orderingDef(int i) {
			return getRuleContext(OrderingDefContext.class,i);
		}
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public OrderingDefsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orderingDefs; }
	}

	public final OrderingDefsContext orderingDefs() throws RecognitionException {
		OrderingDefsContext _localctx = new OrderingDefsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_orderingDefs);
		int _la;
		try {
			setState(399);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(387);
				match(LP);
				setState(388);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				((OrderingDefsContext)_localctx).orderingDef = orderingDef();
				((OrderingDefsContext)_localctx).order.add(((OrderingDefsContext)_localctx).orderingDef);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(390);
				match(LP);
				setState(391);
				match(AND);
				setState(393); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(392);
					((OrderingDefsContext)_localctx).orderingDef = orderingDef();
					((OrderingDefsContext)_localctx).order.add(((OrderingDefsContext)_localctx).orderingDef);
					}
					}
					setState(395); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LP );
				setState(397);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OrderingDefContext extends ParserRuleContext {
		public Token head;
		public Token NAME;
		public List<Token> tail = new ArrayList<Token>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode BEFORE() { return getToken(PDDLParser.BEFORE, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public List<TerminalNode> NAME() { return getTokens(PDDLParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(PDDLParser.NAME, i);
		}
		public OrderingDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orderingDef; }
	}

	public final OrderingDefContext orderingDef() throws RecognitionException {
		OrderingDefContext _localctx = new OrderingDefContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_orderingDef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(LP);
			setState(402);
			match(BEFORE);
			setState(403);
			((OrderingDefContext)_localctx).head = match(NAME);
			setState(404);
			((OrderingDefContext)_localctx).NAME = match(NAME);
			((OrderingDefContext)_localctx).tail.add(((OrderingDefContext)_localctx).NAME);
			setState(405);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstraintDefsContext extends ParserRuleContext {
		public List<ConstraintDefContext> constraintDef() {
			return getRuleContexts(ConstraintDefContext.class);
		}
		public ConstraintDefContext constraintDef(int i) {
			return getRuleContext(ConstraintDefContext.class,i);
		}
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public ConstraintDefsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraintDefs; }
	}

	public final ConstraintDefsContext constraintDefs() throws RecognitionException {
		ConstraintDefsContext _localctx = new ConstraintDefsContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_constraintDefs);
		int _la;
		try {
			setState(417);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(407);
				constraintDef();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(408);
				match(LP);
				setState(409);
				match(AND);
				setState(411); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(410);
					constraintDef();
					}
					}
					setState(413); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LP );
				setState(415);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstraintDefContext extends ParserRuleContext {
		public Token left;
		public Token right;
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public TerminalNode NOT() { return getToken(PDDLParser.NOT, 0); }
		public ConstraintDefContext constraintDef() {
			return getRuleContext(ConstraintDefContext.class,0);
		}
		public TerminalNode EQUALS() { return getToken(PDDLParser.EQUALS, 0); }
		public List<TerminalNode> VARIABLE() { return getTokens(PDDLParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(PDDLParser.VARIABLE, i);
		}
		public ConstraintDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraintDef; }
	}

	public final ConstraintDefContext constraintDef() throws RecognitionException {
		ConstraintDefContext _localctx = new ConstraintDefContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_constraintDef);
		try {
			setState(431);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(419);
				match(LP);
				setState(420);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(421);
				match(LP);
				setState(422);
				match(NOT);
				setState(423);
				constraintDef();
				setState(424);
				match(RP);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(426);
				match(LP);
				setState(427);
				match(EQUALS);
				setState(428);
				((ConstraintDefContext)_localctx).left = match(VARIABLE);
				setState(429);
				((ConstraintDefContext)_localctx).right = match(VARIABLE);
				setState(430);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProblemContext extends ParserRuleContext {
		public Token pname;
		public Token dname;
		public RequireDefContext requirements;
		public ObjectDeclarationContext objects;
		public HtnDefContext htn;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode DEFINE() { return getToken(PDDLParser.DEFINE, 0); }
		public TerminalNode PROBLEM() { return getToken(PDDLParser.PROBLEM, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode DDOMAIN() { return getToken(PDDLParser.DDOMAIN, 0); }
		public InitContext init() {
			return getRuleContext(InitContext.class,0);
		}
		public List<TerminalNode> NAME() { return getTokens(PDDLParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(PDDLParser.NAME, i);
		}
		public GoalContext goal() {
			return getRuleContext(GoalContext.class,0);
		}
		public RequireDefContext requireDef() {
			return getRuleContext(RequireDefContext.class,0);
		}
		public ObjectDeclarationContext objectDeclaration() {
			return getRuleContext(ObjectDeclarationContext.class,0);
		}
		public HtnDefContext htnDef() {
			return getRuleContext(HtnDefContext.class,0);
		}
		public ProblemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_problem; }
	}

	public final ProblemContext problem() throws RecognitionException {
		ProblemContext _localctx = new ProblemContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_problem);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(433);
			match(LP);
			setState(434);
			match(DEFINE);
			setState(435);
			match(LP);
			setState(436);
			match(PROBLEM);
			setState(437);
			((ProblemContext)_localctx).pname = match(NAME);
			setState(438);
			match(RP);
			setState(439);
			match(LP);
			setState(440);
			match(DDOMAIN);
			setState(441);
			((ProblemContext)_localctx).dname = match(NAME);
			setState(442);
			match(RP);
			setState(444);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				{
				setState(443);
				((ProblemContext)_localctx).requirements = requireDef();
				}
				break;
			}
			setState(447);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				{
				setState(446);
				((ProblemContext)_localctx).objects = objectDeclaration();
				}
				break;
			}
			setState(450);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				{
				setState(449);
				((ProblemContext)_localctx).htn = htnDef();
				}
				break;
			}
			setState(452);
			init();
			setState(454);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LP) {
				{
				setState(453);
				goal();
				}
			}

			setState(456);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjectDeclarationContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode OBJECTS() { return getToken(PDDLParser.OBJECTS, 0); }
		public TypedObjListContext typedObjList() {
			return getRuleContext(TypedObjListContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public ObjectDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectDeclaration; }
	}

	public final ObjectDeclarationContext objectDeclaration() throws RecognitionException {
		ObjectDeclarationContext _localctx = new ObjectDeclarationContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_objectDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(458);
			match(LP);
			setState(459);
			match(OBJECTS);
			setState(460);
			typedObjList();
			setState(461);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitContext extends ParserRuleContext {
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode INIT() { return getToken(PDDLParser.INIT, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TerminalNode AND() { return getToken(PDDLParser.AND, 0); }
		public List<InitElContext> initEl() {
			return getRuleContexts(InitElContext.class);
		}
		public InitElContext initEl(int i) {
			return getRuleContext(InitElContext.class,i);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(463);
			match(LP);
			setState(464);
			match(INIT);
			setState(480);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				{
				setState(468);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(465);
					initEl();
					}
					}
					setState(470);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				{
				setState(471);
				match(LP);
				setState(472);
				match(AND);
				setState(476);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LP) {
					{
					{
					setState(473);
					initEl();
					}
					}
					setState(478);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(479);
				match(RP);
				}
				break;
			}
			setState(482);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitElContext extends ParserRuleContext {
		public LiteralContext literal;
		public List<LiteralContext> choices = new ArrayList<LiteralContext>();
		public List<LiteralContext> xchoices = new ArrayList<LiteralContext>();
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode UNKNOWN() { return getToken(PDDLParser.UNKNOWN, 0); }
		public AtomicFormulaContext atomicFormula() {
			return getRuleContext(AtomicFormulaContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public TerminalNode OR() { return getToken(PDDLParser.OR, 0); }
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public TerminalNode ONEOF() { return getToken(PDDLParser.ONEOF, 0); }
		public InitElContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initEl; }
	}

	public final InitElContext initEl() throws RecognitionException {
		InitElContext _localctx = new InitElContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_initEl);
		int _la;
		try {
			setState(508);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,58,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(484);
				match(LP);
				setState(485);
				match(UNKNOWN);
				setState(486);
				atomicFormula();
				setState(487);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(489);
				match(LP);
				setState(490);
				match(OR);
				setState(492); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(491);
					((InitElContext)_localctx).literal = literal();
					((InitElContext)_localctx).choices.add(((InitElContext)_localctx).literal);
					}
					}
					setState(494); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LP );
				setState(496);
				match(RP);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(498);
				match(LP);
				setState(499);
				match(ONEOF);
				setState(501); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(500);
					((InitElContext)_localctx).literal = literal();
					((InitElContext)_localctx).xchoices.add(((InitElContext)_localctx).literal);
					}
					}
					setState(503); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LP );
				setState(505);
				match(RP);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(507);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GoalContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(PDDLParser.LP, 0); }
		public TerminalNode GOAL() { return getToken(PDDLParser.GOAL, 0); }
		public GoalDefContext goalDef() {
			return getRuleContext(GoalDefContext.class,0);
		}
		public TerminalNode RP() { return getToken(PDDLParser.RP, 0); }
		public GoalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_goal; }
	}

	public final GoalContext goal() throws RecognitionException {
		GoalContext _localctx = new GoalContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_goal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(510);
			match(LP);
			setState(511);
			match(GOAL);
			setState(512);
			goalDef();
			setState(513);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class HtnDefContext extends ParserRuleContext {
		public TypedVarListContext parameters;
		public TaskNetworkDefContext tn;
		public List<TerminalNode> LP() { return getTokens(PDDLParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(PDDLParser.LP, i);
		}
		public TerminalNode HTN() { return getToken(PDDLParser.HTN, 0); }
		public List<TerminalNode> RP() { return getTokens(PDDLParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(PDDLParser.RP, i);
		}
		public TaskNetworkDefContext taskNetworkDef() {
			return getRuleContext(TaskNetworkDefContext.class,0);
		}
		public TerminalNode PARAMETERS() { return getToken(PDDLParser.PARAMETERS, 0); }
		public TypedVarListContext typedVarList() {
			return getRuleContext(TypedVarListContext.class,0);
		}
		public HtnDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_htnDef; }
	}

	public final HtnDefContext htnDef() throws RecognitionException {
		HtnDefContext _localctx = new HtnDefContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_htnDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(515);
			match(LP);
			setState(516);
			match(HTN);
			setState(522);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETERS) {
				{
				setState(517);
				match(PARAMETERS);
				setState(518);
				match(LP);
				setState(519);
				((HtnDefContext)_localctx).parameters = typedVarList();
				setState(520);
				match(RP);
				}
			}

			setState(524);
			((HtnDefContext)_localctx).tn = taskNetworkDef();
			setState(525);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameDefContext extends ParserRuleContext {
		public Token name;
		public TerminalNode EQUALS() { return getToken(PDDLParser.EQUALS, 0); }
		public TerminalNode NAME() { return getToken(PDDLParser.NAME, 0); }
		public NameDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nameDef; }
	}

	public final NameDefContext nameDef() throws RecognitionException {
		NameDefContext _localctx = new NameDefContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_nameDef);
		try {
			setState(529);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUALS:
				enterOuterAlt(_localctx, 1);
				{
				setState(527);
				match(EQUALS);
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(528);
				((NameDefContext)_localctx).name = match(NAME);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u0216\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3\2\5\2M\n\2\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\7\3Y\n\3\f\3\16\3\\\13\3\3\3\7\3_\n\3\f\3\16\3b\13\3"+
		"\3\3\3\3\3\4\3\4\3\4\6\4i\n\4\r\4\16\4j\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\6\6\6u\n\6\r\6\16\6v\3\6\3\6\3\6\3\6\7\6}\n\6\f\6\16\6\u0080\13\6\5\6"+
		"\u0082\n\6\3\7\3\7\3\7\3\7\3\7\3\b\6\b\u008a\n\b\r\b\16\b\u008b\3\b\3"+
		"\b\3\b\3\b\7\b\u0092\n\b\f\b\16\b\u0095\13\b\5\b\u0097\n\b\3\t\3\t\3\t"+
		"\6\t\u009c\n\t\r\t\16\t\u009d\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\6\13\u00a8"+
		"\n\13\r\13\16\13\u00a9\3\13\3\13\3\13\3\13\7\13\u00b0\n\13\f\13\16\13"+
		"\u00b3\13\13\5\13\u00b5\n\13\3\f\3\f\3\f\5\f\u00ba\n\f\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\5\r\u00c4\n\r\3\r\3\r\5\r\u00c8\n\r\3\r\3\r\5\r\u00cc"+
		"\n\r\3\r\3\r\5\r\u00d0\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00e3\n\16\f\16\16\16\u00e6"+
		"\13\16\3\16\5\16\u00e9\n\16\3\17\3\17\3\17\3\17\3\17\7\17\u00f0\n\17\f"+
		"\17\16\17\u00f3\13\17\3\17\3\17\5\17\u00f7\n\17\3\20\3\20\3\20\3\20\7"+
		"\20\u00fd\n\20\f\20\16\20\u0100\13\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\5\20\u010d\n\20\3\21\3\21\3\21\7\21\u0112\n\21"+
		"\f\21\16\21\u0115\13\21\3\21\3\21\5\21\u0119\n\21\3\22\3\22\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\5\23\u0123\n\23\3\24\3\24\3\24\7\24\u0128\n\24\f"+
		"\24\16\24\u012b\13\24\3\24\3\24\3\25\3\25\5\25\u0131\n\25\3\26\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\3\26\5\26\u013b\n\26\3\26\3\26\3\26\5\26\u0140"+
		"\n\26\3\26\3\26\3\26\5\26\u0145\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\5\27\u0151\n\27\3\27\3\27\3\27\3\27\5\27\u0157\n\27\3"+
		"\27\5\27\u015a\n\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0162\n\30\3\30"+
		"\3\30\3\30\3\30\5\30\u0168\n\30\3\30\3\30\5\30\u016c\n\30\5\30\u016e\n"+
		"\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0176\n\31\f\31\16\31\u0179\13"+
		"\31\3\31\5\31\u017c\n\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0184\n\32"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\6\33\u018c\n\33\r\33\16\33\u018d\3\33\3"+
		"\33\5\33\u0192\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35"+
		"\6\35\u019e\n\35\r\35\16\35\u019f\3\35\3\35\5\35\u01a4\n\35\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01b2\n\36\3\37"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01bf\n\37\3\37"+
		"\5\37\u01c2\n\37\3\37\5\37\u01c5\n\37\3\37\3\37\5\37\u01c9\n\37\3\37\3"+
		"\37\3 \3 \3 \3 \3 \3!\3!\3!\7!\u01d5\n!\f!\16!\u01d8\13!\3!\3!\3!\7!\u01dd"+
		"\n!\f!\16!\u01e0\13!\3!\5!\u01e3\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\6\"\u01ef\n\"\r\"\16\"\u01f0\3\"\3\"\3\"\3\"\3\"\6\"\u01f8\n\"\r"+
		"\"\16\"\u01f9\3\"\3\"\3\"\5\"\u01ff\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$"+
		"\3$\3$\5$\u020d\n$\3$\3$\3$\3%\3%\5%\u0214\n%\3%\2\2&\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\2\2\u023b\2L\3\2"+
		"\2\2\4N\3\2\2\2\6e\3\2\2\2\bn\3\2\2\2\n\u0081\3\2\2\2\f\u0083\3\2\2\2"+
		"\16\u0096\3\2\2\2\20\u0098\3\2\2\2\22\u00a1\3\2\2\2\24\u00b4\3\2\2\2\26"+
		"\u00b9\3\2\2\2\30\u00bb\3\2\2\2\32\u00e8\3\2\2\2\34\u00f6\3\2\2\2\36\u010c"+
		"\3\2\2\2 \u0118\3\2\2\2\"\u011a\3\2\2\2$\u0122\3\2\2\2&\u0124\3\2\2\2"+
		"(\u0130\3\2\2\2*\u0132\3\2\2\2,\u0148\3\2\2\2.\u016d\3\2\2\2\60\u017b"+
		"\3\2\2\2\62\u0183\3\2\2\2\64\u0191\3\2\2\2\66\u0193\3\2\2\28\u01a3\3\2"+
		"\2\2:\u01b1\3\2\2\2<\u01b3\3\2\2\2>\u01cc\3\2\2\2@\u01d1\3\2\2\2B\u01fe"+
		"\3\2\2\2D\u0200\3\2\2\2F\u0205\3\2\2\2H\u0213\3\2\2\2JM\5\4\3\2KM\5<\37"+
		"\2LJ\3\2\2\2LK\3\2\2\2M\3\3\2\2\2NO\7\3\2\2OP\7\7\2\2PQ\7\3\2\2QR\7\b"+
		"\2\2RS\7(\2\2SZ\7\4\2\2TY\5\6\4\2UY\5\b\5\2VY\5\f\7\2WY\5\20\t\2XT\3\2"+
		"\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[`\3"+
		"\2\2\2\\Z\3\2\2\2]_\5\26\f\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a"+
		"c\3\2\2\2b`\3\2\2\2cd\7\4\2\2d\5\3\2\2\2ef\7\3\2\2fh\7\13\2\2gi\7\'\2"+
		"\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7\4\2\2m\7\3\2"+
		"\2\2no\7\3\2\2op\7\f\2\2pq\5\n\6\2qr\7\4\2\2r\t\3\2\2\2su\7(\2\2ts\3\2"+
		"\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7\5\2\2yz\7(\2\2z\u0082"+
		"\5\n\6\2{}\7(\2\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177"+
		"\u0082\3\2\2\2\u0080~\3\2\2\2\u0081t\3\2\2\2\u0081~\3\2\2\2\u0082\13\3"+
		"\2\2\2\u0083\u0084\7\3\2\2\u0084\u0085\7\r\2\2\u0085\u0086\5\16\b\2\u0086"+
		"\u0087\7\4\2\2\u0087\r\3\2\2\2\u0088\u008a\7(\2\2\u0089\u0088\3\2\2\2"+
		"\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d"+
		"\3\2\2\2\u008d\u008e\7\5\2\2\u008e\u008f\7(\2\2\u008f\u0097\5\16\b\2\u0090"+
		"\u0092\7(\2\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2"+
		"\2\2\u0093\u0094\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0096"+
		"\u0089\3\2\2\2\u0096\u0093\3\2\2\2\u0097\17\3\2\2\2\u0098\u0099\7\3\2"+
		"\2\u0099\u009b\7\16\2\2\u009a\u009c\5\22\n\2\u009b\u009a\3\2\2\2\u009c"+
		"\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2"+
		"\2\2\u009f\u00a0\7\4\2\2\u00a0\21\3\2\2\2\u00a1\u00a2\7\3\2\2\u00a2\u00a3"+
		"\5H%\2\u00a3\u00a4\5\24\13\2\u00a4\u00a5\7\4\2\2\u00a5\23\3\2\2\2\u00a6"+
		"\u00a8\7)\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2"+
		"\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7\5\2\2\u00ac"+
		"\u00ad\7(\2\2\u00ad\u00b5\5\24\13\2\u00ae\u00b0\7)\2\2\u00af\u00ae\3\2"+
		"\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2"+
		"\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00a7\3\2\2\2\u00b4\u00b1\3\2"+
		"\2\2\u00b5\25\3\2\2\2\u00b6\u00ba\5\30\r\2\u00b7\u00ba\5*\26\2\u00b8\u00ba"+
		"\5,\27\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba"+
		"\27\3\2\2\2\u00bb\u00bc\7\3\2\2\u00bc\u00bd\7\22\2\2\u00bd\u00c3\7(\2"+
		"\2\u00be\u00bf\7\23\2\2\u00bf\u00c0\7\3\2\2\u00c0\u00c1\5\24\13\2\u00c1"+
		"\u00c2\7\4\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00be\3\2\2\2\u00c3\u00c4\3\2"+
		"\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c6\7\24\2\2\u00c6\u00c8\5\32\16\2\u00c7"+
		"\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00ca\7\25"+
		"\2\2\u00ca\u00cc\5\34\17\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc"+
		"\u00cf\3\2\2\2\u00cd\u00ce\7\26\2\2\u00ce\u00d0\5\"\22\2\u00cf\u00cd\3"+
		"\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\7\4\2\2\u00d2"+
		"\31\3\2\2\2\u00d3\u00d4\7\3\2\2\u00d4\u00e9\7\4\2\2\u00d5\u00e9\5&\24"+
		"\2\u00d6\u00e9\5$\23\2\u00d7\u00d8\7\3\2\2\u00d8\u00d9\7!\2\2\u00d9\u00da"+
		"\7\3\2\2\u00da\u00db\5\24\13\2\u00db\u00dc\7\4\2\2\u00dc\u00dd\5\32\16"+
		"\2\u00dd\u00de\7\4\2\2\u00de\u00e9\3\2\2\2\u00df\u00e0\7\3\2\2\u00e0\u00e4"+
		"\7 \2\2\u00e1\u00e3\5\32\16\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2"+
		"\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4"+
		"\3\2\2\2\u00e7\u00e9\7\4\2\2\u00e8\u00d3\3\2\2\2\u00e8\u00d5\3\2\2\2\u00e8"+
		"\u00d6\3\2\2\2\u00e8\u00d7\3\2\2\2\u00e8\u00df\3\2\2\2\u00e9\33\3\2\2"+
		"\2\u00ea\u00eb\7\3\2\2\u00eb\u00f7\7\4\2\2\u00ec\u00ed\7\3\2\2\u00ed\u00f1"+
		"\7 \2\2\u00ee\u00f0\5\36\20\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2"+
		"\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1"+
		"\3\2\2\2\u00f4\u00f7\7\4\2\2\u00f5\u00f7\5\36\20\2\u00f6\u00ea\3\2\2\2"+
		"\u00f6\u00ec\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\35\3\2\2\2\u00f8\u00f9"+
		"\7\3\2\2\u00f9\u00fa\7!\2\2\u00fa\u00fe\7\3\2\2\u00fb\u00fd\7)\2\2\u00fc"+
		"\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2"+
		"\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7\4\2\2\u0102"+
		"\u0103\5\34\17\2\u0103\u0104\7\4\2\2\u0104\u010d\3\2\2\2\u0105\u0106\7"+
		"\3\2\2\u0106\u0107\7\"\2\2\u0107\u0108\5\32\16\2\u0108\u0109\5 \21\2\u0109"+
		"\u010a\7\4\2\2\u010a\u010d\3\2\2\2\u010b\u010d\5$\23\2\u010c\u00f8\3\2"+
		"\2\2\u010c\u0105\3\2\2\2\u010c\u010b\3\2\2\2\u010d\37\3\2\2\2\u010e\u010f"+
		"\7\3\2\2\u010f\u0113\7 \2\2\u0110\u0112\5$\23\2\u0111\u0110\3\2\2\2\u0112"+
		"\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2"+
		"\2\2\u0115\u0113\3\2\2\2\u0116\u0119\7\4\2\2\u0117\u0119\5$\23\2\u0118"+
		"\u010e\3\2\2\2\u0118\u0117\3\2\2\2\u0119!\3\2\2\2\u011a\u011b\5&\24\2"+
		"\u011b#\3\2\2\2\u011c\u0123\5&\24\2\u011d\u011e\7\3\2\2\u011e\u011f\7"+
		"\37\2\2\u011f\u0120\5&\24\2\u0120\u0121\7\4\2\2\u0121\u0123\3\2\2\2\u0122"+
		"\u011c\3\2\2\2\u0122\u011d\3\2\2\2\u0123%\3\2\2\2\u0124\u0125\7\3\2\2"+
		"\u0125\u0129\5H%\2\u0126\u0128\5(\25\2\u0127\u0126\3\2\2\2\u0128\u012b"+
		"\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b"+
		"\u0129\3\2\2\2\u012c\u012d\7\4\2\2\u012d\'\3\2\2\2\u012e\u0131\7(\2\2"+
		"\u012f\u0131\7)\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131)\3\2"+
		"\2\2\u0132\u0133\7\3\2\2\u0133\u0134\7\27\2\2\u0134\u013a\7(\2\2\u0135"+
		"\u0136\7\23\2\2\u0136\u0137\7\3\2\2\u0137\u0138\5\24\13\2\u0138\u0139"+
		"\7\4\2\2\u0139\u013b\3\2\2\2\u013a\u0135\3\2\2\2\u013a\u013b\3\2\2\2\u013b"+
		"\u013f\3\2\2\2\u013c\u013d\7\24\2\2\u013d\u013e\7\3\2\2\u013e\u0140\7"+
		"\4\2\2\u013f\u013c\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0144\3\2\2\2\u0141"+
		"\u0142\7\25\2\2\u0142\u0143\7\3\2\2\u0143\u0145\7\4\2\2\u0144\u0141\3"+
		"\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\7\4\2\2\u0147"+
		"+\3\2\2\2\u0148\u0149\7\3\2\2\u0149\u014a\7\30\2\2\u014a\u0150\7(\2\2"+
		"\u014b\u014c\7\23\2\2\u014c\u014d\7\3\2\2\u014d\u014e\5\24\13\2\u014e"+
		"\u014f\7\4\2\2\u014f\u0151\3\2\2\2\u0150\u014b\3\2\2\2\u0150\u0151\3\2"+
		"\2\2\u0151\u0152\3\2\2\2\u0152\u0153\7\27\2\2\u0153\u0156\5&\24\2\u0154"+
		"\u0155\7\24\2\2\u0155\u0157\5\32\16\2\u0156\u0154\3\2\2\2\u0156\u0157"+
		"\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u015a\5.\30\2\u0159\u0158\3\2\2\2\u0159"+
		"\u015a\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\7\4\2\2\u015c-\3\2\2\2"+
		"\u015d\u015e\7\31\2\2\u015e\u0161\5\60\31\2\u015f\u0160\7\34\2\2\u0160"+
		"\u0162\58\35\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u016e\3\2"+
		"\2\2\u0163\u0164\7\32\2\2\u0164\u0167\5\60\31\2\u0165\u0166\7\33\2\2\u0166"+
		"\u0168\5\64\33\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016b\3"+
		"\2\2\2\u0169\u016a\7\34\2\2\u016a\u016c\58\35\2\u016b\u0169\3\2\2\2\u016b"+
		"\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u015d\3\2\2\2\u016d\u0163\3\2"+
		"\2\2\u016e/\3\2\2\2\u016f\u0170\7\3\2\2\u0170\u017c\7\4\2\2\u0171\u017c"+
		"\5\62\32\2\u0172\u0173\7\3\2\2\u0173\u0177\7 \2\2\u0174\u0176\5\62\32"+
		"\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178"+
		"\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017c\7\4\2\2\u017b"+
		"\u016f\3\2\2\2\u017b\u0171\3\2\2\2\u017b\u0172\3\2\2\2\u017c\61\3\2\2"+
		"\2\u017d\u017e\7\3\2\2\u017e\u017f\7(\2\2\u017f\u0180\5&\24\2\u0180\u0181"+
		"\7\4\2\2\u0181\u0184\3\2\2\2\u0182\u0184\5&\24\2\u0183\u017d\3\2\2\2\u0183"+
		"\u0182\3\2\2\2\u0184\63\3\2\2\2\u0185\u0186\7\3\2\2\u0186\u0192\7\4\2"+
		"\2\u0187\u0192\5\66\34\2\u0188\u0189\7\3\2\2\u0189\u018b\7 \2\2\u018a"+
		"\u018c\5\66\34\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3"+
		"\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7\4\2\2\u0190"+
		"\u0192\3\2\2\2\u0191\u0185\3\2\2\2\u0191\u0187\3\2\2\2\u0191\u0188\3\2"+
		"\2\2\u0192\65\3\2\2\2\u0193\u0194\7\3\2\2\u0194\u0195\7\36\2\2\u0195\u0196"+
		"\7(\2\2\u0196\u0197\7(\2\2\u0197\u0198\7\4\2\2\u0198\67\3\2\2\2\u0199"+
		"\u01a4\5:\36\2\u019a\u019b\7\3\2\2\u019b\u019d\7 \2\2\u019c\u019e\5:\36"+
		"\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0"+
		"\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\7\4\2\2\u01a2\u01a4\3\2\2\2\u01a3"+
		"\u0199\3\2\2\2\u01a3\u019a\3\2\2\2\u01a49\3\2\2\2\u01a5\u01a6\7\3\2\2"+
		"\u01a6\u01b2\7\4\2\2\u01a7\u01a8\7\3\2\2\u01a8\u01a9\7\37\2\2\u01a9\u01aa"+
		"\5:\36\2\u01aa\u01ab\7\4\2\2\u01ab\u01b2\3\2\2\2\u01ac\u01ad\7\3\2\2\u01ad"+
		"\u01ae\7\6\2\2\u01ae\u01af\7)\2\2\u01af\u01b0\7)\2\2\u01b0\u01b2\7\4\2"+
		"\2\u01b1\u01a5\3\2\2\2\u01b1\u01a7\3\2\2\2\u01b1\u01ac\3\2\2\2\u01b2;"+
		"\3\2\2\2\u01b3\u01b4\7\3\2\2\u01b4\u01b5\7\7\2\2\u01b5\u01b6\7\3\2\2\u01b6"+
		"\u01b7\7\t\2\2\u01b7\u01b8\7(\2\2\u01b8\u01b9\7\4\2\2\u01b9\u01ba\7\3"+
		"\2\2\u01ba\u01bb\7\n\2\2\u01bb\u01bc\7(\2\2\u01bc\u01be\7\4\2\2\u01bd"+
		"\u01bf\5\6\4\2\u01be\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1\3\2"+
		"\2\2\u01c0\u01c2\5> \2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4"+
		"\3\2\2\2\u01c3\u01c5\5F$\2\u01c4\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5"+
		"\u01c6\3\2\2\2\u01c6\u01c8\5@!\2\u01c7\u01c9\5D#\2\u01c8\u01c7\3\2\2\2"+
		"\u01c8\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\7\4\2\2\u01cb=\3"+
		"\2\2\2\u01cc\u01cd\7\3\2\2\u01cd\u01ce\7\17\2\2\u01ce\u01cf\5\16\b\2\u01cf"+
		"\u01d0\7\4\2\2\u01d0?\3\2\2\2\u01d1\u01d2\7\3\2\2\u01d2\u01e2\7\20\2\2"+
		"\u01d3\u01d5\5B\"\2\u01d4\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4"+
		"\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01e3\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9"+
		"\u01da\7\3\2\2\u01da\u01de\7 \2\2\u01db\u01dd\5B\"\2\u01dc\u01db\3\2\2"+
		"\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1"+
		"\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\7\4\2\2\u01e2\u01d6\3\2\2\2\u01e2"+
		"\u01d9\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\7\4\2\2\u01e5A\3\2\2\2"+
		"\u01e6\u01e7\7\3\2\2\u01e7\u01e8\7$\2\2\u01e8\u01e9\5&\24\2\u01e9\u01ea"+
		"\7\4\2\2\u01ea\u01ff\3\2\2\2\u01eb\u01ec\7\3\2\2\u01ec\u01ee\7%\2\2\u01ed"+
		"\u01ef\5$\23\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2"+
		"\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\7\4\2\2\u01f3"+
		"\u01ff\3\2\2\2\u01f4\u01f5\7\3\2\2\u01f5\u01f7\7&\2\2\u01f6\u01f8\5$\23"+
		"\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa"+
		"\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\7\4\2\2\u01fc\u01ff\3\2\2\2\u01fd"+
		"\u01ff\5$\23\2\u01fe\u01e6\3\2\2\2\u01fe\u01eb\3\2\2\2\u01fe\u01f4\3\2"+
		"\2\2\u01fe\u01fd\3\2\2\2\u01ffC\3\2\2\2\u0200\u0201\7\3\2\2\u0201\u0202"+
		"\7\21\2\2\u0202\u0203\5\32\16\2\u0203\u0204\7\4\2\2\u0204E\3\2\2\2\u0205"+
		"\u0206\7\3\2\2\u0206\u020c\7\35\2\2\u0207\u0208\7\23\2\2\u0208\u0209\7"+
		"\3\2\2\u0209\u020a\5\24\13\2\u020a\u020b\7\4\2\2\u020b\u020d\3\2\2\2\u020c"+
		"\u0207\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\5."+
		"\30\2\u020f\u0210\7\4\2\2\u0210G\3\2\2\2\u0211\u0214\7\6\2\2\u0212\u0214"+
		"\7(\2\2\u0213\u0211\3\2\2\2\u0213\u0212\3\2\2\2\u0214I\3\2\2\2?LXZ`jv"+
		"~\u0081\u008b\u0093\u0096\u009d\u00a9\u00b1\u00b4\u00b9\u00c3\u00c7\u00cb"+
		"\u00cf\u00e4\u00e8\u00f1\u00f6\u00fe\u010c\u0113\u0118\u0122\u0129\u0130"+
		"\u013a\u013f\u0144\u0150\u0156\u0159\u0161\u0167\u016b\u016d\u0177\u017b"+
		"\u0183\u018d\u0191\u019f\u01a3\u01b1\u01be\u01c1\u01c4\u01c8\u01d6\u01de"+
		"\u01e2\u01f0\u01f9\u01fe\u020c\u0213";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}