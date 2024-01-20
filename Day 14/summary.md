## Covered Topics
- Misc

### enumerate
- Provides an iterable containing the index along with the item.
Syntax - enumerate(iterable)
Example - enumerate([1,2,3,4,5]) -> ((0,1), (1,2), (2,3)...) 

### zip
- Provides an iterable containing the items at same indexes.
- Note: zip iterates over the smallest iterable
Example:
 iterable1 = [1,2,3,4]
 iterable2 = [9,8,7,6]
 iterable3 = [5,6,7,8]
 zip(i1, i2, i3) -> ((1, 9, 5), (2,8,6), (3,7,7), (4,6,8))


### Unpacking in python


### iterating on dict
- By default, for loop iterates over dict keys. If you want you iterate over values or key-value pairs, then use .values() or .items() method
- Note: .keys() and .values() do not return tuple or list, they return dict_keys or dict_values, thus do not provide accessing by index

### Update a dict
Syntaxes:
- d1.update(d2)
- d1 = d1 | d2
- d1 |= d2

### Assignment:
- Write a program using zip and enumerate
- Create a repo for the project, setup the dependencies
- By Monday, decide and text the project url
- Start working on the project, progress will be checked on thursday
- For every there must be a PR (pull request).
