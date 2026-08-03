from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html')


def no_permission(request):
    return render(request, 'no_permission.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            messages.error(request, 'Please fill in all fields before sending.')
        else:
            try:
                send_mail(
                    subject=f"New contact message from {name}",
                    message=f"From: {name} <{email}>\n\n{message}",
                    from_email=None,  # uses DEFAULT_FROM_EMAIL
                    recipient_list=['hello@taskmaster.app'],  # change to your real inbox
                    fail_silently=False,
                )
                messages.success(request, "Thanks! Your message has been sent — we'll get back to you soon.")
            except Exception:
                messages.error(request, "Something went wrong sending your message. Please try again later.")

            return redirect('contact')

    return render(request, 'contact.html')