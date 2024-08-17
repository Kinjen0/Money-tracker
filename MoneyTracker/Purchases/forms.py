from django import forms
from .models import *


class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name"]

class Purchase_Form(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['amount', 'date', 'description', 'category']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Renders as HTML date picker
        }



class Category_Filter_Form(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.none(), required=False, label='Search by Category')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Get the user from the view
        super().__init__(*args, **kwargs)
        # Limit categories to only those belonging to the user
        self.fields['category'].queryset = Category.objects.filter(user=user)