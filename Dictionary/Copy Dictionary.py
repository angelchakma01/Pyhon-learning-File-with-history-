

Name_of_Bangladesh_Seasons = {

    "Summer":{
        "Hont Seasons": "Summer",
        "Rainy Seasons":"Monsson",
        "Seasons of clear skies":"Autumn",
        "Hervest Seasons" : "Late Autumn",
        "Cold Seasons" : "Winter",
        "King of seasons": "Spring"
    },
    "Monsoon":"Flood"

}

print(Name_of_Bangladesh_Seasons.get("Rainy Seasons"))

#Use copy method

Seasons = Name_of_Bangladesh_Seasons.copy()
print(Seasons)
#Use Dict method
Monsoon = dict(Name_of_Bangladesh_Seasons)
print(Monsoon)

Seasons_Name = Name_of_Bangladesh_Seasons
print(Seasons_Name)

print(Seasons_Name.clear())
#del Seasons_Name

print(Name_of_Bangladesh_Seasons)
print(Seasons_Name)
# def Anel_Chakma():
#     for i in range(10):
#         print(i)

# Anel_Chakma()
# Anel_Chakma()
# Anel_Chakma()

print(Name_of_Bangladesh_Seasons["Monsoon"])
