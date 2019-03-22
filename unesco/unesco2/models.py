from django.db import models

# Create your models here.

class unesco_category(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class unesco_states(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class unesco_regions(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class unesco_iso(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class unesco_site(models.Model):
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 4096)
    justification = models.CharField(max_length = 4096)
    year = models.IntegerField(null = True)
    longitude = models.FloatField(null = True)
    latitude = models.FloatField(null = True)
    area_hectares = models.FloatField(null = True)
    category = models.ForeignKey(unesco_category, on_delete = models.CASCADE)
    state = models.ForeignKey(unesco_states, on_delete = models.CASCADE)
    region = models.ForeignKey(unesco_regions, on_delete = models.CASCADE)
    iso = models.ForeignKey(unesco_iso, on_delete = models.CASCADE)


    def __str__(self):
        return self.name
