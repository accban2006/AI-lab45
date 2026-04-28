"""
In search.py, you will implement Backtracking and AC3 searching algorithms
for solving Sudoku problem which is called by sudoku.py
"""

from csp import *
from copy import deepcopy
import util



def AC3(csp):
    """
    AC-3 arc consistency algorithm.
    Reduces domains by enforcing arc consistency on all constraints.
    Returns False if an inconsistency is found, True otherwise.
    """
    queue = list(csp.constraints)
    while queue:
        (xi, xj) = queue.pop(0)
        if Revise(csp, xi, xj):
            if len(csp.values[xi]) == 0:
                return False
            for xk in (csp.peers[xi] - {xj}):
                queue.append((xk, xi))
    return True

def Revise(csp, xi, xj):
    """
    Revise the domain of xi to be arc-consistent with xj.
    Returns True if the domain of xi was revised.
    """
    revised = False
    for x in csp.values[xi]:
        # If every value in xj's domain conflicts with x, remove x
        if all(x == y for y in csp.values[xj]):
            csp.values[xi] = csp.values[xi].replace(x, '')
            revised = True
    return revised

def Backtracking_Search(csp):
    """
    Backtracking search initialize the initial assignment
    and calls the recursive backtrack function.
    First runs AC-3 to prune domains, then starts backtracking.
    """
    # Run AC-3 to enforce arc consistency before searching
    AC3(csp)

    # Initialize assignment with cells that already have a single value
    assignment = {}
    for var in squares:
        if len(csp.values[var]) == 1:
            assignment[var] = csp.values[var]

    return Recursive_Backtracking(assignment, csp)


def Recursive_Backtracking(assignment, csp):
    """
    The recursive function which assigns value using backtracking.
    Uses MRV for variable selection, forward checking for inference.
    """
    # If assignment is complete, return it
    if isComplete(assignment):
        return assignment

    # Select an unassigned variable using MRV heuristic
    var = Select_Unassigned_Variables(assignment, csp)

    # Try each value in the variable's domain
    for value in Order_Domain_Values(var, assignment, csp):
        if isConsistent(var, value, assignment, csp):
            assignment[var] = value

            # Save current domains so we can restore on backtrack
            saved_values = deepcopy(csp.values)

            # Apply forward checking inference
            inferences = Inference(assignment, {}, csp, var, value)

            if inferences != "FAILURE":
                result = Recursive_Backtracking(assignment, csp)
                if result != "FAILURE":
                    return result

            # Undo: remove assignment and restore domains
            del assignment[var]
            csp.values = saved_values

    return "FAILURE"

def Inference(assignment, inferences, csp, var, value):
    """
    Forward checking using concept of Inferences
    """

    inferences[var] = value

    for neighbor in csp.peers[var]:
        if neighbor not in assignment and value in csp.values[neighbor]:
            if len(csp.values[neighbor]) == 1:
                return "FAILURE"

            remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

            if len(remaining) == 1:
                flag = Inference(assignment, inferences, csp, neighbor, remaining)
                if flag == "FAILURE":
                    return "FAILURE"

    return inferences

def Order_Domain_Values(var, assignment, csp):
    """
    Returns string of values of given variable
    """
    return csp.values[var]

def Select_Unassigned_Variables(assignment, csp):
    """
    Selects new variable to be assigned using minimum remaining value (MRV)
    """
    unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv

def isComplete(assignment):
    """
    Check if assignment is complete
    """
    return set(assignment.keys()) == set(squares)

def isConsistent(var, value, assignment, csp):
    """
    Check if assignment is consistent
    """
    for neighbor in csp.peers[var]:
        if neighbor in assignment.keys() and assignment[neighbor] == value:
            return False
    return True

def forward_checking(csp, assignment, var, value):
    csp.values[var] = value
    for neighbor in csp.peers[var]:
        csp.values[neighbor] = csp.values[neighbor].replace(value, '')

def display(values):
    """
    Display the solved sudoku on screen
    """
    for row in rows:
        if row in 'DG':
            print("-------------------------------------------")
        for col in cols:
            if col in '47':
                print(' | ', values[row + col], ' ', end=' ')
            else:
                print(values[row + col], ' ', end=' ')
        print(end='\n')

def write(values):
    """
    Write the string output of solved sudoku to file
    """
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output