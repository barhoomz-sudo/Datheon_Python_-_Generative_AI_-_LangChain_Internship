import json

person = {
    "name": "Ibrahim",
    "age": 25,
    "country": "Somalia"
}

to_json = json.dumps(person, indent=4)

print(to_json)
print(type(to_json))

py_data = json.loads(to_json)

print(py_data)
print(type(py_data))