import datetime
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact(request):
    """ A view to allow a superuser to add a new voucher """
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank You! A member of our team will be in touch soon with further information.")  # noqa
            return redirect('home')
        else:
            messages.error(request, 'Failed to submit form. Please ensure the form is valid.')  # noqa
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
            'form': form,
    }

    return render(request, 'contact/contact.html', {'form': form})
