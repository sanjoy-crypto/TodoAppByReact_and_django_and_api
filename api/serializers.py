from rest_framework import serializers
from .models import *


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
