import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import Production, PreRealizationProduction


def run():
    pre_realization = PreRealizationProduction.objects.get(name='XYZ')
    print(pre_realization)
    