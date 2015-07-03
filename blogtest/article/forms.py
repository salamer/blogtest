from django import forms
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class BlogForm(forms.Form):
    title=forms.CharField(label='title',max_length=30,widget=forms.TextInput(attrs={'class': 'special'}))
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    check=forms.BooleanField(required=False)
    birth_year=forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    
