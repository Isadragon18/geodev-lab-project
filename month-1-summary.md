# Month 1 Summary

## Question
Areas prone to flood in Lagos State, Ojo LGA case study.

## Operations
Buffered the clip Water Bodies within the Ojo LGA, of 0.5, 1 and 2 km extent.
Used the buffer to clip settlement / bulit-up areas within the Ojo LGA.
This was done using the principle that areas further away from the waterbodies are of higher elevation than those closer.

## Expected
A radius color change based on distance from waterbodies.

## Got
0.5km(23% settlements), 1km(15% settlements), 2km(26% settlement) and > 2km(36% settlements).
Note only in the northern parts we have settlements > 2km away from waterbodies.

## What surprised me
Nothing changed, confirmed with the basemap on Openstreetmap.

## Limits
- I didn't consider the Ocean at the boundary of the study area, which is why most settlements in southern part appear much further than expected.
- Also River channel wasn't taken into consideration, due to the low impact on flooding.
- Driange network wasn't available for Nigeria and was not used.
- Also LU/LC analysis was not integrated.

## What i still need
- DEM data for OJO LGA.
- LU/LC analysis for the study area.
- Population per settlement areas.
- Analysis to suggest best possible drainage paths for flood prone areas.
