people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Cho", "house": "Ravenclaw"}
]

def f(person):
    return person["house"]

people.sort(key=f)
print(people)