import csv
from django.core.management.base import BaseCommand
from django.db.models import Q

from music_works.models import MusicWorks


class Command(BaseCommand):
    help = "Import music metadata csv"

    def handle(self, *args, **options):
        with open("data/works_metadata.csv") as music_file:
            music_metadata = csv.DictReader(music_file)
            for row in music_metadata:
                if row["iswc"]:
                    music_object, created = MusicWorks.objects.get_or_create(
                                        iswc=row["iswc"],
                                        defaults={"title": row["title"],
                                                "contributors": row["contributors"].split("|")})
                    if not created:
                        music_object.contributors = list(set().union(
                                            music_object.contributors,
                                            row["contributors"].split("|")))
                        music_object.save()

                else:
                    search_query = MusicWorks.objects.filter(Q(title=row["title"]) & Q(
                        contributors__overlap=row["contributors"].split("|"))).first()
                    if search_query:
                        search_query.contributors = list(set().union(
                            search_query.contributors,
                            row["contributors"].split("|")))
                        search_query.save()
