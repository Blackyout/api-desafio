from rest_framework import serializers
from .models import Person, Product

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

class ProductSerializer(serializers.ModelSerializer):
    # Opcional: Mostrar el nombre del owner en lectura
    owner_name = serializers.ReadOnlyField(source='owner.first_name')

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'owner_name')