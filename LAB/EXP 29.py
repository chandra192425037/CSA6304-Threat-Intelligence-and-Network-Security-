# EXP 29 - Recommend an Incident Containment Strategy
incident = "malware infection"

print("Incident Containment Recommendation")
print("Incident:", incident)
if "malware" in incident.lower():
    strategy = "Isolate the infected system from the network"
elif "data leak" in incident.lower():
    strategy = "Disable affected accounts and restrict data access"
elif "ddos" in incident.lower() or "dos" in incident.lower():
    strategy = "Apply traffic filtering and rate limiting"
elif "ransomware" in incident.lower():
    strategy = "Disconnect affected devices and protect backups"
else:
    strategy = "Restrict affected access and investigate the incident"
print("Recommended Strategy:", strategy)
print("Status: Containment Recommended")
