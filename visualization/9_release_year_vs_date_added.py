import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Ensure date_added is datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract year Netflix added the title
df["year_added"] = df["date_added"].dt.year

# Drop rows where year_added is missing
lag_df = df.dropna(subset=["year_added", "release_year"]).copy()

# Calculate lag
lag_df["lag_years"] = lag_df["year_added"] - lag_df["release_year"]

fig1 = plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=lag_df,
    x="release_year",
    y="lag_years",
    alpha=0.5
)

plt.axhline(0, color="red", linestyle="--", linewidth=1)

plt.xlabel("Release Year", fontweight="bold")
plt.ylabel("Lag (Years until added to Netflix)", fontweight="bold")
plt.title(
    "Release Year vs Netflix Addition Lag",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig1.savefig("../photos/9_release_year_vs_date_added_1.png", dpi=300, bbox_inches="tight")

plt.show()

# =======================================================================
# Using Boxplot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Ensure date_added is datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract year Netflix added the title
df["year_added"] = df["date_added"].dt.year

# Drop rows where year_added is missing
lag_df = df.dropna(subset=["year_added", "release_year"]).copy()

# Calculate lag
lag_df["lag_years"] = lag_df["year_added"] - lag_df["release_year"]

fig2 = plt.figure(figsize=(8, 4))

sns.boxplot(
    x=lag_df["lag_years"]
)

plt.xlabel("Lag (Years)", fontweight="bold")
plt.title(
    "Distribution of Netflix Content Addition Lag",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig2.savefig("../photos/9_release_year_vs_date_added_2.png", dpi=300, bbox_inches="tight")

plt.show()
