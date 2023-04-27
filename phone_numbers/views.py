from django.shortcuts import render
from .models import PhoneNumber
from contacts.models import Contact
from .serializers import PhoneNumberSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


class PhoneNumberView(ListAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class PhoneNumberDetailView(
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

    def perform_create(self, serializer: PhoneNumberSerializer) -> None:
        contact_id = self.request.parser_context.get("kwargs").get("pk")
        contact = Contact.objects.get(pk=contact_id)
        serializer.save(contact_id=contact)
