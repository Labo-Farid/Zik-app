from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_pandas.io import read_frame

from marketing.forms import *
from marketing.models import Subscribers


def subscribe(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'marketing/subscribe.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('marketing:mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'marketing/mail_letter.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message envoyé avec succes')
            return redirect('/')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'marketing/contact.html', context)


def user_add_premium_music(request):
    if request.method == 'POST':
        form = UserAddPremiumMusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Envoyé avec succes')
            return redirect('/')
    else:
        form = UserAddPremiumMusicForm()
    context = {
        'form': form,
    }
    return render(request, 'marketing/user_add_premium_music.html', context)


def user_add_free_music(request):
    if request.method == 'POST':
        form = UserAddFreeMusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Envoyé avec succes')
            return redirect('/')
    else:
        form = UserAddFreeMusicForm()
    context = {
        'form': form,
    }
    return render(request, 'marketing/user_add_free_music.html', context)