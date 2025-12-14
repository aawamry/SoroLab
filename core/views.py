from rest_framework import viewsets
from .models import Dataset, Variable
from .serializers import DatasetSerializer, VariableSerializer

# Create your views here.

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer