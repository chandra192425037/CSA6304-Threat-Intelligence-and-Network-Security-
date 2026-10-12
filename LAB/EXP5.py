s = input("Enter report: ").lower()
if "executive" in s or "long-term" in s:
    print("Strategic")
elif "attacker tactics" in s or "techniques" in s:
    print("Tactical")
else:
    print("Operational")
