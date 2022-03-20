f=open("aarsh2.txt")
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())

print(f.seek(44))

print(f.readline())
print(f.readline())