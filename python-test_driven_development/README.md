# python-test_driven_development
Project in python to learn how to properly document the code, and use doctest to test it.

All tests for each task are located in `tests/`.

## 0-add_integer.py - Integers addition
Function that adds 2 integers.
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`

Tests included in `tests/0-add_integer.txt`:
- Adding 2 positive integers
- Adding 1 positive integer and 1 negative integer
- Adding 1 positive integer with default value
- Adding 1 float with 1 integer
- Adding 1 integer with a string
- Adding None with default value
- Passing no arguments
- Passing `float('NaN')`
- Passing `float('inf')`
	
## 2-matrix_divided.py - Divide a matrix 
Function that divides all elements of a matrix.
- Prototype:` def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats
- Each row of `matrix` must be of the same size
- `div` must be a number (integer or float)
- `div` can’t be equal to 0
- All elements of `matrix` should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix

Tests included in `tests/2-matrix_divided.txt`:
- Passing a valid matrix and a valid divider
- Passing an empty matrix
- Passing a matrix of empty rows
- Passing no arguments
- Passing a string instead of a matrix
- Passing a matrix of strings instead of integers or floats
- Passing a matrix with row of different sizes
- Passing a non number div
- Passing 0 as div
- Returns a new matrix
- Passing inf in the matrix
- Passing inf as divider
- Passing NaN in the matrix
- Passing NaN as divider
	
## 3-say_my_name.py - Say my name
Function that prints `My name is <first name> <last name>`
- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings

Tests included in `tests/3-say_my_name.txt`:
- Pass 2 valid strings
- Pass 1 valid string and use default last name
- Pass an integer as first name
- Pass an integer as last name
- Passing no arguments
	
## 4-print_square.py - Print square 
Function that prints a square with the character #.
- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer
- `size` must be greater or equal to 0

Tests included in `tests/4-print_square.txt`:
- Pass a positive size
- Pass size 0
- Pass a string
- Pass a negative integer
- Pass an negative float
- Passing no arguments
	
## 5-text_indentation.py - Text indentation
Function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
- Prototype: `def text_indentation(text):`
- `text` must be a string
- There should be no space at the beginning or at the end of each printed line

Tests included in `tests/4-print_square.txt`:
- Pass a string with split chars
- Pass a string with no split chars
- Pass an empty string
- Pass an integer
- Passing no arguments

## tests/6-max_integer_test.py - Max integer - Unittest
Unittests for the function `def max_integer(list=[]):`
  ```python
  def max_integer(list=[]):
    if len(list) == 0:
          return None
    result = list[0]
    i = 1
    while i < len(list):
      if list[i] > result:
        result = list[i]
      i += 1
    return result
  ```

Tests:
- Passing an empty list
- Passing a list with many valid elements
- Max element in the middle of the list
- Passing a list with 1 element
- Passing a list with only negative elements
- Passing None
- Passing a string
- Passing an integer

## 100-matrix_mul.py - Matrix multiplication
Function that multiplies 2 matrices:
- Prototype: `def matrix_mul(m_a, m_b):`
- `m_a` and `m_b` must be an list of lists of integers or floats:
- `m_a` and `m_b` can't be empty
- `m_a` and `m_b` must be rectangles (all ‘rows’ should be of the same size)
- The number of columns in the `m_a` must be equal to the number of rows in `m_b`.

Tests included in `tests/100-matrix_mul.txt`:
- Multiply two matrix of integers
- Pass an integer for m_a
- Pass a string for m_b
- Pass a list of strings for m_a
- Pass a list of Nones for m_b
- Pass an empty list for m_a
- Pass an list of empty lists for m_b
- Pass a string in m_a
- Pass a None in m_b
- Pass a list of different sized rows to m_a
- Pass a list of different sized rows to m_b
- Pass 2 matrices with incompatible sizes
- Pass only 1 matrix
- Pass no arguments

## 101-lazy_matrix_mul.py - Lazy matrix multiplication 
Function that multiplies 2 matrices by using the module NumPy
- Prototype: `def lazy_matrix_mul(m_a, m_b):`

Tests included in `tests/101-lazy_matrix_mul.txt`:
- Multiply two matrix of integers
- Pass an integer for m_a
- Pass a string for m_b
- Pass a list of strings for m_a
- Pass a list of Nones for m_b
- Pass an empty list for m_a
- Pass an list of empty lists for m_b
- Pass a string in m_a
- Pass a None in m_b
- Pass a list of different sized rows to m_a
- Pass a list of different sized rows to m_b
- Pass 2 matrices with incompatible sizes
- Pass only 1 matrix
- Pass no arguments
