# collection = single "variable" used to store multiple values.
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["Apple", "Orange", "Banana", "Coconut", "Kiwi", "Pear", "Strawberry", "Pineapple"]
# print(dir(fruits)) #Prints all methods
# print(help(fruits)) #Get help
# print(len(fruits)) #
# print("Apple" in fruits) #Boolean method (True or False)

# fruits[0] = "Mango" #Reassign values
# fruits.append("Mango") # Move variable to end
# fruits.remove("apple") # Removes value
# fruits.insert(0, "Mango") # Sets variables at certain value
# fruits.sort() # Sorts by alphabet
# fruits.reverse() # Reverses order of list
# fruits.clear() # Kills list

# print(fruits)

# print(fruits[0])
# for fruit in fruits:
   # print(fruit)

cars = ["BMW", "Maserati", "Audi", "Mercedes","Ferrari"]
print(f"these are a list of {cars}")
print(f"The first being from {cars[0]}")

# changing value of the list
cars[0] = "Lightning Mcqueen"
print(f"The first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1] = "Lamborghini"
print(f"the last car is {cars[-1]}")

# adding a new value
cars.append("Bugatti")
print(cars)
cars.remove("Maserati")
print(cars)

# Looping through the list (AKA iterating)
for car in cars:
   # print(len(car))
   # print(car)
    carRequest = input("Add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break