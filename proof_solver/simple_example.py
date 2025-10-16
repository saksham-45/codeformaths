# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/simple_example.py

<content of simple_example.py>
from math_proof_assistant import MathProof

# Let's prove: If x > 0 and y > 0, then x + y > 0
def prove_sum_positive():
    # Start a new proof
    my_proof = MathProof()
    
    # Write down what we know (like the "given" section in your homework)
    my_proof.add_given("x > 0")
    my_proof.add_given("y > 0")
    
    # Now let's write our proof steps (like in a two-column proof)
    my_proof.add_step("x > 0", "Given")
    my_proof.add_step("y > 0", "Given")
    my_proof.add_step("Adding positives gives positive", "Basic rule")
    my_proof.add_step("x + y > 0", "Therefore, sum is positive")
    
    return my_proof

# Let's run it and see how it looks
if __name__ == "__main__":
    print("Proving that sum of positives is positive:")
    proof = prove_sum_positive()
    proof.display_proof()