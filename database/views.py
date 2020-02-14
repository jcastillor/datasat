from django.shortcuts import render
from django_tables2 import LazyPaginator, SingleTableMixin
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin

from .models import Satelite2
from .tables import SateliteTable
from .filters import SateliteFilter


class FilteredSateliteView(ExportMixin, SingleTableMixin, FilterView):
	table_class = SateliteTable
	template_name = 'database/bootstrap_template.html'

	paginator_class = LazyPaginator
	filterset_class = SateliteFilter

	export_formats = ("csv", "xls")