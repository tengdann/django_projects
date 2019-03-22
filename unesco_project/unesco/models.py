from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class states(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class regions(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class iso(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class site(models.Model):
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 4096)
    justification = models.CharField(max_length = 4096)
    year = models.IntegerField(null = True)
    longitude = models.FloatField(null = True)
    latitude = models.FloatField(null = True)
    area_hectares = models.FloatField(null = True)
    category = models.ForeignKey(category, on_delete = models.CASCADE)
    state = models.ForeignKey(states, on_delete = models.CASCADE)
    region = models.ForeignKey(regions, on_delete = models.CASCADE)
    iso = models.ForeignKey(iso, on_delete = models.CASCADE)


    def __str__(self):
        return self.name
