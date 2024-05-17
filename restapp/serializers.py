from rest_framework import serializers
from .models import Carlist , showRoomList

class showRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = showRoomList
        fields = "__all__"


class CarSerializers(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = Carlist
        fields = "__all__"
    # id = serializers.Serializer(read_only=True)
    # name = serializers.CharField(required=True)
    # description = serializers.CharField()
    # active = serializers.BooleanField(read_only=True)
    # chassisnumber = serializers.CharField(validators=[alphanumeric]) #validators 
    # price = serializers.DecimalField(max_digits=9,decimal_places=2)
    def get_discounted_price(self,object):
        discountPrice = object.price - 5000
        return discountPrice


    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)
    
    
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        # instance.name =validated_data.get('name',instance.name)
        # instance.description =validated_data.description('name',instance.description)
        # instance.active =validated_data.get('name',instance.active)        
        # instance.save()
        # return instance  
    class Meta:
        model = Carlist
        fields = '__all__'

    # This is field level validation 
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
        # return super().validate_price(value)

    # This is object level validation 
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description must be different ")
        return data
        

