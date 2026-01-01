# Top 10 Directors Members or Prepare Directors data (exclude Unknown)
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Prepare directors data (exclude Unknown)
directors = (
    df[df["director"] != "Unknown"]["director"]
    .dropna()
    .str.split(", ")
    .explode()
)

# Top 10 directors
top_directors = directors.value_counts().head(10)

# Plot
fig1 = plt.figure(figsize=(10, 6))
bars = plt.barh(top_directors.index, top_directors.values)

# Largest on top
plt.gca().invert_yaxis()

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center"
    )

plt.xlabel("Number of Titles", fontweight="bold")
plt.ylabel("Director", fontweight="bold")
plt.title(
    "Top 10 Directors on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig1.savefig("../photos/8_top_directors_and_cast_members_1.png", dpi=300, bbox_inches="tight")

plt.show()

# ======================================================================
# Top 10 Cast Members or Prepare cast data (exclude Unknown)

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")
cast = (
    df[df["cast"] != "Unknown"]["cast"]
    .dropna()
    .str.split(", ")
    .explode()
)

# Top 10 cast members
top_cast = cast.value_counts().head(10)

# Plot
fig2 = plt.figure(figsize=(10, 6))
bars = plt.barh(top_cast.index, top_cast.values)

# Largest on top
plt.gca().invert_yaxis()

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center"
    )

plt.xlabel("Number of Titles", fontweight="bold")
plt.ylabel("Actor / Actress", fontweight="bold")
plt.title(
    "Top 10 Cast Members on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig2.savefig("../photos/8_top_directors_and_cast_members_2.png", dpi=300, bbox_inches="tight")
plt.show()
