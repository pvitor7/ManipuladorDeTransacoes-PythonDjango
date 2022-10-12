from rest_framework import serializers
from .models import Account
from rest_framework.authtoken.models import Token
import ipdb

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data: str):
        account = Account.objects.create_user(**validated_data)
        return account
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)