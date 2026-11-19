# EXP 28 - Detect Possible DoS Attack from Server Logs
logs = [
    "192.168.1.10", "192.168.1.10", "192.168.1.10",
    "192.168.1.10", "192.168.1.10", "192.168.1.20",
    "192.168.1.20", "192.168.1.30"
]
threshold = 4
counts = {}
for ip in logs:
    counts[ip] = counts.get(ip, 0) + 1

print("DoS Detection from Web Server Logs")
for ip, count in counts.items():
    print(ip, "->", count, "requests")
    if count > threshold:
        print("Possible DoS Attack from", ip)
