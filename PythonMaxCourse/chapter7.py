from person_class import Person
print("Welcome to creating Person instances!")

person = Person(1, "Marty", "McFly", "marty@b2f.com", "585-585-1989")
print("Person INfo:")
print(f"id: {person.id}")
print(f"name: {person.first_name} {person.last_name}")
print(f"email: {person.email}")
print(f"phone: {person.phone}")
person.phone = "444-444-4444"
print(f"phone: {person.phone}")

print("bye")