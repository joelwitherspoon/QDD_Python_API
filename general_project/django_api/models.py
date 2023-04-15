from django.db import models

# Create your models here.
class Django_api(models.Model):
    name = models.CharField(max_length = 100,null=True)
    description = models.CharField(max_length = 1000, null=True)
    dolphin_count = models.IntegerField(null=True)

