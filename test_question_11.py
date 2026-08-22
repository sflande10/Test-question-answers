import json
mark = {
    "name": "Mark",
    "age": "20",
    "Major": "Computer Science"
}
with open("mark.json", "w") as file:
    json.dump(mark, file, indent=4)
with open("mark.json", "r") as file:
    mark_data = json.load(file)
print(mark_data)