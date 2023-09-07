from rest_framework import serializers

class SampleSerializer(serializers.Serializer):
    name = serializers.CharField(write_only=True)
    place = serializers.CharField(write_only=True)