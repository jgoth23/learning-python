people = [
  {"name": "Harry", "House": "Gryffindor"},
  {"name": "Draco", "House": "Slytherin"},
  {"name": "Cho", "House": "Ravenclaw"}
]

def f(person):
    return person["name"]

people.sort(key=f)
print(people)