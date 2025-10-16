# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/hybrid_prover.py

<content of hybrid_prover.py>
from sympy import (
    symbols, solve, simplify, expand, factor, 
    Symbol, sin, cos, tan, limit, integrate, diff,
    lambdify
)
import numpy as np
from scipy import (
    integrate as scipy_integrate,
    optimize as scipy_optimize,
    linalg as scipy_linalg,
    stats as scipy_stats
)
from typing import List, Dict, Optional, Tuple, Any, Union
from dataclasses import dataclass

@dataclass
class HybridProofStep:
    symbolic_result: Any  # SymPy result
    numeric_result: Any   # NumPy/SciPy result
    explanation: str

class HybridProver:
    def __init__(self):
        # Symbolic variables
        self.x, self.y, self.z = symbols('x y z')
        # Numerical precision for verification
        self.num_points = 1000
        self.tolerance = 1e-10

    def verify_inequality(self, expr_str: str, domain=(-10, 10)) -> List[HybridProofStep]:
        """Verify inequality both symbolically and numerically"""
        steps = []
        
        # Symbolic part
        expr = simplify(expr_str)
        symbolic_result = solve(expr, self.x)
        
        # Numerical verification
        x_vals = np.linspace(domain[0], domain[1], self.num_points)
        expr_lambda = lambdify(self.x, expr)
        numeric_result = expr_lambda(x_vals)
        
        steps.append(HybridProofStep(
            symbolic_result=symbolic_result,
            numeric_result=f"Valid in {sum(numeric_result > 0)} of {self.num_points} test points",
            explanation="Inequality verification"
        ))
        
        return steps

    def numerical_integration(self, expr_str: str, bounds: Tuple[float, float]) -> List[HybridProofStep]:
        """Compare symbolic and numerical integration"""
        steps = []
        
        # Symbolic integration
        expr = simplify(expr_str)
        symbolic_integral = integrate(expr, (self.x, bounds[0], bounds[1]))
        
        # Numerical integration using SciPy
        expr_lambda = lambdify(self.x, expr)
        numeric_integral, error_estimate = scipy_integrate.quad(expr_lambda, bounds[0], bounds[1])
        
        steps.append(HybridProofStep(
            symbolic_result=symbolic_integral,
            numeric_result=f"{numeric_integral} ± {error_estimate}",
            explanation="Integration comparison"
        ))
        
        return steps

    def find_extrema(self, expr_str: str, domain=(-10, 10)) -> List[HybridProofStep]:
        """Find extrema using both symbolic and numerical methods"""
        steps = []
        
        # Symbolic derivative
        expr = simplify(expr_str)
        symbolic_derivative = diff(expr, self.x)
        symbolic_critical = solve(symbolic_derivative, self.x)
        
        # Numerical optimization using SciPy
        expr_lambda = lambdify(self.x, expr)
        numeric_min = scipy_optimize.minimize_scalar(
            lambda x: expr_lambda(x),
            bounds=domain,
            method='bounded'
        )
        numeric_max = scipy_optimize.minimize_scalar(
            lambda x: -expr_lambda(x),
            bounds=domain,
            method='bounded'
        )
        
        steps.append(HybridProofStep(
            symbolic_result=f"Critical points: {symbolic_critical}",
            numeric_result=f"Min at x={numeric_min.x}, Max at x={-numeric_max.x}",
            explanation="Extrema analysis"
        ))
        
        return steps

    def solve_differential_equation(self, 
                                 eq_str: str, 
                                 initial_conditions: Dict[float, float]
                                 ) -> List[HybridProofStep]:
        """Solve differential equations using both symbolic and numerical methods"""
        steps = []
        
        # Symbolic solution attempt
        expr = simplify(eq_str)
        try:
            symbolic_solution = integrate(expr, self.x)
            steps.append(HybridProofStep(
                symbolic_result=symbolic_solution,
                numeric_result=None,
                explanation="Symbolic general solution"
            ))
        except Exception as e:
            symbolic_solution = f"Could not find symbolic solution: {e}"
        
        # Numerical solution using SciPy
        t = np.linspace(0, 10, 100)
        expr_lambda = lambdify(self.x, expr)
        
        try:
            numeric_solution = scipy_integrate.odeint(
                expr_lambda,
                list(initial_conditions.values())[0],
                t
            )
            steps.append(HybridProofStep(
                symbolic_result=symbolic_solution,
                numeric_result="Numerical solution computed for t ∈ [0, 10]",
                explanation="Differential equation solution"
            ))
        except Exception as e:
            steps.append(HybridProofStep(
                symbolic_result=symbolic_solution,
                numeric_result=f"Numerical solution failed: {e}",
                explanation="Solution attempt"
            ))
        
        return steps

    def statistical_analysis(self, data: List[float]) -> List[HybridProofStep]:
        """Perform statistical analysis using SciPy"""
        steps = []
        
        # Basic statistics
        steps.append(HybridProofStep(
            symbolic_result=None,
            numeric_result={
                'mean': np.mean(data),
                'std': np.std(data),
                'median': np.median(data)
            },
            explanation="Basic statistics"
        ))
        
        # Normality test
        statistic, p_value = scipy_stats.normaltest(data)
        steps.append(HybridProofStep(
            symbolic_result=None,
            numeric_result={
                'statistic': statistic,
                'p_value': p_value,
                'is_normal': p_value > 0.05
            },
            explanation="Normality test"
        ))
        
        return steps

    def matrix_operations(self, matrix_A: Union[List[List[float]], List[List[int]]], 
                            matrix_B: Optional[Union[List[List[float]], List[List[int]]]] = None) -> List[HybridProofStep]:
        """Perform matrix operations using SciPy"""
        steps = []
        
        # Convert to numpy arrays
        A = np.array(matrix_A)
        
        # Eigenvalues and eigenvectors
        w, v = scipy_linalg.eigh(A)  # Using eigh for Hermitian matrices
        steps.append(HybridProofStep(
            symbolic_result=None,
            numeric_result={
                'eigenvalues': w.tolist(),
                'eigenvectors': v.tolist()
            },
            explanation="Eigenvalue decomposition"
        ))
        
        # Matrix properties
        steps.append(HybridProofStep(
            symbolic_result=None,
            numeric_result={
                'determinant': scipy_linalg.det(A),
                'matrix_norm': scipy_linalg.norm(A),
                'rank': np.linalg.matrix_rank(A),
                'is_symmetric': np.allclose(A, A.T),
                'trace': np.trace(A)
            },
            explanation="Matrix properties"
        ))
        
        if matrix_B is not None:
            B = np.array(matrix_B)
            # Solve system of equations if B is provided
            try:
                solution = scipy_linalg.solve(A, B)
                steps.append(HybridProofStep(
                    symbolic_result=None,
                    numeric_result={'solution': solution},
                    explanation="System solution"
                ))
            except Exception as e:
                steps.append(HybridProofStep(
                    symbolic_result=None,
                    numeric_result=f"Could not solve system: {e}",
                    explanation="Solution attempt"
                ))
        
        return steps

