from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "address", "phone_numbers"]

        extra_kwargs = {
            "phone_numbers": {"read_only": True}
        }
