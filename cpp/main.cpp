#include <petscksp.h>

int main(int argc, char **argv) {
    PetscErrorCode error = PetscInitialize(&argc, &argv, nullptr, nullptr);
    if (error) return static_cast<int>(error);
    PetscPrintf(PETSC_COMM_WORLD,
                "Scaffold only: matrix loading, KSP solve and diagnostics are pending.\n");
    error = PetscFinalize();
    return error ? static_cast<int>(error) : 2;
}
