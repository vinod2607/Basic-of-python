#Dictionary

karnataka_food = {
    "Bengaluru" : "bisi bele bath",
    "Mysuru" : "mysore pak",
    "Mangalore" : "neer dosa"
}

print(karnataka_food)

print(karnataka_food["Mysuru"])


print(karnataka_food.get("Mangalore"))

print(karnataka_food.get("Raichur","Not found"))

#Adding dictionary

karnataka_food["Ballari"] = "cova"
print(karnataka_food)

#updating

karnataka_food["Bengaluru"] = "dosa"
print(karnataka_food)

#deleting

del karnataka_food["Mysuru"]

print(karnataka_food)


item1 = {
    "name": "milk",
    "weight" : "1",
    "price" : 50
}

item2 = {
    "name" : "sugar",
    "weight" : "1",
    "price" : 99.9
}

items = [item1 , item2 ,]

print(items)


item1 = {
    "name": "milk",
    "weight" : "1",
    "price" : 50
}

item2 = {
    "name" : "sugar",
    "weight" : "1",
    "price" : 99.9
}

print(f"total weight : {item1["weight"] + item2["weight"]}")


