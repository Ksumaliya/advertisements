from django.shortcuts import render
from django.http import HttpResponse
# from .forms import AdversForms
from .models import Advers
# Create your views here.
def index(request):
    ads = Advers.objects.all()
    context = {'ads': ads}
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
# def post_adv(request):
#     context = {
#         'form': form
#     }
#     return render(request, 'post-adv.html', context)