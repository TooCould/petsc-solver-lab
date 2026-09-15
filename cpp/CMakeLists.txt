cmake_minimum_required(VERSION 3.20)
project(petsc_solver_lab LANGUAGES CXX)

find_package(PkgConfig REQUIRED)
pkg_check_modules(PETSC REQUIRED IMPORTED_TARGET PETSc)
add_executable(solver_lab_cpp main.cpp)
target_compile_features(solver_lab_cpp PRIVATE cxx_std_17)
target_link_libraries(solver_lab_cpp PRIVATE PkgConfig::PETSC)
