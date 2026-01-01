import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("../netflix_cleaned_data.xlsx")
type_counts = data['type'].value_counts()
print(type_counts)
fig = plt.figure(figsize=(8, 6))
colors = ['#E50914', '#F16D34']
bars = plt.bar(type_counts.index, type_counts.values, color=colors)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", ha="center", va="bottom")

plt.xlabel("Content Type", fontweight='bold')
plt.ylabel("Number of Titles", fontweight='bold')
plt.title("Netflix Content Type Distribution (Movies vs TV Shows)", pad=20, fontsize=16, fontweight="bold")
plt.legend(
    bars,
    type_counts.index,
    title="Content Type",
    loc="upper left",
    bbox_to_anchor=(1.03, 1)   # 👈 pushes legend outside
)

plt.tight_layout()
fig.savefig("../photos/1_content_type_distribution_1.png", dpi=300, bbox_inches="tight")
plt.show()

# =======================================================================
# Using seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("../netflix_cleaned_data.xlsx")
type_counts = data['type'].value_counts()
plt.figure(figsize=(8, 6))
bars = sns.barplot(x = type_counts.index, y = type_counts.values, hue= type_counts.index, palette='Set2',legend=True)

for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", ha="center", va="bottom")

plt.xlabel("Content Type", fontweight='bold')
plt.ylabel("Number of Titles", fontweight='bold')
plt.title("Netflix Content Type Distribution (Movies vs TV Shows)", pad=20, fontsize=16, fontweight="bold")
plt.legend(
    title="Content Type",
    loc="upper left",
    bbox_to_anchor=(1.03, 1)
)
plt.tight_layout()
plt.show()

# =======================================================================
# Using Pie Chart

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("../netflix_cleaned_data.xlsx")
type_counts = data["type"].value_counts()
explode = [0.1, 0]
colors = ['#E50914', '#1F2937']   # Netflix Red + Slate Gray
fig = plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(type_counts.values, labels=type_counts.index, colors=colors, explode=explode, autopct="%1.1f%%", startangle=65, shadow=True, textprops={"fontsize": 14}, wedgeprops={"edgecolor": "white", "linewidth": 1},)
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
plt.title("Netflix Content Type Distribution (Movies vs TV Shows)", pad=20, fontsize=16, fontweight="bold")
fig.savefig("../photos/1_content_type_distribution_2.png", dpi=300,bbox_inches="tight")
plt.show()