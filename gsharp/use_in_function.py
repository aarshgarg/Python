text=input("Enter the given name")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True

elif("click this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("The spam is done")
else:
    print("Not done")