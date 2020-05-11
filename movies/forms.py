from django import forms

from .models import Reviews

class review_form(forms.ModelForm):
    class Meta():
        model = Reviews
        fields = ('name', 'email', 'text')
