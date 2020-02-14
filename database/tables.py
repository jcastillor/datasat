# database/tables.py
from django_tables2 import static
import django_tables2 as tables
from .models import Satelite2

class SateliteTable(tables.Table):
	class Meta:
		model = Satelite2
		template_name = "django_tables2/bootstrap.html"
		fields = ("id", "genbank_id", "name", "type", "indice", "satlength", "numrep", "replength", "seed", "seq")#tables for database app
