import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


# table = pd.read_csv("data/raw/health_facilities.csv")
# print(table.head(3))
# print(table["type"].value_counts())

# def clean_type(name):
#     if name == "Primary Health Centre":
#         return "PHC"
#     return name

# # table["re_type"] = table["type"].apply(lambda x: clean_type(x, "PHC") if x == "Primary Health Centre" else x)
# table["re_type"] = table["type"].apply(clean_type)
# print(table["re_type"].value_counts())

# facilities = gpd.GeoDataFrame(
#     table,
#     geometry = gpd.points_from_xy(table["longitude"], table["latitude"]),
#     crs="EPSG:4326"
# )

# print(facilities.head(3))
# print(facilities.crs)


# facilities.to_file("data/processed/my_facilities.gpkg", layer="facilities")
# print("Saved ", len(facilities), " facilities")

wards = gpd.read_file("my_data/study_area.gpkg")
natural = gpd.read_file("my_data/naturalwater_reprojected.gpkg")
settle0 = gpd.read_file("my_data/half_settle.gpkg")
settle0 = settle0.to_crs(wards.crs)
settle1 = gpd.read_file("my_data/one_settle.gpkg")
settle1 = settle1.to_crs(wards.crs)
settle2 = gpd.read_file("my_data/two_settle.gpkg")
settle2 = settle2.to_crs(wards.crs)

buf = natural.buffer(10000)

fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
natural.plot(ax=ax, color="#094923")
buf.plot(ax=ax, color="#FFE4B5", alpha=0.5)
settle2.plot(ax=ax, color="#F44308")
settle1.plot(ax=ax, color="#CFF027")
settle0.plot(ax=ax, color="#179BEC")
ax.set_title("My Study Area")
ax.set_axis_off()

fig.savefig("data/processed/my_map.png", dpi=150, bbox_inches="tight")
print("Saved map to data/processed/my_map.png")
print(settle0.crs)
print(natural.crs)
print(wards.crs)
print(settle1.crs)
print(settle2.crs)
