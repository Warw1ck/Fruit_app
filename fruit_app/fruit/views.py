from django.shortcuts import render, redirect

# Create your views here.
from fruit_app.accounts.models import ProfileModel
from fruit_app.fruit.models import FruitModel
from fruit_app.fruit.forms import CreateFruitForm, DeleteFruitForm, EditFruitForm


def fruit_create(request):
    profiles = ProfileModel.objects.all()

    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profiles': profiles,
        'forms': form
    }

    return render(request, 'fruit/create-fruit.html', context=context)


def fruit_edit(request, pk):
    profiles = ProfileModel.objects.all()
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('fruit-details', pk)

    context = {
        'profiles': profiles,
        'form': form
    }
    return render(request, 'fruit/edit-fruit.html', context=context)


def fruit_delete(request, pk):
    profiles = ProfileModel.objects.all()
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')
    form = DeleteFruitForm(initial=fruit.__dict__)

    context= {
        'profiles': profiles,
        'form': form
    }
    return render(request, 'fruit/delete-fruit.html', context=context)


def fruit_details(request, pk):
    profiles = ProfileModel.objects.all()
    fruit = FruitModel.objects.get(pk=pk)

    context = {
        'fruit': fruit,
        'profiles': profiles
    }
    return render(request, 'fruit/details-fruit.html', context=context)


