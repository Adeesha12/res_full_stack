from rest_framework import serializers
from .models import Todos


class TodosSerializer(serializers.ModelSerializer):
    header = serializers.CharField(max_length=200, required = True)
    contains = serializers.CharField(max_length=1000, required = True)
    
    class Meta:
        model = Todos
        fields = ('__all__')
    
    def create(self, validated_data):
        return Todos.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.header = validated_data.get('header',instance.header)
        instance.contains = validated_data.get('contains',instance.contains)
        
        instance.save()
        return instance