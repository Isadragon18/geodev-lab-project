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

# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: <your name>

What I downloaded, where it came from, what is in it, and what is wrong
with it.

---

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | <name> | Vector | <date> | OK |
| 2 | <name> | Raster | <date> | OK |
| 3 | <name> | Vector | <date> | Partial |

---

## 1. <Dataset name>

- **Source:** <https://...>
- **Retrieved:** <date>
- **File:** `data/raw/<filename>`
- **Format:** <GeoPackage / GeoTIFF / CSV>
- **Geometry type:** <Point / Line / Polygon / n/a>
- **Feature count:** <number>
- **CRS as downloaded:** <EPSG:XXXX>

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `<column>` | <description> | <count> |
| `<column>` | <description> | <count> |

**What I noticed**

<Gaps, duplicates, odd values, name spellings that differ from your other
datasets. This section is where the marks are. Do not leave it empty.>

---

## 2. <Dataset name>

<Repeat the block above for each dataset.>

---

## Cross-cutting problems

**<Problem one.>** <For example: everything is at a different resolution
and nothing can be combined until Week 3.>

**<Problem two.>** <For example: LGA names differ between two sources and
the join will fail.>

---

**Status:** Week 2 complete. Reprojection and quality checks in Week 3,
see [03-data-preparation.md](03-data-preparation.md).



