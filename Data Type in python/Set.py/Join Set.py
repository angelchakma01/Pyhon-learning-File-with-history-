
#Use Union & Update method
Favourit_90s_Songs = {"Kuch kuch hota hai","Bahatak Raha Tha Ab tak main","Ae mere humsafar","Neend churayee meri"}

Name = {"Angel Chakma","Noppo Chakma","Lolin Chakma",
        "tonoy Chakma","Arpon Chakma","Junan Chakma","Arnet Chakma","Diten Talukder"}

Number = {1,2,3,4,5}
songka = (1,3,4,5,6,7)

join = Number.union(songka)

uptodate = Number.update(songka)


chakma = Favourit_90s_Songs.union(Name)

print(chakma)
print(join)
print(Number)


#Use intersection

name_of_fruits = {"Banana","Mango","Coconat","Cherry"}

Name_of_Company = {"Google","Facebook","Amazon","Mango"}

intersection = name_of_fruits.intersection(Name_of_Company)
print(intersection)

#Use & sings

set1 = name_of_fruits & Name_of_Company

print(set1)

#Use diiferent method

name_Of_Animal = {"Cow","Human","Goat","Dog"}

name_of_Spaices = {"Terneric Powder","Papper Powder","Solt"}

name1 = name_of_Spaices - name_Of_Animal
print(name1)

name_Of_Animal.difference_update(name_of_Spaices)
print(name_Of_Animal)

a = name_Of_Animal.symmetric_difference(name_of_Spaices)
print(a)

b = name_Of_Animal.symmetric_difference_update(name_of_Spaices)
print(b)
print(name_Of_Animal)