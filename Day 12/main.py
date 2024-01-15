# try:
#     raise TypeError('sakjdhfkj')
#     # ...
# except Exception as e:
#     print(f'Exception raised', e)
from functools import reduce

# def sum():
#     pass
#
#
# sum = lambda first, second: first + second
#
# print(sum(4,5))

list_of_nums = list(range(1, 100))
#
# odd_nums = list(filter(lambda x: x%2, list_of_nums))
# even_nums = list(filter(lambda x: x%2==0, list_of_nums))
#
# print(f'{odd_nums}')
# print(f'{even_nums}')


# product = reduce(lambda a,b: a*b, list_of_nums)

# print(f'{product}')

def calculate_prod(a):
    return a **2


result = tuple(map(calculate_prod, list_of_nums))

print(f'{result}')
