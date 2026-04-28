# Lab45 - Sudoku Solver

A high-performance Sudoku solver using Constraint Satisfaction Problem (CSP) techniques with backtracking and arc consistency algorithms.

## Project Overview

This project implements an intelligent Sudoku puzzle solver that combines advanced search algorithms to efficiently solve multiple Sudoku puzzles. It uses constraint satisfaction techniques including:

- **AC-3 Algorithm**: Arc consistency for domain pruning
- **Backtracking Search**: Systematic exploration with inference
- **Forward Checking**: Constraint propagation for early conflict detection
- **MRV Heuristic**: Minimum Remaining Values variable selection strategy

## Features

- 🎯 Solves multiple Sudoku puzzles from input files
- ⚡ Efficient domain reduction using AC-3 arc consistency
- 🔄 Intelligent backtracking with forward checking inference
- 📊 Performance timing for each puzzle and total execution time
- 📝 Batch processing with results written to output file
- 🎨 Clear puzzle display and solution formatting

## Project Structure

```
Lab45-Sudoku/
├── sudoku.py          # Main entry point for solving puzzles
├── csp.py             # Constraint Satisfaction Problem class definition
├── search.py          # Backtracking and AC-3 search algorithms
├── util.py            # Utility functions and data structures
├── pyproject.toml     # Project configuration
├── output.txt         # Output file with solved puzzles
└── data/              # Sample input files
    ├── euler.txt      # Sample Sudoku puzzles
    └── magictour.txt  # Additional puzzle set
```

## File Descriptions

### `sudoku.py`
Main executable script that orchestrates the solving process. It:
- Parses command-line arguments for input file path
- Reads Sudoku puzzles from the input file
- Solves each puzzle using the CSP solver
- Writes solutions to output.txt
- Tracks performance metrics

### `csp.py`
Defines the `csp` class representing a Sudoku as a Constraint Satisfaction Problem. It:
- Maintains 81 variables (grid cells: A1 through I9)
- Manages 27 units (9 rows + 9 columns + 9 boxes)
- Tracks peer relationships for constraint checking
- Manages variable domains (possible values for each cell)
- Implements constraint pairs for all-different constraints

### `search.py`
Implements core search algorithms:
- **AC3()**: Arc consistency algorithm to reduce domains
- **Revise()**: Domain revision for arc consistency
- **Backtracking_Search()**: Initializes search and calls recursive backtracking
- **Recursive_Backtracking()**: Core backtracking algorithm with:
  - MRV variable selection heuristic
  - Forward checking for constraint propagation
  - Backtracking on conflicts

### `util.py`
Utility functions providing:
- Basic data structures (digits, rows, columns, squares)
- Cross product function for creating units and peers
- Grid cell naming convention (A1-I9)

## Installation

### Requirements
- Python 3.14 or higher
- No external dependencies

### Setup

1. Clone or download the project:
```bash
cd Lab45-Sudoku
```

2. Ensure you have Python installed:
```bash
python --version
```

## Usage

### Running the Solver

Solve puzzles from an input file:

```bash
python sudoku.py --inputFile data/euler.txt
```

### Input File Format

The input file should contain one Sudoku puzzle per line, where:
- Each puzzle is represented as 81 characters
- `0` represents an empty cell
- Digits `1-9` represent given values

Example input format:
```
4.....8.5.3..........7......2.............4.69.1.....8.5.9.......5.4......7.3...
```

### Output

- Solutions are written to `output.txt` with one solved puzzle per line
- Console output displays:
  - Time taken for each puzzle
  - Solved puzzle grids (formatted display)
  - Total number of puzzles solved
  - Total execution time

## Algorithm Details

### AC-3 Algorithm
Enforces arc consistency by:
1. Creating a queue of all constraints
2. For each constraint (xi, xj), revising xi's domain
3. If xi's domain changes, adding affected constraints back to queue
4. Detecting unsolvable states early

### Backtracking Search
Solves the puzzle by:
1. Running AC-3 for initial domain pruning
2. Recursively assigning values to unassigned variables
3. Using MRV heuristic to select the variable with fewest remaining values
4. Applying forward checking to detect conflicts early
5. Backtracking when conflicts occur
6. Restoring previous domains on backtrack

### Forward Checking
After each variable assignment:
- Enforces constraints with unassigned variables
- Removes assigned value from neighbors' domains
- Detects empty domains (indicating failure)

## Performance

The solver efficiently handles:
- Standard 9×9 Sudoku puzzles
- Puzzles with varying difficulty levels
- Batch processing of multiple puzzles
- Timing statistics for performance analysis

## Example

```bash
$ python sudoku.py --inputFile data/euler.txt
The board -  1  takes  0.0234  seconds
After solving: 
 4 1 7 | 3 6 9 | 8 2 5 
 ...

Number of problems solved is:  50
Time taken to solve the puzzles is:  1.2345
```

## Technical Stack

- **Language**: Python 3.14+
- **Paradigm**: Constraint Satisfaction Problems (CSP)
- **Algorithms**: AC-3, Backtracking with Forward Checking
- **Heuristics**: Minimum Remaining Values (MRV)

## Learning Objectives

This project demonstrates:
- Implementation of CSP solvers
- Arc consistency algorithms for constraint propagation
- Backtracking with intelligent search strategies
- Heuristic selection for efficient search
- Performance optimization in algorithm design

## License

Educational project for Lab45

## Author Notes

This project is designed to solve Sudoku puzzles efficiently using AI search techniques, making it an excellent reference for understanding:
- How constraint satisfaction problems are modeled and solved
- The importance of constraint propagation and pruning
- Strategic variable selection and value ordering heuristics
- Trade-offs between solution time and implementation complexity
