# Knowledge

sentence: an assertation representing knowledge.
propositional logic: symbols (t/f)
model: assignment of truth value to all propositions.
"entailment": a "entails" b. if alpha is true, then beta is true.
Inference: does knowledge base entail $\alpha$?
Model checking: enumerate all possible models. If in all models based on KB $\alpha$ is true, then KB entails $\alpha$.
knowledge engineering

## Inference Rules
### Modus Ponens
### And Elimination
### Double Negation Elimination
### Implication Elimination
a -> b => (not a) or b
### Biconditional Elimination
### De Morgan's Laws
### Inference Resolution


## Theorem Proving as Search Problem
1. Initial state = starting KB
2. actions = inference rules
3. transition model = new knowledge base after inference
4. goal test = statement we're trying to prove
5. path cost: number of steps

### Conjunctive Normal Form
Conjunction of clauses.
### Clause Resolution
clause: "disjunction of literals"
P v Q1 v Q2 ... v Qn,
!P v R1 v R2 ... v Rn
=>
Q1 v ... v Rn

### Conversion to CNF
1. Biconditionals
2. Implications
3. Move nots inwards
4. distribute v if neeede

## Inference By Resolution
Prove KB entails a?
Prove (KB and !a) is a contradiction
1. Convert (KB and !a) to CNF
2. Keep checking to see if resolution can generate a new clause
3. Empty clause -> contradiction

## First-Order Logic - Alternative to Propositional Logic
Constant symbols and predicate symbols
Universal quantification ($\forall$) and existential quantification ($\exists$)