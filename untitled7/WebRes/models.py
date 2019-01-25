from django.db import models



class Module(models.Model):
    id_module = models.IntegerField()
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    ping_module = models.BooleanField()
    last_ping_time = models.DateTimeField()
    errors = models.BooleanField()
    error_type = models.CharField(max_length=100)




# Create your models here.
