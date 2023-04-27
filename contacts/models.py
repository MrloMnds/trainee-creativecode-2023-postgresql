from django.db import models


class Contact(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=45, unique=True)
    address = models.CharField(max_length=150)
