from django.db import models


class PhoneNumber(models.Model):
    class Meta:
        ordering = ["id"]

    number = models.CharField(max_length=25, unique=True)

    contact_id = models.ForeignKey(
        "contacts.Contact",
        on_delete=models.CASCADE,
        related_name="phone_numbers",
    )
