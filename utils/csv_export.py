import csv
from io import StringIO
from flask import make_response

def export_to_csv(data, filename):
    """Generates a CSV file from data."""
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(data[0].keys())  # Write headers
    for row in data:
        writer.writerow(row.values())  # Write rows

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f"attachment; filename={filename}.csv"
    output.headers["Content-type"] = "text/csv"
    return output
