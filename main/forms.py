from django.forms import ModelForm
from .models import show
class ShowForm(ModelForm):
    class Meta:
        model=show
        fields='__all__'