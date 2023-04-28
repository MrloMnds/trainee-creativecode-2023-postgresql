from rest_framework import serializers

from .models import Contact
from phone_numbers.serializers import PhoneNumberReturnSerializer


class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberReturnSerializer(many=True)

    class Meta:
        model = Contact
        fields = ["id", "name", "address", "phone_numbers"]

        extra_kwargs = {
            "phone_numbers": {"read_only": True}
        }
        depth = 1
