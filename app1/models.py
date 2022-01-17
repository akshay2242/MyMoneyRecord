from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    date = models.DateField()
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=150)
    STATUS_CHOICES = (('P', 'Paid'),('U', 'Unpaid'))
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    