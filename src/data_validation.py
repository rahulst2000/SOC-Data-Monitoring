import pandas as pd

FILE_PATH = "data/raw/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"

print("=" * 60)
print("CSE-CIC-IDS2018 DATASET VALIDATION")
print("=" * 60)

df = pd.read_csv(FILE_PATH, nrows=10000)

print(f"\nRows loaded: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nLabels:")
print(df["Label"].value_counts())

print("\nDataset validation completed.")
