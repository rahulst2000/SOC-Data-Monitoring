import pandas as pd

INPUT_FILE = "reports/threat_detection.csv"
OUTPUT_FILE = "reports/soc_alerts.csv"

print("=" * 60)
print("SOC L1 AUTOMATED ALERT GENERATION")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

print(f"\nSuspicious records loaded: {len(df):,}")

# --------------------------------------------------
# Determine detection type
# --------------------------------------------------

def determine_detection(row):

    detections = []

    if row["HIGH_PACKET_RATE"]:
        detections.append("HIGH_PACKET_RATE")

    if row["HIGH_BYTE_RATE"]:
        detections.append("HIGH_BYTE_RATE")

    if row["HIGH_FWD_PACKETS"]:
        detections.append("HIGH_FORWARD_PACKETS")

    if row["HIGH_BWD_PACKETS"]:
        detections.append("HIGH_BACKWARD_PACKETS")

    return ", ".join(detections)


df["DETECTION_TYPE"] = df.apply(
    determine_detection,
    axis=1
)

# --------------------------------------------------
# Severity classification
# --------------------------------------------------

def determine_severity(score):

    if score >= 75:
        return "CRITICAL"

    elif score >= 50:
        return "HIGH"

    elif score >= 25:
        return "MEDIUM"

    else:
        return "LOW"


df["SEVERITY"] = df["RISK_SCORE"].apply(
    determine_severity
)

# --------------------------------------------------
# Alert IDs
# --------------------------------------------------

df.insert(
    0,
    "ALERT_ID",
    [
        f"ALERT-{i:05d}"
        for i in range(1, len(df) + 1)
    ]
)

# --------------------------------------------------
# Investigation status
# --------------------------------------------------

df["STATUS"] = "OPEN"

# --------------------------------------------------
# Recommended SOC L1 action
# --------------------------------------------------

def recommended_action(severity):

    if severity == "CRITICAL":
        return "Immediate investigation and L2 escalation"

    elif severity == "HIGH":
        return "Investigate source and destination traffic"

    elif severity == "MEDIUM":
        return "Validate activity and check for related events"

    else:
        return "Monitor"


df["RECOMMENDED_ACTION"] = df["SEVERITY"].apply(
    recommended_action
)

# --------------------------------------------------
# Select important alert fields
# --------------------------------------------------

alert_columns = [
    "ALERT_ID",
    "Timestamp",
    "Src IP",
    "Dst IP",
    "Dst Port",
    "Protocol",
    "Label",
    "DETECTION_TYPE",
    "RISK_INDICATORS",
    "RISK_SCORE",
    "SEVERITY",
    "STATUS",
    "RECOMMENDED_ACTION"
]

# Keep only columns that actually exist
alert_columns = [
    column
    for column in alert_columns
    if column in df.columns
]

alerts = df[alert_columns].copy()

# --------------------------------------------------
# Display summary
# --------------------------------------------------

print("\n--- ALERT SUMMARY ---")

print(f"Total alerts: {len(alerts):,}")

print("\nSeverity distribution:")

print(
    alerts["SEVERITY"]
    .value_counts()
)

print("\nDetection types:")

print(
    alerts["DETECTION_TYPE"]
    .value_counts()
)

# --------------------------------------------------
# Save alerts
# --------------------------------------------------

alerts.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nAlerts saved to: {OUTPUT_FILE}")

print("\n--- SAMPLE ALERTS ---")

print(
    alerts.head(10).to_string(index=False)
)

print("\n" + "=" * 60)
print("SOC ALERT GENERATION COMPLETED")
print("=" * 60)