def format_hybrid_proof(steps: List[HybridProofStep]) -> str:
    """Format hybrid proof steps nicely"""
    result = ["Hybrid Symbolic-Numerical Proof:", "=" * 50]
    for i, step in enumerate(steps, 1):
        result.append(f"Step {i}:")
        result.append(f"Explanation: {step.explanation}")
        if step.symbolic_result is not None:
            result.append(f"Symbolic: {step.symbolic_result}")
        if step.numeric_result is not None:
            result.append(f"Numeric: {step.numeric_result}")
        result.append("-" * 50)
    return "\n".join(result)

if __name__ == "__main__":
    prover = HybridProver()
    
    print("\nTesting matrix operations:")
    # Create sample matrices
    matrix_A = np.array([[4.0, -2.0], [-1.0, 3.0]])  # A well-conditioned matrix
    matrix_B = np.array([[1.0], [2.0]])              # A column vector
    
    print("Matrix A:")
    print(matrix_A)
    print("\nMatrix B:")
    print(matrix_B)
    
    steps = prover.matrix_operations(matrix_A.tolist(), matrix_B.tolist())
    print(format_hybrid_proof(steps))
    
    print("\nTesting with singular matrix:")
    singular_matrix = np.array([[1.0, 1.0], [2.0, 2.0]])  # A singular matrix
    steps = prover.matrix_operations(singular_matrix.tolist())
    print(format_hybrid_proof(steps))