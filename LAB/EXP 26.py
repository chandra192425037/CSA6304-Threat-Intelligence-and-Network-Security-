# EXP 26 - Simplified Static and Dynamic Malware Analysis
sample = "CreateRemoteThread VirtualAlloc WriteProcessMemory"
behavior_log = ["Process started", "Attempted registry modification",
                "Suspicious network connection"]

suspicious_apis = ["CreateRemoteThread", "VirtualAlloc",
                   "WriteProcessMemory"]

print("Malware Analysis")
print("Sample Hash (demo):", "a1b2c3d4")
found = [api for api in suspicious_apis if api in sample]
print("Suspicious APIs:", ", ".join(found) if found else "None")
print("Static Analysis:", "Suspicious" if found else "Clean")
print("Behavior Log:", "; ".join(behavior_log))
print("Dynamic Analysis:", "Suspicious Activity Found"
      if len(behavior_log) > 1 else "No Suspicious Activity")
