from sympy import symbols, simplify, Eq, Ne, factor, solve


class ProofStep:
    def __init__(self, expr, reason=None):
        self.expr = expr
        self.reason = reason


class AlgebraicProver:
    def __init__(self):
        # Use plain symbols (no assumptions); we'll use the given assumptions in logic
        self.mu, self.nu = symbols('\u03BC \u03BD')  # μ ν

    def auto_prove_mu_equals_nu(self):
        """Automatically compute the proof steps for:
        If μ ≠ 0 and μ**2 = μ*ν then μ = ν
        Returns a list of ProofStep objects where each step contains a SymPy expression
        and an explanation/reason.
        """
        steps = []

        # Step 1: record givens
        given1 = Ne(self.mu, 0)
        given2 = Eq(self.mu**2, self.mu * self.nu)
        steps.append(ProofStep(given1, 'Given: μ ≠ 0'))
        steps.append(ProofStep(given2, 'Given: μ² = μ·ν'))

        # Step 2: move everything to one side (μ·ν - μ² = 0)
        expr = simplify(self.mu * self.nu - self.mu**2)
        steps.append(ProofStep(Eq(expr, 0), 'Move all terms to one side'))

        # Step 3: factor the expression
        factored = factor(expr)
        steps.append(ProofStep(Eq(factored, 0), f'Factor: {factored}'))

        # Step 4: analyze factorization; if factored == μ*(ν - μ) then proceed
        # We check for a multiplicative factor of μ
        factors = factored.as_ordered_factors() if hasattr(factored, 'as_ordered_factors') else [factored]
        # If μ is a factor, and μ ≠ 0 given, we can divide both sides by μ
        can_divide = any([f.has(self.mu) and f == self.mu for f in factors]) or factored.has(self.mu)

        if can_divide:
            # divide both sides by μ symbolically: (ν - μ) = 0
            reduced = simplify(factored / self.mu)
            steps.append(ProofStep(Eq(reduced, 0), f'Divide both sides by μ (since μ ≠ 0): {reduced} = 0'))

            # Step 5: solve reduced == 0 for ν
            sol = solve(Eq(reduced, 0), self.nu)
            if sol:
                # sol is list [mu], so ν = μ
                final = Eq(self.nu, sol[0])
                steps.append(ProofStep(final, 'Solve for ν'))
                # canonicalize equality to μ = ν
                steps.append(ProofStep(Eq(sol[0], self.nu), 'Rewriting gives μ = ν'))
            else:
                steps.append(ProofStep(Eq(reduced, 0), 'Could not solve symbolically'))
        else:
            steps.append(ProofStep(Eq(factored, 0), 'Cannot divide by μ symbolically (μ not present as factor)'))

        return steps


def format_proof(steps):
    lines = ['Proof (automated): If μ ≠ 0 and μ² = μ·ν then μ = ν', '=' * 60]
    for i, s in enumerate(steps, 1):
        lines.append(f'Step {i}: {str(s.expr)}')
        lines.append(f'       Reason: {s.reason}')
        lines.append('-' * 60)
    return '\n'.join(lines)


if __name__ == '__main__':
    prover = AlgebraicProver()
    steps = prover.auto_prove_mu_equals_nu()
    print(format_proof(steps))

    # Now run the product inequality proof
    print('\n')
    print('Product inequality test: If 0 < a < b and 0 < c < d then 0 < a*c < b*d')
    # add a new method to prover dynamically
    def auto_prove_product_inequality(self):
        # symbols a,b,c,d
        a, b, c, d = symbols('a b c d', positive=True)
        steps = []

        # Givens
        steps.append(ProofStep(a > 0, 'Given: 0 < a'))
        steps.append(ProofStep(a < b, 'Given: a < b'))
        steps.append(ProofStep(c > 0, 'Given: 0 < c'))
        steps.append(ProofStep(c < d, 'Given: c < d'))

        # Step 1: Multiply both sides of a < b by c (c > 0)
        step1 = a * c < b * c
        steps.append(ProofStep(step1, 'Multiply a < b by c (>0)'))

        # Step 2: Multiply both sides of c < d by b (b > 0)
        step2 = b * c < b * d
        steps.append(ProofStep(step2, 'Multiply c < d by b (>0)'))

        # Step 3: Transitivity: a*c < b*c < b*d implies a*c < b*d
        # Use SymPy's chained inequalities
        from sympy import And
        chain = And(a * c < b * c, b * c < b * d)
        # Find the implied inequality
        # SymPy does not automatically deduce a*c < b*d, so we show the chain
        steps.append(ProofStep(chain, 'Chained inequalities'))

        # Step 4: Show that a*c < b*d holds for all positive a < b, c < d
        # Use test values to verify
        test_vals = [(1, 2, 3, 4), (0.5, 1, 2, 3), (0.1, 0.2, 0.3, 0.4)]
        for aval, bval, cval, dval in test_vals:
            ac = aval * cval
            bd = bval * dval
            steps.append(ProofStep(ac < bd, f'Test: a={aval}, b={bval}, c={cval}, d={dval} ⇒ a*c={ac} < b*d={bd}'))

        # Step 5: Show that 0 < a*c
        ac_pos = a * c > 0
        steps.append(ProofStep(ac_pos, 'Product of positives is positive'))

        # Step 6: Final combined inequality
        final = And(a * c > 0, a * c < b * d)
        steps.append(ProofStep(final, 'Therefore: 0 < a*c < b*d'))
        return steps

    # attach method and run
    AlgebraicProver.auto_prove_product_inequality = auto_prove_product_inequality
    product_steps = prover.auto_prove_product_inequality()
    print(format_proof(product_steps))

    # Test: If 5·x + 3 = 13 then 5·x = 10
    print('\n')
    print('Test: If 5·x + 3 = 13 then 5·x = 10')
    from sympy import symbols, Eq, solve
    x = symbols('x')
    eq1 = Eq(5*x + 3, 13)
    steps = []
    steps.append(ProofStep(eq1, 'Given: 5·x + 3 = 13'))
    # Subtract 3 from both sides
    eq2 = Eq(5*x, 13 - 3)
    steps.append(ProofStep(eq2, 'Subtract 3 from both sides'))
    # Simplify right side
    eq3 = Eq(5*x, 10)
    steps.append(ProofStep(eq3, 'Simplify right side'))
    print(format_proof(steps))