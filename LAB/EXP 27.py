# EXP 27 - Minimal Signature-Based Intrusion Detection System
packet = {
    "protocol": "TCP",
    "port": 80,
    "content": "GET /page?id=1 OR 1=1"
}
signatures = ["OR 1=1", "UNION SELECT"]
web_context = packet["protocol"] == "TCP" and packet["port"] == 80
content_match = any(item in packet["content"] for item in signatures)

print("Signature-Based IDS")
print("Protocol:", packet["protocol"])
print("Port:", packet["port"])
print("Content Match:", "Yes" if content_match else "No")
if web_context and content_match:
    print("Alert: Intrusion Detected")
else:
    print("Alert: No Intrusion")
