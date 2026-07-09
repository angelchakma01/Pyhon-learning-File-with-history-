

Facebook_Users = {
    "Name" : "Angel Chakma",
    "Profile" : "Tech",
    "From" : "Marissa",
    "Distric" : "Rangamati",
    "Favourit Song": " 7 year's ",
    "Will be" : "Programmer",
    "Institute":"Rangamati Govt College"

}

KaliLinux_Users = {
    "Name": "Lolin Chakma",
    "Profile":"Tech",
    "From" : "Marissa",
    "Distric":"Rangamati",
    "Fovourit Songs" : "Sad Songs",
    "Will be ": "Cyber Security Expert",
    "Institue" : "Bangladesh Sweden Polytechnic institue,Kaptai"
}

#Using for loop to print the dictionary items

for i in KaliLinux_Users:
    print(KaliLinux_Users[i])
#Use Value method

for a in KaliLinux_Users.values():
    print(a)

#Use keys method
for d in Facebook_Users.keys():
    print(d)
for f in Facebook_Users.values():
    print(f)
#Using Items method
for v in Facebook_Users.items():
    print(v)





