# Simulate continuous login monitoring
baseline = {"India": 5, "USA": 2}
events = [("user1", "India"), ("user2", "USA"),
          ("user3", "Unknown"), ("user4", "Unknown")]

print("Monitoring login events...")
for user, location in events:
    if location not in baseline or baseline[location] == 0:
        print("ALERT:", user, "login from unusual location:", location)
    else:
        print("Normal:", user, "from", location)
