# Simple Threat Intelligence Platform (TIP)
ioc_feed = ["  192.168.1.10 ", "MALWARE.EXAMPLE.COM", "bad-hash-123"]
internal_logs = ["Login from 192.168.1.10", "User opened example.com",
                 "File hash bad-hash-123 found"]

normalized = [ioc.strip().lower() for ioc in ioc_feed]
print("Normalized IOCs:", normalized)
print("Alerts:")
for ioc in normalized:
    for log in internal_logs:
        if ioc in log.lower():
            print("MATCH:", ioc, "->", log)
