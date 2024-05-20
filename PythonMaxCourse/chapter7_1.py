from person_class import Person
choice = "y"
id = 1
print("Welcome to the contact list applicatoin")
while choice == "y":
    first_name = str(input("Enter First Name: "))
    last_name = str(input("Enter Last Name: "))
    email = str(input("Enter Email Address: "))
    phone = str(input("Enter Phone: "))
    person = Person(id, first_name, last_name, email, phone)
    print(person.get_person_details())
    choice = input("Continue? (y/n): ").lower()
