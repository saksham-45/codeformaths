# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/sympy_prover.py

<content of sympy_prover.py>
from sympy import (
    symbols, solve, Interval, And, Or, Implies,
    simplify, expand, factor, Symbol, S, Q,
    ask, refine, Abs, sin, cos, tan,
    limit, oo, integrate, diff
)
from typing import List, Dict, Optional, Tuple, Union, Any
from dataclasses import dataclass

@dataclass
class SymbolicProofStep:
    statement: str
    symbolic_form: Any  # Can be any SymPy expression
    reason: str

class AdvancedProver:
    def __init__(self):
        # Common mathematical symbols
        self.x, self.y, self.z = symbols('x y z')
        self.a, self.b, self.c = symbols('a b c')
        self.n = Symbol('n', integer=True)  # for sequence proofs
        self.alpha, self.beta = symbols('alpha beta')

    def prove_inequality(self, expr_str: str) -> List[SymbolicProofStep]:
        """Prove inequalities using SymPy's assumptions and refine"""
        try:
            # Convert string to symbolic expression
            expr = simplify(expr_str)
            steps = []
            
            # Check if it's an inequality
            if '>' in expr_str or '<' in expr_str:
                # Parse the inequality
                left, right = str(expr).split('>') if '>' in str(expr) else str(expr).split('<')
                left = simplify(left)
                right = simplify(right)
                
                # Try to prove using assumptions
                result = ask(Q.positive(left - right)) if '>' in str(expr) else ask(Q.negative(left - right))
                
                steps.append(SymbolicProofStep(
                    f"Starting with: {expr}",
                    expr,
                    "Initial expression"
                ))
                
                # Try different proof strategies
                simplified = simplify(left - right)
                if simplified != left - right:
                    steps.append(SymbolicProofStep(
                        f"Simplify to: {simplified} {'> 0' if '>' in str(expr) else '< 0'}",
                        simplified,
                        "Algebraic simplification"
                    ))
                
                factored = factor(simplified)
                if factored != simplified:
                    steps.append(SymbolicProofStep(
                        f"Factor as: {factored} {'> 0' if '>' in str(expr) else '< 0'}",
                        factored,
                        "Factorization"
                    ))
                
                steps.append(SymbolicProofStep(
                    f"Therefore, the inequality is {'valid' if result else 'not proven'}",
                    result,
                    "SymPy verification"
                ))
                
            return steps
        except Exception as e:
            return [SymbolicProofStep(f"Error in proof: {str(e)}", None, "Error")]

    def prove_limit(self, expr_str: str, var_str: str, point_str: str) -> List[SymbolicProofStep]:
        """Prove limit statements using SymPy's limit capabilities"""
        try:
            var = Symbol(var_str)
            expr = simplify(expr_str)
            point = simplify(point_str)
            
            steps = []
            steps.append(SymbolicProofStep(
                f"Evaluating limit of {expr} as {var} → {point}",
                expr,
                "Initial expression"
            ))
            
            # Try direct substitution first
            try:
                direct = expr.subs(var, point)
                steps.append(SymbolicProofStep(
                    f"Try direct substitution: {direct}",
                    direct,
                    "Direct substitution"
                ))
            except:
                pass
            
            # Calculate the limit
            lim = limit(expr, var, point)
            steps.append(SymbolicProofStep(
                f"The limit equals: {lim}",
                lim,
                "Limit evaluation"
            ))
            
            return steps
        except Exception as e:
            return [SymbolicProofStep(f"Error in limit proof: {str(e)}", None, "Error")]

    def prove_derivative(self, expr_str: str, var_str: str) -> List[SymbolicProofStep]:
        """Prove derivative calculations step by step"""
        try:
            var = Symbol(var_str)
            expr = simplify(expr_str)
            
            steps = []
            steps.append(SymbolicProofStep(
                f"Finding derivative of {expr} with respect to {var}",
                expr,
                "Initial expression"
            ))
            
            # Calculate derivative
            derivative = diff(expr, var)
            steps.append(SymbolicProofStep(
                f"Apply differentiation rules: {derivative}",
                derivative,
                "Differentiation"
            ))
            
            # Simplify if possible
            simplified = simplify(derivative)
            if simplified != derivative:
                steps.append(SymbolicProofStep(
                    f"Simplify to: {simplified}",
                    simplified,
                    "Simplification"
                ))
            
            return steps
        except Exception as e:
            return [SymbolicProofStep(f"Error in derivative proof: {str(e)}", None, "Error")]

    def prove_integral(self, expr_str: str, var_str: str) -> List[SymbolicProofStep]:
        """Prove integral calculations step by step"""
        try:
            var = Symbol(var_str)
            expr = simplify(expr_str)
            
            steps = []
            steps.append(SymbolicProofStep(
                f"Finding indefinite integral of {expr} with respect to {var}",
                expr,
                "Initial expression"
            ))
            
            # Calculate integral
            integral = integrate(expr, var)
            steps.append(SymbolicProofStep(
                f"Apply integration rules: {integral} + C",
                integral,
                "Integration"
            ))
            
            # Verify by differentiation
            verification = diff(integral, var)
            steps.append(SymbolicProofStep(
                f"Verify by differentiation: d/d{var}({integral}) = {verification}",
                verification,
                "Verification"
            ))
            
            return steps
        except Exception as e:
            return [SymbolicProofStep(f"Error in integral proof: {str(e)}", None, "Error")]

    def prove_identity(self, expr_str: str) -> List[SymbolicProofStep]:
        """Prove algebraic identities step by step"""
        try:
            expr = simplify(expr_str)
            steps = []
            
            # Original expression
            steps.append(SymbolicProofStep(
                f"Starting with: {expr}",
                expr,
                "Initial expression"
            ))
            
            # Try expansion
            expanded = expand(expr)
            if expanded != expr:
                steps.append(SymbolicProofStep(
                    f"Expand to: {expanded}",
                    expanded,
                    "Expansion"
                ))
            
            # Try factoring
            factored = factor(expanded)
            if factored != expanded:
                steps.append(SymbolicProofStep(
                    f"Factor as: {factored}",
                    factored,
                    "Factorization"
                ))
            
            # Try simplification
            simplified = simplify(factored)
            if simplified != factored:
                steps.append(SymbolicProofStep(
                    f"Simplify to: {simplified}",
                    simplified,
                    "Simplification"
                ))
            
            return steps
        except Exception as e:
            return [SymbolicProofStep(f"Error in identity proof: {str(e)}", None, "Error")]

def format_proof(steps: List[SymbolicProofStep]) -> str:
    """Format proof steps nicely"""
    result = ["Proof:", "=" * 40]
    for i, step in enumerate(steps, 1):
        result.append(f"Step {i}: {step.statement}")
        result.append(f"       Reason: {step.reason}")
        result.append("-" * 40)
    return "\n".join(result)

if __name__ == "__main__":
    prover = AdvancedProver()
    
    # Test cases
    print("\nTesting inequality proof:")
    steps = prover.prove_inequality("x**2 + 2*x + 1 > 0")
    print(format_proof(steps))
    
    print("\nTesting limit proof:")
    steps = prover.prove_limit("sin(x)/x", "x", "0")
    print(format_proof(steps))
    
    print("\nTesting derivative proof:")
    steps = prover.prove_derivative("x**3 + 3*x**2 + 3*x + 1", "x")
    print(format_proof(steps))
    
    print("\nTesting integral proof:")
    steps = prover.prove_integral("x**2 + 2*x", "x")
    print(format_proof(steps))
    
    print("\nTesting algebraic identity proof:")
    steps = prover.prove_identity("(x + y)**2 - (x - y)**2")
    print(format_proof(steps))