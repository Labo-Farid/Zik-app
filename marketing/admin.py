from django.contrib import admin

from .models import *

admin.site.register(Subscribers)
admin.site.register(MailMessage)
admin.site.register(Contact)
admin.site.register(AddPremiumMusic)
admin.site.register(AddFreeMusic)