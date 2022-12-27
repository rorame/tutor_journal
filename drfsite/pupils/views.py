from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pupils
from .serializers import PupilsSerializer

# Базовый класс APIView для представлений
class PupilsAPIView(APIView):
    def get(self, request):
        # lst = Pupils.objects.all().values()
        # return Response({'pupils': list(lst)})

        # Введение в сериализацию. Класс Serializer
        pup = Pupils.objects.all()
        return Response({'pupils': PupilsSerializer(pup, many=True).data})

    def post(self, request):
        # Введение в сериализацию. Класс Serializer
        serializers = PupilsSerializer(data=request.data)
        serializers.is_valid(raise_exception=True )

        post_new = Pupils.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'puplis': PupilsSerializer(post_new).data})
        # return Response({'pupils': model_to_dict(post_new)})


# class PupilsAPIView(generics.ListAPIView):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer
