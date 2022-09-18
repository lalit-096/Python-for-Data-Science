#Program to know properties of dictionary

'''
    Dictionary is a data structure that uses the key-value pair to store the data.
'''

dict1 = {
            'Name' : "ABC",
            'Enr no' : 200220131096,
            'Branch' : "CSE",
            'Division' : "H1"
        }

#Properties of the Dictionary

print(dict1.get('Name')) #get the value of the given key

print(dict1.keys()) #print all the keys

print(dict1.values()) #print all the values

print(dict1.items()) #print all the key-value pair tuples
