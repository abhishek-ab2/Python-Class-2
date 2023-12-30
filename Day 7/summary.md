## Covered Topics
- Exception Handling
- Docstring

### Syntax:
try:
    ...code block
except:
    .. code to handle the exception
finally:
    .. code block

### Try (must have):
- Code block susceptible to exceptions

### Except (at least one):
- For handling the exception(s)
- Can have multiple except clause

### Finally (optional):
- For code which must run whether there is any exception or not

### raise:
- To raise any exception


## Assignment:
- Make changes in the object and class assignment.
- When user adds an element in the storage, validate the type of object if its of invalid data type and raise TypeError if invalid type of object is passed, hint: isinstance
- Add a max_size attribute in the storage, when an item is added and if the resultant size exceeds max size raise MemoryError
Max size = 10
Current size 7
New item size 8