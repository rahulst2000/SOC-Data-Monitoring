import pandas as pd

INPUT_FILE = "reports/soc_alerts.csv"
OUTPUT_FILE = "reports/root_cause_analysis.csv"

print("=" * 60)
print("SOC L1 ROOT CAUSE & FALSE POSITIVE ANALYSIS")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

print(f"\nAlerts loaded: {len(df):,}")

# --------------------------------------------------
# Ground-truth validation
# --------------------------------------------------

if "Label" in df.columns:

    benign_alerts = df[
        df["Label"].astype(str).str.strip().str.lower() == "benign"
    ]

    attack_alerts = df[
        df["Label"].astype(str).str.strip().str.lower() != "benign"
    ]

    print("\n--- GROUND-TRUTH VALIDATION ---")

    print(f"Potential false positives : {len(benign_alerts):,}")
    print(f"Alerts matching attacks   : {len(attack_alerts):,}")

else:

    benign_alerts = pd.DataFrame()
    attack_alerts = pd.DataFrame()

    print("\nLabel column not available.")

# --------------------------------------------------
# Detection type analysis
# --------------------------------------------------

print("\n--- DETECTION TYPES ---")

print(
    df["DETECTION_TYPE"]
    .value_counts()
)

# --------------------------------------------------
# Severity analysis
# --------------------------------------------------

print("\n--- SEVERITY ---")

print(
    df["SEVERITY"]
    .value_counts()
)

# --------------------------------------------------
# Risk score analysis
# --------------------------------------------------

print("\n--- RISK SCORES ---")

print(
    df["RISK_SCORE"]
    .value_counts()
    .sort_index()
)

# --------------------------------------------------
# Root cause classification
# --------------------------------------------------

def classify_root_cause(row):

    label = str(row.get("Label", "")).strip().lower()

    detection = str(
        row.get("DETECTION_TYPE", "")
    )

    if label == "benign":

        return "BENIGN_TRAFFIC_TRIGGERED_THRESHOLD"

    if "HIGH_BYTE_RATE" in detection:

        return "HIGH_TRAFFIC_VOLUME"

    if "HIGH_FORWARD_PACKETS" in detection:

        return "ABNORMAL_PACKET_VOLUME"

    return "REQUIRES_INVESTIGATION"


df["ROOT_CAUSE"] = df.apply(
    classify_root_cause,
    axis=1
)

# --------------------------------------------------
# Recommended L1 disposition
# --------------------------------------------------

def determine_disposition(row):

    label = str(row.get("Label", "")).strip().lower()

    if label == "benign":

        return "FALSE_POSITIVE_CANDIDATE"

    return "ESCALATE_TO_L2"


df["L1_DISPOSITION"] = df.apply(
    determine_disposition,
    axis=1
)

# --------------------------------------------------
# Investigation notes
# --------------------------------------------------

def investigation_note(row):

    if row["L1_DISPOSITION"] == "FALSE_POSITIVE_CANDIDATE":

        return (
            "Alert triggered by statistical traffic threshold. "
            "Dataset ground truth identifies this flow as benign. "
            "Validate application context before closing."
        )

    return (
        "Traffic matches non-benign ground truth. "
        "Review source, destination, timeline and related events. "
        "Escalate to L2 if malicious activity is confirmed."
    )


df["INVESTIGATION_NOTE"] = df.apply(
    investigation_note,
    axis=1
)

# --------------------------------------------------
# Save RCA report
# --------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n--- ROOT CAUSE SUMMARY ---")

print(
    df["ROOT_CAUSE"]
    .value_counts()
)

print("\n--- L1 DISPOSITION ---")

print(
    df["L1_DISPOSITION"]
    .value_counts()
)

print(
    f"\nRCA report saved to: {OUTPUT_FILE}"
)

print("\n" + "=" * 60)
print("ROOT CAUSE ANALYSIS COMPLETED")
print("=" * 60)
