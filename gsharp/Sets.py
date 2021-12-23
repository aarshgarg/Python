# we can make the sets bcz it can obtain the unique value
# we can make the set fom list

s=set()
#print(type(s))
#sets=set([1,2,3,4,4])
#print(sets)
s.add(1)
s.add(2)
s.add(3)
sets=s.union([1,2,3,4,5])
print(s,sets)
s1=s.intersection([1,2,3,4])
print(s,s1)
print(len(s))

print(max(s))
print(min(s))