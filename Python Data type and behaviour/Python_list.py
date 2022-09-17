#Program to discuss the properties of the List:
'''
    List is a mutable orderes sequence of object
    represented by []
    python does not have array, list can be used as array
'''

list1 = [0, 1, 2, 3, 4]

#accessing the elements by index
print(list1[0])
print(list1[-1])

#list slicing:
print(list1[0:2])
print(list1[-3:])

#list.append('element') function:
list1.append(5)
print(list1)

#list.insert(position, element):
list1.insert(2, 8)
print(list1)

#list.extend(another_list):
list2 = [5, 6, 8]
list1.extend(list2)
print(list1)

#list.index() will give index of first occurence
x = list1.index(5)
print(x)

#list.count() will give the number of occurence
x = list1.count(5)
print(x)

#list.reverse() will reverse the list
list1.reverse()
print(list1) 

#list.sort() will sort the list
list1.sort()
print(list1)

#list.pop() to remove the element
temp = list1.pop()
print(temp)

#list.remove() to remove first occurence of the keyword
list1.remove(5)
print(list1)

#list.clear() to clear the list
list1.clear()
print(list1)