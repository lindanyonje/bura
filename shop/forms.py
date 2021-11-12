from django  import forms
from .models import Feedback , Review

class FeedbackForm(forms.Form):
    # specify fields to be displayed.

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)


class ReviewForm(forms.ModelForm):

        model = Review
        name = forms.CharField()
        description = forms.CharField( widget= forms.Textarea)


    # {'rating':(attrs={'class': 'form-control'})}