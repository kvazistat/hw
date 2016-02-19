import collections
import sys

notalist = (1, 2,)
list1 = [1, 2]
list2 = list(notalist)

print(list1 == list2, notalist == list1)
print('list() is iterable', isinstance(list1, collections.Iterable))

list1.append(3)
print('append() returns None: ', list1.append(4))
print(list1)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, 'inserted value')
print(list1)

var = ['kek']
nvar = var[:]
var.append('tat')
var[0] = 'lol'
print(nvar)

test_list = ['a', 'b', 'c']

popped = test_list.pop(0)
print('popped value os "{}"', format(popped))

test_list.remove('b')

del test_list[0]

v, s = ['v', 's']
print(v, s)

multi = [
    [1, 2, 3],
    ['t', 'b', 'k']
]
for row in multi:
    print(row)
    for element in row:
        print('element: ', element)

if sys.version_info[0] == 2:
    print('xrange', xrange(1, 10))  # generator, print range from to
    print('range', range(1, 10))  # print all elements of range
else:
    print('range', range(1, 10))

for i in list(range(1, 15, 2)):
    print(i)
