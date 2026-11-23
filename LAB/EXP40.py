# Recommend a security tool based on task keywords
tools = {
    "network scanning": "Nmap",
    "packet analysis": "Wireshark",
    "vulnerability scanning": "Nessus",
    "web application testing": "Burp Suite",
    "intrusion detection": "Snort"
}

task = "I need packet analysis for network traffic"
text = task.lower()
recommendation = "No matching tool found"
for keyword, tool in tools.items():
    if keyword in text or (keyword == "packet analysis" and "packet" in text):
        recommendation = tool
        break

print("Security Task:", task)
print("Recommended Tool:", recommendation)
