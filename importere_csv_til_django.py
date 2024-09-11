import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_no.settings')
django.setup()

from blog.models import Post

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Post.objects.create(
                HANDLE=row['HANDLE'],
                TITLE=row['TITLE'],
                QTY =row['QTY'],
                PRICE=row['PRICE'],
                IMAGE = row['IMAGE'],
                WIDTH = row['WIDTH'],
                LENGTH = row['LENGTH']
            )

if __name__ == '__main__':
    csv_file_path = 'en_variant.csv'  # Erstatt med den faktiske filbanen
    import_books(csv_file_path)
