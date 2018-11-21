from django.shortcuts import render
from rest_framework import viewsets
from .models import Donador
from .serializers import DonadorSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class DonadorView(viewsets.ModelViewSet):
	queryset = Donador.objects.all()
	serializer_class = DonadorSerializer

class DonadorFiltro(viewsets.ModelViewSet):
	queryset = Donador.objects.all()
	serializer_class = DonadorSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('categoria', 'tipo')

