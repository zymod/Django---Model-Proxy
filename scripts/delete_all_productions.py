import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

from warehouse.models import Production

def run():
    for p in Production.objects.all():
        p.delete()