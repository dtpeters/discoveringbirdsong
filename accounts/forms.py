from django import forms


class RecordingRatingForm(forms.Form):
    like = forms.BooleanField(required=False)
