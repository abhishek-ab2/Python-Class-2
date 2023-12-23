# Covered Topics
- Refresh on loops
- Functions


## continue
- Skips the current iteration

## break
- Exits the loop


## Functions:
- Block of statements which can be reused
### Advantages:
- Reusability
- Reduces Lines of code
- Reduces complexity
- Memory efficient

### Syntax:
 def func_name(arguments):
    return (*optional)
 
### Positional Arguments:
- Arguments which get value by the position of the value passed.

### Keywords Arguments:
- Arguments where value is derived by the key or name of the argument

### Rules:
- Positional must come before keyword argument
- Non-default arguments should come before arguments with default values

### Suggestion:
- Never keep mutable values as default value for your argument

### Variable length Arguments:
- Arguments which are of variable length usually intent for multiple values
- Syntax: def func_name(*name_of_variable)
- Datatype is tuple
- A function can only have one variable length argument and will be empty if no orphan value is there to assign.
- When number of arguments can vary
- Unlimited number of arguments, no need to define parameter for all the values.

### Variable length Keyword Arguments:
- Arguments which are of variable length and are passed as keyword argument
- Syntax: def func_name(**kwargs)
- Datatype is dict
- A function can only have one variable length keywork argument
- Same as above, also you get arguments as dictionary, means the position does not matter as you have keys to maintain the values

### Function possible syntax:
def func(arg1, arg2, *args, key=1, key2, **kwargs):
    return


# Assignments
- Take int input from user
- Run a for loop with the user's input.
- Take int input for every iteration and append it in a list, msg: Enter input 1
- After the loop, take str input from user mentioning choices i.e. add, subtract, divide, multiply, floor divide,
- Perform the operation user has entered on the list and print the result.
- Rules: Can not use sum function, only operators are allowed.
