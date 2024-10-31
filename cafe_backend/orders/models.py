from django.db import models

class Order(models.Model): 
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pending")



