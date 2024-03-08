from django.db import models


class ProductionStep(models.IntegerChoices):
    PRE_REALIZATION = 0
    REALIZATION = 1
    ENDED = 2

class Production(models.Model):
    order_name = models.CharField(max_length=30)
    step = models.IntegerField(choices=ProductionStep.choices)

    def __str__(self):
        return self.order_name
    
class PreRealizationProduction(Production):
    class Meta:
        proxy = True
        # ordering = ('order_name',)

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(step=ProductionStep.PRE_REALIZATION)
        
    def save(self, *args, **kwargs):
        if self._state.adding: # wykonuje sie gdy instancja będzie dodawana do bazy danych po raz pierwszy
            self.step = ProductionStep.PRE_REALIZATION 
        super().save(*args, **kwargs)

    objects = Manager()

class RealizationProduction(Production):
    class Meta:
        proxy = True
        # ordering = ('order_name',)

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(step=ProductionStep.REALIZATION)

    objects = Manager()        


class EndedProduction(Production):
    class Meta:
        proxy = True
        # ordering = ('order_name',)

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            qs = super().get_queryset().filter(step=ProductionStep.ENDED)
            return qs
        
    objects = Manager()