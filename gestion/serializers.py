from dataclasses import fields

from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'username', 'email', 'password', 'created_at')
        read_only_fields = ('created_at', )
