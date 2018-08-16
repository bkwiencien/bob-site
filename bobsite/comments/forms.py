from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(label="comment", widget=forms.Textarea)
    your_name = forms.CharField(label='email address', max_length=100)  
