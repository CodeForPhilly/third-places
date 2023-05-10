from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("locations/", views.location_list),
    path("locations/<int:pk>", views.location_detail),
    path("users/", views.third_place_user_list),
    path("users/<int:pk>", views.third_place_user_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
