from django.shortcuts import render
from rest_framework import viewsets
from api.serilaizers import MovieSerializer, MovieMiniSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from api.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
    	movies = Movie.objects.all()
    	serilaizer = MovieMiniSerializer(movies, many=True)
    	return Response(serilaizer.data)
