#Example of functions in python:

def line_break():
    print("------------------------")

for i in range(0,3):
    line_break()
    print(i)


def sum(n1, n2):

    '''
        This is a doc string
    '''
    return n1 + n2 

a = 23
b = 54

result = sum(a, b)
print(result)