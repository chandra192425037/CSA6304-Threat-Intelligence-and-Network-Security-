# EXP 31 - Simple Packet-Filtering Firewall Rule Engine
rules = [
    {"protocol": "TCP", "port": 80, "action": "ALLOW"},
    {"protocol": "TCP", "port": 22, "action": "DENY"}
]
packet = {"protocol": "TCP", "port": 22}

def check_packet(packet, rules):
    for rule in rules:
        if (packet["protocol"] == rule["protocol"]
                and packet["port"] == rule["port"]):
            return rule["action"]
    return "DENY"  # Default-deny

print("Packet Filtering Firewall")
print("Packet:", packet["protocol"], "Port", packet["port"])
print("Rules: TCP/80 ALLOW, TCP/22 DENY")
print("Decision:", check_packet(packet, rules))
print("Unmatched packets: DENY (default)")
