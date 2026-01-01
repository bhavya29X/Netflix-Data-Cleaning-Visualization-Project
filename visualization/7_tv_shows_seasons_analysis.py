import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Filter only TV Shows
tv_shows = df[df["type"] == "TV Show"].copy()

# Extract number of seasons
tv_shows["num_seasons"] = (
    tv_shows["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)
season_counts = tv_shows["num_seasons"].value_counts().sort_index()

fig1 = plt.figure(figsize=(10, 6))
bars = plt.bar(season_counts.index, season_counts.values)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.xlabel("Number of Seasons", fontweight="bold")
plt.xticks(season_counts.index, [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17])
plt.ylabel("Number of TV Shows", fontweight="bold")
plt.title(
    "Distribution of TV Shows by Number of Seasons on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig1.savefig("../photos/7_tv_shows_season_analysis_1.png", dpi=300, bbox_inches="tight")
plt.show()

# ======================================================================
# Using Seaborn (histoplot)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Filter only TV Shows
tv_shows = df[df["type"] == "TV Show"].copy()

# Extract number of seasons
tv_shows["num_seasons"] = (
    tv_shows["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)
season_counts = tv_shows["num_seasons"].value_counts().sort_index()
fig2 = plt.figure(figsize=(10, 6))

ax = sns.histplot(
    tv_shows["num_seasons"],
    bins=15,
    discrete=True,
    # kde=True
)

for bar in ax.patches:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.xlabel("Number of Seasons", fontweight="bold")
plt.xticks(season_counts.index, [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17])
plt.ylabel("Number of TV Shows", fontweight="bold")
plt.title(
    "TV Show Seasons Distribution on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig2.savefig("../photos/7_tv_shows_season_analysis_2.png", dpi=300, bbox_inches="tight")

plt.show()

# (tv_shows["num_seasons"].max() - tv_shows["num_seasons"].min()) / 15
