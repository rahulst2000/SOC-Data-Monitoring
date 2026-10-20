import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"
OUTPUT_DIR = Path("screenshots")

OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("SOC PROJECT VISUALIZATION")
print("=" * 60)

df = pd.read_csv(
    INPUT_FILE,
    usecols=["Label"],
    low_memory=False
)

label_counts = df["Label"].value_counts()

print("\nTraffic distribution:")
print(label_counts)

plt.figure(figsize=(10, 6))

label_counts.plot(kind="bar")

plt.title("CSE-CIC-IDS2018 Traffic Distribution")
plt.xlabel("Traffic / Attack Type")
plt.ylabel("Number of Records")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

output_file = OUTPUT_DIR / "01_attack_distribution.png"

plt.savefig(output_file, dpi=200)
plt.close()

print(f"\nVisualization saved to: {output_file}")
print("\nVisualization completed successfully.")
# Detection Engine V2

detection_df = pd.read_csv(
    "reports/detection_engine_v2.csv",
    usecols=["DETECTION_STATUS"],
    low_memory=False
)

detection_counts = detection_df["DETECTION_STATUS"].value_counts()

plt.figure(figsize=(8, 6))
detection_counts.plot(kind="bar")

plt.title("SOC Detection Engine V2 Results")
plt.xlabel("Detection Status")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()

output_file = OUTPUT_DIR / "02_detection_engine_v2.png"

plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")
# Risk Score Distribution

risk_df = pd.read_csv(
    "reports/detection_engine_v2.csv",
    usecols=["RISK_SCORE"],
    low_memory=False
)

risk_counts = risk_df["RISK_SCORE"].value_counts().sort_index()

plt.figure(figsize=(8, 6))
risk_counts.plot(kind="bar")

plt.title("SOC Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()

output_file = OUTPUT_DIR / "03_risk_score_distribution.png"
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")


# Alert Severity Distribution

alert_df = pd.read_csv(
    "reports/soc_alerts.csv",
    usecols=["SEVERITY"],
    low_memory=False
)

severity_counts = alert_df["SEVERITY"].value_counts()

plt.figure(figsize=(8, 6))
severity_counts.plot(kind="bar")

plt.title("SOC Alert Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=0)
plt.tight_layout()

output_file = OUTPUT_DIR / "04_alert_severity.png"
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")


# Detection Type Distribution

detection_type_counts = alert_df = pd.read_csv(
    "reports/soc_alerts.csv",
    usecols=["DETECTION_TYPE"],
    low_memory=False
)["DETECTION_TYPE"].value_counts().head(10)

plt.figure(figsize=(10, 6))
detection_type_counts.plot(kind="bar")

plt.title("Top SOC Detection Types")
plt.xlabel("Detection Type")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

output_file = OUTPUT_DIR / "05_detection_types.png"
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")


# Root Cause / False Positive Analysis

rca_df = pd.read_csv(
    "reports/root_cause_analysis.csv",
    usecols=["L1_DISPOSITION"],
    low_memory=False
)

disposition_counts = rca_df["L1_DISPOSITION"].value_counts()

plt.figure(figsize=(8, 6))
disposition_counts.plot(kind="bar")

plt.title("SOC L1 Alert Disposition")
plt.xlabel("L1 Disposition")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

output_file = OUTPUT_DIR / "06_alert_disposition.png"
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")


# Detection Performance

performance = {
    "Precision": 92.03,
    "Overall Recall": 6.01
}

plt.figure(figsize=(8, 6))

plt.bar(
    performance.keys(),
    performance.values()
)

plt.title("Detection Engine Performance")
plt.xlabel("Metric")
plt.ylabel("Percentage (%)")
plt.ylim(0, 100)

for index, value in enumerate(performance.values()):
    plt.text(
        index,
        value + 2,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()

output_file = OUTPUT_DIR / "07_detection_performance.png"
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Visualization saved to: {output_file}")


print("\n" + "=" * 60)
print("ALL SOC VISUALIZATIONS COMPLETED")
print("=" * 60)
