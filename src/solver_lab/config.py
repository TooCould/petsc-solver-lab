"""Load configuration without importing numerical libraries."""

import json
import math
from pathlib import Path

DEFAULTS = {
    "n": 63, "rhs": "discrete", "seed": 2026,
    "solver": "cg", "pc": "jacobi", "rtol": 1e-8, "atol": 1e-12,
    "max_it": 5000, "restart": 30, "output_dir": "results",
}
SUPPORTED = {("cg", "none"), ("cg", "jacobi"),
             ("gmres", "none"), ("gmres", "ilu"),
             ("gmres", "hypre"), ("preonly", "lu")}


def read_json(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("配置文件必须是 JSON 对象。")
    return data


def solve_config(values=None):
    values = values or {}
    unknown = set(values) - set(DEFAULTS)
    if unknown:
        raise ValueError(f"未知配置字段：{sorted(unknown)}")
    config = {**DEFAULTS, **values}
    for key in ("n", "max_it", "restart"):
        if type(config[key]) is not int or config[key] < 1:
            raise ValueError(f"{key} 必须为正整数。")
    if type(config["seed"]) is not int or config["seed"] < 0:
        raise ValueError("seed 必须为非负整数。")
    for key in ("rtol", "atol"):
        value = config[key]
        if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
            raise ValueError(f"{key} 必须为非负有限数。")
    if config["rtol"] == config["atol"] == 0:
        raise ValueError("rtol 与 atol 不能同时为零。")
    if config["rhs"] not in ("discrete", "continuous"):
        raise ValueError("rhs 必须为 discrete 或 continuous。")
    if (config["solver"], config["pc"]) not in SUPPORTED:
        raise ValueError("框架尚未支持此 solver/pc 组合。")
    if not isinstance(config["output_dir"], str) or not config["output_dir"].strip():
        raise ValueError("output_dir 必须为非空路径字符串。")
    return config
