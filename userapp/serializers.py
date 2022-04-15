from rest_framework import serializers
from .models import username

class usernameserializer(serializers.ModelSerializer):
    class Meta:
        model= username
        fields = '__all__'
 