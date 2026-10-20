import pandas as pd

INPUT_FILE = "reports/detection_engine_v2.csv"

print("=" * 60)
print("SOC DETECTION ENGINE V2 - EVALUATION")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

# Ground truth is used ONLY for offline evaluation.
df["IS_ATTACK"] = (
    df["Label"].astype(str).str.strip() != "Benign"
)

predicted = pd.Series(True, index=df.index)
actual = df["IS_ATTACK"]

tp = (predicted & actual).sum()
fp = (predicted & ~actual).sum()

print(f"\nSuspicious records evaluated: {len(df):,}")

print("\n--- GROUND TRUTH ---")
print(f"Actual attacks      : {actual.sum():,}")
print(f"Actual benign       : {(~actual).sum():,}")

print("\n--- V2 RESULTS ---")
print(f"True Positives      : {tp:,}")
print(f"False Positives     : {fp:,}")

precision = (
    tp / (tp + fp)
    if (tp + fp) > 0
    else 0
)

print(f"\nPrecision           : {precision * 100:.2f}%")

print("\n--- ALERT LABEL DISTRIBUTION ---")
print(
    df["Label"]
    .value_counts()
)

print("\n--- ALERT DETECTION TYPES ---")
print(
    df["DETECTION_TYPE"]
    .value_counts()
)

print("\n" + "=" * 60)
print("V2 EVALUATION COMPLETED")
print("=" * 60)
