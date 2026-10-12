policy = input("Enter policy text: ").lower()
items = ["scope", "roles", "enforcement",
         "review", "approval"]
for item in items:
    if item in policy:
        print(item, ": Present")
    else:
        print(item, ": Missing")
