

#List type data

x = ["Angel","Lolin","Arpon","Manek","Tonoy","Noppo"] #list is muteable মানে হচ্ছে  লিস্ট পাল্টােনো যায় 

x[3]= 3
print(x)


print(type(x))


#Tupple Type Data

tuple1 = ("Chakma","Angel Chakma")#But Tupple is unmuteable কিন্তু টাপল পাল্টানো যায় না

#tuple1(0) = "Lolin"

print(tuple1)

print(type(tuple1))


#Range type data

Range = range(10)

print(type(Range))

for i in Range:
    print(i)