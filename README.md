

#  Linear Algebra Toolkit  
### *Gauss–Jordan Elimination • Eigenvalues • Eigenspaces • Diagonalization*

This repository provides a clean, optimized Python toolkit for fundamental linear-algebra operations frequently used in:

- University coursework  
- Exam proofs  
- Computational mathematics  
- Machine learning  
- Engineering/scientific computing  

It performs:

- ✅ **Gauss–Jordan elimination (RREF)**
- ✅ **Eigenvalues (symbolic)**
- ✅ **Eigenspaces**
- ✅ **Diagonalization**
- ⚡ **Caching optimizations** (hashmaps + LRU cache)
-  Powered by **NumPy** + **SymPy**

---

##  Features

###  1. Symbolic Eigenvalue Computation
The tool uses SymPy for **exact eigenvalues**, not floating approximations.

Example:
```
λ = 4 (multiplicity 2)
λ = 2 (multiplicity 1)
```

###  2. Eigenspaces (Basis, Algebraic + Geometric Multiplicities)
For every eigenvalue λ, the script computes:

- Algebraic multiplicity  
- Geometric multiplicity  
- Basis vectors for the eigenspace  

This completely characterizes the linear operator.

###  3. Automatic Diagonalization
The script attempts to factor the matrix as:

\[
A = P D P^{-1}
\]

Where:
- **D** is a diagonal matrix of eigenvalues  
- **P** is the matrix of eigenvectors  

If this decomposition fails, the matrix is **not diagonalizable**.

###  4. Gauss–Jordan Elimination (RREF)
Useful for:
- Solving linear systems  
- Determining independence  
- Computing rank  
- Proofs involving diagonalizability  

###  5. ⚡ Caching via Hashmaps + `functools.lru_cache`
To avoid recomputing symbolic eigenvalues (which is expensive), matrices are cached:

```python
@lru_cache(maxsize=32)
def compute_eigen_data(matrix_tuple):
    ...
```

Matrices are converted to hashable tuples for dictionary-style lookup.

---

##  Installation

```bash
git clone https://github.com/<your-username>/codeformaths
cd codeformaths
pip install numpy sympy
```

---

## 🧪 Usage Example

### `diagonlize.py`

```python
from diagonlize import analyze_matrix

A = [
    [4, 1, 0],
    [0, 4, 0],
    [0, 0, 2]
]

result = analyze_matrix(A)

print(result)
```

### Example Output

```
--- Eigenvalues ---
λ = 4, multiplicity = 2
λ = 2, multiplicity = 1

--- Eigenspaces ---
Eigenvalue λ = 4
Algebraic multiplicity: 2
Geometric multiplicity: 1
Basis vectors:
     Matrix([[1], [0], [0]])

Eigenvalue λ = 2
Algebraic multiplicity: 1
Geometric multiplicity: 1
Basis vectors:
     Matrix([[0], [0], [1]])

--- Diagonalizable? ---
False
```

---

##  Mathematical Foundations  

### **1. Eigenvalues**
The eigenvalues are roots of the characteristic polynomial:

\[
\det(A - \lambda I) = 0
\]

SymPy computes them exactly.

---

### **2. Eigenspaces**
Each eigenspace is computed by solving:

\[
(A - \lambda I)v = 0
\]

The dimension of this null space is the **geometric multiplicity**.

---

### **3. Diagonalizability**
A matrix is diagonalizable iff:

\[
\text{geometric multiplicity of every } \lambda
= \text{algebraic multiplicity}
\]

Otherwise the matrix fails to have a full set of independent eigenvectors.

---

## 📁 Project Structure

```
codeformaths/
│
├── diagonlize.py        # Eigenvalues, eigenspaces, diagonalization
├── gauss_jordan.py      # (recommended extension)
├── README.md            # This file
└── examples/            # Optional examples
```

---

##  License
Open-source under the **MIT License**.

---

##  Contribute
Feel free to open issues or submit pull requests.

---

##  Acknowledgments
Built using:
- **SymPy** for symbolic algebra  
- **NumPy** for efficient numerical matrices  