# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

from copy import deepcopy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the deepest nodes in the search tree first."""
    startState = problem.getStartState()
    path = util.Stack()
    s = util.Stack()

    visited = set()
    visited.add(startState[0])

    for node in problem.getSuccessors(startState):
        s.push((node, 0)) # pusheamos al stack los sucesores del estado inicial y su nivel

    while not s.isEmpty(): # si hay nodos en la pila, recorremos
        (currNode, level) = s.pop()
        for _ in range(0, len(path.list) - level):
            path.pop() # backtrackeamos hasta igualar el nivel del siguiente nodo

        visited.add(currNode[0])
        path.push(currNode[1])
        if problem.isGoalState(currNode[0]): # si el nodo es meta terminamos la búsqueda
            return path.list
        
        for node in problem.getSuccessors(currNode[0]): # agregamos sucesores a la pila
            if node[0] not in visited:
                s.push((node, level+1))

    return path.list # debería ser error porque la lista es vacía? nunca halló la meta


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    # registramos los nodos previamente visitados
    visited = set()
    visited.add(startState)

    q = util.Queue()
    # agregamos los sucesores iniciales al queue
    for node in problem.getSuccessors(startState):
        q.push((node, util.Stack()))
        visited.add(node[0])

    while not q.isEmpty():
        ((state, dir, _), path) = q.pop()
        # construimos un camino para cada nodo, de manera que al encontrar
        # el estado final, tengamos computado el camino tomado para alcanzarlo
        path.push(dir)

        if problem.isGoalState(state):
            return path.list

        for node in problem.getSuccessors(state):
            if node[0] not in visited:
                visited.add(node[0])
                # debemos hacer una copia profunda para evitar que se modifique
                # el mismo camino para distintos nodos
                q.push((node, deepcopy(path)))

    return [] # Error: No se encontro la meta
    


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
