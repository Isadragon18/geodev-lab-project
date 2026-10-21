import csv


def inspect_column(file_path, column):
    with open(file_path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    
    values = []
    non = []
    for row in rows:
        try:
            raw = row[column].strip()
            if raw == "":
                continue
            
            values.append(float(raw))
        except ValueError:
            non.append(raw)
    
    average = sum(values) / len(values) if values else 0
    
    return {
        "smallest": min(values) if values else "No Data",
        "largest": max(values) if values else "No Data",
        "counts": len(values),
        "average": average if average else "No Data",
        "non-numeric": len(non)
    }

poverty_rate = inspect_column('poverty_states.csv', 'Pvrty_rate')
poverty_rank = inspect_column('poverty_states.csv', 'Povrty_Rnk')
state = inspect_column('poverty_states.csv', 'State')
print("Poverty Rate:", poverty_rate)
print("Poverty Rank:", poverty_rank)
print("State:", state)