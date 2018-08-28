#!/usr/bin/python3
"""
Export to CSV
"""

import csv
import requests
from sys import argv


def export_csv():
    """
    Export data in the CSV
    """
    USER_NAME = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(argv[1])).json().get("username")

    DATA = requests.get("https://jsonplaceholder.typicode.com/"
                        "todos?userId={}".format(argv[1])).json()

    with open("{}.csv".format(argv[1]), mode="w") as csv_file:
        data_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for item in DATA:
            completed = item.get("completed")
            title = item.get("title")
            data_writer.writerow([argv[1], USER_NAME, completed, title])


if __name__ == "__main__":
    export_csv()
