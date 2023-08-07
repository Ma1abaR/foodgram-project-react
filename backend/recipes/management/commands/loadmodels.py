import json
from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        file_path = options["path"]

        with open(file_path, encoding="utf-8") as f:
            jsondata = json.load(f)

            if "color" in jsondata[0]:
                tags_to_create = [
                    Tag(
                        name=line["name"],
                        color=line["color"],
                        slug=line["slug"]
                    )
                    for line in jsondata
                    if not Tag.objects.filter(slug=line["slug"]).exists()
                ]
                Tag.objects.bulk_create(tags_to_create)

            elif "measurement_unit" in jsondata[0]:
                ingredients_to_create = [
                    Ingredient(
                        name=line["name"],
                        measurement_unit=line["measurement_unit"]
                    )
                    for line in jsondata
                    if not Ingredient.objects.filter(
                        name=line["name"],
                        measurement_unit=line["measurement_unit"]
                    ).exists()
                ]
                Ingredient.objects.bulk_create(ingredients_to_create)
