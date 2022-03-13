from django.db import models

# Create your models here.

class Course(models.Model):
    ac_code = models.CharField(primary_key=True, max_length=6)
    ac_name = models.CharField(max_length=50)
    ac_credits = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.ac_name, self.ac_credits)