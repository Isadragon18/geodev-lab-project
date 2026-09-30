# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Yusuf Isaiah Ifeanyichukwu

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** EPSG:32631 WGS 84 UTM Zone 31N

**Why this one:** My project work will be dealing with distance, and my study area is focused on the western part of Nigeria. 
The best Zone for these conditions is UTM 31N.

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| LGA Boundary | EPSG:4326 | EPSG:32631 | Reprojected |
| Rivers | EPSG:32631 | EPSG:32631 | No change needed |
| Waterbody | EPSG:32631 | EPSG:32631 | No change needed |
| Settlement | EPSG:4326 | EPSG:32631 | Reprojected |

> Reprojecting recalculates every coordinate. Assigning a CRS only
> relabels the data. Say which one you did.

## 2. Clipping to the study area

- **Boundary used:** C:/Users/isaiah.yusuf/Desktop/GeoDev_GIS/my-project/data/processed/study_area.gpkg
- **Features before clipping:** 202146
- **Features after clipping:** 3109

Some features of the Settlements seem to be pointing to bare ground on the OSM basemap, 
left them due to my confidence in the source.

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | yes | reprojected all layers and project to on common CRS |
| Are there nulls in the fields I need? | yes in the river and waterbody layers | currently working on getting the values |
| Are there duplicate features? | no | all features point to one object in space and time |
| Is the geometry valid? | yes | nothing |
| Does coverage span the whole study area? | yes | nothing |

## 4. Problems found, and what I did

**<Problem.>** <What it was, and whether you fixed it or flagged it.
Flagging honestly is acceptable. Hiding it is not.>

## 5. The analysis-ready output

- **File:** `data/processed/Clipped_settle.gpkg`
- **Format:** GeoPackage
- **CRS:** EPSG:32631 WGS 84 UTM Zone 31N
- **Features:** 3109
- **Produced by:** Vector Clip analysis within study area boundary

## OSM rivers, OJO LGA
- 6 features
- Extracted: 09/13/2026 via QuickOSM, waterway='river'
- COMPLETENESS: good correlation with OpenStreetMap, no missing sector with all rivers represented.
- CURRENCY: was querried from the QuickOSM on QGIS.
- POSITIONAL: all riverss are aligned well with the satellite imagery, no systematic offset
- ATTRIBUTE: all 6 has values for the type of water i.e. river, only 1 has a name i.e. river owo
- FITNESS: adequate for analysis in both built-up and non built-up areas

## OSM waterbody, OJO LGA
- 6 features
- Extracted: 09/13/2026 via QuickOSM, natural='river'
- COMPLETENESS: good correlation with OpenStreetMap, no missing sector with all water bodies represented.
- CURRENCY: was querried from the QuickOSM on QGIS.
- POSITIONAL: all waterbodies are aligned well with the satellite imagery, no systematic offset
- ATTRIBUTE: only 3 out of the 6 has values for the type of water i.e. river or Lagoon, only 2 have names
- FITNESS: adequate for analysis in both built-up and non built-up areas

## CRS and preparation
- All sources: Layers arrived in EPSG: 4326 (WSG84)
- Study Area: Ojo LGA, extracted from GRID3 wards and reprojected to EPSG:32631 (UTM 31N) projected CRS for Western States of Nigeria
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N) projected CRS for Western States of Nigeria
- Area Check: Ojo LGA 172.5 km2, while publised figure is 182 km2 from Wikipedia
- Working file in data/processed/ , raw files untouched 

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
