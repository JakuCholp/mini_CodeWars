from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TodecideSerializer(serializers.Serializer):
    solution = serializers.CharField(max_length = 256)