lst = list(range(50, 100))
lst2 = list(range(100))

# for index, item in enumerate(lst):
#     print(index, item)

users = ['a', 'b', 'c', 'd']

first_user = users[0]
second_user = users[1]

# Unpacking in python
# first_user, *rest_users, last_user = users
# first_user, second_user, *rest_users = users
*rest, fourth_user = users
(first, second), (third, fourth), fifth = [(1,3), (1,4), 8]

a = 1
b = 2

b, a = a, b

# print(b, a)


# Iteration in dict
dct = {
    1: 2,
    'asdk': 345,
    'skaldj': 987
}

# print(f'{dct.keys()}')
# print(f'{dct.values()}')
# print(dct.items())


# for key, val in dct.items():
#     print(key, val)


l1 = list(range(1, 10))
l2 = list(range(0, 9))


for index in range(len(l1)):
    first_val = l1[index]
    second_val = l2[index]


# for i, (first_val, second_val) in enumerate(zip(l1, l2)):
#     print(i, first_val, second_val)

# for i, _ in [[1,2], [1,2], [1,2]]:
#     print(i)

# ([1,1,1], [2,2,2])

d1 = {
    'a': 1,
    'b': 2
}

d2 = {
    'a': 11,
    'c': 3
}

# d1.update(d2)

# d3 = d1 | d2
d1 |= d2
print(d1)
