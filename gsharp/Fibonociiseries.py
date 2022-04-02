def fiboncii(n):
    if n==1:
        return 0
    elif n==2:
        return 1;
    else:
        return fiboncii(n-1)+fiboncii(n-2)


n=int(input("Enter the number="))
print(fiboncii(n))