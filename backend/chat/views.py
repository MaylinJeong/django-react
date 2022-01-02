from django.shortcuts import render
from rest_framework import generics

from .models import Dictionary
from .serializers import DictionarySerializer

# Create your views here.

class ListDictionary(generics.ListCreateAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class DetailDictionary(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
