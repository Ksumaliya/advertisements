from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('adver', index, name='main'),
    path('top-sellers/', top_sellers, name='sellers')
]