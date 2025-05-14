from django.shortcuts import render

def choose_role(request):
    return render(request, 'accounts/choose_role.html')
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerRegistrationForm  # We'll create this next

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('choose')  # Redirect to role selection or dashboard
    else:
        form = CustomerRegistrationForm()
    return render(request, 'accounts/customer_register.html', {'form': form})

from .forms import VendorRegistrationForm

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('choose')
    else:
        form = VendorRegistrationForm()
    return render(request, 'accounts/vendor_register.html', {'form': form})

from .forms import DeliveryPartnerRegistrationForm

def delivery_register(request):
    if request.method == 'POST':
        form = DeliveryPartnerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('choose')
    else:
        form = DeliveryPartnerRegistrationForm()
    return render(request, 'accounts/delivery_register.html', {'form': form})


# 