from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, Permission


class BusinessHours(models.Model):
    WEEKDAYS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )

    day = models.CharField(choices=WEEKDAYS, max_length=3)
    open_time = models.TimeField()
    close_time = models.TimeField()

    REQUIRED_FIELDS = ["day"]

    def __str__(self):
        return f'{self.day}: {self.open_time} - {self.close_time}'


class LocationType(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()

    REQUIRED_FIELDS = ["code", "name"]

    def __str__(self):
        return self.code


class TagType(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()

    REQUIRED_FIELDS = ["code", "name"]

    def __str__(self):
        return self.code


class Location(models.Model):
    location = gis_models.PointField(srid=4326)
    name = models.TextField()
    address = models.TextField()
    hours = models.ForeignKey(BusinessHours, on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    price_category = models.CharField(max_length=5)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["location", "location_type", "created_datetime", "modified_datetime"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.TextField()
    locations = models.ManyToManyField(Location, related_name='tags')
    tag_type = models.ForeignKey(TagType, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=1, max_digits=2)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["name", "tag_type", "value", "created_datetime", "modified_datetime"]

    def __str__(self):
        return self.name


class ThirdPlaceUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    display_name = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='thirdplaceuser_groups',
        verbose_name='groups',
        help_text=('The groups this user belongs to. A user will '
                   'get all permissions granted to each of their '
                   'groups.'),
        related_query_name='thirdplaceuser',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='thirdplaceuser_user_permissions',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='thirdplaceuser',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email", "username", "display_name", "created_datetime", "modified_datetime"]

    def __str__(self):
        return self.email
