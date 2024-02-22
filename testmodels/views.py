from rest_framework import generics, viewsets
from .models import TestModel
from .serializers import TestModelSerializer


class TestModelList(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

