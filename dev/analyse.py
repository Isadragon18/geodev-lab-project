with open("wards.csv") as f:
    lines = f.readlines()
    
total = 0

def classify(area_km2):
    if area_km2 > 9:
        return "Large"
    else:
        return "Small"
    
for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100
    size = classify(area_km2)
    print(f"Ward: {ward}, Area: {area_km2:.2f} km², Hectares: {area_hectares:.2f} hectares. It is {size}.")
    total += area_km2

print(f"Total area: {total:.2f} km²")
