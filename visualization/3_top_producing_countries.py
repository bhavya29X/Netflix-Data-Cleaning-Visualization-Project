import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../netflix_cleaned_data.xlsx')
top_countries = (
    df[df["country"] != "Unknown"]["country"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig = plt.figure(figsize=(10, 6))
bars = plt.barh(top_countries.index, top_countries.values)

plt.margins(x=0.1)        # 👈 adds space on right side
# plt.xlim(0, top_countries.max() * 1.25)
plt.gca().invert_yaxis()   # 👈 makes largest on top

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 30,                     # slight offset to the right
        bar.get_y() + bar.get_height() / 2,
        f"{width}",
        va="center"
    )
    
plt.xlabel("Number of Titles", fontweight='bold')
plt.ylabel("Country", fontweight='bold')
plt.title(
    "Top 10 Producing Countries on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()
fig.savefig("../photos/3_top_producing_countries.png", dpi=300, bbox_inches="tight")

plt.show()

# =======================================================================
# Using Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("../netflix_cleaned_data.xlsx")

# Split multiple countries into separate rows
countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

# Count top 10 countries
top_countries = countries.value_counts().head(10)

order = top_countries.sort_values(ascending=True).index

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    orient="h",
    order=order
)

ax.set_xlim(0, top_countries.max() * 1.1) # key line

# Labels and title
plt.xlabel("Number of Titles", fontweight='bold')
plt.ylabel("Country", fontweight='bold')
plt.title(
    "Top 10 Producing Countries on Netflix",
    fontsize=16,
    fontweight="bold",
    pad=20
)

# Add value labels
for bar in ax.patches:
    width = bar.get_width()
    plt.text(
        width + 30,                          # offset to the right
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center"
    )

plt.tight_layout()
plt.show()

