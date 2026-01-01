import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Exclude Unknown ratings if present
ratings = df[df["rating"] != "Unknown"]["rating"]

# Count ratings
rating_counts = ratings.value_counts()

# Plot
fig = plt.figure(figsize=(10, 6))
bars = plt.bar(rating_counts.index, rating_counts.values)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom",
    )

plt.xlabel("Rating", fontweight="bold")
plt.ylabel("Number of Titles", fontweight="bold")
plt.title("Netflix Rating Distribution", fontsize=16, fontweight="bold", pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
fig.savefig("../photos/5_rating_distribution_audience_targeting.png", dpi=300, bbox_inches="tight")

plt.show()

# =======================================================================
# Using Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Exclude 'Unknown' ratings
df_ratings = df[df["rating"] != "Unknown"]

plt.figure(figsize=(10, 6))

# Count plot (Seaborn)
ax = sns.countplot(
    data=df_ratings, x="rating", order=df_ratings["rating"].value_counts().index
)

# Add value labels
for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom",
    )

# Labels and title
plt.xlabel("Rating", fontweight="bold")
plt.ylabel("Number of Titles", fontweight="bold")
plt.title("Netflix Rating Distribution", fontsize=16, fontweight="bold", pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
