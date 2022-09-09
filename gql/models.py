from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    work = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    chef = models.OneToOneField(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.chef}'

    class Meta:
        verbose_name_plural = 'specialties'
