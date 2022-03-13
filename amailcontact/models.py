from django.db import models

# Create your models here.

class City(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return "{0}".format(self.name)
    

class Human(models.Model):
    dni = models.CharField(max_length=15, primary_key=True)
    lastNamePapa = models.CharField(max_length=30)
    lastNameMama = models.CharField(max_length=30)
    names = models.CharField(max_length=30)
    genders = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='F')
    dateBorn = models.DateField()
    city = models.ForeignKey(City, null=False, blank=False, on_delete=models.CASCADE)


    def completeName(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.lastNamePapa, self.lastNameMama, self.names)

    def __str__(self):
        return self.completeName()
    

class Phone(models.Model):
    human = models.ForeignKey(Human, null=False, blank=False, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return "{0} ({1})".format(self.phone, self.human)


class Email(models.Model):
    human = models.ForeignKey(Human, null=False, blank=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

    def __str__(self):
        return "{0} ({1})".format(self.email, self.human)
    