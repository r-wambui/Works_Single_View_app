import csv
from django.core.management.base import BaseCommand
from django.db.models import Q

from music_works.models import Contributor, MusicWorks


class Command(BaseCommand):
    help = "Import music metadata csv"

    def add_arguments(self, parser):
        parser.add_argument("--csv-path", help="csv path", type=str
                            )

    def handle(self, *args, **options):
        path = "data/works_metadata.csv"
        if options["csv_path"]:
            path = options["csv_path"]

        with open(path) as music_file:
            music_metadata = csv.DictReader(music_file)
            no_iswc = []
            for row in music_metadata:
                if row["iswc"]:
                    query_iswc = MusicWorks.objects.filter(
                        iswc=row["iswc"]).first()
                    if not query_iswc:
                        music_work = MusicWorks.objects.create(
                            iswc=row["iswc"], title=row["title"])

                        # get or create, then add contributors to the music object
                        self.get_or_create_contributor(
                            row["contributors"].split("|"), music_work)

                    if query_iswc:
                        self.get_or_create_contributor(
                            row["contributors"].split("|"), query_iswc)
                else:
                    no_iswc.append(row)

            for row in no_iswc:
                self.check_by_title_contributor(row)

    def check_by_title_contributor(self, row):
        row_contributors = Contributor.objects.filter(
            contributor__in=row["contributors"].split("|"))
        search_query = MusicWorks.objects.filter(Q(title=row["title"]) & Q(
            contributors__in=row_contributors)).first()
        if search_query:
            self.get_or_create_contributor(
                row["contributors"].split("|"), search_query)

    def get_or_create_contributor(self, music_contributors, query):
        # create and update existing title contributors
        for contributor in music_contributors:
            contributor, _ = Contributor.objects.get_or_create(
                contributor=contributor)
            if contributor not in query.contributors.all():
                query.contributors.add(contributor)
