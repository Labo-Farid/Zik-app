from django import forms
from tinymce.widgets import TinyMCE
from video.models import *


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class VideoForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Video
        fields = ('title', 'description', 'video', 'category')


class VideoCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Entrer votre commentaire',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = VideoComment
        fields = ('content', )