#!/usr/bin/env python3
"""Just my doccument"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON and writes the result to data.json.
    Returns True on success, False on failure.
    """
    try:
        data_list = []

        # Open and read the CSV file
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        # Write JSON data to data.json
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False
