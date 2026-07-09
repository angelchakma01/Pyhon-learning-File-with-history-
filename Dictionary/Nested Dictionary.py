

Department_of_Rangmati_Govt_College = {
    "Department_of_physics":{
        "Name":"Angel Chakma",
        "Class Rool" : 19,
        "Weakly Class" : " 4 Days",
        "Hobby" : " Programming",

    },
    "Department_of_English":{
        "Name" : "Noppo Chakma",
        "Roll" : 20,
        "Weakly Class" : "2 Days",
        "Hobby" : "Gutersist",
    }
}

# print(Department_of_Rangmati_Govt_College["Department_of_physics"]["Name"])
# print(Department_of_Rangmati_Govt_College["Department_of_English"]["Name"])

#Using loop

for Physics,Engllish in Department_of_Rangmati_Govt_College.items():
    print(Physics)

    for English in Department_of_Rangmati_Govt_College.items():
        print(English)