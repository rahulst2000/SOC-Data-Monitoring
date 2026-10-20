import pandas as pd

INPUT_FILE = "data/processed/Friday-16-02-2018_cleaned.csv"

print("=" * 60)
print("SOC DETECTION RULE EVALUATION")
print("=" * 60)

df = pd.read_csv(INPUT_FILE, low_memory=False)

# Convert required fields
df["Flow Pkts/s"] = pd.to_numeric(
    df["Flow Pkts/s"],
    errors="coerce"
)

df["Flow Byts/s"] = pd.to_numeric(
    df["Flow Byts/s"],
    errors="coerce"
)

df["Flow Duration"] = pd.to_numeric(
    df["Flow Duration"],
    errors="coerce"
)

# Ground truth
df["IS_ATTACK"] = (
    df["Label"].astype(str).str.strip() != "Benign"
)

# --------------------------------------------------
# Candidate detection rules
# --------------------------------------------------

rules = {

    "Rule_1_High_Packet_Rate":
        df["Flow Pkts/s"] > 13888.89,

    "Rule_2_High_Byte_Rate":
        df["Flow Byts/s"] > 42970.21,

    "Rule_3_High_Packet_AND_Short_Flow":
        (
            (df["Flow Pkts/s"] > 13888.89)
            &
            (df["Flow Duration"] < 83608)
        ),

    "Rule_4_High_Packet_AND_Byte_Rate":
        (
            (df["Flow Pkts/s"] > 13888.89)
            &
            (df["Flow Byts/s"] > 42970.21)
        ),

    "Rule_5_High_Packet_OR_Byte_Rate":
        (
            (df["Flow Pkts/s"] > 13888.89)
            |
            (df["Flow Byts/s"] > 42970.21)
        )
}

# --------------------------------------------------
# Evaluation function
# --------------------------------------------------

def evaluate_rule(predicted, actual):

    true_positive = (
        predicted & actual
    ).sum()

    false_positive = (
        predicted & ~actual
    ).sum()

    true_negative = (
        ~predicted & ~actual
    ).sum()

    false_negative = (
        ~predicted & actual
    ).sum()

    precision = (
        true_positive /
        (true_positive + false_positive)
        if (true_positive + false_positive) > 0
        else 0
    )

    recall = (
        true_positive /
        (true_positive + false_negative)
        if (true_positive + false_negative) > 0
        else 0
    )

    false_positive_rate = (
        false_positive /
        (false_positive + true_negative)
        if (false_positive + true_negative) > 0
        else 0
    )

    return {
        "TP": true_positive,
        "FP": false_positive,
        "TN": true_negative,
        "FN": false_negative,
        "Precision": precision,
        "Recall": recall,
        "False_Positive_Rate": false_positive_rate
    }


# --------------------------------------------------
# Evaluate rules
# --------------------------------------------------

results = []

for rule_name, prediction in rules.items():

    metrics = evaluate_rule(
        prediction,
        df["IS_ATTACK"]
    )

    metrics["Rule"] = rule_name

    results.append(metrics)


results_df = pd.DataFrame(results)

# Reorder columns
results_df = results_df[
    [
        "Rule",
        "TP",
        "FP",
        "TN",
        "FN",
        "Precision",
        "Recall",
        "False_Positive_Rate"
    ]
]

print("\n--- RULE EVALUATION ---")

print(
    results_df.to_string(index=False)
)

print("\n--- PERCENTAGES ---")

for _, row in results_df.iterrows():

    print(f"\n{row['Rule']}")

    print(
        f"Precision: "
        f"{row['Precision'] * 100:.2f}%"
    )

    print(
        f"Recall: "
        f"{row['Recall'] * 100:.2f}%"
    )

    print(
        f"False Positive Rate: "
        f"{row['False_Positive_Rate'] * 100:.2f}%"
    )

print("\n" + "=" * 60)
print("DETECTION EVALUATION COMPLETED")
print("=" * 60)
