from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.generic.list import ListView
from rest_framework import viewsets
from works_app.serializers import  WorkSerializer
from works_app.models import Work


class WorkListView(ListView):
    model = Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer



class WorkList(APIView):

    def get(self, request, format=None):
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = WorkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WorkDetail(APIView):

    def get_object(self, pk):
        try:
            return Work.objects.get(pk=pk)
        except Work.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        work = self.get_object(pk)
        serializer = WorkSerializer(work)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        work = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = WorkSerializer(work, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        work = self.get_object(pk)
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)