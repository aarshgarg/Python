f=open("aarsh2.txt")
# it is used to find where is the file pointer
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())

print(f.seek(44))

print(f.readline())
print(f.readline())