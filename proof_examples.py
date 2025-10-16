# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/proof_examples.py

<content of proof_examples.py>
from math_proof_assistant import MathProof

def prove_transitive_inequality():
    proof = MathProof()
    
    proof.add_given("x < y")
    proof.add_given("y < z")
    
    proof.add_step("x < y", "Given")
    proof.add_step("y < z", "Given")
    proof.add_step("x < z", "Numbers in order stay in order")
    
    return proof

def prove_zero_product():
    proof = MathProof()
    proof.add_given("ab = 0")
    
    proof.add_step("ab = 0", "Given")
    proof.add_step("a = 0 or b = 0", "Zero product rule")
    
    return proof

if __name__ == "__main__":
    print("Proof: Order Property")
    prove_transitive_inequality().display_proof()
    
    print("\nProof: Zero Products")
    prove_zero_product().display_proof()