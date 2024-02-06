from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Training

from flights.models import Aircraft
from .forms import TrainingForm


def training(request):
    """ A view to show all training courses """

    training = Training.objects.all()

    context = {
        'training': training,
    }
    
    return render(request, 'training/training.html', context)


def training_detail(request, training_id):
    """ A view to show individual training course details """

    training = get_object_or_404(Training, pk=training_id)

    context = {
        'training': training,
    }
    
    return render(request, 'training/training_detail.html', context)


@login_required
def add_training(request):
    """ A view to allow a superuser to add a new Training Course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Flight Academy management can access this.')
        return redirect(reverse('training'))

    if request.method == 'POST':
        form = TrainingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a new Training Course!')
            return redirect('training')
        else:
            messages.error(request, 'Failed to add training course. Please ensure the form is valid.')
    else:
            form = TrainingForm()

    template = 'training/add_training.html'
    context = {
            'form': form,
    }

    return render(request, 'training/add_training.html', {'form': form})


@login_required
def edit_training(request, id):
    """ A view to allow a superuser to edit a Training Course """
    training = get_object_or_404(Training, id=id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Flight Academy management can access this.')
        return redirect('training')
    form = TrainingForm(
        request.POST or None, request.FILES or None, instance=training)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {training.title}')
            return redirect('training')
        else:
            messages.error(request, f'Failed to update {training.title}. Please ensure the form is valid.')
    else:
        form = TrainingForm(instance=training)
        messages.info(request, f'You are editing {training.title}.')
    context = {
        'form': form,
        'training': training,
    }

    return render(request, 'training/edit_training.html', context)


