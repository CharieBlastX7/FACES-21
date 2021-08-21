from rest_framework import serializers
from rest_framework.settings import import_from_string

from .models import User, Team

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = ['id', 'team_code', 'team_name', 'members']

class UserSerializer(serializers.ModelSerializer):
  teams = TeamSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = ['id', 'roll_no', 'email', 'password', 'name', 'department', 'semester', 'money_owed', 'has_filled_profile', 'phone_no', 'date_joined', 'teams']
    extra_kwargs = {
      'password': {'write_only': True},
    }
  
  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance
  

