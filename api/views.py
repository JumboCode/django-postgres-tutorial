from django.shortcuts import render
from rest_framework import generics

from .models import *

from .serializers import *

# Creates Views to Create and List All Sleds (Get and POST routes)
class SledList(generics.ListCreateAPIView):
    queryset = Sled.objects.all()
    serializer_class = SledSerializer


# Creates Views to Create and List All Sleds (GET and POST routes)
class MembersList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer