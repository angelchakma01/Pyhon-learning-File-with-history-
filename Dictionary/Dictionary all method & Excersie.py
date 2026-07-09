

#Use the get method to print the value of the "model" key of the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Change the "year" value from 1964 to 2020.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2020
print(car)

#Add the key/value pair "color" : "red" to the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "red"})
print(car)

car["Honda"] ="Japan"
print(car)


#Code Chalange

# est your understanding of creating, accessing, changing, adding, and removing dictionary items.

# Instructions
# Inside the editor, complete the following steps:
# Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# Print the value of the "model" key
# Add a new key "color" with the value "red"
# Remove the "brand" key using pop()
# Print the dictionary
car = {
    "brand":"Ford",
    "model":"Mustang",
    "year": " 2024"


}
print(car["model"])
car["color"] = "red"
car.pop("brand")

print(car)
