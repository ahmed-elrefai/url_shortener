from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import UrlInfo
import string
import random

# Create your views here.

@api_view(['GET'])
def home(request):
    return render(request, 'home.html')

@api_view(['POST'])
def create_url(request):
    url = request.POST['url']           # the url input field should have a name = 'url'
    short = ''.join(random.choices(string.ascii_letters,k=21))
    url_info = UrlInfo(url=url, short_url=short)
    url_info.save()
    return render(request, 'home.html', context={'short_url':short})

@api_view(['GET'])
def resolve_url(request, short):
    url_info = UrlInfo.objects.filter(short_url=short).get()
    return redirect(url_info.url)

