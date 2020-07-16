# Shallow Copy Example

import copy

list1 = [[10,20,30], ["how", "Are", "You"], ["python", "is", "boring"]]

# list2 = list1
# list2 = list(list1)
list2 = list1[:]

list2[2][2] = "fun"

print("old list {}: {}\nnew list {}: {}".format(id(list1), list1, id(list2), list2))
# old list 1786455363464: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun']]
# new list 1786452225352: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun']]

list1.append([1,2,3])
print("old list {}: {}\nnew list {}: {}".format(id(list1), list1, id(list2), list2))
# old list 1786455363464: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun'], [1, 2, 3]]
# new list 1786452225352: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun']]


# Deep Copy Example

list1 = [[10,20,30], ["how", "Are", "You"], ["python", "is", "boring"]]

list2 = copy.deepcopy(list1)

list2[2][2] = "fun"

print("old list {}: {}\nnew list {}: {}".format(id(list1), list1, id(list2), list2))
# old list 1786455301000: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'boring']]
# new list 1786455363464: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun']]

list1.append([1,2,3])
print("old list {}: {}\nnew list {}: {}".format(id(list1), list1, id(list2), list2))
# old list 1786455301000: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'boring'], [1, 2, 3]]
# new list 1786455363464: [[10, 20, 30], ['how', 'Are', 'You'], ['python', 'is', 'fun']]

