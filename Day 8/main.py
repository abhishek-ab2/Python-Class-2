# name = input('Enter ur name: ')
#
# print('Your name is ', name)
# welcome_text = 'Your name is '+ name


# welcome_text = 'Your name is %s' % (name, ) # Python 2

# welcome_text = 'Your name is {}'.format(name) # Python 3

# welcome_text = f'Your name is {name}' # Python3.6


# Python 3
# welcome_text = 'Your name is {1} {0}'.format(name, 12)

# welcome_text = 'Your name is {user_name}'.format(user_name=name)

# f-strings
# welcome_text = f'Your name is {name}'

# print(welcome_text)

# var = 10
# var2 = 'aslkdjfhskj'


# text = 'Hello {name}, Your age is {0}'.format(var, name=var2)

# text2 = f'Hello {var2}, Your age is {var}'


# Decorators
#
# def log_decorator(operation):
#     def wrapper():
#         print('Starting operation...')
#         operation()
#         print('Operation completed')
#     return wrapper
#
#
# @log_decorator
# def perform_operation():
#     print('I am performing operation.')
#
#
# perform_operation()



class A:
    def __init__(self):
        self.item_sizes = list(range(10))

    @property
    def size(self):
        return sum(self.item_sizes)

a = A()
print(f'Total size is {a.size}')




