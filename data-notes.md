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
