from djangoCrud.api.models import Movie

from rest_framework import serializers
from djangoCrud.api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'year']


