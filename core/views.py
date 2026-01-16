from rest_framework import viewsets
import pandas as pd
from .models import Dataset, Variable
from .serializers import DatasetSerializer, VariableSerializer

# Create your views here.

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def perform_create(self, serializer):
        dataset=serializer.save(uploaded_by=self.request.user)
        #Parse CSV
        df = pd.read_csv(dataset.file.path)
        for col in df.columns:
            Variable.objects.create(
                dataset=dataset,
                name=col,
                type=str(df[col].dtype),
            )


class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer