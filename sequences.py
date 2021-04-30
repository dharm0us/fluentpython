'''
    Container sequences
    list, tuple, and collections.deque can hold items of different types, including nested containers.
    
    Flat sequences
    str, bytes, bytearray, memoryview, and array.array hold items of one simple type.
    
    A container sequence holds references to the objects it contains, which may be of any type, while a flat sequence stores the value of its contents in its own memory space, and not as distinct objects.
    
    Thus, flat sequences are more compact, but they are limited to holding primitive machine values like bytes, integers, and floats.
    
    Mutable sequences
    list, bytearray, array.array, collections.deque, and memoryview
    
    Immutable sequences
    tuple, str, and bytes
    
    Listcomp(List comprehension) creates a new list.
    If we want to use memory and consume items one by one, use GenExp(Generator Expressions)
    
    For e.g., to generate a Cross product of two lists of 1000 items each, ListComp would create a list with a million elements whereas GenExp would iterate over them one by one.
    '''

    # list comp
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
    
    # GenExp
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
   print(tshirt)
    
    # tuple unpacking
divmod(20, 8)
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)
print(quotient, remainder)
    
    # capture excess args
a, b, *rest = range(5)
print(a, b, rest)
a, *rest, b = range(5)
print(a, rest, b)
a, b, *rest = range(2)
print(a, b, rest)
    
    # tuples as immutable lists
    # only the refs inside  tuples are immutable, the objects pointed to by refs are mutable
a = (1, 2, [3, 4])
b = (1, 2, [3, 4])
print(a == b)
b[-1].append(99)
print(a == b)
    
    # to check whether a tuple is 'actually' immutable, try to compute its hash..
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True
    
tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
print(fixed(tf))
print(fixed(tm))

# slicing - you can name slices
invoice = """
... 0.....6.................................40........52...55........
... 1909  Pimoroni PiBrella                     $17.50    3    $52.50
... 1489  6mm Tactile Switch x20                 $4.95    2     $9.90
... 1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
... 1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY =  slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

'''
Assigning to slices, 
'''
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100  1
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: can only assign an iterable
l[2:5] = [100]
print(l)


# a strange corner case
# http://www.pythontutor.com/visualize.html#code=t%20%3D%20%281,%202,%20%5B3,4%5D%29%0At%5B2%5D%20%2B%3D%20%5B10,20%5D%0At&cumulative=false&curInstr=2&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

t = (1, 2, [3,4])
try:
  t[2] += [10,20]
except TypeError:
  print(t)
  # so the list is modified and a type error is thrown
  # so += isn't atomic. better to avoid mutables in tuple

import dis
dis.dis('s[a] += b')

# mutable and immutable sequences
l = [1,2,3]
print(id(l))
l *= 2 
print(l)
print(id(l)) # id remains same

t = (1,2,3)
print(id(t))
t *= 2 
print(t)
print(id(t)) # id changes

# list multiplier
# create a tic tac toe board
# right way

board = [['_'] * 3 for i in range(3)] 
board[1][2] = 'O'
print(board)

# the above code is equivalent to:
board = []
for i in range(3):
  row = ['_'] * 3
  board.append(row)
board[1][2] = 'X'
print(board)

# wrong way
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'X'
print(weird_board)

# equivalent to:
row = ['_'] * 3
board = []
for i in range(3):
  board.append(row)

board[1][2] = 'O'
print(board)


