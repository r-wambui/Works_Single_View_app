from django.urls import path

from music_works.views import MusicWorksView

urlpatterns = [
    path('musicworks/<str:iswc>', MusicWorksView.as_view())
]