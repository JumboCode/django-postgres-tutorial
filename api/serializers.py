from rest_framework import serializers
from .models import *


class SledSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sled
        fields = ('id', 'name', 'victories', 'defeats')


class SledTeamSerializer(serializers.ModelSerializer):

    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Sled
        fields = ('id', 'name', 'members')


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = ("id", "first_name", "last_name", "phone_number", "sled")
