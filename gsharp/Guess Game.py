n=18
number_of_guesses=1
print("Number of the guesses is limited to 5 only")

while(number_of_guesses<=5):
    print("Guess the number:")
    num1=int(input())
    if num1<18:

        print("Number you print is less then that number")
    elif num1>18:
        print("Number is the greater then that number")

    else:
        print("you won the match")
        break

    print(5-number_of_guesses,"no of guess left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>5):
    print("game over")



