# Task-01: Save Histogram and Bar Chart as PNG

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
df = pd.read_csv(file_path, skiprows=4)

# Remove empty columns
df = df.dropna(axis=1, how='all')

# Select latest available year column
year_col = df.columns[-1]

# Convert values to numeric
df[year_col] = pd.to_numeric(df[year_col], errors='coerce')

# Remove missing values
population_data = df[year_col].dropna()

# ---- HISTOGRAM ----
plt.figure(figsize=(8,5))
plt.hist(population_data, bins=20)
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.title(f"Population Distribution ({year_col})")

# Save histogram as PNG
plt.savefig("histogram.png")
plt.close()

# ---- BAR CHART ----
top10 = df[['Country Name', year_col]].dropna().sort_values(
    by=year_col, ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.bar(top10['Country Name'], top10[year_col])
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Population")
plt.title(f"Top 10 Countries by Population ({year_col})")

# Save bar chart as PNG
plt.savefig("barchart.png")
plt.close()

print("Graphs saved successfully!")