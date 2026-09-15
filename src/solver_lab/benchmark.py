"""Expand the experiment plan; execution is not implemented."""

from .config import solve_config


def make_plan(config):
    allowed = {"sizes", "repeats", "common", "cases"}
    if set(config) - allowed:
        raise ValueError("批量实验存在未知配置字段。")
    repeats = config["repeats"]
    if type(repeats) is not int or repeats < 1:
        raise ValueError("repeats 必须为正整数。")
    if not isinstance(config["sizes"], list) or not config["sizes"]:
        raise ValueError("sizes 必须为非空数组。")
    if not isinstance(config["cases"], list) or not config["cases"]:
        raise ValueError("cases 必须为非空数组。")
    plan = []
    ids = set()
    for case in config["cases"]:
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id or case_id in ids:
            raise ValueError("case id 必须为不重复的非空字符串。")
        ids.add(case_id)
        for n in config["sizes"]:
            values = {**config.get("common", {}),
                      **{k: v for k, v in case.items() if k != "id"}, "n": n}
            settings = solve_config(values)
            for repeat in range(1, repeats + 1):
                plan.append({"case_id": case_id, "repeat": repeat, "config": settings})
    return plan


def run(plan):
    raise NotImplementedError("批量执行待实现；使用 --dry-run 查看实验计划。")
