import csv
import random



def get_random_city():
    with open('algeria_cities.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        rows = list(reader)
        if not rows:
            raise ValueError("The CSV file is empty or only contains the header.")
        return random.choice(rows)

