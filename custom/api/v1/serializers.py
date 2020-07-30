from rest_framework import serializers
from custom.models import UserLogin


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = "__all__"
