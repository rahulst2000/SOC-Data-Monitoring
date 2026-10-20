import pandas as pd

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"
OUTPUT_FILE = "reports/tuned_detection.csv"

print("=" * 60)
print("SOC TUNED THREAT DETECTION")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

print(f"\nRecords analyzed: {len(df):,}")

# Convert detection features to numeric
features = [
    "Flow Pkts/s",
    "Flow Byts/s",
    "Flow Duration",
    "Tot Fwd Pkts",
    "Tot Bwd Pkts",
    "Pkt Len Mean"
]

for feature in features:
    df[feature] = pd.to_numeric(
        df[feature],
        errors="coerce"
    )

# --------------------------------------------------
# Detection indicators
# --------------------------------------------------

# Very high packet rate
df["HIGH_PACKET_RATE"] = (
    df["Flow Pkts/s"] > 13888.89
)

# High byte rate
df["HIGH_BYTE_RATE"] = (
    df["Flow Byts/s"] > 42970.21
)

# Very short flow duration
df["SHORT_FLOW"] = (
    df["Flow Duration"] < 83608
)

# Very low forward packet count
df["LOW_FWD_PACKETS"] = (
    df["Tot Fwd Pkts"] <= 3
)

# Very low backward packet count
df["LOW_BWD_PACKETS"] = (
    df["Tot Bwd Pkts"] <= 1
)

# Very small average packet length
df["LOW_PACKET_LENGTH"] = (
    df["Pkt Len Mean"] <= 120.75
)

# --------------------------------------------------
# Risk indicators
# --------------------------------------------------

indicator_columns = [
    "HIGH_PACKET_RATE",
    "HIGH_BYTE_RATE",
    "SHORT_FLOW",
    "LOW_FWD_PACKETS",
    "LOW_BWD_PACKETS",
    "LOW_PACKET_LENGTH"
]

df["RISK_INDICATORS"] = (
    df[indicator_columns].sum(axis=1)
)

# --------------------------------------------------
# Detection confidence
# --------------------------------------------------

df["DETECTION_STATUS"] = "NORMAL"

df.loc[
    df["RISK_INDICATORS"] >= 3,
    "DETECTION_STATUS"
] = "SUSPICIOUS"

# --------------------------------------------------
# Risk score
# --------------------------------------------------

df["RISK_SCORE"] = (
    df["RISK_INDICATORS"] * 20
)

df.loc[
    df["RISK_SCORE"] > 100,
    "RISK_SCORE"
] = 100

# --------------------------------------------------
# Detection type
# --------------------------------------------------

def detection_type(row):

    detections = []

    if row["HIGH_PACKET_RATE"]:
        detections.append("HIGH_PACKET_RATE")

    if row["HIGH_BYTE_RATE"]:
        detections.append("HIGH_BYTE_RATE")

    if row["SHORT_FLOW"]:
        detections.append("SHORT_FLOW")

    if row["LOW_FWD_PACKETS"]:
        detections.append("LOW_FWD_PACKETS")

    if row["LOW_BWD_PACKETS"]:
        detections.append("LOW_BWD_PACKETS")

    if row["LOW_PACKET_LENGTH"]:
        detections.append("LOW_PACKET_LENGTH")

    return ", ".join(detections)


df["DETECTION_TYPE"] = df.apply(
    detection_type,
    axis=1
)

# --------------------------------------------------
# Keep suspicious traffic
# --------------------------------------------------

alerts = df[
    df["DETECTION_STATUS"] == "SUSPICIOUS"
].copy()

print("\n--- DETECTION RESULTS ---")

print(
    df["DETECTION_STATUS"]
    .value_counts()
)

print("\n--- RISK DISTRIBUTION ---")

print(
    alerts["RISK_SCORE"]
    .value_counts()
    .sort_index()
)

print(
    f"\nSuspicious records detected: {len(alerts):,}"
)

# --------------------------------------------------
# Save detection output
# --------------------------------------------------

alerts.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    f"\nTuned detection output saved to: "
    f"{OUTPUT_FILE}"
)

print("\n" + "=" * 60)
print("TUNED THREAT DETECTION COMPLETED")
print("=" * 60)
