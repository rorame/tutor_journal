from rest_framework import generics
from django.shortcuts import render

from .models import Pupils
from .serializers import PupilsSerializer


class PupilsAPIView(generics.ListAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer
