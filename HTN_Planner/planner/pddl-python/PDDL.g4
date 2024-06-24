grammar PDDL;

pddl: (domain | problem);

//--------- DOMAIN ----------------

domain: LP DEFINE
  LP DOMAIN name=NAME RP
  ( requirements=requireDef
  | types=typesDef
  | constants=constantsDef
  | predicates=predicatesDef
  // functionsDef?
  )*
  operators+=structureDef*
  RP;

// Requirements
requireDef: LP REQUIREMENTS keys+=REQUIRE_KEY+ RP;

// Types
typesDef: LP TYPES types=typedList RP;
typedList: types+=NAME+ OF supertype=NAME typedList
  | types+=NAME*;
 /*typeDef:  LP EITHER either+=NAME+ RP
  | name=NAME;
*/

// Constants
constantsDef: LP CONSTANTS typedObjList RP;
typedObjList: names+=NAME+ OF objtype=NAME typedObjList
  | names+=NAME*;

// Predicates
predicatesDef: LP PREDICATES predicateDef+ RP;
predicateDef: LP predicate=nameDef typedVarList RP;
typedVarList: names+=VARIABLE+ OF vartype=NAME typedVarList
  | names+=VARIABLE*;

// Functions
// TODO

// Operators
structureDef: actionDef
  | taskDef
  | methodDef;
  //| durationActionDef;

// Action
actionDef: LP ACTION name=NAME
  (PARAMETERS LP parameters=typedVarList RP)?
  (PRECONDITION precondition=goalDef)?
  (EFFECT effect=effectDef)?
  (OBSERVE observe=observeDef)?
  RP;

goalDef
  : LP RP
  | atomicFormula
  | literal // :negative-precondition
  // :disjunctive-preconditions
  | LP FORALL LP variables=typedVarList RP gd=goalDef RP // :universal-preconditions
  // :existential-preconditions
  // :fluents
  | LP AND ands+=goalDef* RP
  ;

effectDef
  : LP RP
  | LP AND ands+=cEffect* RP
  | cEffect
  ;

cEffect
  : LP FORALL LP variables+=VARIABLE* RP effectDef RP
  | LP WHEN when=goalDef condEffect RP
  | literal
  ;

// pEffect
  // :fluents

condEffect
  : LP AND ands+=literal* RP
  | literal
  ;

observeDef: atomicFormula;

literal
  : atomicFormula
  | LP NOT atomicFormula RP;
atomicFormula: LP predicate=nameDef arguments+=term* RP;
term
  : name=NAME
  | variable=VARIABLE;

//---------- Hierarchie

taskDef: LP TASK name=NAME
  (PARAMETERS LP parameters=typedVarList RP)?
  (PRECONDITION LP RP)?
  (EFFECT LP RP)?
  RP;

methodDef: LP METHOD name=NAME
  (PARAMETERS LP parameters=typedVarList RP)?
  TASK task=atomicFormula
  (PRECONDITION precondition=goalDef)?
  (tn=taskNetworkDef)?
  RP;

taskNetworkDef
  : ORDERED subtasks=subtasksDef
  	(CONSTRAINTS constraints = constraintDefs)?
  | SUBTASKS subtasks=subtasksDef
	  (ORDERING orderingDefs)?
  	(CONSTRAINTS constraints = constraintDefs)?;

subtasksDef
  : LP RP
  | tasks+=subtaskDef
  | LP AND tasks+=subtaskDef* RP;

subtaskDef
  : LP taskId=NAME atomicFormula RP
  | atomicFormula;

orderingDefs
  : LP RP
  | order+=orderingDef
  | LP AND order+=orderingDef+ RP;

orderingDef: LP BEFORE head=NAME tail+=NAME RP;

constraintDefs
  : constraintDef
  | LP AND constraintDef+ RP;

constraintDef
  : LP RP
  | LP NOT constraintDef RP
  | LP EQUALS left=VARIABLE right=VARIABLE RP;

//--------- PROBLEM ----------------

