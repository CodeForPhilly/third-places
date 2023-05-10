from django.contrib import admin
from .models import BusinessHours, Location, LocationType, Tag, TagType, ThirdPlaceUser

admin.site.register(ThirdPlaceUser)
admin.site.register(BusinessHours)
admin.site.register(LocationType)
admin.site.register(Tag)
admin.site.register(TagType)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = (
            'name',
            'address',
            'hours',
            'location_type',
            'price_category',
            'tags',
            'location'
        )