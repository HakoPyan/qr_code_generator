from django.forms import ModelForm
from .models import QR_Data


class QR_DataForm(ModelForm):

    class Meta:
        model = QR_Data
        fields = ('name', 'surname', 'phone_number', 'email')