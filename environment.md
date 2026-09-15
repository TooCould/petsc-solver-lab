# 环境与后端验收

状态：待配置、待实测。框架本身仅依赖 Python 3.10+ 标准库。

## 推荐路径

使用 Linux／WSL2，选择相互兼容的 PETSc 与 petsc4py，并确认 PETSc 构建包含 Hypre 和 MUMPS。不要仅因 petsc4py 可导入就判定后端可用。

1. 建立项目独立环境。
2. 安装配套 PETSc／petsc4py 及 Hypre／MUMPS 后端。
3. 安装本项目：`python -m pip install -e '.[numerics,dev]'`。
4. 运行 `solver-lab check-env`，记录依赖可导入状态。
5. 完成求解模块后，对小型 SPD 系统实际执行全部后端，保存有效配置及真实残差。

PETSc 不作为 pip 自动依赖安装，以免框架安装意外触发长时间编译或得到缺少后端的构建。

## 运行前记录

- 操作系统、CPU、内存、Python、PETSc、petsc4py 和数值库版本。
- PETSc 标量与索引类型；计划要求实数双精度。
- 进程数、BLAS/OpenMP 等底层线程设置；首版固定单进程和单线程。
- Hypre／MUMPS 的实际生效后端与验收日志。

## 验收记录

| 项目 | 状态 | 证据 |
|---|---|---|
| PETSc / petsc4py | 未验收 | 待记录 |
| CG / GMRES | 未验收 | 待记录 |
| Jacobi / ILU(0) | 未验收 | 待记录 |
| Hypre BoomerAMG | 未验收 | 待记录 |
| MUMPS LU | 未验收 | 待记录 |

禁止缺失后端时静默替换算法。安装过程和版本信息完成后补充到本文。
