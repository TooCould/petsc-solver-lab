"""TODO: CSR/AIJ conversion and PETSc binary files for C++ reuse."""


def to_petsc(csr_matrix):
    """Check scalar/index types, dimensions, nnz and SpMV equivalence."""
    raise NotImplementedError("待实现 CSR/AIJ 转换。")


def save_system(matrix, rhs, output_prefix):
    raise NotImplementedError("待实现 PETSc 二进制系统导出。")


def load_system(input_prefix):
    raise NotImplementedError("待实现 PETSc 二进制系统加载。")
