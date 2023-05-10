import datetime

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from .models import BusinessHours, Location, LocationType, ThirdPlaceUser, Tag, TagType


class BusinessHoursSerializer(serializers.ModelSerializer):
    day = serializers.CharField()
    open_time = serializers.TimeField(required=False)
    close_time = serializers.TimeField(required=False)

    class Meta:
        model = BusinessHours
        fields = (
            "day",
            "open_time",
            "close_time"
        )


class LocationTypeSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = LocationType
        fields = (
            "code",
            "name"
        )


class TagTypeSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = TagType
        fields = (
            "code",
            "name"
        )


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    tag_type = TagTypeSerializer()
    value = serializers.DecimalField(decimal_places=1, max_digits=2)
    created_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)
    modified_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)

    class Meta:
        model = Tag
        fields = (
            "name",
            "tag_type",
            "value",
            "created_datetime",
            "modified_datetime"
            )
    
    def create(self, validated_data):
        tag_type_data = validated_data.pop("tag_type")
        tag_types = TagType.objects.create(**tag_type_data)
        return Tag.objects.create(tag_types, **validated_data)


class LocationSerializer(gis_serializers.GeoFeatureModelSerializer):
    name = serializers.CharField()
    address = serializers.CharField()
    hours = BusinessHoursSerializer(many=True)
    location_type = LocationTypeSerializer()
    tags = TagSerializer(many=True)
    created_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)
    modified_datetime = serializers.DateTimeField(read_only=True, initial=datetime.datetime)

    class Meta:
        model = Location
        geo_field="location"
        fields = (
            "name",
            "address",
            "hours",
            "location_type",
            "price_category",
            "tags",
            "created_datetime",
            "modified_datetime"
        )

    def create(self, validated_data):
        hours_data = validated_data.pop("hours")
        location_type_data = validated_data.pop("location_type")
        tags_data = validated_data.pop("tags")
        location_type = LocationType.objects.create(**location_type_data)
        location = Location.objects.create(location_type=location_type, **validated_data)
        for hours_datum in hours_data:
            BusinessHoursSerializer(hours_datum)
        for tag_data in tags_data: 
            TagSerializer(tag_data)
        return location

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
