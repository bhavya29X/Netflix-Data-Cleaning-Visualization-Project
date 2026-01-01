import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load raw and cleaned data
raw_df = pd.read_csv("../netflix_data.csv")
clean_df = pd.read_excel("../netflix_cleaned_data.xlsx")

missing_before = raw_df.isnull().sum()
missing_after = clean_df.isnull().sum()

# Combine into one DataFrame
missing_df = pd.DataFrame({
    "Before Cleaning": missing_before,
    "After Cleaning": missing_after
})

# Keep only columns that had missing values
# missing_df = missing_df[(missing_df["Before Cleaning"] > 0) | (missing_df["After Cleaning"] > 0)]

x = np.arange(len(missing_df.index))   # column positions
width = 0.35

fig = plt.figure(figsize=(12, 6))

bars_before = plt.bar(
    x - width/2,
    missing_df["Before Cleaning"],
    width=0.5,
    label="Before Cleaning"
)

bars_after = plt.bar(
    x + width/2,
    missing_df["After Cleaning"],
    width=0.5,
    label="After Cleaning"
)

for bars in [bars_before, bars_after]:
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom"
        )

plt.xlabel("Columns", fontweight="bold")
plt.ylabel("Number of Missing Values", fontweight="bold")
plt.title(
    "Missing Data Audit: Before vs After Cleaning",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xticks(x, missing_df.index, rotation=45, ha="right")
plt.legend(title="Dataset State", loc="upper left",
    bbox_to_anchor=(1.01, 1))

plt.tight_layout()
fig.savefig("../photos/10_missing_data_audit_before_vs_after_cleaning.png", dpi=300, bbox_inches="tight")

plt.show()
