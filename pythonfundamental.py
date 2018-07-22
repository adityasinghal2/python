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
#this is added to differntiate it is as script or imported
if __name__ == '__main__':
    print('such great module!!!!')