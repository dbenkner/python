print("Welcome to control structures")

print(f"Use a match command for a CRUD app")
command = input("Enter a command (list, add, edit): ").lower()
match command:
    case "list":
        print("List Selected")
    case "add":
        print("Add Selected")
    case "edit":
        print("Edit Selected")
    case _: #default case or catch all 
        print("Unknown Command. Try Again.")

print("\n--- loops ---")

even_nbrs = [2, 4,6,8,10]
for nbr in even_nbrs:
    print(f"nbr = {nbr}")

## range starts at 0 for default, stops at 4
for i in range(len(even_nbrs)):
    print(f"{i}: {even_nbrs[i]}", end =", ")

## enumerate
print("\n -- enumerate ---")
for i in enumerate(even_nbrs):
    print(i, i[0], i[1])
for idx, value in enumerate(even_nbrs):
    print(f"idx = {idx}, value = {value}")

## range including start (inclusive) and stop (exclsuive)

for n in range(1,10):
    print(f"n == {n}")
print()
# range including "stepp"
for n  in range(0,10,2):
    print(f"n = {n}")

print("Bye")
