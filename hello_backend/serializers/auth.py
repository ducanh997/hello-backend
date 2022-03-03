from rest_framework import serializers


class GoogleLoginSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.CharField(required=False)
    error = serializers.CharField(required=False)