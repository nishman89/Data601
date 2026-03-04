# collection of unqiue elements
# - They unordered
# - mutable


my_set ={1,2,3,4,5}
my_list =[1,2,3,4,5]
another_set = set(my_list)

# my_set.add(6)
# print(my_set)
# my_set.remove(3)
# print(my_set)
# my_set.discard(8)
# print(my_set)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

# unions- join sets but remove repeated values
union_set = set1 | set2
print(union_set)

# intersections - create a set with the repeated value
intersection_set = set1 & set2
print(intersection_set)

# difference - what does set1 have that set2 does not?
difference_set = set2 - set1
print(difference_set)

my_set.clear()
print(my_set)