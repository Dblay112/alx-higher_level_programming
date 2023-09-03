#!/usr/bin/python3
"""divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    This function divided all elements of a matrix

    Args:
    matrix: a list of integers or floats
    div: a number(integer or float)

    Returns:
    a new matrix with elements rounded to 2 decimal places

    Raises:
    TypeError: if matrix is not list of lists of integers or floats
    TypeError: if each row of the matrix is not the same size
    TypeError: if div is not a number(integer or float)
    ZeroDivisionError: if div is equal to 0
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

      new_matrix = []
      for row in matrix:
          new_row = []
          for element in row:
              new_element = round(element / div, 2)
              new_row.append(new_element)
              new_matrix.append(new_row)

    return new_matrix
