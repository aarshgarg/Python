def func_recursion(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*func_recursion(n-1)


n=int(input("Enter the number="))
print(func_recursion(n))