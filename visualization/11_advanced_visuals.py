import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("../netflix_cleaned_data.xlsx")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

# 1️⃣ HEATMAP — Year vs Content Type Count
# Create pivot table
year_type_pivot = pd.pivot_table(
    df, index="year_added", columns="type", values="title", aggfunc="count"
)

fig1 = plt.figure(figsize=(10, 6))
sns.heatmap(year_type_pivot, cmap="Reds", annot=True, fmt=".0f")

plt.title(
    "Netflix Content Added Over Time by Type", fontsize=16, fontweight="bold", pad=20
)

plt.xlabel("Content Type", fontweight="bold")
plt.ylabel("Year Added", fontweight="bold")

plt.tight_layout()
fig1.savefig("../photos/11_advanced_1.png", dpi=300, bbox_inches="tight")
plt.show()

# 2️⃣ HEATMAP — Country vs Content Type
# Prepare country data
country_df = (
    df[df["country"] != "Unknown"]
    .assign(country=df["country"].str.split(", "))
    .explode("country")
)

country_type_pivot = (
    pd.pivot_table(
        country_df, index="country", columns="type", values="title", aggfunc="count"
    )
    .sort_values(by="Movie", ascending=False)
    .head(10)
)

fig2 = plt.figure(figsize=(10, 6))
sns.heatmap(country_type_pivot, cmap="Blues", annot=True, fmt=".0f")

plt.title(
    "Top Producing Countries by Content Type", fontsize=16, fontweight="bold", pad=20
)

plt.xlabel("Content Type", fontweight="bold")
plt.ylabel("Country", fontweight="bold")

plt.tight_layout()
fig2.savefig("../photos/11_advanced_2.png", dpi=300, bbox_inches="tight")
plt.show()
