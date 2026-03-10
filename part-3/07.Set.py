'''
Sets in Python
A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from a set after it has been created. However, the elements themselves must be immutable (e.g., numbers, strings, tuples). Sets are defined using curly braces {} or the built-in set() function.
Syntax: set_name = {element1, element2, element3, ...}
or
set_name = set([element1, element2, element3, ...])
Elements in a set are unique, which means that duplicate elements will be automatically removed. Sets are also unordered, meaning that the elements do not have a specific order and cannot be accessed by index.
'''

# Example of a set
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

# Creating a set using the set() function
numbers = set([1, 2, 3, 4, 5, 2, 3])
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()


'''
Set Methods
Sets have various built-in methods that allow you to perform operations such as adding, removing, and checking for elements. Here are some common set methods:
1. add(element): Adds an element to the set.
2. remove(element): Removes an element from the set. Raises a KeyError if the element is not found.
3. discard(element): Removes an element from the set if it is present. Does not raise an error if the element is not found.
4. pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
5. clear(): Removes all elements from the set.
6. union(other_set): Returns a new set that is the union of the current set and another set.
7. intersection(other_set): Returns a new set that is the intersection of the current set and another set.
8. difference(other_set): Returns a new set that is the difference between the current set and another set.
9. symmetric_difference(other_set): Returns a new set that is the symmetric difference between the current set and another set.
10. issubset(other_set): Returns True if the current set is a subset of another set.
11. issuperset(other_set): Returns True if the current set is a superset of another set.
12. isdisjoint(other_set): Returns True if the current set has no elements in common with another set.
13. copy(): Returns a shallow copy of the set.
14. len(set): Returns the number of elements in the set.
15. update(other_set): Updates the current set with the union of itself and another set.
16. intersection_update(other_set): Updates the current set with the intersection of itself and another set.
17. difference_update(other_set): Updates the current set with the difference between itself and another set
18. symmetric_difference_update(other_set): Updates the current set with the symmetric difference between itself and another set.
19. frozenset(iterable): Returns an immutable frozenset object, which is a set that cannot be modified after it is created.
20. set(iterable): Returns a new set object, optionally with elements taken from an iterable.
'''

# Example of using set methods

fruits = {"apple", "banana", "cherry"}
# Adding an element to the set
fruits.add("orange")
print(fruits)  # Output: {'banana', 'cherry', 'orange', 'apple'}
# Removing an element from the set
fruits.remove("banana")
print(fruits)  # Output: {'cherry', 'orange', 'apple'}
# Discarding an element from the set
fruits.discard("grape")  # No error, since "grape" is not in the set
print(fruits)  # Output: {'cherry', 'orange', 'apple'}
# Popping an arbitrary element from the set
popped_fruit = fruits.pop()
print(popped_fruit)  # Output: 'cherry' (or 'orange', or 'apple')
print(fruits)  # Output: {'orange', 'apple'} (or the remaining elements)
# Clearing the set
fruits.clear()
print(fruits)  # Output: set()
# Example of set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Union of sets
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
# Intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}
# Difference of sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
# Symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}
# Example of subset and superset
set_c = {1, 2}
print(set_c.issubset(set_a))  # Output: True
print(set_a.issuperset(set_c))  # Output: True
# Example of disjoint sets
set_d = {7, 8}
print(set_a.isdisjoint(set_d))  # Output: True
# Example of copying a set
set_e = set_a.copy()
print(set_e)  # Output: {1, 2, 3, 4}
# Example of frozenset
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})