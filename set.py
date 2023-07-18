set_test = set([1,2,2,2,3,4,5])
set_test2 = {1,2,3,4,5,5,5,6}


set_test3 = set_test.union(set_test2)


print(set_test3)
print(set_test)
print(set_test2)


print(len(set_test2))

print(3 in set_test2)
print(10 in set_test2)

set_test3.add(500)

print(set_test3)

set_test3.remove(500)

print(set_test3)


set_test3.discard(500)

print(set_test3)
