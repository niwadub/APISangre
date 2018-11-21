from rest_framework import serializers
from .models import Donador

class DonadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Donador
		fields = ('id','categoria','nombre','telefono','email','sexo','tipo','centro')