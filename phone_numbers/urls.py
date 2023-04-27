from django.urls import path

from . import views

urlpatterns = [
    path("phoneNumbers/", views.PhoneNumberView.as_view()),
    path("phoneNumbers/<int:pk>/", views.PhoneNumberDetailView.as_view()),
]
