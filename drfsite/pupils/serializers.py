import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Pupils


class PupilsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pupils
        fields = ('title', 'content', 'cat')


# работа с базовым классом Serializer
# class PupilsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=250)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Pupils.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

# Введение в сериализацию. Класс Serializer
# class PupilModel :
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = PupilModel('Varvara', 'Moscow')
#     model_sr = PupilsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Varvara","content":"Moscow"}')
#     data = JSONParser().parse(stream)
#     serializer = PupilsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

# class PupilsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pupils
#         fields = ('title', 'cat_id')
