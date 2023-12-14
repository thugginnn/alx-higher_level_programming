# Python - Almost a Circle

## Concepts Learned
- Python object-oriented programming.
- Three connected classes representing rectangles and squares.
- Writing a custom test suite using the unittest module.
- Utilizing various Python tools, including:
  - Import
  - Exceptions
  - Private attributes
  - Getter/setter
  - Class/static methods
  - Inheritance
  - File I/O
  - args / kwargs
  - JSON and CSV serialization/deserialization
  - Unittesting

## Classes

### Base
- Private class attribute `__nb_objects = 0`.
- Public instance attribute `id`.
- Class constructor `__init__(self, id=None)`.
- Static method `to_json_string(list_dictionaries)`.
- Class method `save_to_file(cls, list_objs)`.
- Static method `from_json_string(json_string)`.
- Class method `create(cls, **dictionary)`.
- Class method `load_from_file(cls)`.
- Class method `save_to_file_csv(cls, list_objs)`.
- Class method `load_from_file_csv(cls)`.
- Static method `draw(list_rectangles, list_squares)`.

### Rectangle
- Private instance attributes `__width`, `__height`, `__x`, and `__y`.
- Class constructor `__init__(self, width, height, x=0, y=0, id=None)`.
- Public method `area(self)`.
- Public method `display(self)`.
- Overwrite of `__str__` method.
- Public method `update(self, *args, **kwargs)`.
- Public method `to_dictionary(self)`.

### Square
- Class constructor `__init__(self, size, x=0, y=0, id=None)`.
- Overwrite of `__str__` method.
- Public method `update(self, *args, **kwargs)`.
- Public method `to_dictionary(self)`.


