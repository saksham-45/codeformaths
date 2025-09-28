# Gauss-Jordan Elimination Solver

A Python implementation of the Gauss-Jordan elimination method for solving systems of linear equations of any size.

## Features

- **No external dependencies** - Uses only Python standard library
- **Handles any size** - Works with 2x2, 3x3, 4x4, or any n×n system
- **Step-by-step output** - Shows each elimination step for learning purposes
- **Error handling** - Detects inconsistent systems and infinite solutions
- **Interactive mode** - Can be run interactively or with predefined examples

## How it Works

The Gauss-Jordan elimination method:

1. **Forward Elimination**: Uses the first equation to eliminate the first variable from all other equations
2. **Continue Process**: Uses the second equation to eliminate the second variable from remaining equations
3. **Repeat**: Continues until all variables are isolated
4. **Back Substitution**: The final matrix gives the solution directly

## Usage

### Run Examples
```bash
python3 gauss_jordan.py
```

### Interactive Mode
Uncomment the `main()` call at the bottom of the script to run in interactive mode.

### Programmatic Usage
```python
from gauss_jordan import solve_linear_system

# Define coefficient matrix and constants
coefficients = [[2, 1], [1, -1]]
constants = [5, 1]

# Solve the system
solution, steps = solve_linear_system(coefficients, constants)

if solution:
    print(f"Solution: {solution}")
else:
    print("No unique solution found")
```

## Examples

### 2x2 System
```
2x + y = 5
x - y = 1
```
Solution: x = 2, y = 1

### 3x3 System
```
x + 2y + 3z = 9
2x + 5y + 2z = 4
6x - 3y + z = 2
```
Solution: x ≈ -0.429, y ≈ -0.390, z ≈ 3.403

## Algorithm Details

1. **Pivot Selection**: Chooses the largest element in the current column as pivot
2. **Row Swapping**: Swaps rows if necessary to get the best pivot
3. **Normalization**: Makes the pivot element equal to 1
4. **Elimination**: Eliminates the current variable from all other rows
5. **Consistency Check**: Verifies the system has a unique solution

## Error Handling

- **Inconsistent Systems**: Detects when no solution exists
- **Infinite Solutions**: Identifies when the system has infinitely many solutions
- **Input Validation**: Ensures proper matrix dimensions and data types
