import pandas as pd

FILE_PATH = "data/raw/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"

CHUNK_SIZE = 100000

total_rows = 0
total_duplicates = 0
label_counts = {}

print("=" * 60)
print("FULL DATASET SECURITY PROFILE")
print("=" * 60)

for chunk in pd.read_csv(FILE_PATH, chunksize=CHUNK_SIZE):

    total_rows += len(chunk)

    total_duplicates += chunk.duplicated().sum()

    counts = chunk["Label"].value_counts()

    for label, count in counts.items():
        label_counts[label] = label_counts.get(label, 0) + count

print("\nTotal rows processed:", total_rows)

print("\nDuplicate rows detected within chunks:", total_duplicates)

print("\nLabel distribution:")

for label, count in sorted(
    label_counts.items(),
    key=lambda x: x[1],
    reverse=True
):
    percentage = (count / total_rows) * 100

    print(
        f"{label}: {count:,} "
        f"({percentage:.2f}%)"
    )

print("\nProfiling completed.")
