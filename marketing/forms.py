from django import forms
from .models import Subscribers, MailMessage, Contact, AddFreeMusic, AddPremiumMusic


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'phone', 'message', ]


class UserAddPremiumMusicForm(forms.ModelForm):

    class Meta:
        model = AddPremiumMusic
        fields = '__all__'

class UserAddFreeMusicForm(forms.ModelForm):
    class Meta:
        model = AddFreeMusic
        fields = '__all__'
