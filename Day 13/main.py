def gen():
    for i in range(100):
        print('lsakdjflks')
        yield i


# for j in gen():
#     print(j)

# lst = iter(['asdf', 1,2,3,4])
#
# first_item = next(lst)
# print(first_item)
# first_item = next(lst)
# print(first_item)
# first_item = next(lst)
# print(first_item)
# first_item = next(lst)
# print(first_item)

generator = gen()

first_item = next(generator)
print(first_item)
first_item = next(generator)
print(first_item)
first_item = next(generator)
print(first_item)
first_item = next(generator)
print(first_item)

# print(list(generator))


