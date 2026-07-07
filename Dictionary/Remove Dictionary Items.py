

#Use pop method
Car = {
    "Brand":"BMW",
    "Prices":"1M USD",
    "From":"United State",
    "year": 2026
}

Car.pop("Prices")
Car.pop("From")

print(Car)

#use popitems method

Car.popitem()
Car.popitem()
print(Car)
