#Program to know the properties of string in python

''' 
    Strings in python are ordered sequence of characters, 
    array of bytes representing the unicode characters,
    they can be represented using single, double or triple quotes,
    Strings in Python are immutable
    
    Like any other language, in Python characters of a string can be accessed using the index
    
    NEGATIVE INDEXING:
    We can also use the negative index to access the character, i.e. x[-1] for the last element
'''

x = "Welcome to python programming"
print(x)
print(type(x))

print('\n')

#character access:
print(x[0]) #first element
print(x[-1]) #last element using negative indexing

#String slicing:
#here we can get a part of string 
print(x[0:7]) #to get Welcome only
print(x[-11:]) #last word of the string

#How String is immutable?
x = 'Hello World'
x[-1] = "D" #String cannot be updated
print(x)


#printing the address of each element of string array
x = 'Banana'
for idx in range(0, len(x)):
    print(x[idx], "=", id(x[idx]))



#String functions:

#len() to get the size of the String
a = 'Hello'
print("The size of array: ", len(a))

#count() to get the count of the letter in the String
a = ''' 
    This is a 
    Multi-line
    String    
    '''
print("The count of s in string a is: ", a.count('s'))


#str.capitalize() to get capital letters as small:
print(a.capitalize())

#str.title() is to get title case:
print(a.title())

#str.lower() to get lower case:
print(a.lower())

#str.upper() to get uppercase:
print(a.upper())


#str.istitle(), str.islower(), str.isuppper() are to verify the case:
l = a.isupper()
m = a.islower()
n = a.istitle()

print(l,m,n)

#str.strip() to remove white spaces, we can also use lstrip or rstrip to get the whitespace removal from left and right sides respectively
b = '   hello world 123 '
c = b.strip()
print(c)

#str.find() method is used to find the index of given keyword.
x = 'Welcome to come come'
f = x.find('co') #first index where key is found
g = x.rfind('co') #first index from the last 
print(f)
print(g)

#str.replace() to replace the given keyword with the new one
h = x.replace('come', 'Doom')
print(h)

#strigs can be concatenated :
x = "Hii"
y = "Python"

#print(x+" "+y)

#Repeatition of character of string or whole string:
print(x * 10)
print(y * 10)

#String spliting:
x = "Hii, I am a Sandbox Dev"
print(x.split(' '))
print(x.split(','))

#Strings can be compared:
x = 'John'
y = 'Deer'

print(x == y)
print(x != y)
print(x == x)