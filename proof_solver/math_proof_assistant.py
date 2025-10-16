# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/math_proof_assistant.py

<content of math_proof_assistant.py>
class MathStatement:
    def __init__(self, statement, is_assumption=False):
        self.statement = statement
        self.is_assumption = is_assumption
        self.reason = None

class ProofStep:
    def __init__(self, statement, reason):
        self.statement = statement
        self.reason = reason

class MathProof:
    def __init__(self, givens=None):
        self.givens = givens if givens else []
        self.steps = []
        self.rules = {
            "products": "Product sign changes with negative numbers",
            "transitivity": "Order carries through inequalities",
            "negatives": "Negative multiplication reverses inequality",
            "zero": "Product is zero only if a factor is zero",
            "equals": "Values equal to same thing are equal to each other"
        }

    def add_given(self, statement):
        self.givens.append(MathStatement(statement, is_assumption=True))

    def add_step(self, statement, reason):
        self.steps.append(ProofStep(statement, reason))

    def display_proof(self):
        print("\nTwo-Column Proof")
        print("-" * 50)
        print("Givens:")
        for given in self.givens:
            print(f"• {given.statement}")
        
        print("\nProof:")
        print("-" * 50)
        print("Statement".ljust(30) + "| Reason")
        print("-" * 50)
        
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step.statement}".ljust(30) + f"| {step.reason}")

# Example usage
def prove_negative_product():
    proof = MathProof()
    
    proof.add_given("a < 0")
    proof.add_given("a·b < 0")
    
    proof.add_step("a < 0", "Given")
    proof.add_step("a·b < 0", "Given")
    proof.add_step("When dividing by a negative", "Negatives rule")
    proof.add_step("b > 0", "Sign changes")
    
    return proof

if __name__ == "__main__":
    proof = prove_negative_product()
    proof.display_proof()