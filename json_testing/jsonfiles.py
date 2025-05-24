import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))  # data is stored as a python dict

# writing to a json file
with open("data2.json", "w") as f:
    json.dump(data, f, indent=2)
