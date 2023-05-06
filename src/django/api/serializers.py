import datetime

from rest_framework import serializers
from .models import ThirdPlaceUser


class ThirdPlaceUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    display_name = serializers.CharField(required=False)
    created_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)
    modified_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)

    class Meta:
        model = ThirdPlaceUser
        fields = (
            "username",
            "email",
            "password",
            "display_name",
            "created_datetime",
            "modified_datetime"
        )



class ThirdPlaceUserPutSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    display_name = serializers.CharField(required=False)

    class Meta:
        model = ThirdPlaceUser
        fields = (
            "username",
            "email",
            "password",
            "display_name",
        )
