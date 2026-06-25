import csv

from app.models import Trade

def parse_trades_csv(file_path: str) -> list[Trade]:
    trades = []
    with open(file_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            print(row)
            

    return trades