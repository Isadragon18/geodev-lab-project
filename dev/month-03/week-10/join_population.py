import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("data/raw/ward_population.csv")


first_try = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
matched = first_try["population_2024"].notna().sum()
print("Matched on first try ", matched, " of ", len(wards), " wards")


def clean_name(name):
    return name.lower().replace(" ", "").replace("-", "")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on = "join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched after Cleaning: ", matched, " of ", len(wards), " wards")
print(joined[["ward_name", "population_2024"]])

fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
joined.plot(column="population_2024", legend=True, cmap="Greens")
# ax.set_title("My Study Area")
ax.set_axis_off()

fig.savefig("data/processed/population_map.png", dpi=150, bbox_inches="tight")
print("Saved map to data/processed/population_map.png")