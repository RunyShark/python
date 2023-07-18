list = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']


print(type(list))

print(len(list))

print(list[0])

print(list[1:2])

print(list[::2])

list3  = list + list2
print(list3)


list3[0] = 'z'


print(list3)

list3.append('wenas')

print(list3)

list3.pop()

print(list3)



list4 = ['9', '2', '3']
list4.sort()
print(list4)