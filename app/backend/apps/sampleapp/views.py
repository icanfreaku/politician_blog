from django.shortcuts import render
from .models import Politician
from .serializers import PoliticianSerializer
from rest_framework import generics


class PoliticianList(generics.ListCreateAPIView):
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer


class PoliticianDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer

# Create your views here.
def index(request):
    return render(request, "sampleapp/index.html")