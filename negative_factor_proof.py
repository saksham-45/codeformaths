# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/negative_factor_proof.py

<content of negative_factor_proof.py>
from math_proof_assistant import MathProof

def prove_negative_factor():
    proof = MathProof()
    
    # Our givens using alpha (α) and beta (β)
    proof.add_given("α < 0")                    # α is negative
    proof.add_given("α·β > 0")                  # their product is positive
    
    proof.add_step("α < 0", "Given")
    proof.add_step("α·β > 0", "Given")
    proof.add_step("When dividing by α (negative)", "Division rule")
    proof.add_step("The inequality sign flips", "Negative division property")
    proof.add_step("β < 0", "Therefore β is negative")
    
    return proof

if __name__ == "__main__":
    print("Proof: If α < 0 and α·β > 0, then β < 0")
    print("(If α ∈ R⁻ ∧ α·β ∈ R⁺, then β ∈ R⁻)")
    proof = prove_negative_factor()
    proof.display_proof()