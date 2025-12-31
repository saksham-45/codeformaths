import numpy as np
from sympy import Matrix
from functools import lru_cache

# ======== Caching using Python Hashmaps (dict) + LRU ========

@lru_cache(maxsize=32)
def compute_eigen_data(matrix_tuple):
    """
    Cached eigenvalue/eigenspace computation.
    Input matrix is passed as tuple-of-tuples (hashable).
    """
    M = Matrix(matrix_tuple)
    
    # Eigenvalues (exact symbolic)
    eigenvals = M.eigenvals()   # dict: {eigenvalue: algebraic_multiplicity}
    
    # Eigenspaces
    eigenspaces = {}
    for val in eigenvals:
        eigenspaces[val] = M.eigenvects()  # will filter later
    
    return eigenvals, eigenspaces


def get_eigenspaces(matrix_tuple):
    M = Matrix(matrix_tuple)
    eigvecs = M.eigenvects()

    eigenspaces = {}
    for eigenvalue, algebraic_multiplicity, eigspace_basis in eigvecs:
        eigenspaces[eigenvalue] = {
            "algebraic_multiplicity": algebraic_multiplicity,
            "geometric_multiplicity": len(eigspace_basis),
            "basis": eigspace_basis
        }
    return eigenspaces


# ======== Main Function: Eigenvalues, Eigenspaces, Diagonalization ========

def analyze_matrix(A):
    """
    A: Python list of lists (matrix)
    
    Returns eigenvalues, eigenspaces, and diagonalization info.
    """
    A_np = np.array(A, dtype=float)
    M = Matrix(A)

    # Convert to hashable tuple for caching
    A_tuple = tuple(tuple(row) for row in A)

    # fetch eigenvalues + eigenspaces (cached)
    eigenvals, _ = compute_eigen_data(A_tuple)

    eigenspaces = get_eigenspaces(A_tuple)

    # Try diagonalization
    try:
        P, D = M.diagonalize()
        diagonalizable = True
    except:
        P, D = None, None
        diagonalizable = False

    return {
        "eigenvalues": eigenvals,
        "eigenspaces": eigenspaces,
        "diagonalizable": diagonalizable,
        "P": P,
        "D": D
    }


# ======== Example Usage ========

if __name__ == "__main__":
    A = [
        [4, 1, 0],
        [0, 4, 0],
        [0, 0, 2]
    ]

    result = analyze_matrix(A)

    print("\n--- Eigenvalues ---")
    for val, mult in result["eigenvalues"].items():
        print(f"λ = {val}, multiplicity = {mult}")

    print("\n--- Eigenspaces ---")
    for val, data in result["eigenspaces"].items():
        print(f"\nEigenvalue λ = {val}")
        print(f"Algebraic multiplicity: {data['algebraic_multiplicity']}")
        print(f"Geometric multiplicity: {data['geometric_multiplicity']}")
        print("Basis vectors:")
        for b in data["basis"]:
            print("   ", b)

    print("\n--- Diagonalizable? ---")
    print(result["diagonalizable"])

    if result["diagonalizable"]:
        print("\nP (eigenvector matrix):")
        print(result["P"])
        print("\nD (diagonal matrix):")
        print(result["D"])