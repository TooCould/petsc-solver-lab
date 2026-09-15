# C++ 入口：第三周实现

当前 main.cpp 只初始化 PETSc、输出占位提示并退出，没有加载或求解矩阵。

后续任务：加载 Python 导出的 PETSc 二进制 A、b；读取 KSP／PC 选项；执行求解并独立验算；输出日志，与 Python 结果对照。

提供 CMake 骨架，要求开发环境的 pkg-config 能找到 `PETSc` 模块。未在当前任务中编译验证。

```sh
cmake -S cpp -B cpp/build
cmake --build cpp/build
```

请先完成两周版，避免把构建系统配置作为前期主线。
