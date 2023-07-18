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


upper_case = 'red'
print(upper_case.upper())

lower_case = 'RED'
print(lower_case.lower())

capitalize_case = 'hello'
print(capitalize_case.capitalize())

array = '123456789'
print(array.split())


a = 'phyton'
b = 'es'
c = 'facil'
f = 'facil'

arr = ' '.join([a,b,c,f])

print(arr)

arr.replace('facil', 'genial')




