from rest_framework import serializers
from .models import Carlist , showRoomList , Review
from django.db.models import Q
class ReviewSerializer(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('car',)
        # fields = "__all__"



class CarSerializers(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    Reviews = ReviewSerializer(many=True,read_only=True)
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

    # def create(self, validated_data):
    #     return Carlist.objects.create(**validated_data)   
    
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
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
        namec=data.get('name')
        descriptionc=data.get('description')

        if namec == descriptionc or Carlist.objects.filter(Q(name=descriptionc)|Q(description=namec)):
            raise serializers.ValidationError("Name and description must be different ")
        return data
        

class showRoomSerializer(serializers.ModelSerializer):
    # showrooms = CarSerializers(many=True,read_only=True)
    showrooms = serializers.StringRelatedField(many=True)
    # showrooms = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # showrooms = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='car_detail')
    class Meta:
        model = showRoomList
        fields = "__all__"