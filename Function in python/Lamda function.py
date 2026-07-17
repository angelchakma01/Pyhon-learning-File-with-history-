

#Without using lamda function

def outlamdafunction(a,b):
    sum = a +b 
    print(sum)

outlamdafunction(50,60)

#Using lamda functions
#for additon
Addition = lambda a,b : a  + b

print(Addition(100,23))

Subtraction = lambda c,d:c -d 
print(Subtraction(1000,749))

#using for multification

multification = lambda E,X : E * X
print(multification(17,27))

#division
division = lambda P,Q : P / Q
print(division(5,6))

#comparision using lamda functions
#Bagsek bahir korar niyom
bakses = lambda X,Y : X % Y
print(bakses(5,3))

#potencial

poten = lambda M,N :M ** N
print(poten(2,4))

#floar division

flor = lambda K,G:K//G
print(flor(11,2))


#Temprasure converter

def far_cel(tem):
  
    Celcias = (5/9) *(tem - 32)
    print(Celcias)
    return Celcias

while True:
    try:
        float(input("Enter your faharenheite tempreture:"))
        break
    except ValueError:
        print("Please enter valid number")

far_cel()
