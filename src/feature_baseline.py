import pandas as pd

FILE_PATH = "data/processed/Friday-16-02-2018_cleaned.csv"

FEATURES = [
    "Flow Pkts/s",
    "Flow Byts/s",
    "Flow Duration",
    "Tot Fwd Pkts",
    "Tot Bwd Pkts",
    "Pkt Len Mean"
]

print("=" * 60)
print("SOC FEATURE BASELINE ANALYSIS")
print("=" * 60)

df = pd.read_csv(FILE_PATH, usecols=FEATURES, low_memory=False)

print(f"\nRecords loaded: {len(df):,}")

print("\n--- FEATURE BASELINE ---")

for feature in FEATURES:

    series = pd.to_numeric(
        df[feature],
        errors="coerce"
    ).dropna()

    print(f"\nFeature: {feature}")

    print(f"  Mean       : {series.mean():,.2f}")
    print(f"  Median     : {series.median():,.2f}")
    print(f"  95th %ile  : {series.quantile(0.95):,.2f}")
    print(f"  99th %ile  : {series.quantile(0.99):,.2f}")
    print(f"  Maximum    : {series.max():,.2f}")

print("\n" + "=" * 60)
print("BASELINE ANALYSIS COMPLETED")
print("=" * 60)
