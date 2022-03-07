a=[]
x=int(input("Enter the max number"))
for i in range(x):
    val=int(input("Enter the value"))
    a.append(val)
    print(a)

print("the lenght of the list",len(a))
print("the max number of the list",max(a))
print("the min num",min(a))
