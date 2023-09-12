import numpy as np
from decimal import Decimal


def find_nullspace_basis(matrix):
    num_rows, num_cols = matrix.shape

    pivot_columns = []

    for col in range(num_cols):
        pivot_row = None
        for row in range(len(pivot_columns), num_rows):
            if matrix[row][col] != 0:
                pivot_row = row
                break

        if pivot_row is not None:
            pivot_columns.append(col)
            pivot_value = Decimal(matrix[pivot_row][col])
            matrix[pivot_row] /= pivot_value
            for other_row in range(num_rows):
                if other_row != pivot_row:
                    factor = matrix[other_row][col]
                    matrix[other_row] -= factor * matrix[pivot_row]

    nullspace_basis_vectors = []

    for col in range(num_cols):
        if col not in pivot_columns:
            basis_vector = np.zeros(num_cols)
            basis_vector[col] = 1

            for row, pivot_col in enumerate(pivot_columns):
                basis_vector[pivot_col] = -matrix[row, col]

            nullspace_basis_vectors.append(basis_vector)

    return nullspace_basis_vectors


def get_matrix_from_user():
    try:
        rows = int(input("Enter the number of rows in the matrix: "))
        cols = int(input("Enter the number of columns in the matrix: "))
        matrix = []
        print("Enter the elements row-wise:")
        for row in range(rows):
            row_values = []
            for col in range(cols):
                element_str = input(
                    f"Enter the element for row {row + 1}, column {col + 1}: "
                )
                element = Decimal(element_str)
                row_values.append(element)
            matrix.append(row_values)
        return np.array(matrix)
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return get_matrix_from_user()


if __name__ == "__main__":
    input_matrix = get_matrix_from_user()

    print("Input matrix:")
    for row in input_matrix:
        print([str(num) for num in row])

    nullspace_basis_vectors = find_nullspace_basis(input_matrix)

    print("Basis vectors of the nullspace:")
    for basis_vector in nullspace_basis_vectors:
        print([str(num) for num in basis_vector])
