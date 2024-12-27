from rest_framework import serializers
from .models import leads

class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model=leads
        fields=['id','name','email','phone','message']