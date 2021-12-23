groceery=["Harpic","Oreo","Blue Berry","Fish","Juice"]
print(groceery)
print(groceery[3])
number=[2,5,1,44,22,6]
#number.sort()
#number.reverse()
number.append(18) # it can attach the 18 number at last
print(number)
print(number[::])
print(number[1:4])
print(number[0::])
print(number[::2])
print(number[::-1]) # by this it can only reverse the list but not in sorted order\

number[2]=62 # it is used to change the value at given index
print(number)
#it is list





numbers=[]
numbers.append(44)
numbers.append(66)
numbers.append(87)
print(numbers)
numbers.insert(2,90) # It is used to insertat any position
print(numbers)
numbers.remove(66)
print(numbers)
#numbers.pop()
print(numbers)


#Muttable be can change the value
# Immutable be canot change the value
# it is tuple not a list
elements=(1,3,2)
print(elements)
# In tupple we cannot change the value
#elements[1]=5
#print(elements)

# we can easily interchange the value
a=55
b=90
a,b=b,a
print(a,b)