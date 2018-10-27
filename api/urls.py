from django.urls import path

from .views import *

urlpatterns = [
    path("sleds/", SledList.as_view(), name="sled-list"),
    path("members/", MembersList.as_view(), name="members-list")
]