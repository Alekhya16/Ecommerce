from django import forms
from django.contrib.auth.models import User
from .models import Customer
from .models import Vendor
from .models import DeliveryPartner

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'phone', 'profile_picture', 'address']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        customer = super().save(commit=False)
        customer.user = user
        if commit:
            customer.save()
        return customer
class VendorRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password', 'business_name', 'phone', 'business_license', 'address']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        vendor = super().save(commit=False)
        vendor.user = user
        if commit:
            vendor.save()
        return vendor
class DeliveryPartnerRegistrationForm(forms.ModelForm) :
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = DeliveryPartner
        fields = ['username', 'email', 'password', 'phone', 'vehicle_type', 'vehicle_number', 'license_document']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        partner = super().save(commit=False)
        partner.user = user
        if commit:
            partner.save()
        return partner
# from django import forms
# from .models import DeliveryPartnerProfile  # Assuming this is your model

# class DeliveryPartnerRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = DeliveryPartnerProfile
#         fields = ['vehicle_type', 'license_number', 'phone_number']  # Modify as needed

