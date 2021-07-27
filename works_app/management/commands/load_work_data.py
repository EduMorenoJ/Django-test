import csv
from django.core.management import BaseCommand
from works_app.models import Work

class Command(BaseCommand):
    help = 'Load work csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        #self.stdout.write(path)
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader, None)
            for row in reader:
                self.stdout.write(f'{row[1].split("|")}')
                work = Work.objects.create(
                    title=row[0],
                    contributors=f'{row[1].split("|")}'.replace('[','{').replace(']','}'),
                    iswc=row[2]
                )
                self.stdout.write(str(work))
            