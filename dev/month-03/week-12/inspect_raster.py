import rasterio

with rasterio.open('data/raw/dem.tif') as src:
    print("Width x Height: ", src.width, " x ", src.height)
    print("Band(s): ", src.count)
    print("Data Type: ", src.dtypes)
    print("Pixel Size: ", src.res)
    print("CRS: ", src.crs)
    print("Bounds: ", src.bounds)
    print("Nodata: ", src.nodata)
    print("Transform")
    print(src.transform)