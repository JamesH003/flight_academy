from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from newsletter.models import Newsletter
from newsletter.forms import NewsletterForm


def about(request):
    """
    A view to return the about page with
    a newsletter subscription form at the bottom.
    """
    form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank You! "
                "You have been added to our Newsletter mailing list."
            )
            # send email to confirm subscription to newsletter
            subject = "Newsletter Subscription Confirmation"
            body = f"""
            Please do not reply to this email.

            Hi {request.POST.get("email")}, and welcome to Flight Academy!

            This is a confirmation email to confirm your subscription to the Flight Academy Newsletter!
            You'll automatically receive our monthly Newsletter, and can unsubscribe at any time.

            Safe flying,
            Flight Academy

            * Flight Academy will never sell your email address or personal data to any third-party companies.
            """
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [request.POST.get("email")]
            )
            # redirect to the about page
            return redirect("about")
        # invalid form / error
        messages.error(
            request,
            "Failed to submit form. Please ensure the form is valid."
        )

    template = "about.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
