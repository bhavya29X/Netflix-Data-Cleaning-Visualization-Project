import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Split multiple genres into separate rows
genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

# Count top 10 genres
top_genres = genres.value_counts().head(10)

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(top_genres.index, top_genres.values)

# Adds space o right side
plt.margins(x=0.1)

# Put largest genre on top
plt.gca().invert_yaxis()

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 20,
        bar.get_y() + bar.get_height() / 2,
        f"{width}",
        va="center"
    )

# Labels & title
plt.xlabel("Number of Titles", fontweight="bold")
plt.ylabel("Genre", fontweight="bold")
plt.title(
    "Top 10 Most Popular Genres on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
plt.show()

# ======================================================================
# Using Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Split multiple genres into separate rows
genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

# Count top 10 genres
top_genres = genres.value_counts().head(10)

# Order so largest appears on top
order = top_genres.sort_values(ascending=False).index

# Plot
fig = plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    orient="h",
    order=order
)

# Add space on right side (IMPORTANT)
ax.set_xlim(0, top_genres.max() * 1.25)

# Add value labels
offset = top_genres.max() * 0.02
for bar in ax.patches:
    width = bar.get_width()
    ax.text(
        width + offset,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center"
    )

# Labels & title
ax.set_xlabel("Number of Titles", fontweight="bold")
ax.set_ylabel("Genre", fontweight="bold")
ax.set_title(
    "Top 10 Most Popular Genres on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig.savefig("../photos/4_genre_category_popularity.png", dpi=300, bbox_inches="tight")

plt.show()