problem: LP DEFINE
  LP PROBLEM pname=NAME RP
  LP DDOMAIN dname=NAME RP
  (requirements=requireDef)?
  (objects=objectDeclaration)?
  (htn=htnDef)?
  init
  goal?
  RP;

objectDeclaration: LP OBJECTS typedObjList RP;

init: LP INIT (initEl* | LP AND initEl* RP) RP;
initEl
  : LP UNKNOWN atomicFormula RP
  | LP OR choices+=literal+ RP
  | LP ONEOF xchoices+=literal+ RP
  | literal
  // fluents
  ;

goal: LP GOAL goalDef RP;

htnDef: LP HTN
  (PARAMETERS LP parameters=typedVarList RP)?
  tn=taskNetworkDef
  RP;

//--------- TOKENS ----------------
LP: '(';
RP: ')';
OF: '-';
EQUALS: '=';

DEFINE: 'define';
DOMAIN: 'domain';
PROBLEM: 'problem';
DDOMAIN: ':domain';
REQUIREMENTS: ':requirements';
TYPES: ':types';
CONSTANTS: ':constants';
PREDICATES: ':predicates';
OBJECTS: ':objects';
INIT: ':init';
GOAL: ':goal';

// Action Tokens
ACTION: ':action';
PARAMETERS: ':parameters';
PRECONDITION: ':precondition';
EFFECT: ':effect';
OBSERVE: ':observe';

// Hierarchi
TASK: ':task';
METHOD: ':method';
ORDERED: ':ordered-tasks' | ':ordered-subtasks';
SUBTASKS: ':subtasks' | ':tasks';
ORDERING: ':order' | ':ordering';
CONSTRAINTS: ':constraints';
HTN: ':htn';
BEFORE: '<';

// Others
NOT: 'not';
AND: 'and';
FORALL: 'forall';
WHEN: 'when';
EITHER: 'either';
UNKNOWN: 'unknown';
OR: 'or';
ONEOF: 'oneof';

REQUIRE_KEY:
 ':strips' // Basic STRIPS-style adds and deletes
 | ':typing' //	Allow type names in declarations of variables
 | ':negative-preconditions' //	Allow not in goal descriptions
 | ':disjunctive-preconditions' //	Allow or in goal descriptions
 | ':equality' //	Support = as built-in predicate
 | ':existential-preconditions' //	Allow exists in goal descriptions
 | ':universal-preconditions' | ':universal-precondition' //	Allow forall in goal descriptions
 | ':quantified-preconditions' //	= :existential-preconditions + :universal-preconditions
 | ':conditional-effects' // Allow when in action effects
 | ':fluents' //	Allow function definitions and use of effects using assignment operators and arithmetic preconditions.
 | ':adl' //	= :strips + :typing + :negative-preconditions	+ :disjunctive-preconditions + :equality	+ :quantified-preconditions	+ :conditional-effects
 | ':durative-actions' //	Allows durative actions. Note that this does not imply :fluents.
 | ':duration-inequalities' //	Allows duration constraints in durative actions using inequalities.
 | ':continuous-effects' //	Allows durative actions to affect fluents	continuously over the duration of the actions.
 | ':hierachie' | ':hierarchy' | ':method-precondition' | ':method-preconditions' // HDDL
;

/*
 * allowing keywords as identifier where allowed
 * may need more to specify
 */
nameDef
	: EQUALS
  | name=NAME
	;

NAME: LETTER ANY_CHAR* ;
fragment LETTER:	'a'..'z' | 'A'..'Z';
fragment ANY_CHAR: LETTER | '0'..'9' | '-' | '_';

VARIABLE : '?' LETTER ANY_CHAR* ;

NUMBER : DIGIT+ ('.' DIGIT+)? ;
fragment DIGIT: '0'..'9';

LINE_COMMENT
    : ';' ~('\n'|'\r')* '\r'? '\n' -> skip
    ;
WHITESPACE
    :   (   ' '
        |   '\t'
        |   '\r'
        |   '\n'
        )+
        -> skip
    ;
