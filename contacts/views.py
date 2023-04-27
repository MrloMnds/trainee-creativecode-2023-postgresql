from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


class ContactView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(
    UpdateAPIView,
    DestroyAPIView
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
