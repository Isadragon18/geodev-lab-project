# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Yusuf Isaiah Ifeanyichukwu

What I downloaded, where it came from, what is in it, and what is wrong
with it.

---

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | Nigeria Operational Wards | Vector | 09/13/2026 | OK |
| 2 | rivers | Vector | 09/13/2026 | OK |
| 3 | waterbody | Vector | 09/13/2026 | OK |
| 4 | Settlement | Vector | 09/28/2026 | OK |

---

## 1. Nigeria Operational Wards

- **Source:** https://data.grid3.org
- **Retrieved:** 09/13/2026
- **File:** `data/raw/NGA_LGA_Boundaries_2_2609687066015738692`
- **Format:** shapefile
- **Geometry type:** Polygon (Multipolygon)
- **Feature count:** 774 features
- **CRS as downloaded:** EPSG:4326 - WGS 84

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `globalid` | holds the IDs of each LGA on a global scale | 0 |
| `uniq_id` | unique id to identify each LGA | 0 |
| `timestamp` | last update of the LGA | 0 |
| `editor` | Who last update the LGA | 0 |
| `lganame` | The LGA name given by the Country | 0 |
| `lgacode` | The unique identifier assigned by the country | 0 |
| `statename` | The state that houses the LGA | 0 |
| `statecode` | two letters to identifier the state | 0 |
| `source` | the source of the LGA information | 0 |
| `amapcode` |  | 10 |

**What I noticed**

I noticed that the boundary outline doesn't match the outlines as shown on my base map from OpenStreetMap. 
Also, the amapcode field was not defined in the metadata (uses) and has null values for 10 features.

---

## 2. rivers

- **Source:** Query: waterway='river' within Ojo LGA extent
- **Retrieved:** 09/13/2026
- **File:** `data/processed/River.gpkg`
- **Format:** Geopackage
- **Geometry type:** Line (MultiLineString)
- **Feature count:** 9, but only 6 are used.
- **CRS as downloaded:** EPSG:32631 - WGS 84 / UTM zone 31N

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `fid` | Feature ID for of each feature in the layer | 0 |
| `full_id` | combination of the osm_type and osm_id | 0 |
| `osm_id` | The id of each feature on OSM | 0 |
| `osm_type` | The OSM type of each feature | 0 |
| `waterway` | The type of waterway, i.e., query parameter (river) | 0 |
| `name` | The local name of the river | 5 |

**What I noticed**

I noticed that the 3 rivers were tied to places that are water bodies. 
Not all features have their local names, except for one: River Owo.

---

## 3. waterbody

- **Source:** Query: natural='river' within Ojo LGA extent
- **Retrieved:** 09/13/2026
- **File:** `data/processed/NaturalWater.gpkg`
- **Format:** Geopackage
- **Geometry type:** Polygon (Multipolygon)
- **Feature count:** 7, but only 6 features are used
- **CRS as downloaded:** EPSG:32631 - WGS 84 / UTM zone 31N

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `fid` | Feature ID for each feature in the layer | 0 |
| `full_id` | combination of the osm_type and osm_id | 0 |
| `osm_id` | The id of each feature on OSM | 0 |
| `osm_type` | The OSM type of each feature | 0 |
| `natural` | The type of natural water, i.e., query parameter (water) | 0 |
| `place` | The location of water | 6 |
| `landuse` | Land usage | 6 |
| `alt_name` | Alternative name | 6 |
| `wikidata` | link to the open Wikidata database | 5 |
| `wetland` |  | 6 |
| `water` | The type of water (river or lagoon) | 4 |
| `type` | Vector type | 5 |
| `name` | Local name of the water body | 4 |

**What I noticed**

I noticed that many fields have null values, meaning the information wasn't recorded or obtained. 
Also, the water bodies covered all areas of my study area.

---

## 4. Settlement

- **Source:** https://data.grid3.org
- **Retrieved:** 07/22/2026
- **File:** `data/raw/GRID3_NGA_settlement_extents_v4_1_7127322163395981696`
- **Format:** shapefile
- **Geometry type:** Polygon (Multipolygon)
- **Feature count:** 3109 features
- **CRS as downloaded:** EPSG:4326 - WGS 84

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `fid` | Feature ID for each feature in the layer | 0 |
| `block_id` | combination of the osm_type and osm_id | 0 |
| `country` | The id of each feature on OSM | 0 |
| `iso3` | The OSM type of each feature | 0 |
| `block_area` | The type of natural water, i.e., query parameter (water) | 0 |
| `block_peri` | The location of water | 6 |
| `block_neig` | Land usage | 6 |
| `building_c` | Alternative name | 6 |
| `building_a` | link to the open Wikidata database | 5 |
| `building_1` |  | 6 |
| `building_2` | The type of water (river or lagoon) | 4 |
| `building_3` | Vector type | 5 |
| `building_4` | Local name of the water body | 4 |
| `building_5` | Land usage | 6 |
| `extent_typ` | Alternative name | 6 |
| `mgrs_code` | link to the open Wikidata database | 5 |
| `ndvi_mean` |  | 6 |
| `evi_mean` | The type of water (river or lagoon) | 4 |
| `gbuilding_` | Vector type | 5 |
| `gbuilding1` | Local name of the water body | 4 |
| `blocks_per` | Alternative name | 6 |
| `building_6` | link to the open Wikidata database | 5 |
| `building_m` |  | 6 |
| `building_7` | The type of water (river or lagoon) | 4 |
| `bd_class` | Vector type | 5 |
| `composite_` | Local name of the water body | 4 |

**What I noticed**

I noticed that many fields have null values, meaning the information wasn't recorded or obtained. 
Also, the water bodies covered all areas of my study area.

---

## Cross-cutting problems

**<Problem one.>** <For example: everything is at a different resolution
and nothing can be combined until Week 3.>

**<Problem two.>** <For example: LGA names differ between two sources and
the join will fail.>

---

**Status:** Week 2 complete. Reprojection and quality checks in Week 3,
see [03-data-preparation.md](03-data-preparation.md).



