import pandas as pd

FILE_PATH = "data/processed/Friday-16-02-2018_cleaned.csv"

print("=" * 60)
print("SECURITY TRAFFIC ANALYSIS")
print("=" * 60)

df = pd.read_csv(FILE_PATH, low_memory=False)

print(f"\nTotal records: {len(df):,}")

print("\n--- LABEL DISTRIBUTION ---")

label_counts = df["Label"].value_counts()

for label, count in label_counts.items():
    percentage = (count / len(df)) * 100
    print(f"{label}: {count:,} ({percentage:.2f}%)")


print("\n--- PROTOCOL DISTRIBUTION ---")

print(df["Protocol"].value_counts())


print("\n--- TOP DESTINATION PORTS ---")

print(df["Dst Port"].value_counts().head(15))


print("\n--- ATTACK TRAFFIC ---")

attack_df = df[df["Label"] != "Benign"]

print(f"Attack records: {len(attack_df):,}")

print("\nAttack types:")
print(attack_df["Label"].value_counts())


print("\n--- BENIGN TRAFFIC ---")

benign_df = df[df["Label"] == "Benign"]

print(f"Benign records: {len(benign_df):,}")


print("\n--- ANALYSIS COMPLETE ---")
