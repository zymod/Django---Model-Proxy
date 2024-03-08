import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from warehouse.models import Production


def run():
    production_4 = Production.objects.get(id=4)
    print(production_4.step) # zwróci 0 nie o to nam chodzi
    print(production_4.get_step_display())

    production_3 = Production.objects.get(id=3)
    print(production_3.get_step_display())
    
