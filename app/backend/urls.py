from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.sampleapp.views import index as index_view
from apps.sampleapp.models import Politician
import os
import csv

def loadPoliticians(parameter):
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

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_view, name='index'),
    url(r'^api/', include('apps.sampleapp.urls')),
    url(r'^load/', loadPoliticians),
    url(r'^.*', index_view) #catch-all
]


