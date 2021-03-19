from rest_framework import serializers

from music_works.models import MusicWorks


class MusicWorkSerializer(serializers.ModelSerializer):
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = MusicWorks
        fields = ['id', 'iswc', 'title', 'contributors']
