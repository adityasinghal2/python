print ("Hello World!/!")
print (2/5)
print (5/5)

def foo(val1=0, val2=0):
    return val1 - val2

print(foo(val1=10, val2=3))
# Note: parameters are in a different order
print(foo(val2=3, val1=10))

def printVals(prefix='', *param, **dict):
    # Print out the extra named parameters and their values
    for key, val in dict.items():
        print('%s %d [%s] => [%s]' % (prefix, param[0] ,str(key), str(val)))

printVals('..', 23, foo=42, bar='!!!')


# x = 6

# def example():
#     print(x)
#     # z, however, is a local variable.  
#     z = 5
#     # this works
#     print(z)
    
# example()
# # this does not, which often confuses people, because z has been defined
# # and successfully even was called... the problem is that it is a local
# # variable only, and you are attempting to access it globally.

# print(z)
# x = 6

# def example2():
#     # works
#     print(x)
#     print(x+5)

#     # but then what happens when we go to modify:
#     x+=6

# example2()
# x = 6


def example3():
    # what we do here is defined x as a global variable. 
    global x
    # now we can:
    print(x)
    x+=5
    print(x)
example3()


x = 6
def example(x):
 
    print(x)
    x+=5
    print(x)
    return x
 
x = example(x)
print(x)
text = '''Sample Text to Save\nNew line!
sdfsfvdv'''

# notifies Python that you are opening this file, with the intention to write
saveFile = open('exampleFile.txt','w')

# actually writes the information
saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()
readMe = open('exampleFile.txt','r').read()
print(readMe)
readMe = open('exampleFile.txt','r').readlines()
print(readMe)

class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
        
    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print(mult)

    def division(x,y):
        div = x / y
        print(div)

calculator.subtraction(5,8)
calculator.multiplication(3,5)
calculator.division(5,3)
calculator.addition(5,2)
x = input('What is your name?: ')
print('Hello',x)
print (type(x))

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

def example():
    return 15, 12

x, y = example()
print(x,y)

# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)
x.insert(2,33)
print(x)
x.remove(6)
print(x)
print(x.index(1))

print(x.count(1))
print(
'''
So it works like a multi-line
comment, but it will print out.

You can make kewl designs like this:

==============
|            |
|            |
|    BOX     |
|            |
|            |
==============
'''
    )
import urllib.request
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #print(x.read())

    saveFile = open('noheaders.txt','w')
    saveFile.write(str(x.read()))
    saveFile.close()
except Exception as e:
    print ("KKK")
    print(str(e))
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''
ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)
url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print result 
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print result.start()
print result.end()
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print result.group(0)
result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print result
result=re.split(r'i','Analytics Vidhya')
print result
result=re.sub(r'India','the World','AV is largest Analytics community of India')
result
import re
pattern=re.compile('AV')
result=pattern.findall('AV Analytics Vidhya AV')
print result
result2=pattern.findall('AV is largest analytics community of India')
print result2
result=re.findall(r'.','AV is largest Analytics community of India')
print result
result=re.findall(r'\w','AV is largest Analytics community of India')
print result
result=re.findall(r'\w*','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\w+','AV is largest Analytics community of India')
print result
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result
result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result
result=re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print result
li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
     print 'yes'
 else:
     print 'no'
result= re.split(r'[;,\s]', line)
print result
line = 'asdf fjdk;afed,fjek,asdf,foo'
result= re.sub(r'[;,\s]',' ', line)
print result
# This tutorial is best followed in a shell / command prompt.
# Open yours up, type python, or python3, and then follow.
import subprocess

# Say you are on windows:
# module  call command in the shell
# you can change that if you'd like, eventually.
# IF YOU ARE NOT IN A SHELL, YOU WILL SEE NO OUTPUT!
subprocess.call('dir', shell=True)
subprocess.call('echo dir', shell=True)

from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:
plt.plot(x,y,linewidth=5)
plt.plot(x2,y2,linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.scatter(x, y)#, align='center')

plt.scatter(x2, y2, color='g')#, align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
style.use('ggplot')

x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter = ',')

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

#Python Operator Overloading
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
(1,5)
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
Addition	p1 + p2	p1.__add__(p2)
Subtraction	p1 - p2	p1.__sub__(p2)
Multiplication	p1 * p2	p1.__mul__(p2)
Power	p1 ** p2	p1.__pow__(p2)
Division	p1 / p2	p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2	p1.__and__(p2)
Bitwise OR	p1 | p2	p1.__or__(p2)
Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	~p1	p1.__invert__()

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
Point(1,1) < Point(-2,-3)
True
Point(1,1) < Point(0.5,-0.2)
False
Point(1,1) < Point(1,1)
False

Less than	p1 < p2	p1.__lt__(p2)
Less than or equal to	p1 <= p2	p1.__le__(p2)
Equal to

p1 == p2	p1.__eq__(p2)
Not equal to	p1 != p2	p1.__ne__(p2)
Greater than	p1 > p2	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)

#Multiple Inheritance in Python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
#Multilevel Inheritance in Python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pas


class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
#Every class in Python is derived from the class object. It is the most base type in Python.

