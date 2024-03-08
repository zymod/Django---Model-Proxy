import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import RealizationProduction

def run():
    qs = RealizationProduction.objects.all()
    print(qs)