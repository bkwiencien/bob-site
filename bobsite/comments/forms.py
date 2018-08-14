from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    your_name = forms.CharField(label='Your name', max_length=100)  
