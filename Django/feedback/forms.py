from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    message = forms.CharField(widget=forms.Textarea, label="Your message")