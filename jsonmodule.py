import json 

data = {
    "Indore" : 2500000,
    "Delhi"  : 3000000,
    "Pune"   : 2000000
}
with open("cities.json","w") as f:
    json_file = json.dump(data,f)

with open("cities.json", "r") as f:
    data = json.load(f)

for city, population in data.items():
    print(city, population)

city = input("Enter new city: ")
population = int(input("Enter population: "))

data[city] = population

with open("cities.json", "w") as f:
    json.dump(data, f)