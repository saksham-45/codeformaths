# This file has been moved to the proof_solver directory.
# Please update your imports accordingly.
# Original location: /Users/saksham/codeformaths/lightweight_prover.py

<content of lightweight_prover.py>
from dataclasses import dataclass
from typing import List, Dict, Optional
import re

@dataclass
class MathPattern:
    pattern: str
    solution_template: str
    verification_rules: List[str]

class LightweightProver:
    def __init__(self):
        # Comprehensive pattern database organized by mathematical domains
        self.patterns = {
            # Inequality Patterns
            "inequality_chain": MathPattern(
                pattern=r"([\w\d]+)\s*([<>])\s*([\w\d]+)\s*(?:and|∧)\s*([\w\d]+)\s*([<>])\s*([\w\d]+)",
                solution_template="transitive_inequality",
                verification_rules=["check_transitivity"]
            ),
            "product_sign": MathPattern(
                pattern=r"([\w\d]+)\s*[<>]\s*0\s*(?:and|∧)\s*([\w\d]+)·([\w\d]+)\s*[<>]\s*0",
                solution_template="sign_rule",
                verification_rules=["check_sign_consistency"]
            ),
            "triangle_inequality": MathPattern(
                pattern=r"\|([^|]+)\s*\+\s*([^|]+)\|\s*([<≤])\s*\|([^|]+)\|\s*\+\s*\|([^|]+)\|",
                solution_template="triangle_inequality",
                verification_rules=["check_absolute_values"]
            ),
            
            # Equality and Identity Patterns
            "quadratic_identity": MathPattern(
                pattern=r"([\w\d]+)\^2\s*([+-])\s*2([\w\d]+)([\w\d]+)\s*\+\s*([\w\d]+)\^2",
                solution_template="perfect_square",
                verification_rules=["check_quadratic_form"]
            ),
            "difference_squares": MathPattern(
                pattern=r"([\w\d]+)\^2\s*-\s*([\w\d]+)\^2",
                solution_template="difference_of_squares",
                verification_rules=["check_factorization"]
            ),
            
            # Set Theory Patterns
            "set_inclusion": MathPattern(
                pattern=r"([\w\d]+)\s*⊆\s*([\w\d]+)\s*(?:and|∧)\s*([\w\d]+)\s*⊆\s*([\w\d]+)",
                solution_template="set_transitivity",
                verification_rules=["check_set_inclusion"]
            ),
            
            # Number Theory Patterns
            "divisibility": MathPattern(
                pattern=r"([\w\d]+)\s*\|\s*([\w\d]+)\s*(?:and|∧)\s*([\w\d]+)\s*\|\s*([\w\d]+)",
                solution_template="divisibility_chain",
                verification_rules=["check_divisibility"]
            ),
            "modular_arithmetic": MathPattern(
                pattern=r"([\w\d]+)\s*≡\s*([\w\d]+)\s*\(mod\s*([\w\d]+)\)",
                solution_template="modular_congruence",
                verification_rules=["check_modular"]
            ),
            
            # Logical Implications
            "if_then_chain": MathPattern(
                pattern=r"if\s*(.*?)\s*then\s*(.*?)\s*(?:and|∧)\s*if\s*(.*?)\s*then\s*(.*)",
                solution_template="logical_chain",
                verification_rules=["check_logical_implication"]
            ),
            
            # Sequence Patterns
            "arithmetic_sequence": MathPattern(
                pattern=r"([\w\d]+)_n\s*=\s*([\w\d]+)\s*\+\s*([\w\d]+)n",
                solution_template="arithmetic_progression",
                verification_rules=["check_sequence_form"]
            ),
            "geometric_sequence": MathPattern(
                pattern=r"([\w\d]+)_n\s*=\s*([\w\d]+)\s*\*\s*([\w\d]+)\^n",
                solution_template="geometric_progression",
                verification_rules=["check_sequence_form"]
            ),
            
            # Function Properties
            "function_composition": MathPattern(
                pattern=r"f\(([\w\d]+)\)\s*=\s*(.*?)\s*,\s*g\(([\w\d]+)\)\s*=\s*(.*)",
                solution_template="compose_functions",
                verification_rules=["check_function_domains"]
            ),
            
            # Calculus Patterns
            "limit_definition": MathPattern(
                pattern=r"lim_{([\w\d]+)→([\w\d]+)}\s*(.*)",
                solution_template="limit_evaluation",
                verification_rules=["check_limit_exists"]
            )
        }
        
        # Quick lookup tables for common math rules
        self.sign_rules = {
            ("negative", "positive"): "negative",
            ("negative", "negative"): "positive",
            ("positive", "positive"): "positive",
            ("positive", "negative"): "negative"
        }
    
    def identify_pattern(self, problem: str) -> Optional[MathPattern]:
        """Quickly identify which pattern matches the problem"""
        for pattern_name, pattern in self.patterns.items():
            if re.search(pattern.pattern, problem):
                return pattern
        return None
    
    def generate_proof(self, problem: str) -> List[str]:
        """Generate a proof based on pattern matching"""
        pattern = self.identify_pattern(problem)
        if not pattern:
            return ["Cannot identify a known pattern in this problem"]
            
        steps = []
        # Extract components using regex
        match = re.search(pattern.pattern, problem)
        if match:
            groups = match.groups()
            handler_map = {
                "transitive_inequality": self._handle_transitivity,
                "sign_rule": self._handle_sign_rules,
                "triangle_inequality": self._handle_triangle_inequality,
                "perfect_square": self._handle_perfect_square,
                "difference_of_squares": self._handle_difference_of_squares,
                "set_transitivity": self._handle_set_inclusion,
                "divisibility_chain": self._handle_divisibility,
                "modular_congruence": self._handle_modular,
                "logical_chain": self._handle_logical_chain,
                "arithmetic_progression": self._handle_arithmetic_progression,
                "geometric_progression": self._handle_geometric_progression
            }
            
            handler = handler_map.get(pattern.solution_template)
            if handler:
                steps = handler(groups)
            else:
                steps = ["Pattern recognized but handler not implemented yet"]
        
        return steps
    
    def _handle_transitivity(self, components) -> List[str]:
        return [
            f"Given: {components[0]} {components[1]} {components[2]}",
            f"Given: {components[3]} {components[4]} {components[5]}",
            "Apply transitivity of inequalities",
            f"Therefore: {components[0]} {components[1]} {components[5]}"
        ]
    
    def _handle_sign_rules(self, components) -> List[str]:
        return [
            f"Given: {components[0]} < 0",
            f"Given: {components[1]}·{components[2]} > 0",
            "Apply sign rules for products",
            f"Therefore: {components[2]} < 0"
        ]
        
    def _handle_triangle_inequality(self, components) -> List[str]:
        return [
            f"Consider: |{components[0]} + {components[1]}|",
            f"By triangle inequality: |a + b| ≤ |a| + |b|",
            f"Therefore: |{components[0]} + {components[1]}| ≤ |{components[0]}| + |{components[1]}|"
        ]
    
    def _handle_perfect_square(self, components) -> List[str]:
        return [
            f"Identify the perfect square pattern: a² ± 2ab + b²",
            f"Group terms: ({components[0]}² {components[1]} 2{components[2]}{components[3]} + {components[4]}²)",
            f"This is equivalent to: ({components[0]} {components[1]} {components[4]})²"
        ]
    
    def _handle_difference_of_squares(self, components) -> List[str]:
        return [
            f"Pattern: a² - b² = (a+b)(a-b)",
            f"Therefore: {components[0]}² - {components[1]}² = ",
            f"({components[0]} + {components[1]})({components[0]} - {components[1]})"
        ]
    
    def _handle_set_inclusion(self, components) -> List[str]:
        return [
            f"Given: {components[0]} ⊆ {components[1]}",
            f"Given: {components[1]} ⊆ {components[2]}",
            "By transitivity of set inclusion",
            f"Therefore: {components[0]} ⊆ {components[2]}"
        ]
    
    def _handle_divisibility(self, components) -> List[str]:
        return [
            f"Given: {components[0]} | {components[1]}",
            f"Given: {components[1]} | {components[2]}",
            "By transitivity of divisibility",
            f"Therefore: {components[0]} | {components[2]}"
        ]
    
    def _handle_modular(self, components) -> List[str]:
        return [
            f"Given: {components[0]} ≡ {components[1]} (mod {components[2]})",
            f"This means: {components[0]} = {components[1]} + k{components[2]}, for some integer k"
        ]
    
    def _handle_logical_chain(self, components) -> List[str]:
        return [
            f"Given: if {components[0]} then {components[1]}",
            f"Given: if {components[2]} then {components[3]}",
            "By logical chaining",
            f"Therefore: if {components[0]} and {components[2]} then {components[1]} and {components[3]}"
        ]
    
    def _handle_arithmetic_progression(self, components) -> List[str]:
        return [
            f"Sequence: {components[0]}_n = {components[1]} + {components[2]}n",
            f"First term a = {components[1]}",
            f"Common difference d = {components[2]}"
        ]
    
    def _handle_geometric_progression(self, components) -> List[str]:
        return [
            f"Sequence: {components[0]}_n = {components[1]} · {components[2]}^n",
            f"First term a = {components[1]}",
            f"Common ratio r = {components[2]}"
        ]

def solve_math_problem(problem: str) -> str:
    """Quick interface to solve math problems"""
    prover = LightweightProver()
    steps = prover.generate_proof(problem)
    
    return "\n".join([
        "Proof:",
        "=" * 40,
        *[f"Step {i+1}: {step}" for i, step in enumerate(steps)]
    ])

if __name__ == "__main__":
    test_problems = [
        ("Transitivity", "x < y and y < z"),
        ("Sign Rules", "α < 0 and α·β > 0"),
        ("Perfect Square", "x^2 + 2xy + y^2"),
        ("Difference of Squares", "a^2 - b^2"),
        ("Set Theory", "A ⊆ B and B ⊆ C"),
        ("Arithmetic Sequence", "a_n = 2 + 3n"),
        ("Geometric Sequence", "g_n = 2 * 3^n"),
        ("Modular Arithmetic", "15 ≡ 3 (mod 4)")
    ]
    
    for name, problem in test_problems:
        print(f"\n{name} Problem: {problem}")
        print("=" * 40)
        print(solve_math_problem(problem))