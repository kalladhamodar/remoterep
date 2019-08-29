from django.db import models
class productdata(models.Model):
    name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Constituecy=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    State=models.CharField(max_length=100)

