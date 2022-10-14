from rest_framework import serializers
from .models import Store
import ipdb

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store', 'owner']

    def create(self, validated_data):
        store_pk,_ = Store.objects.get_or_create(**validated_data)
        if _:
            store_pk = Store.objects.get(store=validated_data['store'])
            return store_pk;
        
        return store_pk;
