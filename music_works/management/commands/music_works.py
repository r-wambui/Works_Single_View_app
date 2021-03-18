import csv
from django.core.management.base import BaseCommand
from django.db.models import Q

from music_works.models import MusicWorks


class Command(BaseCommand):
    help = "Import music metadata csv"

    def handle(self, *args, **options):
        with open ("data/works_metadata.csv") as music_file:
            music_metadata = csv.DictReader(music_file)
            for row in music_metadata:
                if row["iswc"]:
                    object_retrieved_or_created, created = MusicWorks.objects.get_or_create(iswc=row["iswc"],
                                                    defaults={"title": row["title"], 
                                                            "contributors": row["contributors"].split("|")})
                    if not created:
                        object_retrieved_or_created.contributors = list(set().union(object_retrieved_or_created.contributors, row["contributors"].split("|")))
                        object_retrieved_or_created.save()
    
                else:
                    search_query = MusicWorks.objects.filter(Q(title=row["title"]) & Q(contributors__overlap=row["contributors"].split("|"))).first()
                    if search_query:
                        search_query.contributors = list(set().union(search_query.contributors, row["contributors"].split("|")))
                        search_query.save()
    