from rest_framework import serializers
from users.models import Role, User

    
class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    
class ProfileSerializer(serializers.ModelSerializer):
  role = RoleSerializer(
    many=False,
    read_only=True,
  )
  class Meta:
    model = User
    fields = ('role', 'first_name', 'last_name', 'email', 'phone', 'id', )

    
