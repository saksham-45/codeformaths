#!/usr/bin/env python3
"""
Gauss-Jordan Elimination Solver
"""

from typing import List, Tuple, Optional


def format_matrix(matrix: List[List[float]]) -> str:
    lines = []
    for row in matrix:
        line = "[" + " ".join(f"{x:8.3f}" for x in row) + "]"
        lines.append(line)
    return "\n".join(lines)


def gauss_jordan_elimination(matrix: List[List[float]]) -> Tuple[List[List[float]], List[str]]:
    steps = []
    n = len(matrix)
    m = len(matrix[0]) - 1
    
    augmented_matrix = [row[:] for row in matrix]
    
    steps.append("Starting Gauss-Jordan elimination:")
    steps.append(f"System has {n} equations and {m} variables")
    steps.append(f"Initial augmented matrix:")
    steps.append(format_matrix(augmented_matrix))
    
    for i in range(n):
        # Find largest pivot in column i
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented_matrix[k][i]) > abs(augmented_matrix[max_row][i]):
                max_row = k
        
        if max_row != i:
            augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]
            steps.append(f"Swapped row {i+1} with row {max_row+1}")
        
        # Skip if pivot is zero (inconsistent/infinite solutions)
        if abs(augmented_matrix[i][i]) < 1e-10:
            steps.append(f"Warning: Pivot at position ({i+1},{i+1}) is very small or zero")
            continue
        
        # Normalize pivot to 1
        if augmented_matrix[i][i] != 1:
            pivot = augmented_matrix[i][i]
            for j in range(len(augmented_matrix[i])):
                augmented_matrix[i][j] /= pivot
            steps.append(f"Row {i+1} divided by {pivot:.3f} to make pivot = 1")
        
        # Eliminate variable i from all other rows
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                if abs(factor) > 1e-10:
                    for k in range(len(augmented_matrix[j])):
                        augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
                    steps.append(f"Row {j+1} = Row {j+1} - ({factor:.3f}) * Row {i+1}")
        
        steps.append(f"After eliminating variable x{i+1}:")
        steps.append(format_matrix(augmented_matrix))
    
    return augmented_matrix, steps


def solve_linear_system(coefficients: List[List[float]], constants: List[float]) -> Tuple[Optional[List[float]], List[str]]:
    try:
        n = len(coefficients)
        if n != len(constants):
            return None, ["Error: Number of equations must equal number of constants"]
        
        if n == 0 or len(coefficients[0]) != n:
            return None, ["Error: Coefficient matrix must be square (same number of equations and variables)"]
        
        # Create augmented matrix [A|b]
        augmented_matrix = []
        for i in range(n):
            row = coefficients[i][:] + [constants[i]]
            augmented_matrix.append(row)
        
        result_matrix, steps = gauss_jordan_elimination(augmented_matrix)
        
        # Extract solution from last column
        solution = [row[-1] for row in result_matrix]
        
        # Check for inconsistent system (0 = non-zero)
        for i in range(n):
            all_zero = all(abs(result_matrix[i][j]) < 1e-10 for j in range(n))
            if all_zero and abs(result_matrix[i][-1]) > 1e-10:
                steps.append("System is inconsistent - no solution exists")
                return None, steps
        
        # Check rank for infinite solutions
        rank = 0
        for i in range(n):
            if not all(abs(result_matrix[i][j]) < 1e-10 for j in range(n)):
                rank += 1
        
        if rank < n:
            steps.append(f"System has infinite solutions (rank = {rank} < {n})")
            return None, steps
        
        steps.append(f"Solution found: {[f'{x:.6f}' for x in solution]}")
        return solution, steps
        
    except Exception as e:
        return None, [f"Error: {str(e)}"]


def print_solution(solution: Optional[List[float]], steps: List[str], variable_names: Optional[List[str]] = None):
    print("=" * 60)
    print("GAUSS-JORDAN ELIMINATION SOLVER")
    print("=" * 60)
    
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step}")
    
    print("\n" + "=" * 60)
    
    if solution is not None:
        print("SOLUTION:")
        if variable_names is None:
            variable_names = [f"x{i+1}" for i in range(len(solution))]
        
        for i, (var, val) in enumerate(zip(variable_names, solution)):
            print(f"{var} = {val:.6f}")
    else:
        print("NO UNIQUE SOLUTION FOUND")
    
    print("=" * 60)


def main():
    print("Gauss-Jordan Elimination Solver")
    print("Enter the number of equations/variables:")
    
    try:
        n = int(input("n = "))
        
        print(f"\nEnter the coefficient matrix ({n}x{n}):")
        coefficients = []
        for i in range(n):
            row = input(f"Row {i+1}: ").split()
            coefficients.append([float(x) for x in row])
        
        print(f"\nEnter the constants vector ({n} elements):")
        constants = input("Constants: ").split()
        constants = [float(x) for x in constants]
        
        solution, steps = solve_linear_system(coefficients, constants)
        print_solution(solution, steps)
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except KeyboardInterrupt:
        print("\nExiting...")


def example_1():
    print("Example 1: 2x2 System")
    coefficients = [[2, 1], [1, -1]]
    constants = [5, 1]
    solution, steps = solve_linear_system(coefficients, constants)
    print_solution(solution, steps)


def example_2():
    print("Example 2: 3x3 System")
    coefficients = [[1, 2, 3], [2, 5, 2], [6, -3, 1]]
    constants = [9, 4, 2]
    solution, steps = solve_linear_system(coefficients, constants)
    print_solution(solution, steps)


def example_3():
    print("Example 3: 4x4 System")
    coefficients = [
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [1, 3, 6, 10],
        [1, 4, 10, 20]
    ]
    constants = [10, 30, 60, 100]
    solution, steps = solve_linear_system(coefficients, constants)
    print_solution(solution, steps)


if __name__ == "__main__":
    # Run examples
    example_1()
    print("\n" + "="*80 + "\n")
    example_2()
    print("\n" + "="*80 + "\n")
    example_3()
    
    # Uncomment to run interactive mode
    # main()
