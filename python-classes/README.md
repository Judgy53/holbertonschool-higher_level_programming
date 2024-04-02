# python-classes
Project in python to learn OOP, data abstraction and encapsulation.

## 0-square.py - My first square 
Defines an empty class `Square` that represents a square.
	
## 1-square.py - Square with size 
Defines a class `Square` that defines a square by:
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
	
## 2-square.py - Size validation 
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
  - `size` must be an integer
  - `size` must be greater or equal to 0
	
## 3-square.py - Area of a square 
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
  - `size` must be an integer
  - `size` must be greater or equal to 0
- Public instance method: `def area(self):` that returns the current square area
	
## 4-square.py - Access and update private attribute
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer
    - `size` must be greater or equal to 0
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
	
## 5-square.py - Printing a square
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer
    - `size` must be greater or equal to 0
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
	
## 6-square.py - Coordinates of a square
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer
    - `size` must be greater or equal to 0
- Private instance attribute: `position`
  - property `def position(self):` to retrieve it
  - property setter `def position(self, value):` to set it:
    - `position` must be a tuple of 2 positive integers
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
  - `position` is used to offset the square with new lines and spaces
	
## 100-singly_linked_list.py - Singly linked list 
Defines a class `Node` and a class `SinglyLinkedList` that represents singly linked list and its nodes by:

`Node`:
- Private instance attribute: `data`:
  - property `def data(self):` to retrieve it
  - property setter `def data(self, value):` to set it:
    - `data` must be an integer
- Private instance attribute: `next_node`:
  - property def `next_node(self):` to retrieve it
  - property setter `def next_node(self, value):` to set it:
    - `next_node` can be `None` or must be a `Node`
- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

`SinglyLinkedList`:
- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable (ex: `print(list_instance)`):
  - print the entire list in stdout
  - one node number by line
- Public instance method: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order)
	
## 101-square.py - Print Square instance
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer
    - `size` must be greater or equal to 0
- Private instance attribute: `position`
  - property `def position(self):` to retrieve it
  - property setter `def position(self, value):` to set it:
    - `position` must be a tuple of 2 positive integers
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
  - `position` is used to offset the square with new lines and spaces
- Printing a Square instance (ex: `print(square_instance)`) has the same behavior as `my_print()`

## 102-square.py - Compare 2 squares
Defines a class `Square` that represents a square by:
- Private instance attribute: `size`
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer
    - `size` must be greater or equal to 0
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area
