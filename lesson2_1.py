import collections

this_is_dict = {'key': 'value'}
this_is_also_dict = dict([('key', 'value',), ])

print(this_is_dict == this_is_also_dict)
print('dict() is iterable:',
      isinstance(this_is_dict, collections.Iterable))

var = {1: 'value'}
new_var = var
var.update({2: 'new value'})
var[1] = 'mutated value'
print(new_var)

this_is_dict.update({'name': 'Super Mario'})
print(this_is_dict)

print('name is "{}"'.format(
    this_is_dict['name']))
print('name is "{}"'.format(
    this_is_dict.get('name', "Def name"))
)

print('addr n is "{}"'.format(
    this_is_dict.get('addr', 'addr'))
)

print(this_is_dict.keys()) #all keys

print(this_is_dict.values()) #all values

test_dict = {'pop': 1, 'pop2': 2, 'to-d': 3}

del test_dict['to-d']

print(test_dict)

popped = test_dict.pop('pop')
print(popped)

missing = test_dict.pop('not exist key', 'def value')
print(missing)

popped = test_dict.popitem()
print(popped)

it = {1: '2', 2: '3'}
for key in it:
    print(key, it[key])

for key, value in it.items():
    print(key,value)

to_clear = {'key':'value', 1: 2}
to_clear.clear()
print(to_clear)

print('{f},{s}'.format(f='c', s='k'))



