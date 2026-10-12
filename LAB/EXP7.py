logs = ["INFO login", "ERROR failed", "INFO login"]
index = {}
for log in logs:
    level = log.split()[0]
    index[level] = index.get(level, 0) + 1
print("Indexed Logs:", len(logs))
print("Kibana Summary:", index)
