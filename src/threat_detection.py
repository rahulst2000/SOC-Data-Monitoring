import pandas as pd

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"
OUTPUT_FILE = "reports/threat_detection.csv"

print("=" * 60)
print("SOC THREAT DETECTION")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

print(f"\nRecords analyzed: {len(df):,}")

# Convert required features to numeric
features = [
    "Flow Pkts/s",
    "Flow Byts/s",
    "Flow Duration",
    "Tot Fwd Pkts",
    "Tot Bwd Pkts"
]

for feature in features:
    df[feature] = pd.to_numeric(df[feature], errors="coerce")

# Detection thresholds based on observed dataset baseline
packet_rate_threshold = 400000
byte_rate_threshold = 28160.90
fwd_packet_threshold = 5
bwd_packet_threshold = 5

# Detection indicators
df["HIGH_PACKET_RATE"] = (
    df["Flow Pkts/s"] >= packet_rate_threshold
)

df["HIGH_BYTE_RATE"] = (
    df["Flow Byts/s"] >= byte_rate_threshold
)

df["HIGH_FWD_PACKETS"] = (
    df["Tot Fwd Pkts"] > fwd_packet_threshold
)

df["HIGH_BWD_PACKETS"] = (
    df["Tot Bwd Pkts"] > bwd_packet_threshold
)

# Calculate number of suspicious indicators
df["RISK_INDICATORS"] = (
    df[
        [
            "HIGH_PACKET_RATE",
            "HIGH_BYTE_RATE",
            "HIGH_FWD_PACKETS",
            "HIGH_BWD_PACKETS"
        ]
    ]
    .sum(axis=1)
)

# Candidate detection
df["DETECTION_STATUS"] = "NORMAL"

df.loc[
    df["RISK_INDICATORS"] >= 2,
    "DETECTION_STATUS"
] = "SUSPICIOUS"

# Risk score
df["RISK_SCORE"] = df["RISK_INDICATORS"] * 25

print("\n--- DETECTION RESULTS ---")

print(
    df["DETECTION_STATUS"]
    .value_counts()
)

print("\n--- RISK DISTRIBUTION ---")

print(
    df["RISK_SCORE"]
    .value_counts()
    .sort_index()
)

# Keep suspicious records
alerts = df[
    df["DETECTION_STATUS"] == "SUSPICIOUS"
].copy()

print(
    f"\nSuspicious records detected: {len(alerts):,}"
)

# Save alerts
alerts.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nAlerts saved to: {OUTPUT_FILE}")

print("\n" + "=" * 60)
print("THREAT DETECTION COMPLETED")
print("=" * 60)
