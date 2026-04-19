# #Q1.

# with open("names.txt","w") as f:
#     f.write("sayan\nsuman\nsuraj\navijit\nprokash")

# with open("names.txt","r") as f:
#     print(f.read())

# #Q2.

# with open("log.txt","r") as f:
#     # f.write("program run succesfully")
#     print(f.read())


# #Q3.

# list = [5,10,15,20,25]

# result = [val for val in list if val >15]

# print(result)



#Q4.


# #part 1


# import json

# cities = {
#     "Kolkata": 15000000,
#     "Mumbai": 20000000,
#     "Delhi": 19000000
# }

# with open("cities.json", "w") as file:
#     json.dump(cities, file, indent=4)


# #part 2

# import json

# with open("cities.json", "r") as file:
#     data = json.load(file)

# for city, population in data.items():
#     print(f"{city}: {population}")


# #part 3

# import json

# # Load existing data
# with open("cities.json", "r") as file:
#     data = json.load(file)

# # Take input
# new_city = input("Enter new city name: ")
# new_population = int(input("Enter population: "))

# # Update dictionary
# data[new_city] = new_population

# # Save back to JSON
# with open("cities.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("Data updated successfully!")


#Q5.

try:
    with open("data.txt","r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found!")
