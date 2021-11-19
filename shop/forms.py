from django  import forms
from .models import Feedback 

class FeedbackForm(forms.Form):
    # specify fields to be displayed.

    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


# class ReviewForm(forms.Form):

  
#         name = forms.CharField(max_length=100)
#         description = forms.CharField( widget= forms.Textarea)


#     # {'rating':(attrs={'class': 'form-control'})}