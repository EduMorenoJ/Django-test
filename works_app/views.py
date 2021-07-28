from django.views.generic.list import ListView
from rest_framework import viewsets
from works_app.serializers import  WorkSerializer
from works_app.models import Work


class WorkListView(ListView):
    model = Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
