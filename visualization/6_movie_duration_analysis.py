import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Filter only movies
movies = df[df["type"] == "Movie"].copy()

# Extract numeric duration (minutes)
movies["duration_min"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)

fig1 = plt.figure(figsize=(10, 6))

plt.hist(
    movies["duration_min"],
    bins=30,
    density=True,
    edgecolor="black",
    alpha=0.9,
    histtype="bar",
    label="Movies duration",
    # cumulative=True
)
plt.axvline(np.mean(movies['duration_min']), color='black', linestyle='--', linewidth=2, label = 'Average duration')


plt.xlabel("Movie Duration (minutes)", fontweight="bold")
plt.ylabel("Number of Movies", fontweight="bold")
plt.title(
    "Distribution of Movie Durations on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)
plt.legend()
plt.legend(
    loc="upper left",
    bbox_to_anchor=(1.01, 1)   # 👈 pushes legend outside
)

plt.tight_layout()
fig1.savefig("../photos/6_movie_duration_analysis_1.png", dpi=300, bbox_inches="tight")
plt.show()

# how bins work
# bins = 30
# (movies["duration_min"].max() - movies["duration_min"].min()) / bins  #10.3

# ======================================================================
# Using Seaborn (histplot)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Filter only movies
movies = df[df["type"] == "Movie"].copy()

# Extract numeric duration (minutes)
movies["duration_min"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)

fig2 = plt.figure(figsize=(10, 6))

sns.histplot(
    movies["duration_min"],
    bins=30,
    kde=True,
    label="Movies duration"
)
plt.axvline(np.mean(movies['duration_min']), color='red', linestyle='--', linewidth=2, label = 'Average duration')


plt.xlabel("Movie Duration (minutes)", fontweight="bold")
plt.ylabel("Number of Movies", fontweight="bold")
plt.title(
    "Distribution of Movie Durations on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)
plt.legend(
    loc="upper left",
    bbox_to_anchor=(1.01, 1)   # 👈 pushes legend outside
)

plt.tight_layout()
fig2.savefig("../photos/6_movie_duration_analysis_2.png", dpi=300, bbox_inches="tight")

plt.show()

# ======================================================================
# Using Seaborn (boxplot)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Filter only movies
movies = df[df["type"] == "Movie"].copy()

# Extract numeric duration (minutes)
movies["duration_min"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)

fig3= plt.figure(figsize=(8, 4))

sns.boxplot(
    x=movies["duration_min"],  # horizontal
    # y=movies["duration_min"]  # vertical
    label="Movie Duration (minutes)"
)
# sns.boxplot(
#     data=movies,
#     x="rating",
#     y="duration_min",
#     # showfliers=True,
#     # palette="Set2",
#     # width=0.4
# )
plt.xlabel("Movie Duration (minutes)", fontweight="bold")
plt.title(
    "Movie Duration Spread on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)
# plt.legend(loc="upper left",bbox_to_anchor=(1.01, 1))
plt.tight_layout()
fig3.savefig("../photos/6_movie_duration_analysis_3.png", dpi=300, bbox_inches="tight")

plt.show()
