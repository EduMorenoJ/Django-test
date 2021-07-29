from django.core.management import BaseCommand
from works_app.models import Work
from works_app.utils import group_by_title_and_iswc_and_remove_duplicates
from django.db import IntegrityError
import logging

class Command(BaseCommand):
    help = 'Load work csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        formated_data = group_by_title_and_iswc_and_remove_duplicates(
            kwargs['path'])
        for row in formated_data:
            try:
                Work.objects.create(
                    title=row['title'],
                    contributors=row['contributors'],
                    iswc=row['iswc']
                )
            except IntegrityError:
                logging.warning(
                    'There is a registry with the same iswc in de database. '\
                    f'The registry is {row["iswc"]}. It won\'t be inserted. '\
                    'Please report this issue.')
                pass