# EXP 32 - Detect Violations of CIA Security Principles
properties = [
    ("Data encryption", "Confidentiality", True),
    ("File checksum", "Integrity", False),
    ("Server uptime", "Availability", True),
    ("Access control", "Confidentiality", False)
]
violations = set()

for name, principle, status in properties:
    if not status:
        violations.add(principle)

print("CIA Security Principle Check")
for name, principle, status in properties:
    print(name, "-", principle, ":", "OK" if status else "VIOLATED")
print("Violated Principles:",
      ", ".join(sorted(violations)) if violations else "None")
