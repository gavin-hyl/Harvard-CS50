# Probability
## Definition
1. $0 \leq P(\omega) \leq 1$
2. $\Sigma P(\omega) = 1$

## Unconditional vs Conditional
Evidence that has already been revealed?
$P(a\,|\,b),$ "probability of a given b"

## Probability Distribution
Assignment of probability to every possible world

## Independence
Evidence that has already been revealed?
$P(a\,|\,b) = P (a)$

## Bayes' Rule
$P(a \, | \, b) = \dfrac{P(b\,|\,a) P(b)}{P(a)}$

## Joint Probability
$P(a\,|\,b) = \dfrac{P(a, b)}{P(b)} = P(a, b) \cdot \alpha$
### Marginalization
$P(a) = P(a, b) + P(a, \neg b)$
### Conditioning
$P(a) = P(a | b) P(b) + P(a, \neg b) P(\neg b)$

# Bayesian Network
## Inference model
1. directed graph
2. each node represents a rnd variable
3. each node has a probability distribution $P(X \,|\, Parent(X))$

## Inference
1. Query X: variable we want the distribution of (what is $P(X|e)?$)
2. Evidence variables E: observed variables for event e
3. Hidden variables Y: non-evidence, non-query variables.

## By enumeration
$P(X|e) = \alpha P(X, e) = \alpha \sum_y P(X, e, y).$
Marginalization!

## By Sampling
Just...take samples. For conditional inference, use rejection sampling (taking only the samples that match the conditions)

## Likelihood Weighting
1. Start by fixing values for evidence variables
2. Sample non-evidence variables using conditional probabilities in the Bayseian Network
3. Weight each sample by probability

# Uncertainty over Time
Markov Assumption: the current state only depends on a finite number of previous states.

Markov Chain
Transition Model

# Sensor Models
Hidden Markov Model

Sensor Markov Model: sensor data only depends on hidden state

Emission probabilities: $P(emission | state)$

Tasks:
1. filtering: distribution for current state
2. prediction: distribution for future state
3. smoothing: distribution for past state
4. most likely observation: most likely sequence of states