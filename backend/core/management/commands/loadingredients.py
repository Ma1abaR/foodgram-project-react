import csv

from django.db.utils import IntegrityError
from django.core.management import BaseCommand
from core.models import Ingredient

csv_files = (
    (Ingredient, 'ingredients.csv')
)

fields = (
    ('name', 'color', 'slug'),
    ('name', 'measurement_unit')
)


class Command(BaseCommand):
    help = 'Загрузка из csv файла'

    def handle(self, *args, **options):
        print("Старт импорта")
        try:
            for model, file in csv_files:
                with open(
                        f'core/management/data/{file}', encoding='utf-8'
                ) as f:
                    reader = csv.DictReader(f, delimiter=',')
                    for row in reader:
                        if model in fields:
                            row[fields[model][2]] = row.pop(fields[model][0])
                        obj, created = model.objects.get_or_create(**row)
                        if created:
                            print(f'{obj} загружен в таблицу {model.__name__}')
                        print(
                            f'{obj} уже загружен в таблицу {model.__name__}')

        except IntegrityError as err:
            print(f"Сбой в работе импорта: {error}.")

        finally:
            print("Завершена работа импорта.")