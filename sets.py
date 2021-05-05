# very fast and simple membership tests
needles = {'a@b.com', 'b@c.com'}
haystack = {'a@b.com', 'b@c.com', 'k@l.com'}
found = len(needles & haystack)
print(found)

# as compared to the alternative
found = 0;
for n in needles:
  if n in haystack:
    found +=1

print(found)

# but the above alternative would work for all the iterables
# though we can convert all iterables to sets and do the above

#  dict_keys and dict_items implement the special methods to support the powerful set operators & (intersection), | (union), - (difference) and ^ (symmetric difference).

# This means, for example, that finding the keys that appear in two dictionaries is as easy as this:

d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)
print(d1.keys() & d2.keys())

# Note that the return value of & is a set. Even better: the set operators in dictonary views are compatible with set instances. Check this out:

s = {'a', 'e', 'i'}
print(d1.keys() & s)
print(d1.keys() | s)
{'a', 'c', 'b', 'd', 'i', 'e'}

# there are certain optimizations for dicts
# for a class, all the objects hold attributes in dicts, so keys can be shared
# similarly, the older implementation of dict had empty rows to account for future entries, but the current implementation just stores the indices in the entries array