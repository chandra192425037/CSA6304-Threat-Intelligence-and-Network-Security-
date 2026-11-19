# EXP 30 - SIEM Correlation using Firewall, Windows and VPN Logs
firewall_log = {"source_ip": "203.0.113.9", "blocked_attempts": 8}
windows_log = {"source_ip": "203.0.113.9", "failed_logins": 6}
vpn_log = {"source_ip": "203.0.113.9", "login_failed": True}

same_ip = (firewall_log["source_ip"] == windows_log["source_ip"]
           == vpn_log["source_ip"])
attack = (same_ip and firewall_log["blocked_attempts"] >= 5
          and windows_log["failed_logins"] >= 5 and vpn_log["login_failed"])

print("SIEM Log Correlation")
print("Firewall Blocked Attempts:", firewall_log["blocked_attempts"])
print("Windows Failed Logins:", windows_log["failed_logins"])
print("VPN Login Failed:", vpn_log["login_failed"])
print("Source IP:", firewall_log["source_ip"])
print("Alert:", "Possible Brute-Force Attack" if attack else "No Correlated Attack")
