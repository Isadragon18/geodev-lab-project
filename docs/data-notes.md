# Data notes
## GRID3 Nigeria Operational Wards v3.0
- Source: https://data.grid3.org
- Downloaded: 09/13/2026
- 774 features, polygons
- Columns: globalid (String), uniq_id (Integer64), timestamp (Date), editor (String), lganame (String), lgacode (String), statename (String), statecode (String), source (String), amapcode (String).
- No nulls in lganame
- Covers my LGS fully

## OSM rivers, extracted via QuickOSM
- Query: waterway='river' within Ojo LGA extent
- Extracted: 09/13/2026
- 11 features, lines
- Only one had a value in the name column, remaining were null.
- Coverage is good for most parts but not all river are covered in the area.

## OSM waterbody, extracted via QuickOSM
- Query: natural='river' within Ojo LGA extent
- Extracted: 09/13/2026
- 6 features, polygon
- Most columns have null values with only two features has names.
- Coverage is good for most parts but some features also cover area of other features.

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
