import pandas as pd

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"
OUTPUT_FILE = "reports/detection_engine_v2.csv"

print("=" * 60)
print("SOC DETECTION ENGINE V2")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

print(f"\nRecords analyzed: {len(df):,}")

# --------------------------------------------------
# Convert security features to numeric values
# --------------------------------------------------

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

df["IND_HIGH_PACKET_RATE"] = (
    df["Flow Pkts/s"] > 13888.89
)

df["IND_HIGH_BYTE_RATE"] = (
    df["Flow Byts/s"] > 42970.21
)

df["IND_SHORT_FLOW"] = (
    df["Flow Duration"] < 83608
)

df["IND_HIGH_FWD_PACKETS"] = (
    df["Tot Fwd Pkts"] > 5
)

df["IND_HIGH_BWD_PACKETS"] = (
    df["Tot Bwd Pkts"] > 5
)

df["IND_LARGE_PACKET"] = (
    df["Pkt Len Mean"] > 181.82
)

# --------------------------------------------------
# Count indicators
# --------------------------------------------------

indicator_columns = [
    "IND_HIGH_PACKET_RATE",
    "IND_HIGH_BYTE_RATE",
    "IND_SHORT_FLOW",
    "IND_HIGH_FWD_PACKETS",
    "IND_HIGH_BWD_PACKETS",
    "IND_LARGE_PACKET"
]

df["INDICATOR_COUNT"] = (
    df[indicator_columns].sum(axis=1)
)

# --------------------------------------------------
# Risk score
# --------------------------------------------------

df["RISK_SCORE"] = (
    df["INDICATOR_COUNT"] * 20
)

df.loc[
    df["RISK_SCORE"] > 100,
    "RISK_SCORE"
] = 100

# --------------------------------------------------
# Detection decision
# --------------------------------------------------

df["DETECTION_STATUS"] = "NORMAL"

df.loc[
    df["INDICATOR_COUNT"] >= 2,
    "DETECTION_STATUS"
] = "SUSPICIOUS"

# --------------------------------------------------
# Detection explanation
# --------------------------------------------------

def get_detection_type(row):

    detections = []

    if row["IND_HIGH_PACKET_RATE"]:
        detections.append("HIGH_PACKET_RATE")

    if row["IND_HIGH_BYTE_RATE"]:
        detections.append("HIGH_BYTE_RATE")

    if row["IND_SHORT_FLOW"]:
        detections.append("SHORT_FLOW")

    if row["IND_HIGH_FWD_PACKETS"]:
        detections.append("HIGH_FORWARD_PACKETS")

    if row["IND_HIGH_BWD_PACKETS"]:
        detections.append("HIGH_BACKWARD_PACKETS")

    if row["IND_LARGE_PACKET"]:
        detections.append("LARGE_PACKET")

    return ", ".join(detections)


df["DETECTION_TYPE"] = df.apply(
    get_detection_type,
    axis=1
)

# --------------------------------------------------
# Results
# --------------------------------------------------

alerts = df[
    df["DETECTION_STATUS"] == "SUSPICIOUS"
].copy()

print("\n--- DETECTION STATUS ---")

print(
    df["DETECTION_STATUS"]
    .value_counts()
)

print("\n--- INDICATOR COUNT ---")

print(
    df["INDICATOR_COUNT"]
    .value_counts()
    .sort_index()
)

print("\n--- RISK SCORE ---")

print(
    df["RISK_SCORE"]
    .value_counts()
    .sort_index()
)

print(
    f"\nSuspicious records: {len(alerts):,}"
)

print("\n--- DETECTION TYPES ---")

print(
    alerts["DETECTION_TYPE"]
    .value_counts()
    .head(20)
)

# --------------------------------------------------
# Save
# --------------------------------------------------

alerts.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    f"\nDetection output saved to: {OUTPUT_FILE}"
)

print("\n" + "=" * 60)
print("DETECTION ENGINE V2 COMPLETED")
print("=" * 60)
