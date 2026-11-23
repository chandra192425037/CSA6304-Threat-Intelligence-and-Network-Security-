# Identify the likely compliance standard

def find_standard(description):
    text = description.lower()
    if "credit card" in text or "payment card" in text:
        return "PCI-DSS"
    if "patient" in text or "medical" in text or "health" in text:
        return "HIPAA"
    if "personal data" in text or "eu citizen" in text:
        return "GDPR"
    if "financial report" in text or "public company" in text:
        return "SOX"
    return "No clear match"

system = "System stores patient medical records"
print("System:", system)
print("Likely Standard:", find_standard(system))
