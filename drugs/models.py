from django.db import models

# Create your models here.


class Entities(models.Model):
    # For generic term to lookup (Either drug name or mechanism name)
    name = models.CharField(max_length=50)
    # entity type True is Mechanism, False is Drug
    # Would make into different datatype upon expanding DB
    entity_type = models.BooleanField()

    def __str__(self):
        return self.name

class Drugs(models.Model):
    # Individual Drug Records
    name_main = models.CharField(max_length=50)
    condition_name = models.CharField(max_length=50)
    admin_route = models.CharField(max_length=20)
    # entities links the Entities table in a Many to Many relationship
    entities = models.ManyToManyField(Entities, related_name="entities")

    def __str__(self):
        return self.name_main



