from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class CheckoutForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "John Doe"}))
    street_address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "12345 Main Street Dr"})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "City"}))
    state = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "State"}))
    zip = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "XXXXX"}))
    country = CountryField(blank_label="(select country)").formfield(
        widget=CountrySelectWidget(attrs={"class": "custom-select d-block w-100"})
    )

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')