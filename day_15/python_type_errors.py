'''
>>> print 'hello world'
  File "<python-input-0>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello world')
hello world
>>> print(age)
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> age = 22
>>> print(age)
22
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    numbers[5]
    ~~~~~~~^^^
IndexError: list index out of range
>>> import maths
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>> user = {"name":"Ayse", "age":22, "country":"türkiye"}
>>> user["county"]
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    user["county"]
    ~~~~^^^^^^^^^^
KeyError: 'county'
>>> user["country"]
'türkiye'
>>> 4 + '3'
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    4 + '3'
    ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> from math import power
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (/opt/anaconda3/lib/python3.13/lib-dynload/math.cpython-313-darwin.so)
>>> from math import pow
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'
>>> 1/0
Traceback (most recent call last):
  File "<python-input-19>", line 1, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
>>> '''