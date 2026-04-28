# CLASS DESCRIPTION FOR CONSTRAINT SATISFACTION PROBLEM (CSP)

from util import *

class csp:

    # INITIALIZING THE CSP
    def __init__(self, domain=digits, grid=""):
        """
        Unitlist consists of the 27 lists of peers
        Units is a dictionary consisting of the keys and the corresponding lists of peers
        Peers is a dictionary consisting of the 81 keys and the corresponding set of 27 peers
        Constraints denote the various all-different constraints between the variables
        """
        self.variables = squares  # All 81 cells: A1, A2, ..., I9

        # Build the 27 units (9 rows + 9 columns + 9 boxes)
        self.unitlist = (
            [cross(r, cols) for r in rows] +          # 9 row units
            [cross(rows, c) for c in cols] +           # 9 column units
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
                           for cs in ('123', '456', '789')]  # 9 box units
        )

        # Units: for each square, the list of units it belongs to
        self.units = dict((s, [u for u in self.unitlist if s in u])
                          for s in squares)

        # Peers: for each square, the set of squares that share a unit with it (excluding itself)
        self.peers = dict((s, set(sum(self.units[s], [])) - {s})
                          for s in squares)

        # Constraints: list of binary not-equal constraint pairs (var1, var2)
        self.constraints = {(variable, peer) for variable in squares
                            for peer in self.peers[variable]}

        # Values: domain for each variable (initially all digits, narrowed by the grid)
        self.values = self.getDict(grid)



    def getDict(self, grid=""):
        """
        Getting the string as input and returning the corresponding dictionary
        """
        i = 0
        values = dict()
        for cell in self.variables:
            if grid[i] != '0':
                values[cell] = grid[i]
            else:
                values[cell] = digits
            i = i + 1
        return values