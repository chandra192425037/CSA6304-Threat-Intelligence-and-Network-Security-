# Calculate qualitative risk score
likelihood = 4
impact = 5
score = likelihood * impact

if score >= 20:
    level = "Critical"
elif score >= 15:
    level = "High"
elif score >= 8:
    level = "Medium"
else:
    level = "Low"

print("Likelihood:", likelihood)
print("Impact:", impact)
print("Risk Score:", score, "/ 25")
print("Risk Level:", level)
