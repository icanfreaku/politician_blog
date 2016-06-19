from django.shortcuts import render
from .models import Politician
from .serializers import PoliticianSerializer
from rest_framework import generics
import os
import csv


class PoliticianList(generics.ListCreateAPIView):
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer


class PoliticianDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer

class LoadPoliticians(generics.ListAPIView):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'data/politicians.csv')
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Politician.objects.get_or_create(
                last_name=row[0],
                first_name=row[1],
                gender=row[2],
                constituency=row[3],
                party=row[4],
                )


# Create your views here.
def index(request):
    return render(request, "sampleapp/index.html")