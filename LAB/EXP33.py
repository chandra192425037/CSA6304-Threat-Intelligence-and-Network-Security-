# Classify an incident response action into its lifecycle phase
phases = {
    "prepare": "Preparation", "identify": "Identification",
    "detect": "Identification", "contain": "Containment",
    "isolate": "Containment", "remove": "Eradication",
    "patch": "Eradication", "restore": "Recovery",
    "backup": "Recovery", "review": "Lessons Learned",
    "document": "Lessons Learned"
}

action = "Isolate the infected computer from the network"
phase = "Unknown"
for word, name in phases.items():
    if word in action.lower():
        phase = name
        break

print("Action:", action)
print("Incident Response Phase:", phase)
