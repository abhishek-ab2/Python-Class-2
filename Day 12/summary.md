## Covered Topics
- Misc
- Helpful utilities


## Exception Hierarchy

Base Exception Class -> BaseException

BaseException -> 
- Exception (child classes- AttributeError, TypeError)
- GeneratorExit
- KeyboardInterrupt - When user stops the programs
- SystemExit - When your programs exits


StopIteration - Raised when a loop exits

### lambda - expression
- Used to create lambda functions, are anonymous in nature

### filter (lazy in nature)
- Filters elements of an iterable based on the function provided

### reduce - in functools library
- Takes a function and iterable as argument and runs the operation on all the items, returns the result object

### map (lazy in nature)
- Takes a function and iterable as argument and runs the iterable of results

### GIL (Global Interpreter Lock)
- A lock on cpu level which disallows multiple interpreter instances.

### thread
- A simplest form of an operation

### Process
- A process contains multiple threads, and usually are on application level.

### generators (covered in next class)
- Generators are iterator, which are lazy in nature and use coroutines

## Assignment
- Think out - A project to build (2-3) weeks
- reduce, map, filter -> a program to showcase these functions
