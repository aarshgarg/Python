"""def fun():
    print("Inside function")


# Driver's code
# Calling function
fun()"""

def function1(a,b):
    print("sum of number",a+b)

function1(7,8)
function1(8,9)

def function2(a,b):
    """ This is used to calculate the avg and this type is known as doc strings """
    average=(a+b)/2
    print(average)

function2(6,8)
print(function2.__doc__)

def function3(a,b):
    average=(a+b)/2
    print(average)

    return average

v=function3(5,10)
print(v)