#So technically, all other class, either built-in or user-defines, are derived classes and all objects are instances of object class.
# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))

#In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.

#So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

#MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents and in case of multiple parents, the order is same as tuple of base classes.

#MRO of a class can be viewed as the __mro__ attribute or mro() method. The former returns a tuple while latter returns a list.
MultiDerived.__mro__
(<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>)

MultiDerived.mro()
[<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>]
for element in iterable:

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
    # do something with element
# Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().

# The __iter__() method returns the iterator object itself. If required, some initialization can be performed.

# The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

# Here, we show an example that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
a = PowTwo(4)
i = iter(a)
next(i)
1
next(i)
2
next(i)
4
next(i)
8
next(i)
16
next(i)
# Traceback (most recent call last):
# ...
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

 x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
The value of x is 5 and y is 10
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
This same operation can be performed using the eval() function. But it takes it further. It can evaluate even expressions, provided the input is a string
int('2+3')
# Traceback (most recent call last):
#   File "<string>", line 301, in runcode
#   File "<interactive input>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '2+3'
eval('2+3')
5

# While importing a module, Python looks at several places defined in sys.path. It is a list of directory locations.

# import sys
# sys.path
# ['', 
#  'C:\\Python33\\Lib\\idlelib', 
#  'C:\\Windows\\system32\\python33.zip', 
#  'C:\\Python33\\DLLs', 
#  'C:\\Python33\\lib', 
#  'C:\\Python33', 
#  'C:\\Python33\\lib\\site-packages']
# StopIteration
# //	Floor division - division that results into whole number adjusted to the left in the number line
#this is added to differntiate it is as script or imported

# &	Bitwise AND	x& y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# ~	Bitwise NOT	~x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)
# >>	Bitwise right shift	x>> 2 = 2 (0000 0010)
# <<	Bitwise left shift	x<< 2 = 40 (0010 1000)

# Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.
# For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function, id(). Let's check it.

# Note: You may get different value of id

a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

# Note: You may get different value of id

a = 2

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2

# Output: id(2)= 10919424
print('id(2) =', id(2))


def printHello():
    print("Hello")     
a = printHello()

# Output: Hello
a

# for i in digits:
#     print(i)
# else:
#     print("No items left.")
# counter = 0

# while counter < 3:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")

def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")
# print(greet.__doc__)
# This function greets to
# 	the person passed into the
# 	name parameter
#refer https://www.programiz.com/python-programming/methods/built-in

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)

# In Python, anonymous function is a function that is defined without a name.

# While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

# Hence, anonymous functions are also called lambda functions.
# lambda arguments: expression
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.
#We use lambda functions when we require a nameless function for a short period of time.
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# The filter() function in Python takes in a function and a list as arguments.
#The map() function in Python takes in a function and a list.

#Mostly lambda functions are passed as parameters to a function which expects a function objects as parameter like map, reduce, filter functions
# map(function_object, iterable1, iterable2,...)
#map functions expects a function object and any number of iterables like list, dictionary, etc. It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.
def multiply2(x):
  return x * 2
    
map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
map(lambda x, y: x + y, list_a, list_b) # Output: [11, 22, 33]
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c')]

zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]

list_a, list_b = zip(*zipper_list)
print list_a # (1, 2, 3)
print list_b # ('a', 'b', 'c')
# In Python3, zip methods returns a zip object instead of a list. This zip object is an iterator. Iterators are lazily evaluated.

# Lazy evaluation, or call-by-need is an evaluation strategy which delays the evaluation of an expression until its value is needed and which also avoids repeated evaluations (Wikipedia definition).

# Iterators returns only element at a time. len function cannot be used with iterators. We can loop over the zip object or the iterator to get the actual list

list_a = [1, 2, 3]
list_b = [4, 5, 6]

zipped = zip(a, b) # Output: Zip Object. <zip at 0x4c10a30>

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable

list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]

list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.
# filter(function_object, iterable)
# filter function expects two arguments, function_object and an iterable. function_object returns a boolean value. function_object is called for each element of the iterable and filter returns only those element for which the function_object returns true.

# Like map function, filter function also returns a list of element. Unlike map function filter function can only have one iterable as input.


a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

# Similar to map, filter function in Python3 returns a filter object or the iterator which gets lazily evaluated. 
#Python Module Search Path
# While importing a module, Python looks at several places. Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. The search is in this order.

# The current directory.
# PYTHONPATH (an environment variable with a list of directory).
# The installation-dependent default directory.
# >>> import sys
# >>> sys.path
# ['',
# 'C:\\Python33\\Lib\\idlelib',
# 'C:\\Windows\\system32\\python33.zip',
# 'C:\\Python33\\DLLs',
# 'C:\\Python33\\lib',
# 'C:\\Python33',
# 'C:\\Python33\\lib\\site-packages']
# We can add modify this list to add our own path.
# This module shows the effect of
#  multiple imports and reload

# print("This code got executed")
# Now we see the effect of multiple imports.

# import my_module
# This code got executed
# import my_module
# import my_module
# import imp
# import my_module
# This code got executed
# import my_module
# imp.reload(my_module)
# # This code got executed
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)

Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
if __name__ == '__main__':
h great module!!!!')    print('suc