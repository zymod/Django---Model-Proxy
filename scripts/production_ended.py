import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import EndedProduction

def run():
    qs = EndedProduction.objects.all()
    print(qs)