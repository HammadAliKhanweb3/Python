
# A set is an unordered collection of unique elements.
# Sets are mutable, but they cannot contain mutable elements like lists or dictionaries.
s = {1, 2, 3, 4, 5}

# sets methods
# Add an element to a set
s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 6}

s.add(3)  # Adding a duplicate element does not change the set
print(s)  # Output: {1, 2, 3, 4,

s.remove(2)  # Remove an element from the set
print(s)  # Output: {1, 3, 4, 5, 6}

s.discard(10)  # Discard an element (does not raise an error if the element is not present)
print(s)  # Output: {1, 3, 4, 5, 6}

s.pop()  # Remove and return an arbitrary element from the set
print(s)  # Output: {3, 4, 5, 6}

s.clear()  # Remove all elements from the set

# You can perform various operations on sets, such as union, intersection, and difference.
# Union: Combine two sets to get a new set with all unique elements.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: Get a new set with only the elements that are present in both sets.
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3}

# Difference: Get a new set with elements that are present in the first set but not in the second set.
difference_set = set1.difference(set2)

print("Difference:", difference_set)  # Output: {1, 2}  

# Symmetric Difference: Get a new set with elements that are present in either set, but not in both sets.
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}