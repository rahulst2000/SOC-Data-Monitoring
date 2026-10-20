import pandas as pd

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"

print("=" * 60)
print("SOC DETECTION RULE TUNING ANALYSIS")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

# Convert selected features
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

# Compare benign and attack traffic
benign = df[df["Label"] == "Benign"]
attack = df[df["Label"] != "Benign"]

print(f"\nBenign records : {len(benign):,}")
print(f"Attack records : {len(attack):,}")

print("\n--- BENIGN BASELINE ---")

for feature in features:

    print(f"\n{feature}")

    print(
        f"  Median : {benign[feature].median():,.2f}"
    )

    print(
        f"  95th %ile : "
        f"{benign[feature].quantile(0.95):,.2f}"
    )

    print(
        f"  99th %ile : "
        f"{benign[feature].quantile(0.99):,.2f}"
    )

print("\n--- ATTACK TRAFFIC ---")

for feature in features:

    print(f"\n{feature}")

    print(
        f"  Median : {attack[feature].median():,.2f}"
    )

    print(
        f"  95th %ile : "
        f"{attack[feature].quantile(0.95):,.2f}"
    )

    print(
        f"  99th %ile : "
        f"{attack[feature].quantile(0.99):,.2f}"
    )

print("\n--- ATTACK TYPES ---")

print(
    attack["Label"].value_counts()
)

print("\n" + "=" * 60)
print("TUNING ANALYSIS COMPLETED")
print("=" * 60)
