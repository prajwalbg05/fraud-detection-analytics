from services.chroma_client import add_documents

# =========================================================
# 🔹 Fraud Domain Knowledge Documents
# =========================================================
docs = [

    "Multiple failed login attempts may indicate brute-force attacks or unauthorized access attempts.",

    "Rapid transactions across multiple countries can indicate money laundering activity.",

    "Large withdrawals immediately after password reset are considered suspicious behavior.",

    "Transactions from geographically distant locations within a short period may indicate account compromise.",

    "Frequent small transactions below reporting thresholds may indicate structuring activity.",

    "Multiple accounts using the same IP address may indicate coordinated fraudulent behavior.",

    "Sudden spikes in transaction volume may indicate stolen account usage.",

    "Repeated declined card transactions can indicate card testing fraud.",

    "Access from anonymous VPN or proxy services increases fraud risk.",

    "Unusual device changes combined with high-value transactions may indicate identity theft."

]

# =========================================================
# 🔹 Seed ChromaDB
# =========================================================
add_documents(docs)

print("✅ Successfully seeded ChromaDB with fraud documents.")