print("Enter the number1=")
num1=input()
print("Enter the Number2=")
num2=input()

try:
    print("Sum of the Number",int(num1)+int(num2))
except Exception as e:
    print(e)

print("All Good")