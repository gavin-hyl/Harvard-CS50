# Lecture 0 - Search
## Terminology
### state
A configuration of the environment and the agent
### agent
### action
Defined as a function. Returns all possible actions given any state. 
### transition model
Defined as a function, returns the state given a state and a action.
### solution
Sequence of actions that takes us from the initial state to the goal state
### frontier
Set of unexplored nodes.
### Node
Contains: a state, a parent, an action that led from its parent node, and a path cost (from initial node to this node).

## Approach
1. if frontier is empty, then no solution exists
2. remove a node from the frontier
3. goal test the node
4. add it to explored set.
5. expand the node, add new nodes to frontier if the new ones aren't explored.

### how do we remove nodes?
1. Depth-First Search (DFS): frontier is a stack, always explore deepest node in frontier. Doesn't ensure optimal solution.
2. Breadth-First Search (BFS): frontier is a queue, always explore shallowest node in frontier. Not very efficient.
### uninformed search
no problem-specific knowledge (BFS and DFS)
### informed search: A*
uses problem-specific knowledge
1. Greedy Best-First Search: expands the node closest to the goal first, estimated by a heuristic function h(n) (ex: Manhattan Distance in mazes)
2. A* search: heuristic is redesigned. Expand lowest g(n) + h(n), where g(n) is the path cost from initial state to the node. Optimal if (WHY?):
    - h(n) is admissible, i.e., it never overestimates the true cost.
    - h(n) is consistent, i.e., h(n) $\leq$ h(n') + c

## Adverserial Search
### Game
S0, Player (which player's turn?), Actions (legal moves), Result (player action), Terminal (is it over?), Utility (calcualtes score).
### Minimax
Max player attempts to maximize score, min player attempts to minimize. Consider all possible options, called recursively. 

Max Player:
Given state s, choose action $a$ that min(result(s, a)) is the maximum. If s is terminal state, simply return utility.

Min player: same logic

### Optimization
#### Alpha-Beta Pruning
If one branch already presented a worse case than explored, prune that branch and don't explore further.
#### Depth-Limited Minimax
Assigning scores: evaluation function, expected utility estimation.