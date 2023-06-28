from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from fruit_app.accounts.forms import CreateProfileForm, EditProfileForm
from fruit_app.accounts.models import ProfileModel
from fruit_app.fruit.models import FruitModel


def profile_create(request):
    profiles = ProfileModel.objects.all()
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'forms': form,
        'profiles': profiles
    }
    return render(request, 'accounts/create-profile.html', context=context)


def profile_edit(request, pk):
    profiles = ProfileModel.objects.all()
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk)
    context = {
        'form': form,
        'profiles': profiles
    }
    return render(request, 'accounts/edit-profile.html', context=context)


def profile_delete(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    return render(request, 'accounts/delete-profile.html')


def profile_details(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    profiles = ProfileModel.objects.all()
    fruit = FruitModel.objects.all()

    context = {
        'profiles': profiles,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'accounts/details-profile.html', context=context)
