from django.shortcuts import render
from rest_framework import generics

from music_works.models import MusicWorks
from music_works.serializers import MusicWorkSerializer


class MusicWorksView(generics.RetrieveAPIView):
    queryset = MusicWorks.objects.all()
    serializer_class = MusicWorkSerializer
    lookup_field = 'iswc'
