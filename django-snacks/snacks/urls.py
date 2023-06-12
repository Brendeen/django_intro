# Define routes
from django.urls import path

from .views import HomePageView, AboutPageView, ImagePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('practice', ImagePageView.as_view(), name='image')
]
