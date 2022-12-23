from django.db.models import fields
from django.forms.widgets import TextInput, Textarea
from django import forms

from .models import EmissionVideoComment, EmissionPodcastComment


class EmissionVideoCommentForm(forms.ModelForm):
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 2}))
    
    class Meta:
        model = EmissionVideoComment
        fields = [ 'body']
        
        
class EmissionPodcastCommentForm(forms.ModelForm):
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 2}))
    
    class Meta:
        model = EmissionPodcastComment
        fields = [ 'body']
        
