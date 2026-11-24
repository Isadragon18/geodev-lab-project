# Week 12: Raster

## What the folder contains
- inspect_raster.py: Get meta data of raster file.
- read_values.py: Masking nodata from raster.
- pixel_coords.py: how to transform raster values to x and y, also back to values.
- sample_points.py: Get the elevation values of point vectors from raster.
- ndvi.py: How to perform vegetation analysis on raster data.
- plot_ndvi.py: How to plot the raster data while also masking nodata.
- clip_raster.py: Clip the raster file to the ward or area of interest.
- zonal_stats.py: calculates the mean elevation covered by each wards.
- reproject_raster.py: Reprojecting Raster to the right grid using rasterio.warp.

## How to run it
From the Repository root:
uv run month-03/week-12/<filename>.py

## What I found
Fun that one line of code can affect all the cells in a raster.
Nodata can aslo affect the analysis or statistics done.

## What went wrong and how I fixed it
Nil.

## My Natural Water Vector Explore
