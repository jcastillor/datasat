"""datasat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views import static
from django.views.generic.base import TemplateView

from database.views import FilteredSateliteView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name = 'home'),
    path("filtered-satelite2/", FilteredSateliteView.as_view(), name='filteredsatelite2'),
    path('admin/', admin.site.urls),
]