import csv
from reviews.models import Title


def run_title():
    fhand = open('static/data/titles.csv', encoding="utf-8")
    reader = csv.reader(fhand)

    Title.objects.all().delete()

    next(reader)
    for row in reader:
        print(row)
        data = Title(id=row[0], name=row[1], year=row[2], category=row[3])
        data.save()
