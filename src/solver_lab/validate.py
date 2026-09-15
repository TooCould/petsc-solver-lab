"""TODO: finite inputs, CSR integrity, true residual and solution error.

External acceptance: ||b-Ax|| <= max(atol, rtol*||b||).
Handle zero RHS explicitly; symmetry alone does not establish SPD.
"""


def check_inputs(matrix, rhs):
    raise NotImplementedError("待实现输入与矩阵检查。")


def check_solution(matrix, rhs, solution, reference, rtol, atol):
    raise NotImplementedError("待实现独立残差和解误差验证。")
