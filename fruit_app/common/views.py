from django.shortcuts import render

# Create your views here.
from fruit_app.accounts.models import ProfileModel
from fruit_app.fruit.models import FruitModel


def home_page(request):
    profiles = ProfileModel.objects.all()
    context = {
        'profiles': profiles

    }

    return render(request, 'common/index.html', context=context)


def dashboard_page(request):
    profiles = ProfileModel.objects.all()
    fruits = FruitModel.objects.all()
    context = {
        'fruits': fruits,
        'profiles': profiles

    }
    return render(request, 'common/dashboard.html', context=context)