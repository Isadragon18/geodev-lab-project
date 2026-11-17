import geopandas as gpd

clipped = gpd.read_file("my_data/NaturalWater.gpkg", layer="clipped")

print(gpd.list_layers("my_data/NaturalWater.gpkg"))

print(clipped.head(3))
print("Rows and Columns: ", clipped.shape)
print(clipped.geom_type.value_counts())
print("CRS: ", clipped.crs)
print("Bounds: ", clipped.total_bounds)