from rest_framework import serializers

from hello_backend.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'creator_id']
        read_only_fields = ['creator_id']
