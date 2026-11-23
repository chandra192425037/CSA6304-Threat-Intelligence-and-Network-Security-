# Demonstrate three threat-hunting styles
logs = ["Failed login from 10.0.0.9", "Malware hash detected",
        "Normal user login", "Connection to 10.0.0.9"]

# 1. Hypothesis-based hunting
hypothesis = [x for x in logs if "failed login" in x.lower()]
# 2. Intelligence-based hunting
known_ioc = "10.0.0.9"
intelligence = [x for x in logs if known_ioc in x]
# 3. Analytics-based hunting
analytics = [x for x in logs if "malware" in x.lower()]

print("Hypothesis-based:", hypothesis)
print("Intelligence-based:", intelligence)
print("Analytics-based:", analytics)
