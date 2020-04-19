from django.forms import ModelForm
from myapp.models import Address


class AddressForm(ModelForm):
    class Meta:
        model=Address
        fields=("ip",)
