import rasterio
import numpy as np

with rasterio.open('data/raw/dem.tif') as src:
    elevation = src.read(1) 
    print("Array Shape :", elevation.shape)
    print("Smallest value: ", elevation.min())
    print("Affected Mean: ", round(float(elevation.mean()), 1))
    
    
    elevation = src.read(1, masked=True)
    print("Smallest real value: ", round(float(elevation.min()), 1))
    print("Largest: ", round(float(elevation.max()), 1))
    print("Mean: ", round(float(elevation.mean()), 1))
    print("Nodata Cells: ", int(elevation.mask.sum()))