#Programs to understand operators in python:

#ARITHMETIC OPERATORS:

a = 5
b = 10

print(a+b) #addition
print(b-a) #substraction
print(b/a) #simple division
print(a*b) #multiplication
print(b%a) #modulo function that returns the remainder
print(b//a) #returns only the quotient
print(b**a) #exponentiation


#LOGICAL OPERATORS:
print(a>b and b>a)
print(a>b or b>a)
print(not(a>b))


#IDENTITY OPERATORS:
list1 = [0, 1, 2]
list2 = [0, 1, 2]

print(list1 is list2)
print(list1 is not list2)

#MEMBER OPERATOR:
print(2 in list1)
print(2 not in list2)