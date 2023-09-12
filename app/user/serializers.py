from rest_framework import serializers
from .models import Demo
from core.validators import FileValidator



class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields='__all__'

class ExcelSampleSerializer(serializers.Serializer):
    excel = serializers.FileField(
        validators=[FileValidator(max_size=2, allowed_extensions=["xlsx"])]
    )
