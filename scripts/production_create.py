import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import PreRealizationProduction


def run():
    PreRealizationProduction.objects.create(order_name='XYZ')