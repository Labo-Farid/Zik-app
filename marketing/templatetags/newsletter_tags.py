from django import template

from marketing.models import *
from marketing.forms import SubscibersForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,

)

register = template.Library()

@register.inclusion_tag('marketing/snippets/newsletter.html', takes_context=True)
def render_newsletter(context):
    request = context['request']
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()

    return {
        'form': form,
    }
