from rest_framework import serializers

from music_works import models

class MusicWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MusicWorks
        fields = '__all__'
