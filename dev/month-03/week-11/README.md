# Week 11: CRS and Spatial Operations

## What the folder contains
- area_wrong_and_right.py: Area calculation in EPSG for degree and meter.
- coverage_gap.py: get wards that are not within 2km of any facilities.
- spatial_ops.py: Perform operations based on location such as merge, join, buffer and count.
- set_vs_to.py: shows the different result of to_crs and set_crs methods.
- nearest.py: gets the nearest facilities to the center of each wards.
- one_point.py: how to convert the CRS of a point data.
- clip_dissolve.py: clips roads within the Agodi ward and length.
- fix_geometry.py: checks the validity of a test Polygon and how to fix it.

## How to run it
From the Repository root:
uv run month-03/week-11/<filename>.py

## What I found
How best to reproject layers and each questions a spatial operation answers.
How to perfom vector geoprocessing operations in python.

## What went wrong and how I fixed it
Tried to display my maps using matplot but boundary and water were not on each other.
Reprojected both layers to the same EPSG.

## My Natural Water Vector Explore
