
#Truth Table

Angel = 20
lolin = 100
noppo = 30

#Using or oparators

if Angel>lolin or noppo < Angel:
    print("What's That's")


#Using And Oparators

if Angel > lolin and noppo == Angel:
    print("Say About That")

#Using Not Oparators

if not Angel > lolin :
    print(" Angel Lolin er Seye boro ")



age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")


username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")