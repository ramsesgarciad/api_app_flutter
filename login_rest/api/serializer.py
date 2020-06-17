from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id',
            'name',
            'last_name',
        )


class UserSeriallizer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError("Este usuario ya existe, ingese uno nuevo")
        else:
            return data
