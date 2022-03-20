#f=open("aarsh2.txt","a")
#a=f.write("Aarsh is the legend \n")
#print(a)
#f.close()



#if we use the w it is used for write the content in txt
#if we run the program it can delete the previous content and update the new one
#when we use the append the append function it can add new content by not deleting the previous content
# if we writte the a=f.write then it give the number of char store in given line

f=open("aarsh2.txt","r+")

print(f.read())
f.write("Thankyou")