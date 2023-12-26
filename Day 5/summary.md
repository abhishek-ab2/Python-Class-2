# Covered Topics:
- Classes and Objects


## Class:
#### Syntax:
class Name:
    def __init__(self, *args, **kwargs):
        ...


## Object:
#### Syntax:
obj = ClassName()


## Dunder Methods (Double underscore, Special Methods, Magic Methods):
- __init__ (Initializer) > Runs after object is created in memory
- __str__ > Used when an object is printed
- __repr__ > Used to get string representation of an object
- __del__ > Used when object is deleted from memory


## Delete object
#### Syntax:
del object_name


## Assignments:
- Create 2 classes, Storage and Item:
- Item has - name, type, size, others (For all optional data stored as dict)
- Storage has - host, port, protocol, container
- Item init params - name, type, others, 
- Storage - host, port, protocol
- Item methods - calculate_size(length of name + length of type) and will store it in size attribute
- Storage methods :
   add_element (add item to container which will be by default a list)
    calculate_size (gives the container size that is sum of size of all items.)
