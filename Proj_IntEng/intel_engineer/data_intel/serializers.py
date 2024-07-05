from rest_framework import serializers
from .models import *

class DataProjekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataProjek
        fields = ['id', 'nama_proyek']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProjectInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'
