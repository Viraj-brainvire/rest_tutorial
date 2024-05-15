from rest_framework import serializers
from .models import Carlist

class CarSerializers(serializers.ModelSerializer):
    id = serializers.Serializer(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)
    
    class Meta:
        model = Carlist
        fields = '__all__'