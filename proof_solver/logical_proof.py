# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/logical_proof.py

<content of logical_proof.py>
from z3 import *

class LogicalProof:
    def __init__(self):
        self.solver = Solver()
        self.steps = []
        
    def add_premise(self, expr, explanation):
        """Add a premise to the proof"""
        self.solver.add(expr)
        self.steps.append(("Premise", str(expr), explanation))
    
    def verify_conclusion(self, conclusion, explanation):
        """Verify if conclusion follows from premises"""
        # Check if premises → conclusion is valid
        # by checking if premises ∧ ¬conclusion is unsatisfiable
        s = Solver()
        s.add(self.solver.assertions())
        s.add(Not(conclusion))
        
        if s.check() == unsat:
            self.steps.append(("Conclusion", str(conclusion), explanation))
            return True
        return False
    
    def display(self):
        print("\nLogical Proof with Verification")
        print("-" * 50)
        print("Statement".ljust(35) + "| Reason")
        print("-" * 50)
        for step_type, expr, reason in self.steps:
            print(f"{expr}".ljust(35) + f"| {reason}")

def prove_negative_multiplication():
    # Create real-valued variables
    alpha, beta = Reals('alpha beta')
    proof = LogicalProof()
    
    # Add premises
    proof.add_premise(alpha < 0, "Given: α is negative")
    proof.add_premise(alpha * beta > 0, "Given: α·β is positive")
    
    # Verify conclusion
    proof.verify_conclusion(beta < 0, "Therefore β must be negative")
    
    return proof

if __name__ == "__main__":
    print("Proving: If α < 0 and α·β > 0, then β < 0")
    proof = prove_negative_multiplication()
    proof.display()