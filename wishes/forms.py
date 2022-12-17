from django import forms
from .models import Wishes

class WishForm(forms.ModelForm):
    class Meta:
        model = Wishes
        fields = ['user', 'title', 'status', 'main_photo', 'photo_1', 'photo_2', 'list_date']