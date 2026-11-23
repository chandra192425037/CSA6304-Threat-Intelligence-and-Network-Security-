# Audit accounts using the principle of least privilege
roles = {"Admin": {"read", "write", "delete"},
         "Analyst": {"read", "analyze"},
         "Guest": {"read"}}
accounts = {"Arun": ("Analyst", {"read", "analyze", "delete"}),
            "Bala": ("Guest", {"read"}),
            "Charan": ("Admin", {"read", "write"})}

for user, (role, access) in accounts.items():
    excess = access - roles[role]
    print(user, "-", role, "- Excess access:", sorted(excess) if excess else "None")
