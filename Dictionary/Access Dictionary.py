


College_Information = {
    "Rangamati Govt college":{

        "Name":"Rangamati Govt college",
        "Location":"Rangamati",
        "Established":"1962",
        "Department":"Science, Arts, Commerce",
        "Student Name":"Angel Chakma",
    },
    "Angel Chakma":{
        "Name":"Angel Chakma",
        "Home":"Bangaltuli",
        "Department":"Physics",
        "Age":18,
        "Phone":1608137187,
    },
    "Laptops":"MacBook",
        
    
}
#Use Get method

#print(College_Iformaion["Rangamati Govt college"]["Department"])

print(College_Information["Laptops"])
A = College_Information.get("Angel Chakma")["Age"]
B = College_Information.get("Rangamati Govt college")
C = College_Information.get("Laptops")
print(A)
print(B)

print(C)
# Use key method

Chakma = College_Information.keys()
print(Chakma)

# Using value method

print(College_Information.values())



Info_Angel_Chakma = {"Name":"Angel Chakma","Home":"Bangaltuli","Department":"Physics","Age":18,"Phone":1608137187}
print(Info_Angel_Chakma.get("Age"))
print(Info_Angel_Chakma["Department"])
print(Info_Angel_Chakma.keys())
print(Info_Angel_Chakma.values())
print(Info_Angel_Chakma.items())
