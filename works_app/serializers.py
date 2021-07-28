from rest_framework import serializers
from works_app.models import Work

from django_restql.mixins import DynamicFieldsMixin

class WorkSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['title', 'contributors', 'iswc']

    