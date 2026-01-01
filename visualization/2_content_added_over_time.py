import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../netflix_cleaned_data.xlsx')
df["date_added"] = pd.to_datetime(df["date_added"])
df['year_added'] = df["date_added"].dt.year
yearly_counts = df['year_added'].value_counts().sort_index()

fig = plt.figure(figsize=(10,6))
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linewidth=2)
plt.xlabel("Year", fontweight='bold')
plt.xticks(yearly_counts.index,[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
plt.ylabel("Number of Titles Added", fontweight='bold')
plt.title(
    "Netflix Content Added Over Time (Year-wise)",
    fontsize=16,
    fontweight="bold",
    pad=20
)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
fig.savefig("../photos/2_content_added_over_time.png", dpi=300, bbox_inches="tight")
plt.show()

# ======================================================================
# Using Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('../netflix_cleaned_data.xlsx')
df["date_added"] = pd.to_datetime(df["date_added"])
df['year_added'] = df["date_added"].dt.year
yearly_counts = df['year_added'].value_counts().sort_index()

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(
    x=yearly_counts.index,
    y=yearly_counts.values,
    linewidth=2.5,
    marker="o"
)

plt.xlabel("Year", fontweight='bold')
plt.ylabel("Number of Titles Added", fontweight='bold')
plt.xticks(yearly_counts.index,[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
plt.title(
    "Netflix Content Added Over Time (Year-wise)",
    fontsize=16,
    fontweight="bold",
    pad=20
)
plt.tight_layout()
plt.show()