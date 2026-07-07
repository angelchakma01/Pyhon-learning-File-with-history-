

#Change Dictionary Items




Name_of_Friends ={
    "Cyber Expert":"Lolin Chakma",
    "Programmer":"Angel Chakma",
    "Ml Players":"Arpon Chakma",
    "Guiter's":"Noppo Chakma",
    "Nurse":"Tonoy Chakma",
}

print(Name_of_Friends["Friend1"])

Name_of_Friends["Friends4"] ="Nurses"


print(Name_of_Friends["Friends4"])

#Use Update method


Name_of_Friends.update({"Programmer":" Angel Chakma Will be a Programmer"})
print(Name_of_Friends["Programmer"])

# 
Use_of_programming_Language = {"Python":"Meching Learning","JavaScript":"Web Development","Swift":"Ios Development"}

Use_of_programming_Language["Python"] = "Ai & Data Science"

Use_of_programming_Language.update({"JavaScript":"Web Development & Backend Development"})



print(Use_of_programming_Language["Python"])
print(Use_of_programming_Language["JavaScript"])