import json


f1 = open("dataJourn\data\hateCrimesData.csv", "r")
lines = f1.readlines()

dictionary ={}

# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("hateCrimesData.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
