# Totally Unimodular Checker

A Jupyter Notebook that verifies whether a given matrix is **Totally Unimodular (TU)** — a property with important consequences in linear programming, combinatorial optimization, and graph theory.

This project was developed as a university assignment on algorithm modeling and implementation.

---

## What Is a Totally Unimodular Matrix?

A matrix $A$ is called **totally unimodular** if the determinant of **every** square submatrix $B$ (obtained by deleting any subset of rows and columns) satisfies:

$$\det(B) \in \{-1, 0, 1\}$$

Note that the condition applies to **all** square submatrices, not only to the matrix itself. This makes full verification computationally expensive in general, and the algorithm must enumerate all relevant combinations.

---

## Why Does TU Matter?

Totally unimodular matrices play a central role in optimization and combinatorics:

- **Integer solutions from linear programs:** If the constraint matrix of a linear program is TU, then the vertices of the feasible polyhedron are integral. Solving the LP therefore yields an integer optimal solution directly.
- **Network problems:** Incidence matrices of graphs are classic examples of TU matrices. This includes problems such as maximum flow, shortest path, and matching.
- **Transportation and assignment problems:** Their constraint matrices are TU, so LP solvers can be used instead of integer programming solvers.
- **Integer linear programming (ILP):** When the constraint matrix is TU, the LP relaxation is exact and branch-and-bound is unnecessary.
- **Graph theory and combinatorics:** TU matrices are a key tool for proving properties of incidence matrices and network structures.

---

## Components

| Component | Description |
|-----------|-------------|
| `evaluation(matrix)` | Validates the input: must be a non-empty 2D matrix with entries in `{-1, 0, 1}` |
| `submatrix(matrix)` | Generates all square submatrices of every possible size |
| `determinant_laplace(matrix)` | Computes determinants using Laplace (cofactor) expansion |
| `determinant_bareiss(matrix)` | Computes determinants using the Bareiss algorithm (exact for integer matrices) |
| `is_totally_unimodular(matrix, method=...)` | Main function: checks whether the matrix is TU using the selected method |
| Testing section | Examples and automated tests |

---

## Usage Example

```python
A = [
    [-1, 0, 0],
    [ 1, 1, 0],
    [ 0,-1,-1]
]

result = is_totally_unimodular(A)
print(result["result"])
print("Determinants calculated:", result["determinant_runs"])