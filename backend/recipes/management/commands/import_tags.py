import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from recipes.models import Tag


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        with open(
            f'{settings.BASE_DIR}/data/tags.csv',
            # f'{settings.STATIC_ROOT}/data/tags.csv',
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                Tag.objects.bulk_create(
                    Tag(**items) for items in reader
                )
            except IntegrityError:
                return 'Такие Теги уже есть...'
        return (f'Теги успешно загружены -> '
                f'{(", ").join([_.get("name") for _ in Tag.objects.values()])}'
                )
