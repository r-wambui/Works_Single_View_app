import csv
from django.core.management.base import BaseCommand
from django.db.models import Q

from music_works.models import Contributor, MusicWorks


class Command(BaseCommand):
    help = "Import music metadata csv"

    def handle(self, *args, **options):
        with open("data/works_metadata.csv") as music_file:
            music_metadata = csv.DictReader(music_file)
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
                    row_contributors = Contributor.objects.filter(
                        contributor__in=row["contributors"].split("|"))
                    search_query = MusicWorks.objects.filter(Q(title=row["title"]) & Q(
                        contributors__in=row_contributors)).first()
                    if search_query:
                        self.get_or_create_contributor(
                            row["contributors"].split("|"), search_query)

    @ staticmethod
    def get_or_create_contributor(music_contributors, query):
        # create and update existing title contributors
        for contributor in music_contributors:
            contributor, _ = Contributor.objects.get_or_create(
                contributor=contributor)
            query.contributors.add(contributor)
