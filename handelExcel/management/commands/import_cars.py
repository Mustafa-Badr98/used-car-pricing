from django.shortcuts import render

import pandas as pd
from django.core.management.base import BaseCommand
from handelExcel.models import Car

class Command(BaseCommand):
    help = 'Import cars from an Excel-like file to the database.'

    def handle(self, *args, **options):
        file_path = 'path/to/your/excel_like_file.csv'  # Replace with the actual file path

        # Read data from the Excel-like file into a DataFrame
        df = pd.read_excel('cr.xlsx')

        # Loop through DataFrame and create Car objects
        for index, row in df.iterrows():
            Car.objects.create(
                make=row['Make'],
                model=row['Model'],
                year=row['Year'],
                color=row['Color'],
                mileage=row['Mileage'],
                location=row['Location'],
                car_class=row['Class'],
                price=row['Price'],
                date=row['Date'],
                link=row['Link'],
            )

        self.stdout.write(self.style.SUCCESS('Cars imported successfully.'))
