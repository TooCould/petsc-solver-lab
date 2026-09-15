"""TODO D8: reproducible faults and explicit result status."""

STATUSES = (
    "success", "not_converged", "residual_check_failed", "invalid_input",
    "incompatible_solver", "backend_unavailable",
)


def run_case(case_name):
    raise NotImplementedError(f"故障案例 {case_name} 待实现。")
