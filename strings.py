name = 'Dario'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-1])


print(name.index('i'))

print(name.index('r', 2, 4))

print(name.rindex('o'))


base = 'red blue red'
fragment = base[3:8]
print(fragment)



fragment = base[3:]
print(fragment)


base = '123456789'
fragment = base[::2]
print(fragment)

fragment = base[::3]
print(fragment)

fragment = base[::-3]
print(fragment)