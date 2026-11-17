# Week 10: Geopandas, layers as tables

## What the folder contains
- explore_pandas.py: Various Pandas attribute and describe() method of csv file.
- filter_sort.py: Perform a simple filter based on population > 35000 in a csv file.
- explore_layer.py: Get some attributes of a particular column in a gpkg file.
- geom_props.py: carrying a method on the first record / row of a gpkg file.
- csv_to_points.py: create a gpkg file from a csv file along with a geometry table.
- join_population.py: Joins the population and ward using normal join and a cleaned data before joining.
- make_map.py: creates a png file of the map with th wards as polygon and facilities as point data.
- save_outputs.py: creates and saves two files a gpkg and csv file.

## How to run it
From the Repository root:
uv run month-03/week-10/<filename>.py

## What I found
The outputs showed how traditional workflow of a single project, can be automated for several projects.
The way to plot maps and vectors using matplotlib.

## What went wrong and how I fixed it
Ran the code outside the root file in my terminal, fixed by "cd" into the root folder.

## My Natural Water Vector Explore
QGIS bounds: min - 3.0234, 6.4 & max - 3.2314, 6.5057
Bounds:  min - 3.02204885, 6.3997411 & max - 3.2300363, 6.5052137
Has almost similar bounds.