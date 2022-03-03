from rest_framework import serializers

from hello_backend.models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'creator_id']
        read_only_fields = ['creator_id']
