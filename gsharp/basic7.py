# Dictionary is nothing but key value
# We can take the value of dictionary as number and struct type

d1=[]
d2={}
d3=()
print(type(d1))
print(type(d2))
print(type(d3))


d4={"Ankit":"Burger","Harsh":"Allo Burger","Gagan":"Chicken",
    "shubham":{ "B":"Veg puff" ,"L":"Maggie"}}
# Shubham has diffrent dictionary
d4["Anmol"]="Junk food" # It is used to update the function
d5=d4.copy()
#del d4["Anmol"]
#del d4["Anmol"] by using this it can delete from the d4 and d5
#d4[]
print(d4)
#print(d4["Gagan"])
#print(d4["shubham"])
print(d5)
d4.update({"Sourav":"Paties"})
print(d4)

print(d4.keys())
print(d4.items())
