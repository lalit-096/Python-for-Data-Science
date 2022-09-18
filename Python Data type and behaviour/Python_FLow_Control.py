#Program to understand flow control in python:

#simply we have if statements, if-else statements and if-elif-else statements in python

a = 200 
b = 100 
c = 300

if b > a:
    print("yes")
elif c > b:
    print("yes 2")
else:
    print("no")


#We also have for loop in python :
list1 = [0, 1, 2, 3, 4]

for i in list1:
    print(i)

list2 = [(0,1), (1,2), (2,3)]
for a,b in list2: #this is known as tuple unpacking
    print(a + b)

for i in range(0, 5): #range() will create the list from 0 to n-1
    print(i)

#While loop:
t = 5

while t>0:
    print("Hello")
    t -= 1

#Continue, Break and Pass statements:
for i in range(0, 5):

    if i == 2:
        continue

    if i == 4:
        break

    print(i)

for i in range(0, 3):
    pass