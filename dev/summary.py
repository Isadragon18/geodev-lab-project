import csv


def read_rows(file_path):
    with open(file_path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    return rows

def clean_values(rows, column):
    values = []
    text = []
    for row in rows:
        try:
            raw = row[column].strip()
            if raw == "":
                continue
            
            values.append(float(raw))
        except ValueError:
            text.append(row[column])
    return values, text

def summarise(values):
    if len(values) == 0:
        return {
            "smallest": None,
            "largest": None,
            "counts": 0,
            "average": None
        }
    return {
        "smallest": min(values),
        "largest": max(values),
        "counts": len(values),
        "average": sum(values) / len(values)
    }
    
def largest_value(rows, column):
    largest_value = None
    data = None
    for row in rows:
        try:
            raw = row[column].strip()
            if raw == "":
                continue
            
            value = float(raw)
            if largest_value is None or value > largest_value:
                largest_value = value
                data = row
        except ValueError:
            continue
    return data

def export_file(report, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Column", "Smallest", "Largest", "Counts", "Average", "Non_Numeric"])
        for column, summary in report.items():
            writer.writerow([
                column,
                summary.get("smallest"),
                summary.get("largest"),
                summary.get("counts"),
                summary.get("average"),
                summary.get("Non_Numeric")
            ])



def summarize_all(filename):
    rows = read_rows(filename)
    headers = list(rows[0].keys())
    report = {}
    for column in headers:
        values, text = clean_values(rows, column)
        report[column] = summarise(values)
        report[column]["largest_value"] = largest_value(rows, column)
        report[column]["Non_Numeric"] = len(set(text))
    return report

report = summarize_all('settlement.csv')


for column in report:
    print(f"{column} -> {report[column]}")
    
export_file(report, 'summary.csv')