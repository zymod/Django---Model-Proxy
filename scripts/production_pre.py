import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import PreRealizationProduction


def run():
    pre_realization = PreRealizationProduction.objects.all()
    print(pre_realization)