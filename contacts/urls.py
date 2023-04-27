from django.urls import path

from .views import ContactView, ContactDetailView

urlpatterns = [
    path("contacts/", ContactView.as_view()),
    path("contacts/<int:pk>/", ContactDetailView.as_view()),
]
