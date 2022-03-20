print("Pattren of half pyrimid")
num=int(input("Enter the number for rows="))

print("Enter the value from 0 and 1")
bool_val=input(" Enter 1 for true or 0 for false value=")

if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":

    for i in range(num,0,-1):
        print("*"*i)

