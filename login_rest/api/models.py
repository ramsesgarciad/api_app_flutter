from django.db import models


# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=1100)
    last_name = models.CharField('LastName', max_length=100)

    def __str__(self):
        return '{0},{1}'.format(self.name, self.last_name)
