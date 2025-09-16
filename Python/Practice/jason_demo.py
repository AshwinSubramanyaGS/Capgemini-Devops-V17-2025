import json

# Python dictionary
""" data = {"Current batch":{
    "name": "V-17",
    "age": 24,
    "isStudent": False,
    "courses": ["DevOps", "Python"]
},
"Next batch":{
    "name": "V-17",
    "age": 24,
    "isStudent": False,
    "courses": ["Ansible", "Terraform"]
}
} """

# Serialize to JSON string
""" json_string = json.dumps(data, indent=4) # indent for pretty printing
print("JSON String:")
print(json_string)
 """

# Deserialize JSON string to Python object
""" python_object = json.loads(json_string)
print("\nPython Object (from JSON string):")
print(python_object)
 """
# Write to a JSON file
""" with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
 """
# Read from a JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print("\nLoaded Data (from JSON file):")
print(loaded_data)

loaded_data.update({"Future Batch":{
    "name": "V-17",
    "age": 24,
    "isStudent": False,
    "courses": ["Cloud", "Multicloud"]
}})

with open("data.json", "w") as f:
    json.dump(loaded_data, f, indent=4)
