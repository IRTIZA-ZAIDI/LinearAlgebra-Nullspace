# Null Space Basis Calculator

This Python program calculates the null space of a given matrix. The null space is a fundamental concept in linear algebra, representing the set of all vectors that, when multiplied by the matrix, result in the zero vector.

The program:
- Takes a user-provided matrix as input.
- Uses Gaussian elimination to compute the null space basis vectors.
- Displays the basis vectors of the null space.

## Features

- **User Input**: Input any matrix of any size.
- **Null Space Calculation**: Uses Gaussian elimination to find the null space basis vectors.
- **Decimal Precision**: Handles matrix elements with `Decimal` precision for higher accuracy.
- **Interactive**: Prompts the user for matrix elements row by row.

## Usage

1. Run the program and input the matrix dimensions (rows and columns).
2. Enter the matrix elements row by row.
3. The program will display the matrix and calculate its null space basis vectors.

### Example:

```bash
Enter the number of rows in the matrix: 3
Enter the number of columns in the matrix: 3
Enter the elements row-wise:
Enter the element for row 1, column 1: 1
Enter the element for row 1, column 2: 2
Enter the element for row 1, column 3: 3
Enter the element for row 2, column 1: 4
Enter the element for row 2, column 2: 5
Enter the element for row 2, column 3: 6
Enter the element for row 3, column 1: 7
Enter the element for row 3, column 2: 8
Enter the element for row 3, column 3: 9

Input matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Basis vectors of the nullspace:
[1, -2, 1]
````

## Requirements

* Python 3.x
* numpy
* decimal

