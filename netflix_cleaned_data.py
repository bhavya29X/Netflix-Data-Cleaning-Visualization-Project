import os
import pandas as pd

data = pd.read_csv("netflix_data.csv")

data = data.drop_duplicates()

data["director"] = data["director"].fillna("Unknown")
data["cast"] = data["cast"].fillna("Unknown")
data["country"] = data["country"].fillna("Unknown")

data = data.dropna(subset=["title", "type"])

data["date_added"] = pd.to_datetime(data["date_added"], errors="coerce")
print(data["date_added"].head())

print(data[data.isnull().any(axis=1)])

mask = data["rating"].str.contains("min|Season", case=False, na=False)
data.loc[mask, "duration"] = data.loc[mask, "rating"]
data.loc[mask, "rating"] = None
rating_mode = data["rating"].mode()[0]
data["rating"] = data["rating"].fillna(rating_mode)

data.loc[data["date_added"].isna(), "release_year"]
data.loc[data["date_added"].isna(), "release_year"].value_counts()
adjusted_year = data["release_year"].where(data["release_year"] >= 2008, 2008)
data["date_added"] = data["date_added"].fillna(
    pd.to_datetime(adjusted_year, format="%Y")
)


print(data.isnull().sum())

if not os.path.exists("netflix_cleaned_data.xlsx"):
    data.to_excel("netflix_cleaned_data.xlsx", index=False)
    print("netflix_cleaned_data.xlsx created successfully")
else:
    print("netflix_cleaned_data.xlsx already exists")


# df = data.sort_values(by="date_added", ascending=True)

# if not os.path.exists("netflix_cleaned_ascending_data.xlsx"):
#     df.to_excel("netflix_cleaned_ascending_data.xlsx", index=False)
#     print("netflix_cleaned_ascending_data.xlsx created successfully")
# else:
#     print("netflix_cleaned_ascending_data.xlsx already exists")

# print(data)
# print(data.isnull().sum())
