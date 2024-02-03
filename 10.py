people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 15}]

min_age = min(person["age"] for person in people)
youngest_names = [person["name"] for person in people if person["age"] == min_age]

print("Наймолодші люди:", youngest_names)

people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 25}]

max_length = max(len(person["name"]) for person in people)
longest_names = [person["name"] for person in people if len(person["name"]) == max_length]

print("Найдовші імена:", longest_names)

people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 25}]

average_age = sum(person["age"] for person in people) / len(people)

print("Середній вік:", average_age)