# EXP 25 - Verify Evidence Chain of Custody
records = [
    {"id": "E1", "previous_hash": "GENESIS", "hash": "A100", "timestamp": 10},
    {"id": "E2", "previous_hash": "A100", "hash": "B200", "timestamp": 15},
    {"id": "E3", "previous_hash": "B200", "hash": "C300", "timestamp": 20}
]

valid = True
for i in range(1, len(records)):
    if records[i]["previous_hash"] != records[i - 1]["hash"]:
        valid = False
    if records[i]["timestamp"] < records[i - 1]["timestamp"]:
        valid = False

print("Evidence Chain Verification")
print("Hash Chain:", "Valid" if valid else "Broken")
print("Timestamp Chain:", "Valid" if valid else "Invalid")
print("Result:", "Chain is Unbroken" if valid else "Chain is Broken")
