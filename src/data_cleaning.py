import pandas as pd

INPUT_FILE = "data/raw/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"
OUTPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"

print("=" * 60)
print("CSE-CIC-IDS2018 DATA CLEANING")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

original_rows = len(df)

print(f"\nOriginal rows: {original_rows:,}")

# Remove repeated header rows
header_rows = df["Label"].astype(str).str.strip().eq("Label").sum()

df = df[~df["Label"].astype(str).str.strip().eq("Label")].copy()

print(f"Repeated header rows removed: {header_rows:,}")

# Remove exact duplicate records
duplicate_count = df.duplicated().sum()

df = df.drop_duplicates().copy()

print(f"Exact duplicate rows removed: {duplicate_count:,}")

# Normalize labels
df["Label"] = df["Label"].astype(str).str.strip()

# Convert timestamp
df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    format="%d/%m/%Y %H:%M:%S",
    errors="coerce"
)

invalid_timestamps = df["Timestamp"].isna().sum()

print(f"Invalid timestamps: {invalid_timestamps:,}")

# Remove records with invalid timestamps
df = df.dropna(subset=["Timestamp"]).copy()

# Reset index
df.reset_index(drop=True, inplace=True)

print(f"\nFinal rows: {len(df):,}")

print("\nFinal label distribution:")
print(df["Label"].value_counts())

print("\nSaving cleaned dataset...")

df.to_csv(OUTPUT_FILE, index=False)

print(f"\nSaved to: {OUTPUT_FILE}")
print("\nCleaning completed successfully.")
