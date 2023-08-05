from rest_framework import serializers

from .pymongo_client import (
    id_collection,
    pizza_collection
)

class PizzaSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10, required=True)
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.IntegerField(max_value=1000, min_value=100, required=True)
    image = serializers.CharField(max_length=100, required=True)

    def get(self):
        pizza_list = list(pizza_collection.find({}, {'_id': 0}))
        return pizza_list
    
    def create(self, validated_data):
        pizza = {
            'id': validated_data['id'],
            'name': validated_data['name'],
            'price': validated_data['price'],
            'image': validated_data['image']
        }

        pizza_collection.insert_one(pizza)

        return pizza
