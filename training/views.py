from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Training

from flights.models import Aircraft
# from .forms import TrainingForm


def training(request):
    """ A view to show all training courses """

    training = Training.objects.all()

    context = {
        'training': training,
    }
    
    return render(request, 'training/training.html', context)
