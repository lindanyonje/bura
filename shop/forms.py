from django  import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    # specify fields to be displayed.

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

