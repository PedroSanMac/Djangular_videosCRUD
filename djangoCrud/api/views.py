import rest_framework
from rest_framework.response import Response
from djangoCrud.api.models import Movie
from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from rest_framework import permissions
from .serializers import MovieMiniSerializer, MovieSerializer
from .models import Movie
from rest_framework.response import Response 


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)


