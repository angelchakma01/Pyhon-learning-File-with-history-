

Name = {0,1,3,3,4,"Angel Chakma",True,3.4 ,None}

print(type(Name))
print(Name)


a = len(Name)

print(a)

Name.add("Chakma")
Name.remove("Chakma")
Name.remove(None)
Name.remove("Angel Chakma")
Name.remove(1)
Name.remove(0)
Name.remove(3.4)
Name.remove(3)

Name.remove(4)

#Name.pop()
print(Name)
