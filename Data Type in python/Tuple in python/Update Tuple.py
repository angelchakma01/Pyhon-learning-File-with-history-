


#List to tupple
# Tuple to List

Name_of_Country = ("Angel Chakma","Bangladesh","USA","India","UK","Russia","Japan",
                   "South Africa","Norway","Switzerland","Srilanka","Thailand","Rangamati")



print(type(Name_of_Country))

#Name_of_Country[1] = "America"

country = list(Name_of_Country)

country.append("Brazil, Neymer")

Name_of_Country = tuple(country)




print(Name_of_Country)

print(type(country))

#Add tupple to Tupple

FIFA = ("Takla","Lambu","Kalu")

Name_of_Country = Name_of_Country + FIFA

print(Name_of_Country)

#Delet Tuple

del(Name_of_Country)

print(Name_of_Country)