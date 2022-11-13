fruit = {"Apple" :10 , "Orange" :20 , "peach": 100}
#print(fruit.keys())
#print(fruit.values())
#adding a new element
#fruit["Mango"]=50
#print(fruit)
#changing an existing element
#fruit["Apple"]=30
#print(fruit)
fruit2={"hello":5 , "Bye":10}
fruit.update(fruit2)
print(fruit)
fruit.pop("Apple")
print(fruit)