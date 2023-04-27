from rest_framework import serializers

from .models import PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ["id", "number", "contact_id"]

        extra_kwargs = {
            "contact_id": {"read_only": True}
        }
