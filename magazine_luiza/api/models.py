from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=200, null=False)

    email = models.EmailField(max_length=80, null=False)

    department = models.CharField(max_length=100, null=False)
