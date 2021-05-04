import collections.abc as abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))
'''
Using isinstance with an ABC is often better than checking whether a function argument is of the concrete dict type, because then alternative mapping types can be used.
'''
a = dict(one=1, two=2, three=3)
b = {'three': 3, 'two': 2, 'one': 1}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

dial_codes = [(880, 'Bangladesh'), (55,  'Brazil'), (86,  'China'), (91,  'India'), (62,  'Indonesia'), (81,  'Japan'), (234, 'Nigeria'), (92,  'Pakistan'), (7,   'Russia'), (1,   'United States'), ]
# dict comprehension
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
country_dial = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
print(country_dial)

'''
__missing__ method will be called when a key is missing when get is called.
In the class below we convert int key to str to get key
'''
class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

sd = StrKeyDict0()
sd["1"] = "One"
print(sd[1])

# it's better to inherit from UserDict rather than dict
# see this: https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/
import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

sd = StrKeyDict()
sd[1] = "one"
print(sd[1])
print(sd["1"])

# read only dict
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# this will fail - d_proxy[1] = 'B'
# but you can update the original dict, its changes will reflect
d[1] = 'B'
print(d_proxy[1])

# similarly, there are methods for fetching keys and values of dict which just return a view
values = d.values()
print(values)
d[2] = 'C'
print(values) # since it's just a view, it gets auto updated
print(type(values))
class1 = type(values)
# this will fail as dict_values can't be used publicly - d1 = class1()