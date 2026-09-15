"""Runnable scaffold CLI. No numerical results are produced yet."""

import argparse
import importlib
import json
import sys

from .config import read_json, solve_config


def parser():
    root = argparse.ArgumentParser(description="PETSc 稀疏求解工具（框架阶段）")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("check-env", help="检查依赖导入；不代表后端通过验收")
    solve = commands.add_parser("solve", help="单次求解配置")
    solve.add_argument("--config")
    for name in ("n", "seed", "max-it", "restart"):
        solve.add_argument(f"--{name}", type=int)
    for name in ("rtol", "atol"):
        solve.add_argument(f"--{name}", type=float)
    solve.add_argument("--solver", choices=("cg", "gmres", "preonly"))
    solve.add_argument("--pc", choices=("none", "jacobi", "ilu", "hypre", "lu"))
    solve.add_argument("--rhs", choices=("discrete", "continuous"))
    solve.add_argument("--output-dir")
    solve.add_argument("--dry-run", action="store_true")
    batch = commands.add_parser("benchmark", help="批量实验配置")
    batch.add_argument("--config", required=True)
    batch.add_argument("--dry-run", action="store_true")
    diagnose = commands.add_parser("diagnose", help="故障案例（待实现）")
    diagnose.add_argument("--case", required=True,
                          choices=("nonfinite", "not-converged", "incompatible-solver"))
    report = commands.add_parser("report", help="结果报告（待实现）")
    report.add_argument("--input", required=True)
    return root


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def check_env():
    packages = {}
    for name in ("numpy", "scipy", "matplotlib", "petsc4py.PETSc"):
        try:
            module = importlib.import_module(name)
            packages[name] = {"importable": True,
                              "version": getattr(module, "__version__", None)}
        except Exception as exc:
            packages[name] = {"importable": False, "error": str(exc)}
    emit({"python": sys.version, "packages": packages,
          "hypre": "not_verified", "mumps": "not_verified",
          "note": "导入检查不等于求解器后端验收。"})
    return 0 if all(item["importable"] for item in packages.values()) else 1


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "check-env":
            return check_env()
        if args.command == "solve":
            values = read_json(args.config) if args.config else {}
            values.update({key: value for key, value in vars(args).items()
                           if key not in ("command", "config", "dry_run") and value is not None})
            config = solve_config(values)
            if args.dry_run:
                emit({"status": "plan_only", "config": config,
                      "note": "仅预览配置，未构造矩阵或执行求解。"})
                return 0
            from .solve import run
            run(config)
        elif args.command == "benchmark":
            from .benchmark import make_plan, run
            plan = make_plan(read_json(args.config))
            if args.dry_run:
                emit({"status": "plan_only", "run_count": len(plan), "runs": plan})
                return 0
            run(plan)
        elif args.command == "diagnose":
            from .diagnose import run_case
            run_case(args.case)
        elif args.command == "report":
            from .report import generate
            generate(args.input)
        return 0
    except (NotImplementedError, ValueError, OSError, TypeError, KeyError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
