from rest_framework import serializers

from .models import Pupils


class PupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ('title', 'cat_id')
