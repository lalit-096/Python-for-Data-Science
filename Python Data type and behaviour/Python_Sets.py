#Program to know the properties of sets:

'''
    A set is mutable, unordered and have unique elements
    represented by {}
    like mathematics, this set has also union, intersection and many other functions.
'''

set1 = {0, 1, 2, 3, 4, 5, 6}


#print(set1[0]) #cannot be called

#to display the elements of a set:

print(set1) #print complete set

for i in set1: #print each element one by one in new line
    print(i)

#to verify the element belongs to set or not:
print(6 in set1) #output: True or False

#we can add elements to the set:
set1.add(7)
print(set1)

#we can use update() for more than one element:
#set1.update(8, 9, 10)
#print(set1)

#getting the length of set:
print(len(set1))

#getting max and min values of the set:
print(max(set1), min(set1))


#removing elements:
set2 = set(("Apple", "Bat", "Cat"))
print(set2)

set2.remove("Apple")
print(set2)
set2.discard("Bat")
print(set2)
set2.clear()
print(set2)

#immutable sets: Frozensets
set3 = frozenset(set1)
print(set3)

#SET OPERATIONS:
setA = {0, 1, 2, 3, 3, 2}
setB = {4, 3, 2, 4, 5}
setC = {5, 8, 4, 5}

print("Union: ", setA | setB) #setA.union(setB)
print("Intersection: ", setA & setB) #setA.intersection(setB)
print("Difference: ", setA - setB) #setA.difference(setB)
print("Sym-Diff: ", setA ^ setB) #setA.symmetric_difference(setB)

print(setA.issubset(setB))
print(setA.isdisjoint(setC))
print(setB.issuperset(setC))
