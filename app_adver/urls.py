from django.urls import path
from .views import index, top_sellers, post_adv

urlpatterns = [
    path('adver', index, name='main'),
    path('top-sellers/', top_sellers, name='sellers'),
    path('post_adv/', post_adv, name='post'),
]