# collection = single "variable" used to store multiple values.
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ("Apple", "Orange", "Banana", "Coconut", "Kiwi", "Pear", "Strawberry", "Pineapple")
# print(dir(fruits)) #Prints all methods
# print(help(fruits)) #Get help
# print(len(fruits)) #
# print("Apple" in fruits) #Boolean method (True or False)

# print(fruits.index("Orange"))
# print(fruits.count("Coconut"))

#print(fruits)
#for fruit in fruits:
#   print(fruit)

# fruits.add("Cherry") adds a new thingy to the list
# fruits.remove("apple") can remove any variable in the list
# fruits.pop() pops off the first variable
# fruits.clear() MURDER THEM A- uh i mean, wipes the whole list

# fruits[0] = "Mango" #Reassign values
# fruits.append("Mango") # Move variable to end
# fruits.remove("apple") # Removes value
# fruits.insert(0, "Mango") # Sets variables at certain value
# fruits.sort() # Sorts by alphabet
# fruits.reverse() # Reverses order of list
# fruits.clear() # Kills list

#print(fruits)

# print(fruits[0])
# for fruit in fruits:
#    print(fruit)

#cars = ["BMW", "Maserati", "Audi", "Mercedes","Ferrari"]
#print(f"these are a list of {cars}")
#print(f"The first being from {cars[0]}")

# changing value of the list
#cars[0] = "Lightning Mcqueen"
#print(f"The first car is {cars[0]}")

#print(f"the last car is {cars[-1]}")
#cars[-1] = "Lamborghini"
#print(f"the last car is {cars[-1]}")

# adding a new value
#cars.append("Bugatti")
#print(cars)
#cars.remove("Maserati")
#print(cars)

# Looping through the list (AKA iterating)
#for car in cars:
   # print(len(car))
   # print(car)
   # carRequest = input("Add a new car please: ")
   # cars.append(carRequest)
   # print(cars)
   # print(len(cars))
   # print(cars)
   # if len(cars) > 10:
       # break
    #space
#space

#Challenge
#create a list of friend
#Make sure the intial list is none
# friends = []
# add a new friend to the list, add at least 5
# remove a friend
# insert a new friend at a specific index (maybe 2)
# print the list
# loop through the list and print the friends names
# see if a particular friend is in the list (Boolean value)
# if the list is greater than 10, break the loop.
# friendRequest = input("Add a new friend please: ")
# friends.append(friendRequest)
# print(len(friends))
# print(friends)
# friendRequest = input("Add a new friend please: ")
# friends.append(friendRequest)
# print(len(friends))
# print(friends)
# friendRequest = input("Add a new friend please: ")
# friends.append(friendRequest)
# print(len(friends))
# print(friends)
# friendRequest = input("Add a new friend please: ")
# friends.append(friendRequest)
# print(len(friends))
# print(friends)
# friendRequest = input("Add a new friend please: ")
# friends.append(friendRequest)
# print(len(friends))
# print(friends)
# friends.remove("DaddyDoc")
# friends.insert(2, "Drift")
# print(friends)
# print("Cryptic" in friends)

# dictionary = a collection of {key:value} pairs ordered and changeable. No dupes

# capitals = {"USA": "Washington D.C",
#            "India": "New Delhi",
#            "China": "Beijing",
#            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")

# print(capitals)