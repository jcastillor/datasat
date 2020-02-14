# Fichero para aplicar los filtros a la base de datos

from django_filters import FilterSet

from .models import Satelite2

class SateliteFilter(FilterSet):
	class Meta:
		model = Satelite2
		fields = {
		"type": ["contains"],
		"indice": ["contains"],
		"satlength": ["contains"],
		"numrep": ["contains"],
		"replength": ["contains"],
		"seed": ["contains"],
		"seq": ["contains"],
		"genbank_id": ["contains"],
		"name": ["contains"]
		}
