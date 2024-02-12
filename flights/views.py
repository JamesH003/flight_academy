from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Voucher, Aircraft
from .forms import VoucherForm


def all_vouchers(request):
    """ A view to show all vouchers """

    vouchers = Voucher.objects.all()

    context = {
        'vouchers': vouchers,
    }
    return render(request, 'flights/vouchers.html', context)


def voucher_detail(request, voucher_id):
    """ A view to show individual voucher details """

    voucher = get_object_or_404(Voucher, pk=voucher_id)

    context = {
        'voucher': voucher,
    }

    return render(request, 'flights/voucher_detail.html', context)


@login_required
def add_voucher(request):
    """ A view to allow a superuser to add a new voucher """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Flight Academy management can access this.')  # noqa
        return redirect(reverse('vouchers'))

    if request.method == 'POST':
        form = VoucherForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a new voucher!')  # noqa
            return redirect('vouchers')
        else:
            messages.error(request, 'Failed to add voucher. Please ensure the form is valid.')  # noqa
    else:
        form = VoucherForm()

    template = 'flights/add_product.html'
    context = {
            'form': form,
    }

    return render(request, 'flights/add_voucher.html', {'form': form})


@login_required
def edit_voucher(request, id):
    """ A view to allow a superuser to edit a voucher """
    voucher = get_object_or_404(Voucher, id=id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Flight Academy management can access this.')  # noqa
        return redirect('vouchers')
    form = VoucherForm(
        request.POST or None, request.FILES or None, instance=voucher)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {voucher.title}')
            return redirect('vouchers')
        else:
            messages.error(request, f'Failed to update {voucher.title}. Please ensure the form is valid.')  # noqa
    else:
        form = VoucherForm(instance=voucher)
        messages.info(request, f'You are editing {voucher.title}.')
    context = {
        'form': form,
        'voucher': voucher,
    }

    return render(request, 'flights/edit_voucher.html', context)


@login_required
def delete_voucher(request, id):
    """ A view to allow a superuser to delete a voucher """
    voucher = get_object_or_404(Voucher, id=id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Flight Academy management can access this.')  # noqa
        return redirect('vouchers')
    voucher.delete()
    return redirect('vouchers')
