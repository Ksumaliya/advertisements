from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import AdversForm
from .models import Advers
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def index(request):
    ads = Advers.objects.all()
    context = {'ads': ads}
    return render(request, 'app_adver/index.html', context)
def top_sellers(request):
    return render(request, 'app_adver/top-sellers.html')
def post_adv(request:WSGIRequest):
    if request.method == "POST":
        form = AdversForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advers(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(reverse('main'))
    else:
        form = AdversForm()
    context = {'form': form}
    return render(request, 'app_adver/advertisement-post.html', context)