from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('snacks', HomePageView.as_view(), name='snacks'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
]
