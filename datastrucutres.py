#list
cars = ["Mercedes", "Subaru", "Toyota", "VW", ]
num= [5,7,8,48,90,232,89,0.1]
cars.sort()

print(cars)
print(f"I love {cars[1]}")

print(num)

#tupple are immutable(unchangeable). accepts duplicates
fruits= ("banana", "mangoes", "berries", "banana")
print(fruits[2])
print(fruits)

#set unordered
color={"yellow", "blue", "red"}
print(color)

#dictionaries. Has key and corresponding values
employees = {"name": "becky", "Age": 89,}
print(employees)
print(f"The age of {employees['name']} is {employees['Age']}") # use the keys to access the values in the dictionary
