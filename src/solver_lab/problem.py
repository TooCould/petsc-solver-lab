"""TODO D2: five-point Poisson CSR and discrete/continuous RHS.

Only interior unknowns, p=j*n+i, h=1/(n+1), nnz=5*n*n-4*n.
Use a deterministic multicomponent reference vector for timing cases.
"""


def build_problem(n, rhs_mode="discrete", seed=2026):
    """Return CSR matrix, RHS, reference solution and problem metadata."""
    raise NotImplementedError("待实现 Poisson 系统和两类右端项。")
